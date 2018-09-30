import re



left = ['(', '[', '{', '<']
right = [')', ']', '}', '>']
cache = []

def check(string):
	for char in string:
		if char in left + right:
			if char in left:
				cache.append(char)
				print(cache)
			elif char in right and char == right[left.index(cache[-1])]:
				cache.pop(-1)
				print(cache)
			else:
				return False

def main():
	if check(input()) is False:
		print("no")
	else:
		print("yes")

main()