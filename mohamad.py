import os

list_dir = os.listdir()
print(os.getcwd())
files = []
folders = []

for i in list_dir:
	if(os.path.isdir(i)):
		folders.append(i)
	else:
		files.append(i)

for i in folders:
	print(i)
print()
for i in files:
	print(i)

