def rightShift(numbers):
  a,b,c = numbers

  newA = a[0] + a[0:-1]
  newB = a[-1] + b[0:-1]
  newC = b[-1]

  return [newA,newB,newC]

def leftShift(numbers):
  a,b = numbers

  newA = a[1:] + b[0]
  newB = b[1:] + '0'

  return [newA, newB]

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


