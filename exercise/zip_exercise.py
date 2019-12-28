import zipfile
import os


newZip = zipfile.ZipFile(r"newZip.zip", "w")

for path, dirs, files in os.walk(os.getcwd()):
	for file in files:
		print(file)
		newZip.write(file, compress_type=zipfile.ZIP_DEFLATED)

newZip.close()