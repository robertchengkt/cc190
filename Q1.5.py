def oneEditAway (str1, str2):
	if len(str1) == len(str2):
		return oneEditReplace(str1, str2)
	elif len(str1) + 1 == len(str2):
		return oneEditInsert(str1, str2)
	elif len(str1) - 1 == len(str2):
		return oneEditInsert(str2, str1)
	else:
		return False

# match by replacing a character 
def oneEditReplace(str1, str2):
	isOneEdit = False
	for i in range(len(str1)):
		if str1[i] != str2[i]:
			# check if there is already another difference
			if isOneEdit:
				return False
		else:
			isOneEdit = True

	return True
# match by adding or deleting a character 
def oneEditInsert(str1, str2):
	index1 = 0
	index2 = 0
	while index1 < len(str1) & index2 < len(str2):
		if str1[index1] != str2[index2]:
			if index1 != index2:
				return False
			else:
				index2 += 1
		else:
			index1 += 1
			index2 += 1
	return True 


print oneEditAway("adbc","adc")

