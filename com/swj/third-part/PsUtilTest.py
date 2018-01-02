# -*- coding: utf-8 -*-

# psutil == process and system utilities 系统监控 可以跨平台使用
import psutil
if __name__ == '__main__':
    print(psutil.cpu_count())  # cpu逻辑数量
    print(psutil.cpu_count(logical=False))  # cpu物理核心
    print(psutil.cpu_times())  # 统计CPU的用户／系统／空闲时间
    # for x in range(10):
    #    print( psutil.cpu_percent(interval=1, percpu=True))  # CPU使用率，每秒刷新一次
    print(psutil.virtual_memory())  # 物理内存
    print(psutil.swap_memory())  # 交换内存
    print(psutil.disk_partitions())  # 磁盘分区信息
    print(psutil.disk_usage('E:'))  # 磁盘使用情况
    print(psutil.disk_io_counters())  # 磁盘IO
    print(psutil.net_io_counters())  # 获取网络读写字节/包的个数
    print(psutil.net_if_addrs())  # 获取网络接口信息
    print(psutil.net_if_stats())  # 获取网络接口状态
    print(psutil.net_connections())  # 获取网络连接信息
    print(psutil.pids())  # 获取所有进程ID
    p = psutil.Process(11488)  # 获取指定进程
    print(p.name())
    print(p.exe())  # 进程exe路径
    print(p.cwd())  # 进程工作目录
    print(p.cmdline())  # 进程启动的命令行
    print(p.ppid())  # 父进程ID
    print(p.parent())
    print(p.children())
    print(p.status())
    print(p.username())
    print(p.create_time())
    print(p.cpu_times())
    print(p.memory_info())
    print(p.open_files())
    print(p.connections())
    print(p.num_threads())
    print(p.threads())
    print(p.environ())  # 进程环境变量
    # print(p.terminate())  # 结束进程