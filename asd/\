#!/usr/bin/env python
import unittest

n=5
# oto nasz unit
def IsOdd(n):
	return n % 2 == 1
# testy dla naszego unita
class IsOddTests(unittest.TestCase):

	def testOne(self):
		self.failUnless(IsOdd(1))

	def testTwo(self):
		self.failIf(IsOdd(2))

def main():
	unittest.main()

if __name__=='__main__':
	main()

