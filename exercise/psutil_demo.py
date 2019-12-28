import psutil
import datetime
from subprocess import PIPE

# print(psutil.cpu_times(percpu=True))

# print(psutil.cpu_count())
# print(psutil.cpu_count(logical=False))
# print(psutil.cpu_times().user)
# print(psutil.cpu_percent())


# print(psutil.virtual_memory())

# print(psutil.disk_partitions())
# print(psutil.disk_usage(r'D:\\'))

# print(psutil.disk_io_counters())
# print(psutil.disk_io_counters(perdisk=True))

# print(psutil.net_io_counters())
# print(psutil.net_io_counters(pernic=True))

# print(psutil.users())

# print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))

print(psutil.pids())

print(psutil.Process(5596).cpu_times())