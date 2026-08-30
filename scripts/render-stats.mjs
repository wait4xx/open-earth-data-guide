#!/usr/bin/env node
/**
 * render-stats.mjs — zero-dependency README stats charts (SVG).
 *
 * Generates:
 *   docs/stats/npm-downloads.svg  — daily npm downloads over the last 180 days
 *   docs/stats/stars.svg          — cumulative GitHub stargazers (full history)
 *
 * Data sources:
 *   npm:     https://api.npmjs.org/downloads/range/{from}:{to}/{pkg}   (public, no auth)
 *   GitHub:  /repos/{repo}/stargazers with the star+json preview       (needs a token
 *            that may read the repo — since 2026-06-30 GitHub limits stargazer access
 *            to repo admins/collaborators, which the repo's own Actions token is)
 *
 * Env:
 *   GH_TOKEN  optional; without it (or on any GitHub failure) the stars chart is
 *             skipped with a notice and the run still succeeds — npm is the point.
 *
 * Runs anywhere with plain Node >= 18. Never throws on missing data: a chart with
 * zero points renders a readable "no data yet" placeholder.
 */
import { execSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";

const STATS_DIR = path.join(process.cwd(), "docs", "stats");
const NPM_WINDOW_DAYS = 180;

// ---------------------------------------------------------------- data fetch

async function fetchJson(url, headers = {}) {
	const res = await fetch(url, { headers: { "User-Agent": "stats-renderer", ...headers } });
	if (!res.ok) throw new Error(`${res.status} ${res.statusText} <- ${url}`);
	return res.json();
}

async function fetchNpmDownloads(pkg, days) {
	const to = new Date(Date.now() - 86400_000); // full days only — today is still in progress
	const from = new Date(to.getTime() - days * 86400_000);
	const fmt = (d) => d.toISOString().slice(0, 10);
	const data = await fetchJson(`https://api.npmjs.org/downloads/range/${fmt(from)}:${fmt(to)}/${pkg}`);
	// { downloads: [{ day, downloads }...] } — days before first publish come back as 0;
	// trim that zero prefix (keep one zero day of padding) so a young package's
	// chart isn't flattened into its baseline. Returns the effective start date.
	const all = (data.downloads ?? []).map((d) => ({ date: d.day, value: d.downloads }));
	let first = all.findIndex((p) => p.value > 0);
	if (first < 0) return { start: all[0]?.date, trimmed: false, series: all };
	first = Math.max(0, first - 1);
	return { start: all[first].date, trimmed: true, series: all.slice(first) };
}

async function fetchStargazers(repo, token) {
	const out = [];
	let page = 1;
	for (;;) {
		const batch = await fetchJson(`https://api.github.com/repos/${repo}/stargazers?per_page=100&page=${page}`, {
			Accept: "application/vnd.github.star+json",
			Authorization: `Bearer ${token}`,
		});
		if (!Array.isArray(batch) || batch.length === 0) break;
		for (const s of batch) if (s?.starred_at) out.push({ date: s.starred_at.slice(0, 10), value: 1 });
		if (batch.length < 100) break;
		page += 1;
	}
	// cumulative count per date
	let total = 0;
	return out
		.sort((a, b) => (a.date < b.date ? -1 : 1))
		.map((p) => ({ date: p.date, value: (total += 1) }));
}

// ---------------------------------------------------------------- svg chart

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

function fmtNum(n) {
	if (n >= 1_000_000) return `${(n / 1_000_000).toFixed(n >= 10_000_000 ? 0 : 1)}M`;
	if (n >= 1_000) return `${(n / 1_000).toFixed(n >= 10_000 ? 0 : 1)}k`;
	return String(n);
}

/**
 * Hand-drawn (star-history-style) line chart: xkcd-ish font stack, slightly
 * wobbling line, dotted grid, framed plot area, legend box with name + stats.
 * points: [{date: "YYYY-MM-DD", value}] in chronological order.
 */
function lineChart({ name, stats, points, color }) {
	const W = 880;
	const H = 520;
	const M = { top: 40, right: 30, bottom: 48, left: 74 };
	const iw = W - M.left - M.right;
	const ih = H - M.top - M.bottom;
	const FONT = `xkcd, 'Comic Sans MS', 'Comic Sans', 'Segoe Print', 'Chalkboard SE', cursive`;

	const noData = points.length === 0;
	const maxValue = noData ? 1 : Math.max(...points.map((p) => p.value), 1);
	const t0 = noData ? 0 : new Date(points[0].date).getTime();
	const spanMs = noData ? 1 : Math.max(new Date(points.at(-1).date).getTime() - t0, 86400_000);
	const x = (p) => M.left + ((new Date(p.date).getTime() - t0) / spanMs) * iw;
	const y = (v) => M.top + ih - (v / maxValue) * ih;

	// deterministic ±1.8px wobble (hash of the point index) — same input always
	// renders identical bytes, so the daily commit only fires on real changes
	const wob = (i) => {
		let h = ((i + 1) * 2654435761) % 4294967296;
		h = (h ^ (h >>> 13)) >>> 0;
		h = (h * 1274126177) % 4294967296;
		return (((h >>> 8) % 1000) / 1000 - 0.5) * 3.6;
	};
	const line = points.map((p, i) => `${x(p).toFixed(1)},${(y(p.value) + wob(i)).toFixed(1)}`);

	const fracs = [0, 0.25, 0.5, 0.75, 1];
	const fmtDay = (frac) => {
		const d = new Date(t0 + frac * spanMs);
		return `${d.getUTCFullYear()}-${String(d.getUTCMonth() + 1).padStart(2, "0")}-${String(d.getUTCDate()).padStart(2, "0")}`;
	};

	// legend box (top-left, inside the plot); width covers the longest line
	const lx = M.left + 14;
	const ly = M.top + 12;
	const nameW = 12 + 24 + 8 + name.length * 8.4 + 14;
	const statsW = stats ? 12 + stats.length * 6.2 + 14 : 0;
	const legendW = Math.round(Math.max(nameW, statsW));
	const legendH = stats ? 54 : 34;

	const seriesSvg = noData
		? `<text x="${M.left + iw / 2}" y="${M.top + ih / 2}" text-anchor="middle" font-size="16" fill="#57606a">no data yet</text>`
		: points.length === 1
			? `<circle cx="${(M.left + iw / 2).toFixed(1)}" cy="${y(points[0].value).toFixed(1)}" r="4" fill="${color}"/>`
			: `<polyline points="${line.join(" ")}" fill="none" stroke="${color}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>`;

	return [
		`<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" font-family="${FONT}">`,
		`<rect width="${W}" height="${H}" fill="#ffffff"/>`,
		// interior dotted grid (horizontal)
		...[0.25, 0.5, 0.75].map(
			(f) =>
				`<line x1="${M.left}" y1="${(M.top + ih - f * ih).toFixed(1)}" x2="${M.left + iw}" y2="${(M.top + ih - f * ih).toFixed(1)}" stroke="#d0d7de" stroke-width="1.5" stroke-dasharray="2 7"/>`,
		),
		// y labels (de-duplicated — tiny maxima round several ticks to the same text)
		...(() => {
			const seen = new Set();
			return fracs
				.map((f) => {
					const label = fmtNum(Math.round(maxValue * f));
					if (seen.has(label)) return "";
					seen.add(label);
					return `<text x="${M.left - 10}" y="${(M.top + ih - f * ih + 5).toFixed(1)}" text-anchor="end" font-size="13" fill="#57606a">${label}</text>`;
				})
				.filter(Boolean);
		})(),
		// x ticks + labels (meaningless without data — all dates would be 1970-01-01)
		...(noData
			? []
			: fracs.map((f) => {
				const tx = M.left + f * iw;
				const anchor = f === 0 ? "start" : f === 1 ? "end" : "middle";
				return `<line x1="${tx.toFixed(1)}" y1="${M.top + ih}" x2="${tx.toFixed(1)}" y2="${M.top + ih + 7}" stroke="#8b98a5" stroke-width="1.5"/><text x="${(f === 0 ? tx + 2 : f === 1 ? tx - 2 : tx).toFixed(1)}" y="${M.top + ih + 26}" text-anchor="${anchor}" font-size="13" fill="#57606a">${esc(fmtDay(f))}</text>`;
			})),
		// plot frame (drawn after grid so its edges stay crisp)
		`<rect x="${M.left}" y="${M.top}" width="${iw}" height="${ih}" fill="none" stroke="#8b98a5" stroke-width="2" rx="3"/>`,
		// series
		seriesSvg,
		// legend
		`<rect x="${lx}" y="${ly}" width="${legendW}" height="${legendH}" fill="#ffffff" stroke="#8b98a5" stroke-width="1.5" rx="6"/>`,
		`<line x1="${lx + 12}" y1="${ly + 17}" x2="${lx + 36}" y2="${ly + 17}" stroke="${color}" stroke-width="3" stroke-linecap="round"/>`,
		`<text x="${lx + 44}" y="${ly + 22}" font-size="14" fill="#1f2328">${esc(name)}</text>`,
		...(stats ? [`<text x="${lx + 12}" y="${ly + 42}" font-size="12" fill="#57606a">${esc(stats)}</text>`] : []),
		`</svg>`,
	].join("\n");
}

// ---------------------------------------------------------------- main

function pkgName() {
	return JSON.parse(fs.readFileSync("package.json", "utf8")).name;
}

function gitRepo() {
	try {
		const url = execSync("git remote get-url origin", { encoding: "utf8" }).trim();
		const m = url.match(/(?:github\.com[:/])([\w.-]+\/[\w.-]+?)(?:\.git)?$/i);
		return m?.[1];
	} catch {
		return undefined;
	}
}

async function main() {
	fs.mkdirSync(STATS_DIR, { recursive: true });
	const results = [];

	// npm downloads — only when this repo ships an npm package
	let pkg;
	try {
		pkg = pkgName();
	} catch {
		console.error("[stats] no readable package.json — skipping npm chart");
	}
	if (pkg) {
	try {
		const { start, trimmed, series } = await fetchNpmDownloads(pkg, NPM_WINDOW_DAYS);
		const total = series.reduce((s, p) => s + p.value, 0);
		const last30 = series.slice(-30).reduce((s, p) => s + p.value, 0);
		const subtitle = `${trimmed ? `since ${start}` : `last ${NPM_WINDOW_DAYS}d`}: ${total}${series.length > 30 ? ` · last 30d: ${last30}` : ""}`;
		fs.writeFileSync(
			path.join(STATS_DIR, "npm-downloads.svg"),
			lineChart({
				name: pkg,
				stats: `npm downloads/day · ${subtitle}`,
				points: series,
				color: "#42bb88",
			}),
		);
		results.push(`npm-downloads.svg: ${series.length} days, ${total} total`);
	} catch (err) {
		// A package that is not on npm (private root package.json, monorepo
		// shells) is not a failure — just skip the chart entirely.
		if (/^404/.test(err.message)) {
			console.error(`[stats] package not on npm — skipping npm chart (${err.message})`);
			results.push("npm-downloads.svg: not on npm — skipped");
		} else {
			// Keep the previous chart on transient npm API failures — a 5xx/429
			// blip must not replace a good README chart with "unavailable" for a day.
			console.error(`[stats] npm chart failed: ${err.message}`);
			const target = path.join(STATS_DIR, "npm-downloads.svg");
			if (!fs.existsSync(target)) {
				fs.writeFileSync(
					target,
					lineChart({ name: pkg, stats: "npm downloads/day · unavailable", points: [], color: "#42bb88" }),
				);
			} else {
				console.error("[stats] keeping previous npm chart");
			}
			results.push("npm-downloads.svg: FAILED");
		}
	}
	}

	// stars — best effort, needs GH_TOKEN
	const repo = process.env.GH_REPO?.replace(/^.*github\.com\//, "") || gitRepo();
	const token = process.env.GH_TOKEN || process.env.GITHUB_TOKEN;
	if (!repo || !token) {
		console.error(`[stats] stars chart skipped (${!repo ? "no repo" : "no GH_TOKEN"})`);
		return results;
	}
	try {
		const series = await fetchStargazers(repo, token);
		const total = series.at(-1)?.value ?? 0;
		fs.writeFileSync(
			path.join(STATS_DIR, "stars.svg"),
			lineChart({
				name: repo,
				stats: `${total} stars`,
				points: series,
				color: "#3297d4",
			}),
		);
		results.push(`stars.svg: ${total} stars`);
	} catch (err) {
		console.error(`[stats] stars chart failed: ${err.message} — writing placeholder, keeping any previous chart`);
		if (!fs.existsSync(path.join(STATS_DIR, "stars.svg"))) {
			fs.writeFileSync(path.join(STATS_DIR, "stars.svg"), lineChart({ name: repo, stats: "unavailable", points: [], color: "#3297d4" }));
		}
		results.push("stars.svg: FAILED");
	}
	return results;
}

main()
	.then((results) => {
		for (const line of results) console.log(`[stats] ${line}`);
	})
	.catch((err) => {
		console.error(`[stats] fatal: ${err.message}`);
		process.exit(1);
	});
