import os,sys

# malware api sequence files
MALPATH = './API/1/'
MALFILES = os.listdir(MALPATH)
# normal api sequence files
NORMPATH = './API/0/'
NORMFILES = os.listdir(NORMPATH)

# filtered api
APIFILTER = './filtered_API.txt'

api_list = []
# extract unique api
for i in range(len(MALFILES)):
	filtered_words = []
	r = open(MALPATH+MALFILES[i], mode='r', encoding='utf-8')
	words = r.read().split()
	for j in words:
		if j not in api_list:
			api_list.append(j)

for i in range(len(NORMFILES)):
	filtered_words = []
	r = open(NORMPATH+NORMFILES[i], mode='r', encoding='utf-8')
	words = r.read().split()
	for j in words:
		if j not in api_list:
			api_list.append(j)

with open(APIFILTER, 'w') as f:
	for line in api_list:
		f.write('{0}\n'.format(line))