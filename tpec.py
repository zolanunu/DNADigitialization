# -*- coding:utf-8 -*-
# calculate the topological entropy

import math
import re
import os
import sys

def topologicalentropy(strs, k): # 计算给定长度的拓扑熵
	strs_len = len(strs)
	#print(strs_len)
	lk = []
	tpe = 0
	Htop = 0
	for i in range(strs_len-k+1):
		if strs[i:i+k] not in lk:
			lk.append(strs[i:i+k])
	if len(lk) > 1:
		tpe = math.log(len(lk), 4)
		Htop = tpe / k
	return Htop

def multientropy(filedir, length = 100, k = 2): # 输入文件，整段文件计算信息熵
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
		
def mean(strs, k): # 取251bp,然后算平均
	seqs = 0
	count = 0
	for i in range(0, len(strs)-251):
		tseq = strs[i:i+259]
		ec = topologicalentropy(tseq, k)
		seqs = seqs + ec
		count = count + 1
	if count > 0:
		mean = seqs / count
	return mean

# 进来的文件都先格式化一下
def format(filein, fileout):
	fr = open(filein)
	fw = open(fileout, 'w')
	lines = ''
	count = 0
	for line in fr.readlines():
		if re.match('>', line):
			fw.write(lines)
			fw.write("\n"+line)
			lines = ''
			if count > 100:
				break
		else:
			lines = lines + line.strip("\n")


if __name__ == "__main__":
	multientropy("E:\\GraduationProject\\SVD\\HMR195_20\\format")
	
	#print(len(seq))

