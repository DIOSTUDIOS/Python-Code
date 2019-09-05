import os


def formatTime(longtime):
	import time

	return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(longtime))

def formatByte(number):
	for (scale, label) in [(1024*1024*1024, "GB"), (1024*1024, "MB"), (1024, "KB")]:
		if number >= scale:
			return "%.2f %s" % (number*1.0/scale, label)
		elif number == 1:
			return "1 字节"
		else:
			byte = "%.2f" % (number or 0)

	return (byte[:-3] if byte.endwith(".00") else byte) + "字节"

if __name__ == "__main__":
	fileinfo = os.stat(r"image_1.jpg")
	print("文件完整路径：", os.path.abspath(r"image_1.jpg"))

	print("索引号：", fileinfo.st_ino)
	print("设备名：", fileinfo.st_dev)
	print("文件大小：", formatByte(fileinfo.st_size))
	print("最后一次访问时间：", formatTime(fileinfo.st_atime))
	print("最后一次修改时间：", formatTime(fileinfo.st_mtime))
	print("最后一次状态变化时间：", formatTime(fileinfo.st_ctime))
