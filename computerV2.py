#!/usr/bin/env python3.5

import sys
import readline
import re

from modules.Calculator import *
from modules.ComplexNum import *

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
		# self.__comand = re.sub(r'\s', '', self.__comand).lower()
		# lst = Calculator(self.__comand)
		# tmp2 = ComplexNum(float(self.__comand), 0)
		print("orig = {0} my = {1}".format(
			(float(self.__comand) / complex(1,3)),
			(float(self.__comand) / ComplexNum(1,3))
			))

def main():
	g = General()
	g.start()

if __name__ == "__main__":
	main()
