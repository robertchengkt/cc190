def strPermute (str1, str2):
	if len(str1) != len(str2):
		return False
	else:
		sortStr1 = sorted[str1]
		sortStr2 = sorted[str2]
		pointer1 = 0
		pointer2 = 0
		for i in range(len(str1)):
			if sortStr1[i] != sortStr2[i]:
				return False
			else:
				pointer1 += 1
				pointer2 += 1
	return True


print strPermute("asdjaisdaoisdjoaisjdoa", "Aaosidaois")