def geturl(name):
	t = name.split(" ")

	f = t[0][:2].lower()
	l = t[1][:5].lower()
	fullname = l + f + "01"

	first_letter = l[0]
	p_letter = f[0]
	player = p_letter + t[1].lower()

	return player,"https://www.basketball-reference.com/players/{}/{}".format(first_letter, fullname)

