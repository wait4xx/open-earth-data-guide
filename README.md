<div align="center">

# 🌍 公开地球系统数据下载资源指南

**一站式索引全球公开气象 · 海洋 · 气候 · 环境数据，提供下载渠道、访问说明与配套脚本**

[![GitHub Stars](https://img.shields.io/github/stars/wait4xx/open-earth-data-guide?style=for-the-badge&logo=github)](https://github.com/wait4xx/open-earth-data-guide/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/wait4xx/open-earth-data-guide?style=for-the-badge&logo=github)](https://github.com/wait4xx/open-earth-data-guide/network/members)
[![License: MIT](https://img.shields.io/github/license/wait4xx/open-earth-data-guide?style=for-the-badge&logo=github)](#许可证)
[![Last Commit](https://img.shields.io/github/last-commit/wait4xx/open-earth-data-guide?style=for-the-badge&logo=git)](https://github.com/wait4xx/open-earth-data-guide/commits)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge&logo=github)](CONTRIBUTING.md)

🌍 全球数据源 · 📥 配套下载脚本 · 🔄 持续更新 · 🤝 欢迎贡献

`气象数据` `数值预报` `大模型` `再分析` `气候` `观测` `卫星` `雷达` `空气质量` `海洋数据` `海洋观测` `SST/海冰` `海洋模式`

**简体中文** · [English](README_EN.md)

</div>

> 📌 收集整理全球公开气象、海洋、气候与环境数据的下载渠道与访问说明，为气象研究、数据分析与应用开发提供便捷的数据获取入口。

---

### 🧩 配套工具：[Open Earth Data Kit](https://github.com/wait4xx/open-earth-data-kit)

本仓库是**资源指南**——聚焦“有哪些数据、去哪下载”，汇总各机构公开数据源的链接、访问说明与配套下载脚本。如果你希望把这些数据源收敛成一个**统一的命令行下载平台**，欢迎使用同源配套项目：

> 🌍 **[Open Earth Data Kit](https://github.com/wait4xx/open-earth-data-kit)** · 统一地球系统公开数据下载工具包
>
> 提供 `meteo` 命令行工具（`list` / `info` / `plan` / `download` / `tasks`）、结构化数据源目录（catalog，已收录 59 个数据源）、多协议适配器（HTTP 目录 / S3 / OPeNDAP / Zarr）与可切换的下载后端（Python / IDM / XDM），并用 SQLite 追踪下载任务状态。

**一句话理解两者关系：指南告诉你“在哪下”，Kit 帮你“自动下”。** 两者同源、互补，既可独立使用，也可配合使用。

---

### 📢 最新动态
> **2026-07-26** · 🤖 大模型预报区完善：将 `noaa-oar-mlwp-data` S3 桶的**目录结构与命名规则**（模型码 `FOUR`/`PANG`/`GRAP`、版本号、`GFS`/`IFS` 初始化系统、起报时刻等字段）及 **FourCastNet v1 / v2-small / Pangu-Weather / GraphCast Operational** 各模型可用变量清单**内联**进 AI 模型集合条目（中英同步），关键访问信息不再仅外链 txt 原文
>
> **2026-06-20** · 🗂️ 重构 IRI Data Library 与 CMEMS 条目：IRI 收敛为「再分析」入口并按数据类型将数据集分散到各主题章节（各条目标 `via IRI`，附**已登录实测**的 `SOURCES/...` 路径），新增 COADS / Levitus / ISCCP / NMME / ENSO-PDO-QBO 条目；CMEMS 拆分为门户 + GLORYS / WAVERY / BGC / DUACS / OSTIA 五个独立条目（OPeNDAP/THREDDS 已退役，现经 Marine Data Store）。实测发现 IRI 不含 ERA5 / MERRA-2 / SODA，已移除相关条目。
>
> **2026-06-18** · 🔐 新增 IRI Data Library、扩充 NASA Earthdata（MERRA-2/GPM/MODIS LST/AIRS/CERES/AVHRR SST/CCMP/OSCAR/SMAP/GRACE/GLDAS/NSIDC 海冰/MODIS 积雪/CALIPSO）与 CMEMS 的详细条目，标注认证要求与 short_name；数据源均经可通联性验证
>
> **2026-06-13** · 🎉 重大更新：新增 18 个公开数据源（气候 / 观测 / 卫星 / 海洋 / 空气质量）；开源工具区扩充至 20 个并改为分类表格；新增 MIT 许可证与 Star History 星标曲线；中英双语文档全面同步
>
> **2026-05-21** · 📝 新增 Planette ERA5 AWS S3 下载脚本用于下载 ERA5 日平均、周平均、月平均数据（`era5_planette_downloader.py`），支持多变量并发、单位转换、实时进度
>
> **2026-04-11** · 📝 新增 ERA5 AWS S3 多线程下载脚本使用教程（`s3_downloader_multi.py`）
>
> **2026-03-03** · 🎇 更新readme文档，优化显示
> 
> **2025-12-09** · ✨ ECMWF 下载脚本升级 — 新增 **IFS / EFS / AIFS / AIEFS** 全系列数据支持
>
> **2025-12-05** · 🚀 ECMWF 下载脚本发布 — 支持 **4 线程并行下载**，大幅提升效率

---

### 🔧 项目进展

| 大类 | 类别 | 状态 |
|:----:|:-----|:----:|
| 🌐 气象 | 数值预报 | ✅ |
| | 大模型预报 | ✅ |
| | 再分析 | ✅ |
| | 气候数据 | ✅ |
| | 实况观测 | ✅ |
| | 卫星 | ✅ |
| | 雷达 | ✅ |
| | 空气质量 | ✅ |
| 🌊 海洋 | 海洋观测 | ✅ |
| | 海表温度与海冰 | ✅ |
| | 海洋模式 | ✅ |
| | 海洋水色 | ✅ |
| 🛠️ 工具 | 开源代码与工具 | ✅ |

---

## 📚 目录

| 数据类型 | 工具与社区 |
|:--------:|:----------:|
| **[🌐 气象数据](#气象数据)** · [数值预报](#数值预报) · [大模型](#大模型预报) · [再分析](#再分析) · [气候](#气候数据) · [观测](#实况观测) · [卫星](#卫星) · [雷达](#雷达) · [空气质量](#空气质量) | [贡献指南](#贡献指南) · [许可证](#许可证) |
| **[🌊 海洋数据](#海洋数据)** · [海洋观测](#海洋观测) · [SST/海冰](#海表温度与海冰) · [海洋模式](#海洋模式) · [海洋水色](#海洋水色) | [开源工具](#开源代码与工具) · [致谢](#致谢) |


## 气象数据

### 数值预报

#### 实时预报数据

<details>
<summary><b>ECMWF</b> · 欧洲中期天气预报中心</summary>

---

**IFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-官方-9CF?style=flat-square)

🔗 [ECMWF Open Data](https://data.ecmwf.int/forecasts/) · 📅 最近 4 日

---

**EFS** · 集合预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-官方-9CF?style=flat-square)

🔗 [ECMWF Open Data](https://data.ecmwf.int/forecasts/) · 📅 最近 4 日

---

**IFS 数据格式说明**

> ![ec_file](./pics/ec_file.png)


</details>

<details>
<summary><b>NCEP</b> · 美国全球预报系统</summary>

---

**GFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-UCAR-800080?style=flat-square)

🔗 [GFS_UCAR](https://motherlode.ucar.edu/native/grid/NCEP/GFS/) · 📅 最近 3 个月

---

**GFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~120h(1h)_120~384h(3h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [GFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/) · 📅 最近 10 日

---

**GFS OPeNDAP** · ⚠️ 已退役

![状态](https://img.shields.io/badge/状态-已退役-red?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOMADS_OpeNDAP-lightgrey?style=flat-square)

> ❌ NOMADS GFS OPeNDAP 端点（`gfs_0p25_1hr` / `gfs_0p25` / `gfs_0p50` / `gfs_1p00`）已于 2025 年全部退役（Service Change Notice 25-81）。替代方案：上方 [GFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/) 原始 GRIB、[GFS_UCAR](https://motherlode.ucar.edu/native/grid/NCEP/GFS/) THREDDS；历史气候/再分析数据见下方 [NOAA PSL THREDDS](#气候与再分析数据)。

---

**GEFS** · 集合预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(3h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [GEFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/gens/) · 📅 最近 4 日

---

**GEFS** · 集合预报

![分辨率](https://img.shields.io/badge/分辨率-0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(3h)_240~840h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [GEFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/gens/) · 📅 最近 4 日

</details>

<details>
<summary><b>DWD</b> · 德国天气局</summary>

---

**ICON** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.125°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-官方-9CF?style=flat-square)

🔗 [ICON Open Data](https://opendata.dwd.de/weather/nwp/icon/grib/) · 📅 最近 4 个起报

</details>

<details>
<summary><b>JMA</b> · 日本气象厅（无法直接下载，需要申请账号）</summary>

---

**GSM** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-官方-9CF?style=flat-square)

🔗 [JMA GSM](https://www.wis-jma.go.jp/cms/gsm/download.html) · 📅 最近 5 日

</details>


#### 历史预报数据

<details>
<summary><b>ECMWF</b> · 欧洲中期天气预报中心</summary>

---

**IFS (HRES ~ 地面)** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.1°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~12h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-UCAR-800080?style=flat-square)

🔗 [IFS_UCAR](https://gdex.ucar.edu/datasets/d113001/dataaccess/#) · 📅 2016 年 1 月 1 日至今

---

**IFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.4°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-Google-4285F4?style=flat-square)
![魔法](https://img.shields.io/badge/魔法-√-3126F0?style=flat-square)

🔗 [🪜 ECMWF_GOOGLE](https://console.cloud.google.com/storage/browser/ecmwf-open-data) · 📅 2023 年 7 月 12 日至今（有延迟）

---

**IFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.4°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://ecmwf-forecasts.s3.amazonaws.com/) · 📅 2023 年 3 月 18 日至今 · ⚠️ 需 awscli 或补全 URL

---

**EFS** · 集合预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.4°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-Google-4285F4?style=flat-square)
![魔法](https://img.shields.io/badge/魔法-√-3126F0?style=flat-square)

🔗 [🪜 ECMWF_GOOGLE](https://console.cloud.google.com/storage/browser/ecmwf-open-data) · 📅 2023 年 7 月 12 日至今（有延迟）

---

**EFS** · 集合预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.4°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://ecmwf-forecasts.s3.amazonaws.com/) · 📅 2023 年 3 月 18 日至今 · ⚠️ 需 awscli 或补全 URL

</details>

<details>
<summary><b>NCEP</b> · 美国全球预报系统</summary>

---

**GFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(3h)_240~384h(12h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-UCAR-800080?style=flat-square)

🔗 [GFS_UCAR](https://gdex.ucar.edu/datasets/d084001/dataaccess/) · 📅 2015 年 1 月 15 日至今（2026 年停更）

---

**GFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.5°/1°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~384h(3h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-gfs-bdp-pds.s3.amazonaws.com/index.html) · 📅 2021 年 1 月 1 日至今 · 🔍 搜索 `gfs`

---

**GFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.5°/1°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~384h(3h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-Google-4285F4?style=flat-square)
![魔法](https://img.shields.io/badge/魔法-√-3126F0?style=flat-square)

🔗 [🪜 GFS_GOOGLE](https://console.cloud.google.com/storage/browser/global-forecast-system) · 📅 2021 年 1 月 1 日至今 · 🔍 搜索 `gfs`

---

**GEFS** · 集合预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~384h(6h)_0~240h(3h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-gefs-pds.s3.amazonaws.com/index.html) · 📅 2017 年 1 月 1 日至今

---

**GEFS** · 集合预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(3h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-Google-4285F4?style=flat-square)
![魔法](https://img.shields.io/badge/魔法-√-3126F0?style=flat-square)

🔗 [🪜 GFS_GOOGLE](https://console.cloud.google.com/storage/browser/gfs-ensemble-forecast-system) · 📅 2020 年 9 月 25 日至今

</details>

<details>
<summary><b>NMME</b> · 北美多模式季节预报集合 · via IRI（dlauth）· OPeNDAP</summary>

![分辨率](https://img.shields.io/badge/分辨率-~1°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-月_季节-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-IRI-9CF?style=flat-square)

North American Multi-Model Ensemble：多机构耦合模式季节预报 + 回报（hindcast）集合（CFSv2、GFDL、NASA GEOS-5、NCAR CCSM、CanCM 等），NOAA CPC 季节展望主输入。

🔗 via [IRI Data Library](https://iridl.ldeo.columbia.edu/)（dlauth）：`SOURCES/Models/.NMME`

</details>

### 大模型预报

#### 实时数据

<details>
<summary><b>ECMWF</b> · 欧洲中期天气预报中心</summary>

---

**AIFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-官方-9CF?style=flat-square)

🔗 [ECMWF Open Data](https://data.ecmwf.int/forecasts/) · 📅 最近 4 日

---

**AIEFS** · 集合预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-官方-9CF?style=flat-square)

🔗 [ECMWF Open Data](https://data.ecmwf.int/forecasts/) · 📅 最近 4 日

</details>

<details>
<summary><b>NCEP</b> · 美国全球预报系统</summary>

---

**AIGFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [AIGFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/aigfs/) · 📅 最近 2 日

---

**AIGEFS** · 集合预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [AIGEFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/aigefs/) · 📅 最近 2 日

</details>

<details>
<summary><b>AI 模型集合</b> · Aurora / FourCastNet / GraphCast / PANGU</summary>

---

**Aurora** · 微软 · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日2次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📝 [数据说明](./docs/noaa-oar-mlwp-data.txt)

---

**FourCastNet** · NVIDIA · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日2次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📝 [数据说明](./docs/noaa-oar-mlwp-data.txt)

---

**GraphCast** · Google / DeepMind · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日2次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📝 [数据说明](./docs/noaa-oar-mlwp-data.txt)

---

**PANGU** · 华为 · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日2次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📝 [数据说明](./docs/noaa-oar-mlwp-data.txt)

</details>

#### 历史数据

<details>
<summary><b>ECMWF</b> · 欧洲中期天气预报中心</summary>

---

**AIFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://ecmwf-forecasts.s3.amazonaws.com/) · 📅 2024 年 2 月 29 日至今 · ⚠️ 需 awscli 或补全 URL

---

**AIEFS** · 集合预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://ecmwf-forecasts.s3.amazonaws.com/) · ⚠️ 需 awscli 或补全 URL

</details>

<details>
<summary><b>AI 模型集合</b> · Aurora / FourCastNet / GraphCast / PANGU</summary>

<details>
<summary>📖 目录结构与命名规则</summary>

公开 S3 桶 `noaa-oar-mlwp-data`（AWS，无需鉴权）。文件路径：

```
s3://noaa-oar-mlwp-data/MMMM_vNNN_III/YYYY/mmdd/MMMM_vNNN_III_YYYYmmddhh_fXXX_fYYY_ZZ.nc
```

| 字段 | 含义 | 取值 |
|:----:|:-----|:-----|
| `MMMM` | 模型代码 | `FOUR` / `PANG` / `GRAP` |
| `NNN` | 版本号 | `100`、`200` |
| `III` | 初始条件系统 | `GFS`（全期）；`IFS`（2025-01 起） |
| `YYYY`/`mm`/`dd` | 起报日期 | 年 / 月 / 日 |
| `hh` | 起报时刻 (UTC) | `00`、`06`、`12`、`18` |
| `XXX` / `YYY` | 单文件首 / 末预报时 | `000` / `240` |
| `ZZ` | 预报步长 (h) | `06` |

起报时刻：00 / 12 UTC 全年可用；06 / 18 UTC 仅 2023 年提供。

</details>

<details>
<summary>📋 各模型可用变量</summary>

**FourCastNet v1**：10 m / 100 m 风（u、v）、2 m 温度、地面气压、海平面气压、整层水汽；位势 / 温度 / u-v 风（1000、850、500、250 hPa，位势含 50 hPa）；相对湿度（850、500 hPa）。

**FourCastNet v2-small**：10 m / 100 m 风（u、v）、2 m 温度、地面气压、海平面气压、整层水汽；位势 / 温度 / u-v 风 / 相对湿度（1000、925、850、700、600、500、400、300、250、200、150、100、50 hPa）。

**Pangu-Weather**：10 m 风（u、v）、2 m 温度、海平面气压；位势 / 温度 / u-v 风 / 比湿（1000、925、850、700、600、500、400、300、250、200、150、100、50 hPa）。

**GraphCast Operational**：10 m 风（u、v）、2 m 温度、海平面气压；位势 / 温度 / u-v 风 / 比湿 / 垂直速度（同上 13 层）；6 h 累积降水。

</details>

---

**Aurora** · 微软 · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日2次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📅 2025 年 1 月 23 日至今 · 📝 [数据说明](./docs/noaa-oar-mlwp-data.txt)

---

**FourCastNet** · NVIDIA · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日2次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📅 2020 年 9 月 30 日至今 · 📝 [数据说明](./docs/noaa-oar-mlwp-data.txt)

---

**GraphCast** · Google / DeepMind · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日2次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📅 2020 年 9 月 30 日至今 · 📝 [数据说明](./docs/noaa-oar-mlwp-data.txt)

---

**PANGU** · 华为 · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日2次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📅 2020 年 9 月 30 日至今 · 📝 [数据说明](./docs/noaa-oar-mlwp-data.txt)

</details>

### 再分析

<details>
<summary><b>ERA5-land</b> · ECMWF 地面再分析 </summary>

***无魔法情况下推荐通过AWS+IDM多线程下载，下载速度最快***

---

**ERA5-land (hourly)**

![分辨率](https://img.shields.io/badge/分辨率-0.1°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1950年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-CDS-00CED1?style=flat-square)

🔗 [ERA5-land](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=download)

---

**ERA5-land (hourly)**

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1940年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://nsf-ncar-era5.s3.amazonaws.com/index.html#e5.oper.an.sfc/) · 📅 数据延迟3-4个月 · 📝 [Python 多线程下载脚本](./sources/s3_downloader_multi.py)

<details>
<summary>📖 s3_downloader_multi.py 使用教程</summary>

---

**脚本简介**

`s3_downloader_multi.py` 是一个针对 AWS S3 ERA5 数据的智能并发下载脚本，通过调用 IDM 或 XDM 实现多任务并行下载，支持断点续传、字节级校验和自动跳过已完成文件。

**环境依赖**

```bash
pip install requests beautifulsoup4 lxml
```

同时需要安装以下任意一款下载工具：
- **IDM**（Windows，推荐）：[Internet Download Manager](https://www.internetdownloadmanager.com/)
- **XDM**（跨平台）：[Xtreme Download Manager](https://xtremedownloadmanager.com/)

**配置下载工具路径**

打开脚本，修改 `Config` 类中的路径：

```python
class Config:
    DOWNLOAD_TOOL = "idm"   # 或 "xdm"
    IDM_PATH = r"D:\Program Files (x86)\Internet Download Manager\IDMan.exe"
    XDM_PATH_LINUX  = "/opt/xdman/xdman"
    XDM_PATH_WINDOWS = r"C:\Program Files\XDM\xdman.exe"
```

---

**命令行模式（推荐）**

```bash
python s3_downloader_multi.py -v <变量> -y <年份范围> -o <输出目录> [选项]
```

| 参数 | 说明 | 示例 |
|------|------|------|
| `-v` | 变量名，多个用逗号分隔 | `2t` / `2t,10u,10v` |
| `-y` | 年份范围，单年或区间 | `2024` / `2020-2024` |
| `-m` | 月份，多个用逗号分隔（默认全年） | `1,2,3` |
| `-o` | 本地输出目录 | `./era5_data` |
| `-t` | 下载工具，`idm` 或 `xdm`（默认 `idm`） | `idm` |
| `-c` | 最大并发数（默认 6） | `4` |
| `--dry-run` | 预览模式，不实际下载 | — |
| `--export` | 导出文件列表为 CSV/TXT | — |
| `--delay` | 数据延迟月数（默认 5） | `3` |

**示例**

```bash
# 预览 2024 年 2m 气温数据（不下载）
python s3_downloader_multi.py -v 2t -y 2024 -o ./era5_data --dry-run --export

# 下载 2023-2024 年 2m 气温 + 10m 风场，6 线程并发
python s3_downloader_multi.py -v 2t,10u,10v -y 2023-2024 -o ./era5_data -c 6

# 只下载 2024 年 6-8 月地面气压
python s3_downloader_multi.py -v sp -y 2024 -m 6,7,8 -o ./era5_data
```

---

**代码调用模式**

修改脚本顶部 `Config` 类中的 `RUN_MODE` 和 `CODE_PARAMS`，然后直接运行：

```python
class Config:
    RUN_MODE = "code"   # 切换为代码模式
    CODE_PARAMS = {
        "variables":      ["2t", "10u"],   # 变量列表
        "start_year":     2023,
        "end_year":       2024,
        "months":         [6, 7, 8],       # None 表示全年
        "output_dir":     "./era5_data",
        "dry_run":        False,
        "export_preview": True,
        "preview_file":   "preview_list.csv",
    }
```

---

**支持的变量（默认数据集 `e5.oper.an.sfc`，共 62 个）**

| 变量代码 | 含义 | 单位 | 变量代码 | 含义 | 单位 |
|----------|------|------|----------|------|------|
| `2t` | 2米气温 | K | `2d` | 2米露点温度 | K |
| `10u` | 10米纬向风/10米U风分量 | m s⁻¹ | `10v` | 10米经向风/10米V风分量 | m s⁻¹ |
| `100u` | 100米纬向风/100米U风分量 | m s⁻¹ | `100v` | 100米经向风/100米V风分量 | m s⁻¹ |
| `u10n` | 10米中性纬向风 | m s⁻¹ | `v10n` | 10米中性经向风 | m s⁻¹ |
| `sp` | 地面气压/表面气压 | Pa | `msl` | 平均海平面气压 | Pa |
| `skt` | 表皮温度/地表表皮温度 | K | `sstk` | 海表表皮温度 | K |
| `sd` | 积雪深度/雪水当量 | m | `rsn` | 积雪密度 | kg m⁻³ |
| `asn` | 积雪反照率 | 0~1 | `tsn` | 积雪层温度/雪层温度 | K |
| `cape` | 对流有效位能 | J kg⁻¹ | `blh` | 边界层高度 | m |
| `tcc` | 总云量 | 0~1 | `lcc` | 低云量 | 0~1 |
| `mcc` | 中云量 | 0~1 | `hcc` | 高云量 | 0~1 |
| `tcw` | 大气柱总水含量 | kg m⁻² | `tcwv` | 大气柱总水汽含量 | kg m⁻² |
| `tciw` | 大气柱总冰水含量 | kg m⁻² | `tclw` | 大气柱总液态水含量 | kg m⁻² |
| `tco3` | 大气柱总臭氧含量 | kg m⁻² | `ci` | 海冰密集度/海冰浓度 | 0~1 |
| `stl1`~`stl4` | 土壤温度 1~4层 | K | `swvl1`~`swvl4` | 土壤体积含水量 1~4层 | m³ m⁻³ |
| `istl1`~`istl4` | 冰层温度 1~4层 | K | `src` | 表皮层储水量/表层截留水量 | m |
| `alnid` | 近红外直接反照率 | 0~1 | `alnip` | 近红外漫射反照率 | 0~1 |
| `aluvd` | 紫外直接反照率 | 0~1 | `aluvp` | 紫外漫射反照率 | 0~1 |
| `fal` | 预报反照率 | 0~1 | `fsr` | 预报表面粗糙度 | m |
| `flsr` | 预报对数表面粗糙度 | 无量纲 | `chnk` | Charnock系数 | 无量纲 |
| `lailv` | 低植被叶面积指数 | m² m⁻² | `laihv` | 高植被叶面积指数 | m² m⁻² |
| `tcrw` | 大气柱总雨水含量 | kg m⁻² | `tcsw` | 大气柱总雪水含量 | kg m⁻² |
| `ie` | 瞬时水汽通量/瞬时蒸发 | kg m⁻² s⁻¹ | `ishf` | 瞬时表面感热通量 | W m⁻² |
| `iews` | 瞬时东西向表面应力 | N m⁻² | `inss` | 瞬时南北向表面应力 | N m⁻² |
| `lblt` | 湖底温度 | K | `ltlt` | 湖全层温度/湖混合层温度 | K |
| `licd` | 湖冰总深度/湖冰厚度 | m | `lict` | 湖冰表面温度 | K |
| `lshf` | 湖表总热通量 | W m⁻² | | | |

---

> 1. 比例值 (0~1)：云量 (`tcc` 等)、反照率 (`asn` 等)、海冰浓度 (`ci`) 在 ERA5 原生数据中是 0 到 1 的小数，而不是百分比。若需百分比需乘以 100。
> 2. 水当量 (m)：积雪深度 (`sd`) 和表皮储水量 (`src`) 的单位 m 指的是米水当量 (`m of water equivalent`)，并非实际的物理几何深度。
> 3. 瞬时通量：由于该数据集是分析场 (analysis)，通量和应力变量（如 `ie`, `ishf`, `iews`）代表的是瞬时值，因此单位包含时间倒数（如 kg m⁻² s⁻¹, W m⁻², N m⁻²）。如果是预报场 (forecast)，则为累积量，单位会有所不同。
> 4. 柱含量 (kg m⁻²)：如 `tcwv`, `tcrw` 等，数值上等同于 毫米 (mm) 的液态水深度。

---

> 脚本默认下载 `e5.oper.an.sfc`（地面分析）数据集，可通过修改 `DATASET_PREFIX` 访问其他数据集（见下方）。完整变量说明可参考 [ECMWF ERA5 参数表](https://codes.ecmwf.int/grib/param-db/)。

---

**气压层分析 `e5.oper.an.pl`（共 16 个变量）**

> 设置 `DATASET_PREFIX = "e5.oper.an.pl"` 访问。变量覆盖多个气压层（1–1000 hPa），包含风、温度、位势高度、湿度、云、臭氧等三维大气分析场。这是 ERA5 最核心的高空数据集之一，常用于天气分析、气候诊断和数值模式验证。

| 变量代码 | 含义 | 单位 | 变量代码 | 含义 | 单位 |
|----------|------|------|----------|------|------|
| `z` | 位势（地转高度） | m²/s² | `t` | 温度 | K |
| `u` | 纬向风 | m/s | `v` | 经向风 | m/s |
| `w` | 垂直速度 | Pa/s | `q` | 比湿 | kg/kg |
| `r` | 相对湿度 | % | `d` | 散度 | s⁻¹ |
| `vo` | 相对涡度 | s⁻¹ | `pv` | 位涡 | PVU |
| `o3` | 臭氧质量混合比 | kg/kg | `cc` | 云量 | (0–1) |
| `clwc` | 云液态水含量 | kg/kg | `ciwc` | 云冰水含量 | kg/kg |
| `crwc` | 雨水含量 | kg/kg | `cswc` | 雪水含量 | kg/kg |

---

<details>
<summary>📂 其他数据集（修改 <code>DATASET_PREFIX</code> 访问）</summary>

---

**垂直积分 `e5.oper.an.vinteg`（共 36 个变量）**

> 大气柱垂直积分量，包含质量、能量、水汽的积分及通量。

**基本积分量**

| 变量代码 | 含义 | 单位 | 变量代码 | 含义 | 单位 |
|----------|------|------|----------|------|------|
| `vima` | 大气柱总质量 | kg m⁻² | `vit` | 大气柱温度积分 | K kg m⁻² |
| `vike` | 大气柱动能积分 | J m⁻² | `vithe` | 大气柱热能积分 | J m⁻² |
| `vipie` | 大气柱干静力能积分 | J m⁻² | `vipile` | 大气柱湿静力能积分 | J m⁻² |
| `vitoe` | 大气柱总能量积分 | J m⁻² | `viec` | 能量转换率积分 | W m⁻² |

**水汽/质量/能量通量**

| 变量代码 | 含义 | 单位 | 变量代码 | 含义 | 单位 |
|----------|------|------|----------|------|------|
| `vimae` | 纬向质量通量 | kg m⁻¹ s⁻¹ | `viman` | 经向质量通量 | kg m⁻¹ s⁻¹ |
| `viwve` | 纬向水汽通量 | kg m⁻¹ s⁻¹ | `viwvn` | 经向水汽通量 | kg m⁻¹ s⁻¹ |
| `vige` | 纬向位势通量 | W m⁻¹ | `vign` | 经向位势通量 | W m⁻¹ |
| `vikee` | 纬向动能通量 | W m⁻¹ | `viken` | 经向动能通量 | W m⁻¹ |
| `vithee` | 纬向热通量 | W m⁻¹ | `vithen` | 经向热通量 | W m⁻¹ |
| `vitoee` | 纬向总能量通量 | W m⁻¹ | `vitoen` | 经向总能量通量 | W m⁻¹ |
| `vioze` | 纬向臭氧通量 | kg m⁻¹ s⁻¹ | `viozn` | 经向臭氧通量 | kg m⁻¹ s⁻¹ |

**云水通量**

| 变量代码 | 含义 | 单位 | 变量代码 | 含义 | 单位 |
|----------|------|------|----------|------|------|
| `vilwe` | 纬向云液态水通量 | kg m⁻¹ s⁻¹ | `vilwn` | 经向云液态水通量 | kg m⁻¹ s⁻¹ |
| `viiwe` | 纬向云冰水通量 | kg m⁻¹ s⁻¹ | `viiwn` | 经向云冰水通量 | kg m⁻¹ s⁻¹ |

**通量散度**

| 变量代码 | 含义 | 单位 | 变量代码 | 含义 | 单位 |
|----------|------|------|----------|------|------|
| `vimad` | 质量通量散度 | kg m⁻² s⁻¹ | `viked` | 动能通量散度 | W m⁻² |
| `vithed` | 热能通量散度 | W m⁻² | `viwvd` | 水汽通量散度 | kg m⁻² s⁻¹ |
| `vigd` | 位势通量散度 | W m⁻² | `vitoed` | 总能量通量散度 | W m⁻² |
| `viozd` | 臭氧通量散度 | kg m⁻² s⁻¹ | `vilwd` | 云液态水通量散度 | kg m⁻² s⁻¹ |
| `viiwd` | 云冰水通量散度 | kg m⁻² s⁻¹ | `vimat` | 垂直积分水汽平流倾向 | kg m⁻² s⁻¹ |

---

**地面预报累积量 `e5.oper.fc.sfc.accumu`（共 38 个变量）**

> 预报模式输出的地面累积量，默认累积时段为 0–24h（或步长内累积）。

**降水与蒸发**

| 变量代码 | 含义 | 单位 | 变量代码 | 含义 | 单位 |
|----------|------|------|----------|------|------|
| `lsp` | 大尺度降水 | m | `cp` | 对流降水 | m |
| `sf` | 降雪量 (水当量) | m | `csf` | 对流降雪量 (水当量) | m |
| `lsf` | 大尺度降雪量 (水当量) | m | `ro` | 径流总量 | m |
| `sro` | 地表径流 | m | `ssro` | 地下径流 | m |
| `es` | 蒸发量 (水当量) | m | `pev` | 潜在蒸发量 | m |
| `lspf` | 大尺度降水比例 | 0~1 | `e` | 蒸发量 | m |

**辐射（地面）**

| 变量代码 | 含义 | 单位 | 变量代码 | 含义 | 单位 |
|----------|------|------|----------|------|------|
| `ssrd` | 地面向下太阳辐射 | J m⁻² | `strd` | 地面向下长波辐射 | J m⁻² |
| `ssr` | 地面净太阳辐射 | J m⁻² | `str` | 地面净长波辐射 | J m⁻² |
| `ssrc` | 地面净太阳辐射（晴空） | J m⁻² | `strc` | 地面净长波辐射（晴空） | J m⁻² |
| `ssrdc` | 地面向下太阳辐射（晴空） | J m⁻² | `strdc` | 地面向下长波辐射（晴空） | J m⁻² |
| `fdir` | 地面直接太阳辐射 | J m⁻² | `cdir` | 地面直接太阳辐射（晴空）| J m⁻² |
| `uvb` | 地面紫外辐射 | J m⁻² | | | |

**辐射（大气顶）**

| 变量代码 | 含义 | 单位 | 变量代码 | 含义 | 单位 |
|----------|------|------|----------|------|------|
| `tsr` | 大气顶净太阳辐射 | J m⁻² | `ttr` | 大气顶净长波辐射 (OLR) | J m⁻² |
| `tsrc` | 大气顶净太阳辐射（晴空） | J m⁻² | `ttrc` | 大气顶净长波辐射（晴空） | J m⁻² |
| `tisr` | 大气顶入射太阳辐射 | J m⁻² | | | |

**热量与湍流**

| 变量代码 | 含义 | 单位 | 变量代码 | 含义 | 单位 |
|----------|------|------|----------|------|------|
| `sshf` | 地面感热通量 (累积) | J m⁻² | `slhf` | 地面潜热通量 (累积) | J m⁻² |
| `bld` | 边界层耗散 (累积) | J m⁻² | `gwd` | 重力波耗散 (累积) | J m⁻² |
| `ewss` | 纬向湍流应力 (累积) | N m⁻² s | `nsss` | 经向湍流应力 (累积) | N m⁻² s |
| `lgws` | 纬向重力波应力 (累积) | N m⁻² s | `mgws` | 经向重力波应力 (累积) | N m⁻² s |
| `smlt` | 融雪量 (水当量) | m | `vimd` | 垂直积分水汽散度 | kg m⁻² |

---

**地面预报瞬时量 `e5.oper.fc.sfc.instan`（共 14 个变量）**

> 预报模式输出的地面瞬时量，包含云底高度、阵风、降水率和波浪参数。

| 变量代码 | 含义 | 单位 | 变量代码 | 含义 | 单位 |
|----------|------|------|----------|------|------|
| `cbh` | 云底高度 | m | `zust` | 摩擦速度 | m s⁻¹ |
| `i10fg` | 瞬时 10m 阵风 | m s⁻¹ | `deg0l` | 零度层高度 | m |
| `crr` | 对流降水率 | kg m⁻² s⁻¹ | `lsrr` | 大尺度降水率 | kg m⁻² s⁻¹ |
| `csfr` | 对流降雪率 | kg m⁻² s⁻¹ | `lssfr` | 大尺度降雪率 | kg m⁻² s⁻¹ |
| `ilspf` | 瞬时大尺度降水比例 | 0~1 | `dctb` | 风浪和涌浪合成波向 | ° |
| `tplb` | 合成波周期（一阶矩） | s | `tplt` | 合成波周期（二阶矩） | s |
| `dndzn` | 风浪波向 | ° | `dndza` | 风浪波向（调整） | ° |

---

**地面预报平均通量 `e5.oper.fc.sfc.meanflux`（共 39 个变量）**

> 预报模式输出的地面时间平均通量，前缀 `m` = mean（平均），是累积量的时间平均版本。

**降水与蒸发**

| 变量代码 | 含义 | 单位 | 变量代码 | 含义 | 单位 |
|----------|------|------|----------|------|------|
| `mtpr` | 平均总降水率 | kg m⁻² s⁻¹ | `mcpr` | 平均对流降水率 | kg m⁻² s⁻¹ |
| `mlspr` | 平均大尺度降水率 | kg m⁻² s⁻¹ | `mcsr` | 平均对流降雪率 | kg m⁻² s⁻¹ |
| `mlssr` | 平均大尺度降雪率 | kg m⁻² s⁻¹ | `msr` | 平均降雪率 | kg m⁻² s⁻¹ |
| `mer` | 平均蒸发率 | kg m⁻² s⁻¹ | `mper` | 平均潜在蒸发率 | kg m⁻² s⁻¹ |
| `msror` | 平均地表径流率 | kg m⁻² s⁻¹ | `mssror` | 平均地下径流率 | kg m⁻² s⁻¹ |
| `mror` | 平均径流率 | kg m⁻² s⁻¹ | `mlspf` | 平均大尺度降水比例 | 0~1 |
| `msmr` | 平均融雪率 | kg m⁻² s⁻¹ | `mvimd` | 平均垂直积分水汽散度 | kg m⁻² s⁻¹ |

**辐射（地面）**

| 变量代码 | 含义 | 单位 | 变量代码 | 含义 | 单位 |
|----------|------|------|----------|------|------|
| `msdwswrf` | 平均地面向下短波辐射 | W m⁻² | `msdwlwrf` | 平均地面向下长波辐射 | W m⁻² |
| `msnswrf` | 平均地面净短波辐射 | W m⁻² | `msnlwrf` | 平均地面净长波辐射 | W m⁻² |
| `msdwswrfcs`| 晴空平均地面向下短波 | W m⁻² | `msdwlwrfcs`| 晴空平均地面向下长波 | W m⁻² |
| `msnswrfcs` | 晴空平均地面净短波 | W m⁻² | `msnlwrfcs` | 晴空平均地面净长波 | W m⁻² |
| `msdrswrf` | 平均地面直接短波辐射 | W m⁻² | `msdrswrfcs`| 晴空平均地面直接短波 | W m⁻² |
| `msdwuvrf` | 平均地面向下 UV 辐射 | W m⁻² | | | |

**辐射（大气顶）**

| 变量代码 | 含义 | 单位 | 变量代码 | 含义 | 单位 |
|----------|------|------|----------|------|------|
| `mtnswrf` | 平均大气顶净短波辐射 | W m⁻² | `mtnlwrf` | 平均大气顶净长波 (OLR) | W m⁻² |
| `mtnswrfcs` | 晴空平均大气顶净短波 | W m⁻² | `mtnlwrfcs` | 晴空平均大气顶净长波 | W m⁻² |
| `mtdwswrf` | 平均大气顶向下短波 | W m⁻² | | | |

**热量与湍流**

| 变量代码 | 含义 | 单位 | 变量代码 | 含义 | 单位 |
|----------|------|------|----------|------|------|
| `msshf` | 平均地面感热通量 | W m⁻² | `mslhf` | 平均地面潜热通量 | W m⁻² |
| `mbld` | 平均边界层耗散 | W m⁻² | `mgwd` | 平均重力波耗散 | W m⁻² |
| `metss` | 平均纬向湍流应力 | N m⁻² | `mntss` | 平均经向湍流应力 | N m⁻² |
| `megwss` | 平均纬向重力波应力 | N m⁻² | `mngwss` | 平均经向重力波应力 | N m⁻² |

---

**地面预报极值 `e5.oper.fc.sfc.minmax`（共 5 个变量）**

> 预报模式输出的地面极值量，包含最高/最低温度、最大阵风和极值降水率。

| 变量代码 | 含义 | 单位 | 变量代码 | 含义 | 单位 |
|----------|------|------|----------|------|------|
| `10fg` | 10m 风速阵风极值 | m s⁻¹ | `mx2t` | 2m 最高温度 | K |
| `mn2t` | 2m 最低温度 | K | `mxtpr` | 最大总降水率 | kg m⁻² s⁻¹ |
| `mntpr` | 最小总降水率 | kg m⁻² s⁻¹ | | | |

---

**恒定不变量 `e5.oper.invariant`（共 14 个变量）**

> 地理/地表特征常量，不随时间变化，仅含一个时间步。

| 变量代码 | 含义 | 单位 | 变量代码 | 含义 | 单位 |
|----------|------|------|----------|------|------|
| `z` | 地形位势 (除以9.8得高度)| m² s⁻² | `lsm` | 陆海掩码 | 0~1 |
| `cl` | 湖泊覆盖度 | 0~1 | `dl` | 湖泊深度 | m |
| `cvl` | 低植被覆盖度 | 0~1 | `cvh` | 高植被覆盖度 | 0~1 |
| `tvl` | 低植被类型 (类别代码) | 无量纲 | `tvh` | 高植被类型 (类别代码) | 无量纲 |
| `slt` | 土壤类型 (类别代码) | 无量纲 | `sdfor` | 滤波次网格地形标准差 | m |
| `sdor` | 地形标准差 | m | `isor` | 次网格地形各向异性 | 无量纲 |
| `anor` | 次网格地形走向角 | rad | `slor` | 次网格地形坡度 | 无量纲 |

</details>

---

**注意事项**

- 数据通常延迟约 **3-5 个月**，脚本会自动跳过未发布的月份
- 下载任务由 IDM/XDM 接管，脚本通过扫描本地文件大小判断完成状态
- 日志自动写入当前目录的 `download_log.txt`
- 已完整下载的文件（字节数 ≥ 预期 × 99%）会自动跳过，支持断点续传

</details>

---

**ERA5-land (monthly)**

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-monthly_mean-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1950年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-CDS-00CED1?style=flat-square)

🔗 [ERA5-land (monthly)](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land-monthly-means?tab=download)

---

**ERA5-land (daily/7-day/monthly/3-month)**

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1940年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://planette-era5.s3.amazonaws.com/index.html#era5/) · 📅 数据延迟3-4个月 · 数据为zarr格式 · 📝 [Python 下载脚本](./sources/era5_planette_downloader.py)

<details>
<summary>📖 era5_planette_downloader.py 使用教程</summary>

---

**脚本简介**

`era5_planette_downloader.py` 是一个针对 AWS S3 Planette ERA5 数据的下载脚本，支持多变量并发下载、自动单位转换、空间/时间裁剪，实时显示下载进度和速度。

**环境依赖**

```bash
pip install xarray icechunk s3fs numpy netcdf4 requests dask
```

**基本用法**

```bash
python era5_planette_downloader.py -v <变量> -f <频率> -o <输出路径> [选项]
```

| 参数 | 说明 | 示例 |
|------|------|------|
| `-v` | 变量名，支持多个 | `t2m` / `t2m pr slp` |
| `-f` | 时间频率 | `day` / `7day` / `month` / `3month` |
| `-g` | 网格分辨率（默认 0p25latx0p25lon） | `0p25latx0p25lon` |
| `-t` | 时间范围 (YYYY-MM-DD) | `2020-01-01 2024-12-31` |
| `-r` | 空间裁剪 (lon_min lon_max lat_min lat_max) | `70 140 15 55` |
| `-o` | 输出文件或目录（目录对应多变量） | `./t2m.nc` / `./output/` |
| `--format` | 输出格式（默认 netcdf4） | `netcdf4` / `zarr` |
| `--auto-name` | 自动生成文件名 | — |
| `--concurrent` | 多变量并发下载 | — |
| `--workers` | 并发下载线程数（默认 4） | `8` |
| `--no-convert` | 禁用单位转换 | — |
| `--no-resume` | 禁用断点续传 | — |
| `--no-compress` | 禁用压缩（加快写入） | — |
| `--no-validate` | 跳过数据校验 | — |
| `--list-variables` | 列出 S3 可用变量 | — |
| `--list-tree` | 显示变量数据目录树 | — |

**示例**

```bash
# 查看可用变量
python era5_planette_downloader.py --list-variables

# 下载月平均 2m 气温 (2020-2024年)
python era5_planette_downloader.py -v t2m -f month -t 2020-01-01 2024-12-31 -o ./t2m_monthly.nc

# 下载并裁剪中国区域
python era5_planette_downloader.py -v t2m -f month -t 2020-01-01 2020-12-31 -r 70 140 15 55 -o ./t2m_china.nc

# 多变量并发下载 + 自动命名
python era5_planette_downloader.py -v t2m pr slp -f month -t 2020-01-01 2024-12-31 -o ./output/ --auto-name --concurrent

# 导出为 Zarr 格式
python era5_planette_downloader.py -v t2m -f day -o ./t2m.zarr --format zarr
```

**支持的变量（共 64 个）**

> 使用 `--list-variables` 可实时查看 S3 上的最新变量列表。以下为截至 2026 年 5 月的完整变量，按类别分组。脚本对部分常用变量内置了单位自动转换（见"转换"列），其余变量以原始单位输出。

**地面变量**

| 变量 | 含义 | 原始单位 | 转换说明 / 目标单位 |
|------|------|----------|---------------------|
| `t2m` | 2m 气温 | K | → °C (减去 273.15) |
| `t2m_max` | 2m 最高气温 | K | → °C (减去 273.15) |
| `t2m_min` | 2m 最低气温 | K | → °C (减去 273.15) |
| `td2m` | 2m 露点温度 | K | → °C (减去 273.15) |
| `ts` | 地表温度 | K | → °C (减去 273.15) |
| `sst` | 海表温度 | K | → °C (减去 273.15) |
| `ps` | 地面气压 | Pa | → hPa (除以 100) |
| `slp` | 海平面气压 | Pa | → hPa (除以 100) |
| `pr` | 降水率 | kg m⁻² s⁻¹ | |
| `tcwv` | 大气总可降水量 | kg m⁻² | |
| `cape` | 对流有效位能 | J kg⁻¹ |  |
| `olr` | 外逸长波辐射 | W m⁻² | ⚠️ **注意符号**：ERA5原生`ttr`向下为正(负值)，OLR向上为正，通常需 `OLR = -ttr` |
| `cdd` | 制冷度日 | °C·day | 基于阈值(如26°C)的累积量 |
| `hdd` | 采暖度日 | °C·day | 基于阈值(如18°C)的累积量 |
| `sic` | 海冰浓度 | 0~1 | |

> 1. 外逸长波辐射 (olr)：ERA5 原生的 ttr (大气顶净长波辐射) 规定向下为正，因此地表向外太空散发的长波辐射在原生数据中是负值。物理学上的 OLR 定义为向上为正，因此通常需要 OLR = -ttr。
> 2. 降水率 (pr)：如果原始数据是 ERA5 的 tp (m)，转换为 mm/day 需要乘以 1000 * 24 = 24000（如果是小时累积则乘对应系数）。如果是瞬时通量 kg m⁻² s⁻¹，则乘以 86400。

**风场（高度层）**

| 变量 | 含义 | 原始单位 | 转换说明 / 目标单位 |
|------|------|----------|---------------------|
| `u10m` | 10m 纬向风 | m s⁻¹ | |
| `v10m` | 10m 经向风 | m s⁻¹ | |
| `u100m` | 100m 纬向风 | m s⁻¹ | |
| `v100m` | 100m 经向风 | m s⁻¹ | |
| `tau_x` | 纬向风应力 | N m⁻² | |
| `tau_y` | 经向风应力 | N m⁻² | |

**风场（气压层）**

| 变量 | 含义 | 原始单位 | 变量 | 含义 | 原始单位 |
|------|------|----------|------|------|----------|
| `u10` | 10hPa 纬向风 | m s⁻¹ | `v10` | 10hPa 经向风 | m s⁻¹ |
| `u50` | 50hPa 纬向风 | m s⁻¹ | `v50` | 50hPa 经向风 | m s⁻¹ |
| `u100` | 100hPa 纬向风 | m s⁻¹ | `v100` | 100hPa 经向风 | m s⁻¹ |
| `u200` | 200hPa 纬向风 | m s⁻¹ | `v200` | 200hPa 经向风 | m s⁻¹ |
| `u500` | 500hPa 纬向风 | m s⁻¹ | `v500` | 500hPa 经向风 | m s⁻¹ |
| `u700` | 700hPa 纬向风 | m s⁻¹ | `v700` | 700hPa 经向风 | m s⁻¹ |
| `u850` | 850hPa 纬向风 | m s⁻¹ | `v850` | 850hPa 经向风 | m s⁻¹ |

**温度（气压层）**

| 变量 | 含义 | 原始单位 | 变量 | 含义 | 原始单位 |
|------|------|----------|------|------|----------|
| `t10` | 10hPa 温度 | K (→ °C) | `t50` | 50hPa 温度 | K (→ °C) |
| `t100` | 100hPa 温度 | K (→ °C) | `t200` | 200hPa 温度 | K (→ °C) |
| `t500` | 500hPa 温度 | K (→ °C) | `t700` | 700hPa 温度 | K (→ °C) |
| `t850` | 850hPa 温度 | K (→ °C) | | | |

**位势高度与垂直速度（气压层）**

| 变量 | 含义 | 原始单位 | 变量 | 含义 | 原始单位 |
|------|------|----------|------|------|----------|
| `z10` | 10hPa 位势高度 | m² s⁻² | `w10` | 10hPa 垂直速度 | Pa s⁻¹ |
| `z50` | 50hPa 位势高度 | m² s⁻² | `w50` | 50hPa 垂直速度 | Pa s⁻¹ |
| `z200` | 200hPa 位势高度 | m² s⁻² | `w200` | 200hPa 垂直速度 | Pa s⁻¹ |
| `z300` | 300hPa 位势高度 | m² s⁻² | `w500` | 500hPa 垂直速度 | Pa s⁻¹ |
| `z500` | 500hPa 位势高度 | m² s⁻² | `w850` | 850hPa 垂直速度 | Pa s⁻¹ |
| `z700` | 700hPa 位势高度 | m² s⁻² | | | |
| `z850` | 850hPa 位势高度 | m² s⁻² | | | |

**湿度（气压层）**

| 变量 | 含义 | 原始单位 | 变量 | 含义 | 原始单位 |
|------|------|----------|------|------|----------|
| `q10` | 10hPa 比湿 | kg kg⁻¹ | `q50` | 50hPa 比湿 | kg kg⁻¹ |
| `q200` | 200hPa 比湿 | kg kg⁻¹ | `q500` | 500hPa 比湿 | kg kg⁻¹ |
| `q850` | 850hPa 比湿 | kg kg⁻¹ | | | |

**土壤湿度**

| 变量 | 含义 | 原始单位 | 转换说明 |
|------|------|----------|----------|
| `swv_1` | 土壤湿度第 1 层 (0–7cm) | m³ m⁻³ | 体积含水量 (0~1) |
| `swv_2` | 土壤湿度第 2 层 (7–28cm) | m³ m⁻³ | 体积含水量 (0~1) |
| `swv_3` | 土壤湿度第 3 层 (28–100cm) | m³ m⁻³ | 体积含水量 (0~1) |
| `swv_4` | 土壤湿度第 4 层 (100–289cm)| m³ m⁻³ | 体积含水量 (0~1) |

**注意事项**

- 数据为 **Icechunk Zarr** 格式，通过 Icechunk 库访问 S3，与直接下载 GRIB/NetCDF 文件方式不同
- 下载速度受网络延迟和 Icechunk 协议开销影响，**数据量越大效率越高**
- 输出为标准 **NetCDF4** 或 **Zarr** 格式，可用 `xarray` 直接打开

</details>

---

**ERA5 (hourly/monthly)**

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly/monthly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1940年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-Google-4285F4?style=flat-square)
![魔法](https://img.shields.io/badge/魔法-√-3126F0?style=flat-square)

🔗 [🪜 ERA5_GOOGLE](https://console.cloud.google.com/storage/browser/gcp-public-data-arco-era5/raw/ERA5GRIB/HRES)

</details>

<details>
<summary><b>ERA5-pressure</b> · ECMWF 气压层再分析</summary>

***无魔法情况下推荐通过AWS+IDM多线程下载，下载速度最快***

---

**ERA5-pressure (hourly)**

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1940年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-CDS-00CED1?style=flat-square)

🔗 [ERA5-pressure](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-pressure-levels?tab=download)

---

**ERA5-pressure (hourly)**

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1940年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://nsf-ncar-era5.s3.amazonaws.com/index.html#e5.oper.an.pl/) · 📅 数据延迟3-4个月 · 📝 [Python 多线程下载脚本](./sources/s3_downloader_multi.py)（修改 `DATASET_PREFIX` 为 `e5.oper.an.pl`）

---

**ERA5-pressure (monthly)**

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-monthly_mean-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1940年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-CDS-00CED1?style=flat-square)

🔗 [ERA5-pressure (monthly)](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-pressure-levels-monthly-means?tab=download)

---

**ERA5-pressure (daily/7-day/monthly/3-month)**

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1940年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://planette-era5.s3.amazonaws.com/index.html#era5/) · 📅 数据延迟3-4个月 · 数据为zarr格式 · 📝 [Python 下载脚本](./sources/era5_planette_downloader.py)

---

**ERA5 (hourly/monthly)**

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly/monthly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1940年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-Google-4285F4?style=flat-square)
![魔法](https://img.shields.io/badge/魔法-√-3126F0?style=flat-square)

🔗 [🪜 ERA5_GOOGLE](https://console.cloud.google.com/storage/browser/gcp-public-data-arco-era5/raw/ERA5GRIB/HRES)

</details>


<details>
<summary><b>FNL</b> · NCEP 最终分析</summary>

---

**FNL**

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-6_hourly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-2015年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-UCAR-800080?style=flat-square)

🔗 [FNL_UCAR](https://gdex.ucar.edu/datasets/d083003/dataaccess/#)

---

**FNL**

![分辨率](https://img.shields.io/badge/分辨率-1°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-6_hourly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1999年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-UCAR-800080?style=flat-square)

🔗 [FNL_UCAR](https://gdex.ucar.edu/datasets/d083002/dataaccess/#)

</details>

<details>
<summary><b>JRA-3Q</b> · JMA 再分析</summary>

---

**DIAS**

![分辨率](https://img.shields.io/badge/分辨率-1.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly/monthly_mean-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1947年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-DIAS-9CF?style=flat-square)

🔗 [JRA-3Q_DIAS](https://data.diasjp.net/dl/storages/filelist/dataset:645) · ⚠️ 需登录

---

**UCAR (historical)**

![分辨率](https://img.shields.io/badge/分辨率-1.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1947年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-UCAR-800080?style=flat-square)

🔗 [JRA-3Q_UCAR](https://gdex.ucar.edu/datasets/d640000/dataaccess/#)

---

**UCAR (near-real)**

![分辨率](https://img.shields.io/badge/分辨率-1.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-2023年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-UCAR-800080?style=flat-square)

🔗 [JRA-3Q_UCAR](https://gdex.ucar.edu/datasets/d640001/dataaccess/#) · 🔄 近实时

---

**UCAR (monthly)**

![分辨率](https://img.shields.io/badge/分辨率-1.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-monthly_mean-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1947年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-UCAR-800080?style=flat-square)

🔗 [JRA-3Q_UCAR](https://gdex.ucar.edu/datasets/d640002/dataaccess/#)

</details>

<details>
<summary><b>MERRA-2</b> · NASA 再分析 · 🔒 需 Earthdata Login</summary>

![分辨率](https://img.shields.io/badge/分辨率-0.5°×0.625°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly/3hourly/monthly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1980年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA_Earthdata-FF0000?style=flat-square)

⚠️ **需免费注册 [Earthdata Login](https://urs.earthdata.nasa.gov/)，使用 `earthaccess` 库自动处理认证与 S3 凭据。**

主要 short_name：`M2T1NXSLV`（2D 逐时地面 T2M/SLP/风）、`M2I1NXASM`（2D 瞬时分析场）、`M2T1NXFLX`（逐时通量/降水）、`M2I3NPASM`（3D 3h 气压层 72 层）。

协议：OPeNDAP/DAP4 流式 + AWS S3（requester-pays，`earthaccess.open()` 自动换凭据批量下载）。

🔗 [GES DISC](https://disc.gsfc.nasa.gov/datasets?project=MERRA-2) · [FTP](https://goldsmr4.gesdisc.eosdis.nasa.gov/data/)

</details>

<details>
<summary><b>NCEP/NCAR R1</b> · 经典全球再分析 · OPeNDAP</summary>

![分辨率](https://img.shields.io/badge/分辨率-2.5°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-逐日/月均-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1948年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-PSL_THREDDS-00CED1?style=flat-square)

地面（slp/air/pr_wtr/rhum）、气压层 17 层（hgt/uwnd/vwnd/air/shum）；另有 2m 气温、土壤湿度、对流层顶、硫酸盐 AOD 等变量。逐日数据按年分文件。

🔗 📂 [目录](https://psl.noaa.gov/thredds/catalog/Datasets/ncep.reanalysis.derived/surface/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis.derived/surface/air.mon.mean.nc` · 📝 [下载脚本](./sources/download_from_opendap.py)

🔗 via [IRI Data Library](https://iridl.ldeo.columbia.edu/)（dlauth）：`SOURCES/.NOAA/.NCEP-NCAR/.CDAS-1/.MONTHLY/.Intrinsic/.PressureLevel` / `.MSL`（CDAS-1 = R1 月均）

</details>

<details>
<summary><b>NCEP/DOE R2</b> · R1 改进版 · OPeNDAP</summary>

![分辨率](https://img.shields.io/badge/分辨率-2.5°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-逐日/月均-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1979年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-PSL_THREDDS-00CED1?style=flat-square)

🔗 📂 [目录](https://psl.noaa.gov/thredds/catalog/Datasets/ncep.reanalysis2.derived/surface/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis2.derived/surface/mslp.mon.mean.nc` · 📝 [下载脚本](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>NARR</b> · 北美区域再分析 · OPeNDAP</summary>

![分辨率](https://img.shields.io/badge/分辨率-~32km-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-逐日/3小时-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1979年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-PSL_THREDDS-00CED1?style=flat-square)

⚠️ Lambert Conformal 投影，lat/lon 为 2D 数组，需额外处理。

🔗 📂 [目录](https://psl.noaa.gov/thredds/catalog/Datasets/NARR/monolevel/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/NARR/monolevel/air.2m.2024.nc` · 📝 [下载脚本](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>20th Century Reanalysis V2/V2c</b> · 长历史再分析 · OPeNDAP</summary>

![分辨率](https://img.shields.io/badge/分辨率-~2°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-逐日-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1851~2014-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-PSL_THREDDS-00CED1?style=flat-square)

用地表气压观测同化的历史再分析，时间跨度极长。

🔗 📂 [目录](https://psl.noaa.gov/thredds/catalog/Datasets/20thC_ReanV2c/Dailies/pressure/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/20thC_ReanV2c/Dailies/pressure/hgt.2014.nc` · 📝 [下载脚本](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>IRI Data Library</b> · 哥伦比亚大学 IRI · 🔒 需 dlauth 登录 · OPeNDAP</summary>

![分辨率](https://img.shields.io/badge/分辨率-0.25°–2.5°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-逐日/月均-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1871年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-IRI_LDEO-9CF?style=flat-square)

⚠️ **需免费注册 [IRI Data Library](https://iridl.ldeo.columbia.edu/)（支持 Google/GitHub SSO），登录取 dlauth 会话 Cookie；现已要求所有用户登录。**

哥伦比亚大学维护的跨机构气候门户，可经 OPeNDAP 访问各机构**再分析**数据（CDAS-1 = NCEP/NCAR R1、ECMWF ERA-Interim），对应条目均标 `via IRI` 并附已验证 `SOURCES/...` 路径。其余类型（降水 / SST / 陆面 / 季节预报 / 云 / 历史观测 / 气候指数）见各主题章节。

协议：OPeNDAP（`pydap` + `requests.Session`），取数格式 `https://iridl.ldeo.columbia.edu/SOURCES/{路径}/dods`，节点名须精确（如 `.Surface`、`.PressureLevel`）。

🔗 [IRI Data Library](https://iridl.ldeo.columbia.edu/) · [登录](https://iridl.ldeo.columbia.edu/auth/login)

</details>


### 气候数据

<details>
<summary><b>CRU TS</b> · 格点化观测</summary>

![类型](https://img.shields.io/badge/类型-格点化观测-blue?style=flat-square)
![分辨率](https://img.shields.io/badge/分辨率-0.5°-green?style=flat-square)
![时段](https://img.shields.io/badge/时段-1901~现在-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-UEA-00BFFF?style=flat-square)

🔗 [UEA](https://crudata.uea.ac.uk/cru/data/hrg/)

🔗 via [IRI Data Library](https://iridl.ldeo.columbia.edu/)（dlauth）：`SOURCES/.UEA/.CRU/.TS2p1`（CRU-TS2.1）

</details>

<details>
<summary><b>GPCC</b> · 降水数据集</summary>

![类型](https://img.shields.io/badge/类型-降水-blue?style=flat-square)
![分辨率](https://img.shields.io/badge/分辨率-0.25°~2.5°-green?style=flat-square)
![时段](https://img.shields.io/badge/时段-1891~现在-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-DWD-00BFFF?style=flat-square)

🔗 [DWD](https://www.dwd.de/EN/ourservices/gpcc/gpcc.html)

</details>

<details>
<summary><b>GPCP</b> · 全球降水气候学（卫星+站）· OPeNDAP</summary>

![分辨率](https://img.shields.io/badge/分辨率-2.5°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-月均-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1979年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-PSL_THREDDS-00CED1?style=flat-square)

结合卫星与地面观测的全球降水产品。

🔗 📂 [目录](https://psl.noaa.gov/thredds/catalog/Datasets/gpcp/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/gpcp/precip.mon.mean.nc` · 📝 [下载脚本](./sources/download_from_opendap.py)

🔗 via [IRI Data Library](https://iridl.ldeo.columbia.edu/)（dlauth）：`SOURCES/.NASA/.GPCP/.V2p2`（V2.2）/ `.V2p3`（V2.3）

</details>

<details>
<summary><b>CPC 全球降水/最高温</b> · 高分辨率格点观测 · OPeNDAP</summary>

![分辨率](https://img.shields.io/badge/分辨率-0.5°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-逐日-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1979年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-PSL_THREDDS-00CED1?style=flat-square)

站基格点化产品，`precip`（降水）/`tmax`（最高温），分辨率比 GPCP（2.5°）高 5 倍。

🔗 📂 [目录](https://psl.noaa.gov/thredds/catalog/Datasets/cpc_global_precip/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2024.nc` · 📝 [下载脚本](./sources/download_from_opendap.py)

🔗 via [IRI Data Library](https://iridl.ldeo.columbia.edu/)（dlauth）：`SOURCES/.NOAA/.NCEP/.CPC/.UNIFIED_PRCP`（CPC Unified gauge）

</details>

<details>
<summary><b>CPC Blended OLR</b> · 向外长波辐射 · OPeNDAP</summary>

![分辨率](https://img.shields.io/badge/分辨率-1.0°/2.5°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-逐日-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1979年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-PSL_THREDDS-00CED1?style=flat-square)

台风/热带对流研究核心数据，`olr`（W/m²）。

🔗 📂 [目录](https://psl.noaa.gov/thredds/catalog/Datasets/cpc_blended_olr-1deg/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_blended_olr-1deg/olr.day.mean.nc` · 📝 [下载脚本](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>Dai PDSI</b> · Palmer 干旱指数 · OPeNDAP</summary>

![分辨率](https://img.shields.io/badge/分辨率-2.5°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-月均-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1850年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-PSL_THREDDS-00CED1?style=flat-square)

仅陆地，时间跨度 170+ 年的长期干旱监测数据。

🔗 📂 [目录](https://psl.noaa.gov/thredds/catalog/Datasets/dai_pdsi/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/dai_pdsi/pdsi.mon.mean.nc` · 📝 [下载脚本](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>NOAA 全球温度异常</b> · 气候监测 · OPeNDAP</summary>

![分辨率](https://img.shields.io/badge/分辨率-5.0°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-月均-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1880年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-PSL_THREDDS-00CED1?style=flat-square)

全球地表温度异常（`air`，°C），气候变化监测基础数据。

🔗 📂 [目录](https://psl.noaa.gov/thredds/catalog/Datasets/noaaglobaltemp/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/noaaglobaltemp/air.mon.anom.nc` · 📝 [下载脚本](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>JMA 全球温度异常</b> · 气候监测 · OPeNDAP</summary>

![分辨率](https://img.shields.io/badge/分辨率-5.0°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-月均-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1891年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-PSL_THREDDS-00CED1?style=flat-square)

日本气象厅全球地表温度异常（`air`，°C），与 NOAA 温度异常互为交叉验证。

🔗 📂 [目录](https://psl.noaa.gov/thredds/catalog/Datasets/jmatemp/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/jmatemp/air.mon.anom.nc` · 📝 [下载脚本](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>Berkeley Earth</b> · 独立全球地表温度</summary>

![类型](https://img.shields.io/badge/类型-地表温度-blue?style=flat-square)
![分辨率](https://img.shields.io/badge/分辨率-1°-green?style=flat-square)
![时段](https://img.shields.io/badge/时段-1753~现在-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-Berkeley_Earth-00BFFF?style=flat-square)

独立构建的全球陆地与海洋表面温度数据集，常用于气候变暖交叉验证。

🔗 [Berkeley Earth](http://berkeleyearth.org/data/)

</details>

<details>
<summary><b>HadCRUT5</b> · Met Office 陆海温度</summary>

![类型](https://img.shields.io/badge/类型-陆海温度-blue?style=flat-square)
![分辨率](https://img.shields.io/badge/分辨率-5°-green?style=flat-square)
![时段](https://img.shields.io/badge/时段-1850~现在-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-Met_Office-00BFFF?style=flat-square)

英国气象局 Hadley 中心与东英吉利大学 CRU 联合维护，含集合版不确定性评估。

🔗 [HadCRUT5](https://www.metoffice.gov.uk/hadobs/hadcrut5/)

</details>

<details>
<summary><b>GHCN-Daily</b> · 全球历史气候网络（日值）</summary>

![类型](https://img.shields.io/badge/类型-台站观测-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-气温/降水/积雪-green?style=flat-square)
![时段](https://img.shields.io/badge/时段-1763~现在-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NCEI-00CED1?style=flat-square)

全球陆地气象站逐日观测（气温、降水、积雪等），长期气候研究的台站基础数据。

🔗 [NCEI GHCN-Daily](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily)

</details>

<details>
<summary><b>GHCN-Monthly</b> · 全球历史气候网络（月值）</summary>

![类型](https://img.shields.io/badge/类型-台站观测-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-气温/降水-green?style=flat-square)
![时段](https://img.shields.io/badge/时段-1680~现在-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NCEI-00CED1?style=flat-square)

全球陆地气象站月平均统计，适合长期趋势与年代际变化分析。

🔗 [NCEI GHCN-Monthly](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-monthly)

</details>

<details>
<summary><b>ENSO / PDO / QBO</b> · 气候遥相关指数 · via IRI（dlauth）· OPeNDAP</summary>

![类型](https://img.shields.io/badge/类型-气候指数时间序列-blue?style=flat-square)
![来源](https://img.shields.io/badge/来源-IRI-9CF?style=flat-square)

ENSO（Niño3.4 / MEI / SOI）、PDO（太平洋年代际振荡）、QBO（赤道平流层纬向风）等气候遥相关指数（时间序列）。

🔗 via [IRI Data Library](https://iridl.ldeo.columbia.edu/)（dlauth）：`SOURCES/Indices/.PDO` / `.QBO` / `.nino`

</details>


### 实况观测

#### 地面观测

<details>
<summary><b>ASOS/AWOS</b> · 全球机场观测</summary>

![覆盖](https://img.shields.io/badge/覆盖-全球机场-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-多要素-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-实时-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [NOAA](https://www.ncei.noaa.gov/maps/hourly/)

</details>

<details>
<summary><b>SYNOP</b> · 全球地面观测</summary>

![覆盖](https://img.shields.io/badge/覆盖-全球-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-基本气象要素-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-3/6小时-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-OGIMET-00BFFF?style=flat-square)

🔗 [OGIMET](https://www.ogimet.com/)

</details>

<details>
<summary><b>MADIS</b> · 北美多源数据</summary>

![覆盖](https://img.shields.io/badge/覆盖-北美-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-多源数据-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-实时-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [NOAA MADIS](https://madis.ncep.noaa.gov/)

</details>

<details>
<summary><b>NOAA ISD</b> · 全球综合地面数据库</summary>

![覆盖](https://img.shields.io/badge/覆盖-全球2万+站-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-多要素逐时-green?style=flat-square)
![时段](https://img.shields.io/badge/时段-1901~现在-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NCEI-00CED1?style=flat-square)

整合全球地面气象站的小时级观测（气温、露点、风、气压、能见度、天气现象等）。

🔗 [NOAA ISD](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database)

</details>

<details>
<summary><b>Iowa Environmental Mesonet</b> · 多源气象聚合</summary>

![覆盖](https://img.shields.io/badge/覆盖-美国为主-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-ASOS/NWS/雷达-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-近实时-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-IEM-00BFFF?style=flat-square)

聚合 ASOS/METAR、NWS 警报、雷达拼图、道路交通气象等，提供便捷的归档与接口。

🔗 [IEM](https://mesonet.agron.iastate.edu/)

</details>

#### 高空观测

<details>
<summary><b>IGRA</b> · 全球探空</summary>

![覆盖](https://img.shields.io/badge/覆盖-全球-blue?style=flat-square)
![层次](https://img.shields.io/badge/层次-标准层-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日2次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [NOAA IGRA](https://www.ncei.noaa.gov/data/integrated-global-radiosonde-archive/)

</details>

<details>
<summary><b>AMDAR</b> · 全球航线观测</summary>

![覆盖](https://img.shields.io/badge/覆盖-全球航线-blue?style=flat-square)
![层次](https://img.shields.io/badge/层次-飞行层-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-实时-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-WMO-9CF?style=flat-square)

🔗 [WMO AMDAR](https://community.wmo.int/en/activity-areas/aircraft-based-observations)

</details>

#### 自动气象站

<details>
<summary><b>MesoWest</b> · 美国区域站网</summary>

![规模](https://img.shields.io/badge/规模-数千站-blue?style=flat-square)
![区域](https://img.shields.io/badge/区域-美国-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-MesoWest-00BFFF?style=flat-square)

🔗 [MesoWest](https://mesowest.utah.edu/)

</details>

<details>
<summary><b>Weather Underground</b> · 全球个人站</summary>

![规模](https://img.shields.io/badge/规模-全球个人站-blue?style=flat-square)
![区域](https://img.shields.io/badge/区域-全球-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-WUnderground-00BFFF?style=flat-square)

🔗 [WUnderground](https://www.wunderground.com/)

</details>

### 卫星

#### 地球同步卫星

<details>
<summary><b>Himawari-8/9</b> · JMA · 亚太</summary>

![产品](https://img.shields.io/badge/产品-云图/气溶胶-blue?style=flat-square)
![覆盖](https://img.shields.io/badge/覆盖-亚太-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-JAXA-9CF?style=flat-square)

🔗 [JAXA](https://www.eorc.jaxa.jp/ptree/)

</details>

<details>
<summary><b>GOES-16/18</b> · NOAA · 美洲</summary>

![产品](https://img.shields.io/badge/产品-多通道图像-blue?style=flat-square)
![覆盖](https://img.shields.io/badge/覆盖-美洲-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [NOAA STAR GOES](https://www.star.nesdis.noaa.gov/goes/)

</details>

<details>
<summary><b>FY-4A/4B</b> · CMA · 亚洲</summary>

![产品](https://img.shields.io/badge/产品-云图/降水-blue?style=flat-square)
![覆盖](https://img.shields.io/badge/覆盖-亚洲-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NSMC-9CF?style=flat-square)

🔗 [NSMC](http://satellite.nsmc.org.cn/)

</details>

#### 极轨卫星

<details>
<summary><b>Suomi NPP</b> · NASA/NOAA</summary>

![分辨率](https://img.shields.io/badge/分辨率-750m-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-VIIRS数据-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA-FF0000?style=flat-square)

🔗 [NASA LAADS](https://ladsweb.modaps.eosdis.nasa.gov/)

</details>

<details>
<summary><b>JPSS</b> · NOAA</summary>

![分辨率](https://img.shields.io/badge/分辨率-375m-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-多光谱数据-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [NOAA STAR JPSS](https://www.star.nesdis.noaa.gov/jpss/)

</details>

<details>
<summary><b>MODIS</b> · NASA Terra/Aqua 大气产品</summary>

![分辨率](https://img.shields.io/badge/分辨率-250m~1km-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-气溶胶/云/水汽-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA-FF0000?style=flat-square)

Terra/Aqua 卫星 MODIS 传感器大气产品（气溶胶光学厚度、云属性、可降水量等）。

🔗 [NASA LAADS DAAC](https://ladsweb.modaps.eosdis.nasa.gov/)

</details>

<details>
<summary><b>MODIS LST</b> · NASA 地表温度 · 🔒 需 Earthdata Login</summary>

![分辨率](https://img.shields.io/badge/分辨率-1km_0.05°-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-地表温度_LST-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA_Earthdata-FF0000?style=flat-square)

⚠️ **需免费注册 Earthdata Login。**

short_name：`MOD11C1`（Terra 日均 0.05° 全球）、`MOD11A1`（Terra 日均 1km）。

🔗 [LP DAAC](https://lpdaac.usgs.gov/)

</details>

<details>
<summary><b>AIRS</b> · NASA 大气温湿廓线 · 🔒 需 Earthdata Login</summary>

![分辨率](https://img.shields.io/badge/分辨率-~1°-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-温度_湿度_臭氧廓线-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA_Earthdata-FF0000?style=flat-square)

⚠️ **需免费注册 Earthdata Login。**

short_name：`AIRS3STD`（Aqua/AIRS L3 标准产品，日，2002-）。

🔗 [GES DISC](https://disc.gsfc.nasa.gov/datasets/AIRS3STD_006)

</details>

<details>
<summary><b>CERES</b> · NASA 大气顶辐射通量 · 🔒 需 Earthdata Login</summary>

![分辨率](https://img.shields.io/badge/分辨率-1°-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-大气顶_地表辐射-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA_Earthdata-FF0000?style=flat-square)

⚠️ **需免费注册 Earthdata Login。**

short_name：`CERES_EBAF`（月均，2000-）。

🔗 [CERES](https://ceres.larc.nasa.gov/data/)

</details>

<details>
<summary><b>CALIPSO</b> · NASA 气溶胶/云廓线</summary>

![产品](https://img.shields.io/badge/产品-气溶胶_云廓线-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA-FF0000?style=flat-square)

short_name：`CAL_LID_L3_Tropospheric_APro`（L3 气溶胶廓线，月，2006-2023）。

🔗 [CALIPSO](https://www-calipso.larc.nasa.gov/products/)

</details>

<details>
<summary><b>ISCCP</b> · 国际卫星云气候学 · via IRI（dlauth）· OPeNDAP</summary>

![分辨率](https://img.shields.io/badge/分辨率-2.5°-blue?style=flat-square)
![时段](https://img.shields.io/badge/时段-1983年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-IRI-9CF?style=flat-square)

International Satellite Cloud Climatology Project：多卫星融合全球云量/云类型/辐射通量气候态。

🔗 via [IRI Data Library](https://iridl.ldeo.columbia.edu/)（dlauth）：`SOURCES/.ISCCP`

</details>

#### 卫星降水产品

<details>
<summary><b>GPM IMERG</b> · NASA 全球降水 · 🔒 需 Earthdata Login</summary>

![空间分辨率](https://img.shields.io/badge/空间分辨率-0.1°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-30分钟-green?style=flat-square)
![覆盖](https://img.shields.io/badge/覆盖-全球-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA_Earthdata-FF0000?style=flat-square)

⚠️ **需免费注册 Earthdata Login。**

short_name：`GPM_3IMERGHH`（Final 半小时）、`GPM_3IMERGDF`（逐日）、`GPM_3IMERGM`（月均）。

协议：OPeNDAP/DAP4 + AWS S3（`earthaccess`）。

🔗 [GES DISC](https://disc.gsfc.nasa.gov/)

</details>

<details>
<summary><b>CMORPH</b> · 全球降水</summary>

![空间分辨率](https://img.shields.io/badge/空间分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-30分钟-green?style=flat-square)
![覆盖](https://img.shields.io/badge/覆盖-全球-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [CPC](https://www.cpc.ncep.noaa.gov/products/janowiak/cmorph_description.html)

</details>

### 雷达

#### 天气雷达

<details>
<summary><b>NEXRAD</b> · 美国天气雷达网</summary>

![覆盖](https://img.shields.io/badge/覆盖-美国-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-基数据/产品-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [NOAA NCEI](https://www.ncdc.noaa.gov/nexradinv/)

</details>

<details>
<summary><b>OPERA</b> · 欧洲雷达网</summary>

![覆盖](https://img.shields.io/badge/覆盖-欧洲-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-合成产品-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-EUMETNET-9CF?style=flat-square)

🔗 [EUMETNET](https://www.eumetnet.eu/activities/observations-programme/current-activities/opera/)

</details>

### 空气质量

#### 空气质量监测

<details>
<summary><b>AirNow</b> · 美国空气质量</summary>

![覆盖](https://img.shields.io/badge/覆盖-美国-blue?style=flat-square)
![污染物](https://img.shields.io/badge/污染物-主要污染物-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-AirNow-00BFFF?style=flat-square)

🔗 [AirNow](https://www.airnow.gov/)

</details>

<details>
<summary><b>OpenAQ</b> · 全球空气质量</summary>

![覆盖](https://img.shields.io/badge/覆盖-全球-blue?style=flat-square)
![污染物](https://img.shields.io/badge/污染物-多种污染物-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-OpenAQ-00BFFF?style=flat-square)

🔗 [OpenAQ](https://openaq.org/)

</details>

<details>
<summary><b>EPA AirData</b> · 美国室外空气质量</summary>

![覆盖](https://img.shields.io/badge/覆盖-美国-blue?style=flat-square)
![污染物](https://img.shields.io/badge/污染物-PM2.5/O3/SO2/NO2/CO-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-EPA-00BFFF?style=flat-square)

美国环保署监测网逐时/逐日空气质量数据，含历史归档下载。

🔗 [EPA AirData](https://www.epa.gov/outdoor-air-quality-data)

</details>

<details>
<summary><b>WAQI</b> · 全球空气质量指数</summary>

![覆盖](https://img.shields.io/badge/覆盖-全球-blue?style=flat-square)
![污染物](https://img.shields.io/badge/污染物-PM2.5/PM10/AQI-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-WAQI-00BFFF?style=flat-square)

聚合全球数千个监测站的实时 AQI，提供 API 与历史查询。

🔗 [WAQI](https://waqi.info/)

</details>

<details>
<summary><b>EEA Air Quality</b> · 欧洲空气质量</summary>

![覆盖](https://img.shields.io/badge/覆盖-欧洲-blue?style=flat-square)
![污染物](https://img.shields.io/badge/污染物-PM/NO2/O3/SO2-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-EEA-003399?style=flat-square)

欧洲环境署成员国监测站逐时空气质量观测与历史归档。

🔗 [EEA Air Index](https://airindex.eea.europa.eu/)

</details>

#### 空气质量模式

<details>
<summary><b>CAMS</b> · ECMWF 全球空气质量预报</summary>

![分辨率](https://img.shields.io/badge/分辨率-0.4°-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-全球空气质量预报-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-CAMS-00CED1?style=flat-square)

🔗 [CAMS](https://atmosphere.copernicus.eu/)

</details>


## 海洋数据

### 海洋观测

<details>
<summary><b>Argo</b> · 剖面浮标观测</summary>

![平台](https://img.shields.io/badge/平台-剖面浮标-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-温盐深-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-Argo-00BFFF?style=flat-square)

🔗 [Argo GDAC](https://argo.ucsd.edu/data/argo-data/)

</details>

<details>
<summary><b>TAO/TRITON</b> · 锚定浮标阵列</summary>

![平台](https://img.shields.io/badge/平台-锚定浮标-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-海洋气象-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [PMEL](https://www.pmel.noaa.gov/tao/)

</details>

<details>
<summary><b>NDBC</b> · 国家资料浮标中心</summary>

![平台](https://img.shields.io/badge/平台-浮标/岸站-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-风/浪/SST/气压-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

美国沿海及全球浮标/岸站实时与历史海洋气象观测。

🔗 [NOAA NDBC](https://www.ndbc.noaa.gov/)

</details>

<details>
<summary><b>WOD</b> · World Ocean Database 海洋剖面</summary>

![平台](https://img.shields.io/badge/平台-CTD/XBT/Argo-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-温盐深/氧气/营养盐-green?style=flat-square)
![时段](https://img.shields.io/badge/时段-1772~现在-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NCEI-00CED1?style=flat-square)

NCEI 维护的全球最大海洋剖面数据库，整合历年温盐深、化学要素观测。

🔗 [NCEI WOD](https://www.ncei.noaa.gov/products/world-ocean-database)

</details>

<details>
<summary><b>COADS</b> · 船舶/浮标海气观测 · via IRI（dlauth）· OPeNDAP</summary>

![分辨率](https://img.shields.io/badge/分辨率-2°-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-SST_风_气压-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-IRI-9CF?style=flat-square)

Comprehensive Ocean-Atmosphere Data Set：历史船舶/浮标海面观测集成（SST、风、气压等），海洋气候长期统计基础；现行版为 ICOADS。

🔗 via [IRI Data Library](https://iridl.ldeo.columbia.edu/)（dlauth）：`SOURCES/.COADS`

</details>

<details>
<summary><b>Levitus 海洋气候态</b> · via IRI（dlauth）· OPeNDAP</summary>

![分辨率](https://img.shields.io/badge/分辨率-1°-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-温盐氧_气候态-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-IRI-9CF?style=flat-square)

Levitus（WOA94）全球海洋气候态：温/盐/氧多年平均场，1°（Z19 深度层）；海洋模式初始化与验证常用。

🔗 via [IRI Data Library](https://iridl.ldeo.columbia.edu/)（dlauth）：`SOURCES/.LEVITUS94`

</details>

### 海表温度与海冰

<details>
<summary><b>OISST v2</b> · 高分辨率海表温度 + 海冰浓度 · OPeNDAP</summary>

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-逐日-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1981年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-PSL_THREDDS-00CED1?style=flat-square)

`sst`（海温）与 `icec`（海冰浓度）共享 0.25° 网格；另有 1° 月均版本。逐日数据按年分文件。

🔗 📂 [目录](https://psl.noaa.gov/thredds/catalog/Datasets/noaa.oisst.v2.highres/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2024.nc` · 📝 [下载脚本](./sources/download_from_opendap.py)

🔗 via [IRI Data Library](https://iridl.ldeo.columbia.edu/)（dlauth）：`SOURCES/.NOAA/.NCDC/.OISST/.version2p1`（v2.1）

</details>

<details>
<summary><b>ERSST</b> · 重建海表温度（v3/v4/v5/v6）· OPeNDAP</summary>

![分辨率](https://img.shields.io/badge/分辨率-2.0°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-月均-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1854年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-PSL_THREDDS-00CED1?style=flat-square)

基于观测重建的全球海表温度，提供 v3/v4/v5/v6 多版本（推荐 v6）。

🔗 📂 [目录](https://psl.noaa.gov/thredds/catalog/Datasets/noaa.ersst.v6/catalog.html) · OPeNDAP（v3–v6，换版本号）`https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst.v6/sst.mnmean.nc` · 📝 [下载脚本](./sources/download_from_opendap.py)

🔗 via [IRI Data Library](https://iridl.ldeo.columbia.edu/)（dlauth）：`SOURCES/.NOAA/.NCDC/.ERSST/.version5`（v5）

</details>

<details>
<summary><b>COBE / COBE2</b> · 日本气象厅海表温度 · OPeNDAP</summary>

![分辨率](https://img.shields.io/badge/分辨率-1.0°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-月均-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1850年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-PSL_THREDDS-00CED1?style=flat-square)

JMA 长期历史海温重建（COBE2 为现行版，COBE 为前身）。

🔗 📂 [COBE2 目录](https://psl.noaa.gov/thredds/catalog/Datasets/COBE2/catalog.html) · [COBE 目录](https://psl.noaa.gov/thredds/catalog/Datasets/COBE/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/COBE2/sst.mon.mean.nc` · 📝 [下载脚本](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>Kaplan SST</b> · 重建海表温度异常 · OPeNDAP</summary>

![分辨率](https://img.shields.io/badge/分辨率-5.0°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-月均-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1856年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-PSL_THREDDS-00CED1?style=flat-square)

粗网格（5°）SST 异常重建，适合长期趋势研究。

🔗 📂 [目录](https://psl.noaa.gov/thredds/catalog/Datasets/kaplan_sst/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/kaplan_sst/sst.mon.anom.nc` · 📝 [下载脚本](./sources/download_from_opendap.py)

🔗 via [IRI Data Library](https://iridl.ldeo.columbia.edu/)（dlauth）：`SOURCES/.KAPLAN/.EXTENDED`（延展 SST）

</details>

<details>
<summary><b>CoastWatch IMS 海冰</b> · 北极积雪/海冰 1km · OPeNDAP</summary>

![分辨率](https://img.shields.io/badge/分辨率-1km-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-15天-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-2006~2020-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-CoastWatch-00CED1?style=flat-square)

NOAA CoastWatch ERDDAP 托管的 IMS（Interactive Multisensor Snow and Ice Mapping）产品，`IMS_mean`（积雪/海冰存在）。

🔗 [IMS 1km 海冰](https://coastwatch.noaa.gov/erddap/griddap/ims1k_15day_baseline_stats) · 📝 [下载脚本](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>AVHRR OI SST</b> · NOAA/NASA 高分辨率海表温度 · 🔒 需 Earthdata Login</summary>

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-逐日-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1981年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA_Earthdata-FF0000?style=flat-square)

⚠️ **需免费注册 Earthdata Login。**

short_name：`AVHRR_OI-NCEI-L4-GLOB-v2.1`（当前版本，2016-）、`AVHRR_OI-NCEI-L4-GLOB-v2.0`（历史版本，1981-2020）。

协议：OPeNDAP/DAP4 + AWS S3（`earthaccess`）。

🔗 [GES DISC](https://disc.gsfc.nasa.gov/)

</details>

<details>
<summary><b>CCMP Winds</b> · NASA 10m 海面风</summary>

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-6小时-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA-FF0000?style=flat-square)

short_name：`CCMP_WINDS_10M6HR_L4_V3.1`（1993-）。

🔗 [RSS/CCMP](https://www.remss.com/measurements/ccmp/)

</details>

<details>
<summary><b>OSCAR</b> · NASA 海面流</summary>

![分辨率](https://img.shields.io/badge/分辨率-1_3°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-5日-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA-FF0000?style=flat-square)

short_name：`OSCAR_L4_OC_FINAL_V2.0`（1993-2022）。

🔗 [PODAAC](https://podaac.jpl.nasa.gov/dataset/OSCAR_L4_OC_FINAL_V2.0)

</details>

<details>
<summary><b>SMAP</b> · NASA 土壤湿度/海面盐度</summary>

![分辨率](https://img.shields.io/badge/分辨率-9km_0.25°-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-土壤湿度_海面盐度-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA-FF0000?style=flat-square)

short_name：`SPL3SMP_E`（土壤湿度 9km，2015-）、`SMAP_JPL_L3_SSS_CAP_8DAY`（海面盐度 0.25°）。

🔗 [NSIDC](https://nsidc.org/data/SPL3SMP)

</details>

<details>
<summary><b>GRACE/GRACE-FO</b> · NASA 地下水/土壤水</summary>

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-7日-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA-FF0000?style=flat-square)

short_name：`GRACEDADM_CLSM025GL_7D`（2003-）。

🔗 [PODAAC](https://podaac.jpl.nasa.gov/dataset/GRACEDADM_CLSM025GL_7D)

</details>

<details>
<summary><b>NSIDC 海冰 CDR</b> · NASA 海冰浓度</summary>

![分辨率](https://img.shields.io/badge/分辨率-25km-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-逐日-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA-FF0000?style=flat-square)

short_name：`G02202`（1978-）。

🔗 [NSIDC](https://nsidc.org/data/G02202)

</details>

<details>
<summary><b>MODIS 积雪</b> · NASA 积雪覆盖</summary>

![分辨率](https://img.shields.io/badge/分辨率-500m-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-逐日-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA-FF0000?style=flat-square)

short_name：`MOD10A1`（日，2000-）、`MOD10A2`（8日）。

🔗 [NSIDC](https://nsidc.org/data/MOD10A1)

</details>

<details>
<summary><b>GLDAS</b> · NASA 全球陆面数据同化</summary>

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-3小时-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA-FF0000?style=flat-square)

short_name：`GLDAS_NOAH025_3H`（1948-2014）、`NLDAS_FORA0125_H`（北美逐时，1979-）。

🔗 [GLDAS](https://ldas.gsfc.nasa.gov/)

</details>

### 海洋模式

<details>
<summary><b>HYCOM</b> · 美国海军海洋模式</summary>

![分辨率](https://img.shields.io/badge/分辨率-1/12°-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-海洋分析预报-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-HYCOM-00BFFF?style=flat-square)

🔗 [HYCOM 项目](https://www.hycom.org/) · [THREDDS 数据目录](https://tds.hycom.org/thredds/catalog.html)

</details>

<details>
<summary><b>CMEMS</b>（门户）· Copernicus 海洋监测预报 · 🔒 需 Copernicus 账号</summary>

![来源](https://img.shields.io/badge/来源-Copernicus-003399?style=flat-square)
![产品](https://img.shields.io/badge/产品-307产品_1259数据集-green?style=flat-square)

⚠️ **需免费注册 [Copernicus Marine](https://marine.copernicus.eu/) 账号，用 `copernicusmarine` CLI（`describe` / `get` / `subset`）访问。** ⚠️ 原 OPeNDAP/THREDDS/MOTU/FTP（`*.cmems-du.eu`）已整体退役，现统一经 **Marine Data Store + ARCO Zarr/S3** 取数，无体积/带宽配额。

覆盖主题：物理 PHY、生化 BGC、SST、波浪 WAV、海冰 SI、海面风 WIND、海面高度 SL、海洋监测指标 OMI。区域：全球 + 北极/波罗的海/黑海/地中海/IBI/西北陆架。旗舰产品已拆为下列独立条目。

🔗 [Copernicus Marine](https://marine.copernicus.eu/)

</details>

<details>
<summary><b>CMEMS · GLORYS</b> · 全球物理海洋再分析 · 🔒 Copernicus 账号</summary>

![分辨率](https://img.shields.io/badge/分辨率-1/12°-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-温盐流_SSH-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-Copernicus-003399?style=flat-square)

产品 ID `cmems_mod_glo_phy_my_0.083deg_P1D-m`：全球 1/12° 物理（温盐流 + SSH）再分析，日均值。

</details>

<details>
<summary><b>CMEMS · WAVERY</b> · 全球波浪再分析 · 🔒 Copernicus 账号</summary>

![分辨率](https://img.shields.io/badge/分辨率-0.2°-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-波浪-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-Copernicus-003399?style=flat-square)

产品 ID `cmems_mod_glo_wav_my_0.2deg_PT3H-i`：全球 0.2° 波浪再分析，3 小时。

</details>

<details>
<summary><b>CMEMS · BGC</b> · 全球生物地球化学再分析 · 🔒 Copernicus 账号</summary>

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-叶绿素_营养盐_碳-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-Copernicus-003399?style=flat-square)

产品 ID `cmems_mod_glo_bgc_my_0.25deg_P1D-m`：全球 0.25° 生化（叶绿素/营养盐/碳）再分析，日均值。

</details>

<details>
<summary><b>CMEMS · DUACS</b> · 海面高度（ADT/SLA）· 🔒 Copernicus 账号</summary>

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-ADT_SLA_地转流-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-Copernicus-003399?style=flat-square)

多卫星高度计同化的格点海面绝对动力地形（ADT）与异常（SLA），0.25°，日。

</details>

<details>
<summary><b>CMEMS · OSTIA SST NRT</b> · 近实时海表温度 · 🔒 Copernicus 账号</summary>

![分辨率](https://img.shields.io/badge/分辨率-0.05°-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-SST_海冰-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-Copernicus-003399?style=flat-square)

OSTIA 近实时多源融合 SST（0.05°），日。

</details>

### 海洋水色

<details>
<summary><b>Sentinel-3</b> · ESA · 海洋颜色</summary>

![分辨率](https://img.shields.io/badge/分辨率-300m-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-海洋颜色-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-ESA-003399?style=flat-square)

🔗 [Copernicus Data Space](https://dataspace.copernicus.eu/)

</details>

<details>
<summary><b>NASA OB.DAAC</b> · 海洋水色</summary>

![分辨率](https://img.shields.io/badge/分辨率-1km~4km-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-叶绿素/透明度/SST-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA-FF0000?style=flat-square)

MODIS-Aqua / Sentinel-3 / OC-CCI 海洋水色产品（叶绿素 a、透明度、固有光学量）。

🔗 [NASA OceanColor](https://oceancolor.gsfc.nasa.gov/)

</details>

<details>
<summary><b>CoastWatch ERDDAP</b> · NOAA 海岸带数据</summary>

![分辨率](https://img.shields.io/badge/分辨率-多种-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-叶绿素/SST/海冰-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-CoastWatch-00CED1?style=flat-square)

NOAA CoastWatch ERDDAP 服务器，提供海洋水色、SST、海冰等格点数据（griddap 可浏览下载）。

🔗 [CoastWatch ERDDAP](https://coastwatch.noaa.gov/erddap/index.html)

</details>

## 开源代码与工具

<div align="center">

<i>本项目配套的下载工具平台是 [Open Earth Data Kit](https://github.com/wait4xx/open-earth-data-kit)（统一 CLI · catalog · 多协议适配器）。下面精选社区生态中各环节的优秀开源工具，覆盖 <b>数据下载 → 格式处理 → 物理分析 → 可视化</b> 全流程。</i>

</div>

---

#### 🔽 数据下载与访问

| 工具 | 功能 | ⭐ Stars | 📅 最近更新 |
|:-----|:-----|:-------:|:----------:|
| [**cdsapi**](https://github.com/ecmwf/cdsapi) | ECMWF Climate Data Store 官方接口（ERA5 等） | ![GitHub Stars](https://img.shields.io/github/stars/ecmwf/cdsapi?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/ecmwf/cdsapi?style=flat-square) |
| [**ecmwf-opendata**](https://github.com/ecmwf/ecmwf-opendata) | ECMWF 实时开放数据（IFS / EFS / AIFS） | ![GitHub Stars](https://img.shields.io/github/stars/ecmwf/ecmwf-opendata?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/ecmwf/ecmwf-opendata?style=flat-square) |
| [**Herbie**](https://github.com/blaylockbk/Herbie) | 下载 NOAA HRRR / GFS 等模式数据 | ![GitHub Stars](https://img.shields.io/github/stars/blaylockbk/Herbie?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/blaylockbk/Herbie?style=flat-square) |
| [**Siphon**](https://github.com/Unidata/siphon) | THREDDS / OPeNDAP 远程数据访问 | ![GitHub Stars](https://img.shields.io/github/stars/Unidata/siphon?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/Unidata/siphon?style=flat-square) |
| [**satpy**](https://github.com/pytroll/satpy) | 多源卫星数据读取与定标 | ![GitHub Stars](https://img.shields.io/github/stars/pytroll/satpy?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/pytroll/satpy?style=flat-square) |

#### 📊 格点数据处理

| 工具 | 功能 | ⭐ Stars | 📅 最近更新 |
|:-----|:-----|:-------:|:----------:|
| [**xarray**](https://github.com/pydata/xarray) | NetCDF / GRIB 多维数组处理（事实标准） | ![GitHub Stars](https://img.shields.io/github/stars/pydata/xarray?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/pydata/xarray?style=flat-square) |
| [**cfgrib**](https://github.com/ecmwf/cfgrib) | 将 GRIB 映射为 xarray 数据集 | ![GitHub Stars](https://img.shields.io/github/stars/ecmwf/cfgrib?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/ecmwf/cfgrib?style=flat-square) |
| [**netCDF4**](https://github.com/Unidata/netcdf4-python) | 经典 NetCDF 读写库 | ![GitHub Stars](https://img.shields.io/github/stars/Unidata/netcdf4-python?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/Unidata/netcdf4-python?style=flat-square) |
| [**pygrib**](https://github.com/jswhit/pygrib) | GRIB1 / GRIB2 数据读写 | ![GitHub Stars](https://img.shields.io/github/stars/jswhit/pygrib?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/jswhit/pygrib?style=flat-square) |
| [**dask**](https://github.com/dask/dask) | 大规模并行计算（xarray 后端） | ![GitHub Stars](https://img.shields.io/github/stars/dask/dask?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/dask/dask?style=flat-square) |

#### 🌡️ 气象分析与计算

| 工具 | 功能 | ⭐ Stars | 📅 最近更新 |
|:-----|:-----|:-------:|:----------:|
| [**MetPy**](https://github.com/Unidata/MetPy) | 气象计算、分析与可视化 | ![GitHub Stars](https://img.shields.io/github/stars/Unidata/MetPy?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/Unidata/MetPy?style=flat-square) |
| [**WRF-python**](https://github.com/NCAR/wrf-python) | WRF 模式后处理诊断量计算 | ![GitHub Stars](https://img.shields.io/github/stars/NCAR/wrf-python?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/NCAR/wrf-python?style=flat-square) |
| [**xwrf**](https://github.com/xarray-contrib/xwrf) | WRF 数据 xarray 后处理 | ![GitHub Stars](https://img.shields.io/github/stars/xarray-contrib/xwrf?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/xarray-contrib/xwrf?style=flat-square) |
| [**tropycal**](https://github.com/tropycal/tropycal) | 热带气旋追踪与分析 | ![GitHub Stars](https://img.shields.io/github/stars/tropycal/tropycal?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/tropycal/tropycal?style=flat-square) |

#### 📡 雷达数据处理

| 工具 | 功能 | ⭐ Stars | 📅 最近更新 |
|:-----|:-----|:-------:|:----------:|
| [**Py-ART**](https://github.com/ARM-DOE/pyart) | 天气雷达数据处理（ARM） | ![GitHub Stars](https://img.shields.io/github/stars/ARM-DOE/pyart?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/ARM-DOE/pyart?style=flat-square) |
| [**wradlib**](https://github.com/wradlib/wradlib) | 雷达数据反演与分析 | ![GitHub Stars](https://img.shields.io/github/stars/wradlib/wradlib?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/wradlib/wradlib?style=flat-square) |
| [**ACT**](https://github.com/ARM-DOE/ACT) | ARM 大气数据工具包 | ![GitHub Stars](https://img.shields.io/github/stars/ARM-DOE/ACT?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/ARM-DOE/ACT?style=flat-square) |

#### 🎨 可视化与制图

| 工具 | 功能 | ⭐ Stars | 📅 最近更新 |
|:-----|:-----|:-------:|:----------:|
| [**Cartopy**](https://github.com/SciTools/cartopy) | 地图投影与地理制图 | ![GitHub Stars](https://img.shields.io/github/stars/SciTools/cartopy?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/SciTools/cartopy?style=flat-square) |
| [**proplot**](https://github.com/proplot-dev/proplot) | 出版级科研绘图 | ![GitHub Stars](https://img.shields.io/github/stars/proplot-dev/proplot?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/proplot-dev/proplot?style=flat-square) |
| [**geoviews**](https://github.com/holoviz/geoviews) | 交互式地理可视化 | ![GitHub Stars](https://img.shields.io/github/stars/holoviz/geoviews?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/holoviz/geoviews?style=flat-square) |

## 贡献指南

<div align="center">

我们欢迎并感谢所有形式的贡献！请参阅 [**CONTRIBUTING.md**](CONTRIBUTING.md) 了解详细指南。

> 💡 **贡献去向**：补充或修正**数据源、访问说明等指南内容**，请在 [本仓库](https://github.com/wait4xx/open-earth-data-guide) 提 Issue / PR；改进 **`meteo` CLI 工具、下载适配器与后端**，请前往 [Open Earth Data Kit](https://github.com/wait4xx/open-earth-data-kit)。

<br/>

[![报告问题](https://img.shields.io/badge/报告问题-Issues-e05d44?style=for-the-badge&logo=github)](https://github.com/wait4xx/open-earth-data-guide/issues)
[![添加资源](https://img.shields.io/badge/添加资源-Pull_Request-2962ff?style=for-the-badge&logo=github)](https://github.com/wait4xx/open-earth-data-guide/pulls)
[![分享用例](https://img.shields.io/badge/分享用例-Discussions-9CF?style=for-the-badge&logo=github)](https://github.com/wait4xx/open-earth-data-guide/discussions)

<br/>

**📋 提交规范**

`✓ 链接有效`　`✓ 描述清晰`　`✓ 格式统一`　`✓ 注明许可`

</div>

---

## 许可证

<div align="center">

![License: MIT](https://img.shields.io/github/license/wait4xx/open-earth-data-guide?style=for-the-badge&logo=github)

本资源指南采用 **MIT License** 开源，适用于本仓库的**指南内容与下载脚本**。

</div>

> ⚠️ **重要区分**：MIT 协议仅覆盖本仓库自身的内容与代码；清单中链接的第三方数据源（ERA5、NOAA、CMEMS 等）**各有其独立的使用条款与许可协议**，使用数据前请务必查阅并遵守相应数据提供方的规定。本仓库不持有任何数据所有权。

---

## 致谢

<div align="center">

感谢以下数据提供机构，以及每一位为本项目贡献力量的开发者 ✨

<br/>

![CMA](https://img.shields.io/badge/CMA-中国气象局-blue?style=flat-square)
![NOAA](https://img.shields.io/badge/NOAA-美国国家海洋和大气管理局-green?style=flat-square)
![ECMWF](https://img.shields.io/badge/ECMWF-欧洲中期天气预报中心-orange?style=flat-square)
![NASA](https://img.shields.io/badge/NASA-美国国家航空航天局-red?style=flat-square)
![ESA](https://img.shields.io/badge/ESA-欧洲空间局-purple?style=flat-square)
![NCEI](https://img.shields.io/badge/NCEI-环境信息中心-00CED1?style=flat-square)
![DWD](https://img.shields.io/badge/DWD-德国气象局-9CF?style=flat-square)
![Met Office](https://img.shields.io/badge/Met_Office-英国气象局-00BFFF?style=flat-square)
![JMA](https://img.shields.io/badge/JMA-日本气象厅-9CF?style=flat-square)
![Copernicus](https://img.shields.io/badge/Copernicus-欧盟哥白尼-003399?style=flat-square)

<br/>

![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=flat-square&logo=googlecloud&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-FF9900?style=flat-square&logo=amazonaws&logoColor=white)

</div>

---

<div align="center">

<h3>💖 支持本项目</h3>

如果这个资源指南对您有帮助，欢迎点亮 Star、Fork 或分享给同行！

<br/>

[![GitHub Stars](https://img.shields.io/github/stars/wait4xx/open-earth-data-guide?style=for-the-badge&logo=github)](https://github.com/wait4xx/open-earth-data-guide/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/wait4xx/open-earth-data-guide?style=for-the-badge&logo=github)](https://github.com/wait4xx/open-earth-data-guide/network/members)
[![GitHub Watchers](https://img.shields.io/github/watchers/wait4xx/open-earth-data-guide?style=for-the-badge&logo=github)](https://github.com/wait4xx/open-earth-data-guide/watchers)
[![Discussions](https://img.shields.io/badge/Discussions-分享用例-9CF?style=for-the-badge&logo=github)](https://github.com/wait4xx/open-earth-data-guide/discussions)

</div>

---

<div align="center">

<h3>📈 Star History</h3>

<a href="https://star-history.com/#wait4xx/open-earth-data-guide&Date">
<img src="https://api.star-history.com/svg?repos=wait4xx/open-earth-data-guide&type=Date" alt="Star History" width="600">
</a>

</div>

---

<div align="center">

<sub>🔄 数据链接与可用性可能随时间变化 · 发现失效链接或有新资源推荐，请通过 <a href="https://github.com/wait4xx/open-earth-data-guide/issues">Issues</a> 告知我们</sub>

<br/><br/>

<sub><b>Made with ❤️ for the meteorology community</b> · 数据可用性以各提供方为准</sub>

</div>
