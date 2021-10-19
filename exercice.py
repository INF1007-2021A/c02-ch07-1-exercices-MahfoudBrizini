#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


def get_fibonacci_number(index):
	# Élements initiaux : 0 et 1
	return (0 if index ==0 else
			1 if index == 1 else
			get_fibonacci_number(index - 1) + get_fibonacci_number(index - 2))
	pass

def get_fibonacci_sequence(lenght):
	#return[get_fibonacci_number(i) for i in range(lenght)]
	seq = [0,1]
	if lenght <= 2:
		return seq[0:lenght]
	for i in range(2,lenght):
		seq.append(seq[-1]+seq[-2])
	return seq
	pass

def get_sorted_dict_by_decimals(elems):
	return dict(sorted(elems.items(),key=lambda elems:elems[1]%1.0))
	pass

def fibonacci_numbers(length):
	init_values = [0,1]
	for elem in init_values[0:lenght]:
		yield elems

def build_recursive_sequence_generator(TODO):
	pass
def nums(lenght):
	pass
# EXAM FAIRE DES FONCTIONS GENERATRICES
if __name__ == "__main__":


	print((lambda minim, maxim,val: max(minim,min(maxim,val)))(0,10,15))

	print([get_fibonacci_number(0), get_fibonacci_number(1), get_fibonacci_number(2)])
	print([get_fibonacci_number(i) for i in range(10)])
	print()

	print(get_fibonacci_sequence(1))
	print(get_fibonacci_sequence(2))
	print(get_fibonacci_sequence(10))
	print()

	spam = {
		2: 2.1,
		3: 3.3,
		1: 1.4,
		4: 4.2
	}
	eggs = {
		"foo": 42.6942,
		"bar": 42.9000,
		"qux": 69.4269,
		"yeet": 420.1337
	}
	print(get_sorted_dict_by_decimals(spam))
	print(get_sorted_dict_by_decimals(eggs))
	print()

	for fibo_num in fibonacci_numbers(10):
		print(fibo_num, end=" ")
	print("\n")

	def fibo_def(last_elems):
		return last_elems[-1] + last_elems[-2]
	fibo = build_recursive_sequence_generator([0, 1], fibo_def)
	for fi in fibo(10):
		print(fi, end=" ")
	print("\n")

	lucas = build_recursive_sequence_generator(TODO)
	print(f"Lucas : {[elem for elem in lucas(10)]}")
	perrin = build_recursive_sequence_generator(TODO)
	print(f"Perrin : {[elem for elem in perrin(10)]}")
	hofstadter_q = build_recursive_sequence_generator(TODO)
	print(f"Hofstadter-Q : {[elem for elem in hofstadter_q(10)]}")
