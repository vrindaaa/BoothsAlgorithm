# two's compliment
def two_compliment(num):
	temp = binary(num)
	l = list(temp.strip(""))
	for i in range(len(l)):
		if(l[i]=="0"):
			l[i] = "1"
		else:
			l[i] = "0"
	carry = "1"
	l = l[::-1]
	final = ""
	for i in range(len(l)):
		if(l[i]=="0"):
			if(carry == "0"):
				final = "0" + final
			else:
				final = "1" + final
				carry = "0"
		else:
			if(carry == "0"):
				final = "1" + final
			else:
				final = "0" + final
	return final
# binary
def binary(num):
	if(num>=0):
		temp = bin(num)[2:]
		return "0"*(12 - len(temp)) + temp
	else:
		return(two_compliment(-1*num))