# -*- coding:utf-8 -*-
# 

from enum import Enum
import os
class Aminoacid:
	A = 0.61+88.3j
	C = 1.07+112.4j
	D = 0.46+110.8j
	E = 0.47+140.5j
	F = 2.02+189.0j
	G = 0.07+60.0j
	H = 0.61+152.6j
	I = 2.22+168.5j
	K = 1.15+175.6j
	L = 1.53+168.5j
	M = 1.18+162.2j
	Y = 1.88+193.0j
	W = 2.65+227.0j
	V = 1.32+141.4j
	P = 1.95+122.2j
	N = 0.06+125.1j
	Q = 148.7j
	R = 0.60+181.2j
	S = 0.05+88.7j
	T = 0.05+118.2j

# 输入的是蛋白质序列
# 
def gcc(seq):
	result = []
	for i in range(len(seq)):
		if seq[i] == "A":
			result.append(Aminoacid.A)
		elif seq[i] == "C":
			result.append(Aminoacid.C)
		elif seq[i] == "R":
			result.append(Aminoacid.R)
		elif seq[i] == "N":
			result.append(Aminoacid.N)
		elif seq[i] == "L":
			result.append(Aminoacid.L)
		elif seq[i] == "D":
			result.append(Aminoacid.D)
		elif seq[i] == "Q":
			result.append(Aminoacid.Q)
		elif seq[i] == "E":
			result.append(Aminoacid.E)
		elif seq[i] == "F":
			result.append(Aminoacid.F)
		elif seq[i] == "G":
			result.append(Aminoacid.G)
		elif seq[i] == "H":
			result.append(Aminoacid.H)
		elif seq[i] == "I":
			result.append(Aminoacid.I)
		elif seq[i] == "K":
			result.append(Aminoacid.K)
		elif seq[i] == "M":
			result.append(Aminoacid.M)
		elif seq[i] == "P":
			result.append(Aminoacid.P)
		elif seq[i] == "S":
			result.append(Aminoacid.S)
		elif seq[i] == "T":
			result.append(Aminoacid.T)
		elif seq[i] == "W":
			result.append(Aminoacid.W)
		elif seq[i] == "Y":
			result.append(Aminoacid.Y)
		elif seq[i] == "V":
			result.append(Aminoacid.V)
	return result

def gccread(filein, fileout):
	list = os.listdir(filein)  # 列出文件夹下所有的目录与文件
	for i in range(0, len(list)):
		path = os.path.join(filein, list[i])
		print(list[i])
		fw = open(fileout + "/" + list[i], "w")
		if os.path.isfile(path):
			fr = open(path, "r")
			for eachline in fr.readlines():
				if ">" in eachline:
					continue
				else:
					result = gcc(eachline)
					for item in result:
						fw.write(str(item))
						fw.write("\n")
		fw.close()

def freoccurread(filein, fileout):
	list = os.listdir(filein)  # 列出文件夹下所有的目录与文件
	for i in range(0, len(list)):
		path = os.path.join(filein, list[i])
		print(list[i])
		fw = open(fileout + "/" + list[i], "w")
		if os.path.isfile(path):
			fr = open(path, "r")
			for eachline in fr.readlines():
				if ">" in eachline:
					continue
				else:
					result = frencleoccur(eachline)
					for item in result:
						fw.write(str(item))
						fw.write("\n")
		fw.close()

def frencleoccur(seq):
	result = []
	for i in range(len(seq)):
		if seq[i] == "A":
			result.append(0.22750)
		elif seq[i] == "C":
			result.append(0.28312)
		elif seq[i] == "G":
			result.append(0.27600)
		elif seq[i] == "T":
			result.append(0.21336)
	return result

def atomicnumberread(filein, fileout):
	list = os.listdir(filein)  # 列出文件夹下所有的目录与文件
	for i in range(0, len(list)):
		path = os.path.join(filein, list[i])
		print(list[i])
		fw = open(fileout + "/" + list[i], "w")
		if os.path.isfile(path):
			fr = open(path, "r")
			for eachline in fr.readlines():
				if ">" in eachline:
					continue
				else:
					result = atomicnumber(eachline)
					for item in result:
						fw.write(str(item))
						fw.write("\n")
		fw.close()

def atomicnumber(seq):
	result = []
	for i in range(len(seq)):
		if seq[i] == "A":
			result.append(70)
		elif seq[i] == "C":
			result.append(58)
		elif seq[i] == "G":
			result.append(78)
		elif seq[i] == "T":
			result.append(66)
	return result

def twobinaryread(filein, fileout):
	list = os.listdir(filein)  # 列出文件夹下所有的目录与文件
	for i in range(0, len(list)):
		path = os.path.join(filein, list[i])
		print(list[i])
		fw = open(fileout + "/" + list[i], "w")
		if os.path.isfile(path):
			fr = open(path, "r")
			for eachline in fr.readlines():
				if ">" in eachline:
					continue
				else:
					result = twobinary(eachline)
					for item in result:
						fw.write(str(item))
						fw.write("\n")
		fw.close()

def twobinary(seq):
	result = []
	for i in range(len(seq)):
		if seq[i] == "A":
			result.append("00")
		elif seq[i] == "C":
			result.append("11")
		elif seq[i] == "G":
			result.append("10")
		elif seq[i] == "T":
			result.append("01")
	return result

def eiipread(filein, fileout):
	list = os.listdir(filein)  # 列出文件夹下所有的目录与文件
	for i in range(0, len(list)):
		path = os.path.join(filein, list[i])
		print(list[i])
		fw = open(fileout + "/" + list[i], "w")
		if os.path.isfile(path):
			fr = open(path, "r")
			for eachline in fr.readlines():
				if ">" in eachline:
					continue
				else:
					result = eiip(eachline)
					for item in result:
						fw.write(str(item))
						fw.write("\n")
		fw.close()

def eiip(seq):
	result = []
	for i in range(len(seq)):
		if seq[i] == "A":
			result.append(0.1260)
		elif seq[i] == "C":
			result.append(0.1340)
		elif seq[i] == "G":
			result.append(0.0806)
		elif seq[i] == "T":
			result.append(0.1335)
	return result

if __name__ == "__main__":
	inputfile = "D:/zola_workspace/worklab/entropyproject/newSVD/dataset/dna/format"
	outputfile = "D:/zola_workspace/worklab/entropyproject/newSVD/result/dnamapping"
	twobinaryread(inputfile, outputfile)

	#print(Aminoacid.V)
	#print(gcc("MANKGPSYGMSREVQSKIEKKYDEELEERLVEWIIVQCGPDVGRPDRGRLGFQ"))
	#print("end")