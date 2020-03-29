def rightShift(numbers):
  #Right Shift a number divided into two parts a and b. 
  #Store last character of b in c.
  a,b,c = numbers

  newA = a[0] + a[0:-1]
  newB = a[-1] + b[0:-1]
  newC = b[-1]

  return [newA,newB,newC]

def leftShift(numbers):
  #Left shift a number divided into two parts a and b.
  a,b = numbers

  newA = a[1:] + b[0]
  newB = b[1:] + '0'

  return [newA, newB]

def add(numbers):
  #Function to add two binary numbers
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
	#Function to take 2's compliment of a number.
	l = list(num.strip(""))
	#inverting all the digits
	for i in range(len(l)):
		if(l[i]=="0"):
			l[i] = "1"
		else:
			l[i] = "0"
	#adding 1 to the number.
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
	#Returning 2's compliment form of a number num.
	if(num>=0):
		temp = bin(num)[2:]
		return "0"*(12 - len(temp)) + temp
	else:
		return(two_compliment(binary(-1*num)))

def multiply(num1, num2):
	#Function to multiply two numbers using Booth's Algorithm
	q = binary(num1) #one
	m = binary(num2) #two
	m_comp = two_compliment(m) #two_comp
	ac = "0"*12 #Accumulator content
	sc = 12 #sequence counter
	q_n1 = "0" #Q_n+1 initially 0
	while(sc>0):
		val = q[-1] + q_n1
		if(val=="01"):
			ac = add([ac, m])
		if(val=="10"):
			ac = add([ac, m_comp])
		ac, q, q_n1 = rightShift([ac, q, q_n1])
		sc-=1
	ans = ac+q
	if(ac[0]=="0"):
		final = int(ans, 2)
	else:
		final = -1*int(two_compliment(ans), 2)
	return [final, ans]

def divide(num1, num2):
	#Function to divide two numbers using Booth's Algorithm.
	#num1/num2
	rem_neg = False
	compliment_quotient = False
	dividend = binary(num1)
	divisor = binary(num2)
	if(num1<0):
		dividend = two_compliment(dividend)
		rem_neg = True
	if(num2<0):
		divisor = two_compliment(divisor)
	if(num1*num2<0):
		compliment_quotient = True
	if(num2==0):
		print("Error -> Division by 0.")
		return
	divisor_neg = two_compliment(divisor)
	acc = "0"*12
	sc = 12
	while(sc>0):
		acc, dividend = leftShift([acc, dividend])
		acc_old = acc
		acc = add([acc, divisor_neg])
		if(acc[0]=="0"):
			dividend = dividend[:-1] + "1"
		else:
			acc = acc_old
		sc-=1
	rem = acc
	quotient = dividend
	if(rem_neg):
		rem = two_compliment(rem)
	if(compliment_quotient):
		quotient = two_compliment(quotient)
	if(quotient[0]=="1"):
		ans = -1*(int(two_compliment(quotient), 2))
	else:
		ans = int(quotient, 2)
	if(rem[0]=="1"):
		ans2 = -1*(int(two_compliment(rem), 2))
	else:
		ans2 = int(rem, 2)
	return [ans, ans2, quotient, rem]

def check():
	#Function to check correctness of Multiply and Divide Functions
	for i in range(-1000, 1000):
		for j in range(-1000, 1000):
			if(j!=0):
				a, b = divide(i, j)
				if(i!=((j*a)+b)):
					print("DIVIDE FAILED ", i, j)
					exit()
				else:
					print("DIVIDE OK", i, j)
			if((i*j)!=multiply(i, j)[0]):
				print("MULTIPLY FAILED", i, j)
			else:
				print("MULTIPLY OK", i, j)

print("Enter two Numbers")
#Multiplying and dividing 2 numbers.
a, b = map(int, input().split())
file=open("output.txt","w+")
file.write("Two numbers are "+str(a)+" " + str(b)+"\n")
temp = multiply(a, b)
temp2 = divide(a, b)
file.write("Multiplication Answer: "+str(temp[0])+" Binary: "+str(temp[1])+"\n")
file.write("Division Answer: Quotient " + str(temp2[0]) +" Remainder: "+str(temp2[1])+"\n")
file.write("Binary: "+temp2[2]+" "+temp2[3]+"\n")
file.close()
