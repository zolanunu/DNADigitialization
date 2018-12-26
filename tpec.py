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

