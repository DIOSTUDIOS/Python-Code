import os


# print(os.name)
# print(os.linesep)
# print(os.sep)
# print(os.getcwd())
# print(os.listdir(os.getcwd()))
for root, dirs, files in os.walk("\\", topdown = False):
	for name in files:
		print(os.path.join(root, name))