def rSubString(inputStr1, inputStr2):
	if len(inputStr1) == 0:
		return True
	elif inputStr1[0] not in list(inputStr2):
		return False
	else:
		return rSubString(inputStr1[1:], inputStr2)

print rSubString("abcdef", "abc") 