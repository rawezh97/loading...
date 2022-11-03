import os
import time

loading = "loading..."

for i in range(0,5):
	array_list = []
	os.system("clear")

	for j in range(0,len(loading)):
		array_list.append(loading[j])
		print(''.join(array_list) , end = "\r")
		time.sleep(0.1)
