#!/usr/bin/env python3

import sys
import readline
import re

from modules.Calculator import *
from modules.ComplexNum import *
from modules.Matrix import *

class General:
	def __init__(self):
		pass
	def start(self):
		while True:
			try:
				self.__comand = input()
			except EOFError:
				break
			except :
				print("(interrupt) use CTRL + D for exit")
			else:
				self.__pars()
		print("\nThx for wasted time!")
	def __pars(self):
		self.__comand = re.sub(r'\s', '', self.__comand).lower()
		# Global
		# lst = Calculator(self.__comand)
		# Complex Number
		# tmp2 = ComplexNum(float(self.__comand), 0)
		# print("orig = {0} my = {1}".format(
		# 	(complex(float(self.__comand), 2.3) / complex(1,3)),
		# 	(ComplexNum(float(self.__comand), 2.3) / ComplexNum(1,3))
		# 	))
		# Matrix
		left = re.findall(r'(.+)(?=[\+\-\*\/](?=\[))', self.__comand)[0]
		right = re.findall(r'(?<=(?<=\])[\-\+\/\*])(.+)', self.__comand)[0]
		op = re.findall(r'(?<=\])([\-\+\/\*])(?=\[)', self.__comand)[0]
		A = Matrix(left)
		B = Matrix(right)
		C = None
		if op == '+':
			C = A+B
		elif op == '-':
			C = A-B
		elif op == '*':
			C = A*B
		elif op == '/':
			C = A/B
		# lol = Matrix([[10]]) + Matrix([[20]])
		print(C)
def main():
	g = General()
	g.start()

if __name__ == "__main__":
	main()
