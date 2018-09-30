import re



left = ['(', '[', '{', '<']
right = [')', ']', '}', '>']
cache = []

def check(string):
	for char in string:
		if char in left + right:
			if char in left:
				cache.append(char)
			elif char in right and char == right[left.index(cache[-1])]:
				cache.pop(-1)
			else:
				return False

def main():
	if not check(input()):
		print("no")
	else:
		print("yes")

main()