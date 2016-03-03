def replaceSpce (str):
	index = 0
	newStr = ""
	for i in str:
		index += 1
		if i == " ":
			newStr = newStr[:index] + "%20" + newStr[index:]
			index += 2
		else:
			newStr = newStr + i
	str = newStr
	return str

print replaceSpce("    asd asoid")