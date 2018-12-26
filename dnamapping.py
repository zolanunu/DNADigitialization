# -*- coding:utf-8 -*-
# 

from enum import Enum
import os
def tpedigital(filedir, length = 100, k = 2): # 输入文件，整段文件计算信息熵
	listfile = os.listdir(filedir) # 列出文件夹下的所有的目录和文件
	#print(listfile)
	#print(len(listfile))
	for i in listfile:
		if(i.find(".fasta") > 0):
			filepath = os.path.join(filedir, i)
			writefile = os.path.join(filedir, i[:-13]+"_2.txt")
			#print(writefile)
			#print(filepath)
			fr = open(filepath, "r")
			fw = open(writefile, "w")
			count = 0
			for line in fr.readlines():
				if re.match(">", line):
					continue
				else:
					for i in range(len(line.strip())-length):
						tpecvalue = topologicalentropy(line[i:i+length], k)
						count += 1
						fw.write(str(tpecvalue)+"\n")
						print("tpecvalue= " ,tpecvalue)
					for i in range(len(line.strip())-length, len(line.strip())):
						tpecvalue = topologicalentropy(line[i-length:i], k)
						count += 1
						fw.write(str(tpecvalue)+"\n")
						print("tpecvalue= " ,tpecvalue)
			print(count)
			fr.close()
			fw.close()


if __name__ == "__main__":
	tpedigital("/AJ229040.fasta")