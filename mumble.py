def mumbling(str):
	leng = len(str)
	ret = ""
	for i in range(leng):
		char = str[i]
		ret += char.upper()
		for j in range(i):
			ret += char
		ret += "-"
	return ret
