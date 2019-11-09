def rightShift(numbers):
  a,b,c = numbers

  newA = a[0] + a[0:-1]
  newB = a[-1] + b[0:-1]
  newC = b[-1]

  return [newA,newB,newC]

def add(numbers):
  a,b = numbers

  carry = 0
  r = ''

  i = max(len(a),len(b)) - 1

  while i >= 0:
    n = int(a[i]) + int(b[i]) + carry
    if n == 0:
      r = '0' + r
      carry = 0
    elif  n == 1:
      r = '1' + r
      carry = 0
    elif n == 2:
      r = '0' + r
      carry = 1
    elif n == 3:
      r = '1' + r
      carry = 1
    i -= 1
  return r

# two's compliment
def two_compliment(num):
	l = list(num.strip(""))
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
		return(two_compliment(binary(-1*num)))

def multiply(num1, num2):
	one = binary(num1)
	two = binary(num2)
	two_comp = two_compliment(two)
	ac = "0"*12 #Accumulator content
	sc = 12 #sequence counter
	q_n1 = "0" #Q_n+1 initially 0
	while(sc>0):
		val = one[-1] + q_n1
		if(val=="01"):
			ac = add([ac, two])
		if(val=="10"):
			ac = add([ac, two_comp])
		ac, one, q_n1 = rightShift([ac, one, q_n1])
		sc-=1
	ans = ac+one
	if(ac[0]=="0"):
		final = int(ans, 2)
	else:
		final = -1*int(two_compliment(ans), 2)
	return [final, ans]

#print(multiply(2, 3))

