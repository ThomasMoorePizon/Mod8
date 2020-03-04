import itertools
import string
import copy

allchar = string.printable
print("We will start with all of the printable characters")
print(allchar)

"""Working with Copy"""
x = [1,2,3]
print("x:")
print(x)
y = x
print("y:")
print(y)
x.append(4)
print("x after append:")
print(x)
print("y after append:")
print(y)
x = [4,5]
print("x after reassignment:")
print(x)
print("y after x was reassigned:")
print(y)
y = copy.copy(x)
print("x:")
print(x)
print("y:")
x.append(4)
print("x after append using copy:")
print(x)
print("y after x append using copy:")
print(y)


"""For easier demo we will use just the letters abc"""
testletters = ['a','b','c']
print("Print the test case letters for demo")
print(testletters)

"""All of the combinations of length 2"""
combotwo = itertools.combinations(testletters,2)
print("All the combinations of length 2")
for each in combotwo:
	print(each)

"""All of the permutations of length 2"""
permtwo = itertools.permutations(testletters, 2)
print("All the permutations of length 2")
for each in permtwo:
	print(each)

"""Combinations with replacements"""
combotwore = itertools.combinations_with_replacement(testletters, 2)
print("All the combinations with replacement of length 2")
for each in combotwore:
	print(each)

"""You might think that you could just create a dictionary directly"""
dicttwo = dict.fromkeys(testletters, 2)
print("Dictionary of 2")
print(dicttwo)

"""Using Stackoverflow search: https://stackoverflow.com/questions/7074051/what-is-the-best-way-to-generate-all-possible-three-letter-strings"""
from itertools import product
testwordslist = [''.join(i) for i in product(testletters, repeat = 2)]
print("All words of length 2 List")
print(testwordslist)

testwordsgen = (''.join(i) for i in product(testletters, repeat = 2))
print("All words of length 2 Generator")
for each in testwordsgen:
	print(each)

"""Code without the join"""
letterlist = itertools.product(testletters, repeat = 2)
print("If you leave off the join, you list of letters not words")
for each in letterlist:
	print(each)

"""This is similiar to the Deck of Cards from: https://realpython.com/python-itertools/"""
ranks = ['Ace','King','Queen','Jack','10','9','8','7','6','5','4','3','2','1']
suits = ['Hearts','Diamonds','Clubs','Spades']
cards = ((rank,suit) for rank in ranks for suit in suits)
print("A Deck of Cards")
for each in cards:
	print(each)

