# -*- coding: utf-8 -*-
'''
Created on 2025/11/26 22:04

@Author  : XX
@File    : ifs_oper_download.py
@Software: Visual Studio Code

'''

import requests
from bs4 import BeautifulSoup
import os
import re
import time
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from tqdm import tqdm
from datetime import datetime, timedelta

class HighSpeedDownloader:
    def __init__(self, download_dir="./downloads", max_workers=5, timeout=60, retry_count=3):
        self.download_dir = download_dir
        self.max_workers = max_workers  # 用于同时下载多个文件的线程数
        self.timeout = timeout  # 单个请求超时时间
        self.retry_count = retry_count  # 下载失败重试次数
        self.session = requests.Session()
        
        # 创建下载目录
        os.makedirs(download_dir, exist_ok=True)
        
        # 设置请求头，模拟浏览器
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': '*/*',
            'Accept-Encoding': 'identity'  # 避免压缩，便于计算进度
        })

    def extract_file_links(self, url, file_extensions=None, pattern=None):
        """
        从网页提取包含特定后缀或模式的文件链接
        """
        try:
            print(f"正在分析网页: {url}")
            response = self.session.get(url, timeout=30)  # 增加超时时间
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            file_links = []
            
            # 查找所有链接
            for link in soup.find_all('a', href=True):
                file_url = urljoin(url, link['href'])
                
                # 过滤掉目录链接和上级目录链接
                if file_url.endswith('/') or '/../' in file_url:
                    continue
                    
                filename = os.path.basename(urlparse(file_url).path)
                
                if not filename:  # 跳过没有文件名的链接
                    continue
                
                # 基于后缀过滤
                if file_extensions:
                    if any(filename.lower().endswith(ext.lower()) for ext in file_extensions):
                        file_links.append(file_url)
                        continue
                
                # 基于正则模式过滤
                if pattern and re.search(pattern, filename, re.IGNORECASE):
                    file_links.append(file_url)
            
            print(f"找到 {len(file_links)} 个候选文件")
            return list(set(file_links))  # 去重
            
        except Exception as e:
            print(f"提取文件链接时出错: {e}")
            return []

    def get_file_size(self, url):
        """获取远程文件大小"""
        try:
            response = self.session.head(url, timeout=15, allow_redirects=True)
            if response.status_code == 200:
                size = int(response.headers.get('content-length', 0))
                return size
            else:
                print(f"HEAD请求失败 {url}: 状态码 {response.status_code}")
        except Exception as e:
            print(f"获取文件大小失败 {url}: {e}")
        return 0

    def filter_large_files(self, file_urls, min_size_mb=100):
        """过滤出大于指定大小的文件"""
        tqdm.write("正在检查文件大小...")
        large_files = []
        
        with ThreadPoolExecutor(max_workers=min(5, len(file_urls))) as executor:
            future_to_url = {executor.submit(self.get_file_size, url): url for url in file_urls}
            
            for future in tqdm(as_completed(future_to_url), total=len(file_urls), desc="检查文件大小"):
                url = future_to_url[future]
                try:
                    size = future.result()
                    if size > 0:
                        size_mb = size / (1024 * 1024)
                        if size_mb >= min_size_mb:
                            large_files.append((url, size))
                            tqdm.write(f"✓ {os.path.basename(urlparse(url).path)} - {size_mb:.1f} MB")
                        else:
                            tqdm.write(f"✗ {os.path.basename(urlparse(url).path)} - {size_mb:.1f} MB (小于 {min_size_mb}MB)")
                    else:
                        tqdm.write(f"✗ {os.path.basename(urlparse(url).path)} - 无法获取文件大小")
                except Exception as e:
                    tqdm.write(f"检查文件大小失败 {url}: {e}")
        
        return large_files

    def wait_for_download_completion(self, filepath, expected_size, timeout=10):
        """等待文件下载完成并稳定"""
        start_time = time.time()
        last_size = -1
        stable_count = 0
        
        while time.time() - start_time < timeout:
            if not os.path.exists(filepath):
                return False
                
            current_size = os.path.getsize(filepath)
            
            # 如果文件大小达到预期，等待一小段时间确认稳定
            if current_size == expected_size:
                stable_count += 1
                if stable_count >= 2:  # 连续2次检查大小稳定
                    return True
            else:
                stable_count = 0
                
            # 如果文件大小没有变化，可能是下载完成
            if current_size == last_size:
                stable_count += 1
                if stable_count >= 3:  # 连续3次检查大小不变
                    return current_size == expected_size
            else:
                stable_count = 0
                
            last_size = current_size
            time.sleep(0.5)  # 短暂等待后再次检查
        
        # 超时后检查最终大小
        return os.path.exists(filepath) and os.path.getsize(filepath) == expected_size

    def download_single_file(self, file_info):
        """下载单个文件，支持断点续传"""
        url, expected_size = file_info
        filename = os.path.basename(urlparse(url).path) or f"download_{hash(url)}.grib2"
        filepath = os.path.join(self.download_dir, filename)
        temp_filepath = filepath + '.tmp'  # 临时文件，下载完成后重命名
        
        # 检查是否已有完整文件
        if os.path.exists(filepath) and os.path.getsize(filepath) == expected_size:
            tqdm.write(f"文件已存在且完整: {filename}")
            return True
        
        # 检查是否有临时文件（部分下载的文件）
        downloaded_size = 0
        if os.path.exists(temp_filepath):
            downloaded_size = os.path.getsize(temp_filepath)
            if downloaded_size == expected_size:
                # 临时文件已经完整，重命名为正式文件
                os.rename(temp_filepath, filepath)
                tqdm.write(f"发现完整临时文件，重命名: {filename}")
                return True
            elif downloaded_size > expected_size:
                # 临时文件异常，大于预期大小，删除重新下载
                tqdm.write(f"临时文件异常（大小{downloaded_size} > 预期{expected_size}），重新下载: {filename}")
                os.remove(temp_filepath)
                downloaded_size = 0
            else:
                tqdm.write(f"发现部分下载的临时文件，继续下载: {filename} ({downloaded_size}/{expected_size} bytes)")
        
        # 重试机制
        for attempt in range(self.retry_count):
            try:
                # 设置Range头以支持断点续传
                headers = {}
                if downloaded_size > 0:
                    headers['Range'] = f'bytes={downloaded_size}-'
                    tqdm.write(f"从字节 {downloaded_size} 处继续下载")
                
                # 使用流式下载
                response = self.session.get(url, stream=True, timeout=self.timeout, headers=headers)
                
                # 检查服务器响应
                if downloaded_size > 0 and response.status_code == 200:
                    # 服务器不支持断点续传，需要重新下载
                    tqdm.write("服务器不支持断点续传，重新下载")
                    downloaded_size = 0
                    if os.path.exists(temp_filepath):
                        os.remove(temp_filepath)
                    # 重新设置Range头
                    headers = {}
                
                response.raise_for_status()
                
                # 计算剩余需要下载的大小
                content_length = 0
                if 'content-range' in response.headers:
                    # 服务器返回了内容范围，解析实际大小
                    content_range = response.headers.get('content-range', '')
                    if '/' in content_range:
                        total_size_from_header = int(content_range.split('/')[-1])
                        if total_size_from_header != expected_size:
                            tqdm.write(f"警告: 服务器返回的文件大小与预期不符 ({total_size_from_header} vs {expected_size})")
                elif response.status_code == 206:  # 部分内容
                    content_length = int(response.headers.get('content-length', 0))
                else:  # 全部内容
                    content_length = int(response.headers.get('content-length', 0))
                    if content_length > 0 and content_length != expected_size:
                        tqdm.write(f"警告: 服务器返回的文件大小与预期不符 ({content_length} vs {expected_size})")
                
                # 创建进度条，从已下载的位置开始
                progress_bar = tqdm(
                    total=expected_size, 
                    initial=downloaded_size,
                    unit='B', 
                    unit_scale=True, 
                    desc=filename[:40].ljust(40),  # 限制描述长度
                    leave=False,  # 下载完成后清除进度条
                    dynamic_ncols=True,  # 动态调整进度条宽度
                    mininterval=0.1,  # 更频繁地更新显示
                )
                
                current_size = downloaded_size
                last_activity_time = time.time()
                
                # 打开文件，如果已存在部分内容则追加，否则新建
                mode = 'ab' if downloaded_size > 0 else 'wb'
                with open(temp_filepath, mode) as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            f.flush()  # 确保数据写入磁盘
                            current_size += len(chunk)
                            progress_bar.update(len(chunk))
                            last_activity_time = time.time()  # 更新最后活动时间
                        
                        # 检查连接是否超时（超过30秒没有数据）
                        if time.time() - last_activity_time > 30:
                            raise requests.exceptions.Timeout("连接超时，超过30秒没有收到数据")
                
                # 确保进度条显示最终大小
                progress_bar.n = expected_size
                progress_bar.refresh()
                progress_bar.close()
                
                # 显式关闭响应
                response.close()
                
                # 等待下载完成并稳定
                tqdm.write(f"等待文件 {filename} 稳定...")
                if self.wait_for_download_completion(temp_filepath, expected_size, timeout=15):
                    # 下载完成且文件稳定，重命名临时文件为正式文件
                    os.rename(temp_filepath, filepath)
                    tqdm.write(f"✓ 下载完成: {filename}")
                    return True
                else:
                    # 文件大小不匹配或文件不稳定
                    final_size = os.path.getsize(temp_filepath)
                    tqdm.write(f"✗ 文件大小不匹配或下载不稳定: {filename} ({final_size} vs {expected_size})")
                    
                    # 检查是否是服务器返回的大小与预期不符
                    if final_size > 0 and final_size < expected_size:
                        # 可能是服务器上的文件实际大小与HEAD请求获取的大小不同
                        # 尝试重新获取文件大小
                        new_expected_size = self.get_file_size(url)
                        if new_expected_size > 0 and new_expected_size == final_size:
                            tqdm.write(f"文件大小已更新: {filename} ({expected_size} -> {new_expected_size})")
                            os.rename(temp_filepath, filepath)
                            return True
                    
                    # 保留临时文件，下次可以继续下载
                    if attempt < self.retry_count - 1:
                        tqdm.write(f"准备重试 ({attempt + 1}/{self.retry_count})...")
                        time.sleep(2)  # 等待2秒后重试
                    continue
                    
            except requests.exceptions.Timeout as e:
                tqdm.write(f"下载超时 {filename}: {e}")
                # 保留已下载的部分，下次继续
                if attempt < self.retry_count - 1:
                    tqdm.write(f"准备重试 ({attempt + 1}/{self.retry_count})...")
                    time.sleep(2)
                continue
                    
            except requests.exceptions.RequestException as e:
                tqdm.write(f"网络错误 {filename} (尝试 {attempt + 1}/{self.retry_count}): {e}")
                # 保留已下载的部分，下次继续
                if attempt < self.retry_count - 1:
                    tqdm.write(f"准备重试 ({attempt + 1}/{self.retry_count})...")
                    time.sleep(2)
                continue
                
            except Exception as e:
                tqdm.write(f"下载失败 {filename} (尝试 {attempt + 1}/{self.retry_count}): {e}")
                # 对于其他异常，删除临时文件重新开始
                if os.path.exists(temp_filepath):
                    os.remove(temp_filepath)
                
                if attempt < self.retry_count - 1:
                    tqdm.write(f"准备重试 ({attempt + 1}/{self.retry_count})...")
                    time.sleep(2)
                continue
        
        tqdm.write(f"✗ 下载失败: {filename} (已尝试 {self.retry_count} 次)")
        # 如果最终失败，保留临时文件以便手动恢复
        if os.path.exists(temp_filepath):
            tqdm.write(f"部分下载的文件保留在: {temp_filepath}")
        return False

    def batch_download(self, url, file_extensions=None, pattern=None, min_size_mb=100, max_downloads=None):
        """批量下载文件的主函数"""
        print("=" * 50)
        print("开始批量下载任务")
        print("=" * 50)
        
        # 1. 提取文件链接
        file_urls = self.extract_file_links(url, file_extensions, pattern)
        if not file_urls:
            print("未找到符合条件的文件链接")
            return 0
        
        # 2. 过滤大文件
        large_files = self.filter_large_files(file_urls, min_size_mb)
        if not large_files:
            print("未找到大于指定大小的文件")
            return 0
        
        print(f"找到 {len(large_files)} 个大于 {min_size_mb}MB 的文件")
        
        # 限制下载数量
        if max_downloads and len(large_files) > max_downloads:
            large_files = large_files[:max_downloads]
            print(f"限制下载前 {max_downloads} 个文件")
        
        # 3. 多线程下载文件（每个文件一个线程，不分块）
        print(f"开始多线程下载（同时下载 {self.max_workers} 个文件）...")
        successful_downloads = 0
        
        # 使用线程池执行下载任务
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # 提交所有下载任务
            future_to_file = {
                executor.submit(self.download_single_file, file_info): file_info 
                for file_info in large_files
            }
            
            # 处理完成的任务
            for future in tqdm(as_completed(future_to_file), total=len(large_files), desc="总体进度".ljust(10)):
                file_info = future_to_file[future]
                url, size = file_info
                filename = os.path.basename(urlparse(url).path)
                
                try:
                    if future.result():
                        successful_downloads += 1
                except Exception as e:
                    tqdm.write(f"下载任务异常 {filename}: {e}")
        
        print(f"下载完成: {successful_downloads}/{len(large_files)} 个文件成功下载")
        return successful_downloads

def check_url(url):
    """检查URL是否可访问"""
    try:
        # 使用HEAD方法检查，但有些服务器可能不支持HEAD，所以也尝试GET
        try:
            response = requests.head(url, timeout=10, allow_redirects=True)
            if response.status_code == 200:
                return url, True
        except:
            pass
            
        # 如果HEAD失败，尝试GET但只读取少量内容
        response = requests.get(url, timeout=10, stream=True, allow_redirects=True)
        if response.status_code == 200:
            response.close()  # 立即关闭连接，不下载内容
            return url, True
        return url, False
    except:
        return url, False

def get_url(data_symbol):
    """获取最新的可用数据URL"""
    time_now = datetime.utcnow()
    candidate_urls = []

    # 根据不同的数据请求类型，生成不同的URL
    url_ecmwf = "https://data.ecmwf.int/forecasts/"
    url_gfs = "https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/gfs."
    if data_symbol == 'IFS':
        # scda 目录已退役（2026-10 实测 404），06z/18z 确定性预报统一在 oper/
        url_input = "/ifs/0p25/oper/"
    elif data_symbol == 'IFS01':
        # 0.1°（约9km）分发网格（2026-10-20 起），-sfc/-pl 分文件，比 0p25 晚约2h上线
        url_input = "/ifs/0p1/oper/"
    elif data_symbol == 'EFS':
        url_input = "/ifs/0p25/enfo/"
    elif data_symbol == 'EFS01':
        url_input = "/ifs/0p1/enfo/"
    elif data_symbol == 'AIFS':
        url_input = "/aifs-single/0p25/oper/"
    elif data_symbol == 'AIEFS':
        url_input = "/aifs-ens/0p25/enfo/"
    elif data_symbol == 'GFS':
        url_input = "/atmos/"
    else:
        raise ValueError(f"未知数据请求类型：{data_symbol}（可选 IFS / IFS01 / EFS / EFS01 / AIFS / AIEFS / GFS）")


    # 保存基础路径，每次循环重新计算
    base_url_input = url_input

    # 生成最近 4 个可能的时次（按优先级排序）
    for i in range(4):
        dt = time_now - timedelta(hours=6 * i)
        date_str = dt.strftime("%Y%m%d")
        cycle = dt.hour // 6  # 0,1,2,3 → 0,6,12,18
        hour_str = f"{cycle * 6:02d}"

        url_input = base_url_input
        if data_symbol in ['IFS', 'IFS01', 'EFS', 'EFS01', 'AIFS', 'AIEFS']:
            url_latest = url_ecmwf + f"{date_str}/{hour_str}z" + url_input
        elif data_symbol == 'GFS':
            url_latest = url_gfs + f"{date_str}/{hour_str}" + url_input
        else:
            raise ValueError(f"未知数据请求类型：{data_symbol}")
        
        candidate_urls.append(url_latest)

    print("正在检查候选URL...")
    available_urls = {}
    
    # 并行检查URL可用性
    with ThreadPoolExecutor(max_workers=len(candidate_urls)) as executor:
        future_to_url = {executor.submit(check_url, url): url for url in candidate_urls}
        
        for future in as_completed(future_to_url):
            url, is_available = future.result()
            available_urls[url] = is_available
            status = "可用" if is_available else "不可用"
            print(f"  {url} - {status}")

    # 按候选顺序（即时间从新到旧）选择第一个可用的
    for url in candidate_urls:
        if available_urls.get(url, False):
            print(f"选择最新可用数据网址：{url}")
            return url

    raise RuntimeError("所有候选 URL 均不可用")


# 使用示例
if __name__ == "__main__":
    # 创建下载器实例
    downloader = HighSpeedDownloader(
        download_dir="./ifs_data",  # 下载目录
        max_workers=4,              # 同时下载的文件数
        timeout=10,                # 单个请求超时时间（秒）
        retry_count=3               # 下载失败重试次数
    )
    
    try:
        # 获取目标网页URL（可选：IFS / IFS01(0.1°) / EFS / EFS01(0.1°) / AIFS / AIEFS / GFS）
        target_url = get_url('IFS')
        
        # 开始批量下载
        success_count = downloader.batch_download(
            url=target_url,
            file_extensions=['.grib2', '.grb2', '.grib', '.grb'],  # GRIB文件后缀
            min_size_mb=50,              # 最小文件大小50MB
            # max_downloads=8              # 最大下载文件数
        )
        
        print(f"任务完成，成功下载 {success_count} 个文件")
        
    except Exception as e:
        print(f"程序执行出错: {e}")