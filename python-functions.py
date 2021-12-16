def sum_to(n):
  int(n)
  val1 = 0
  val2 = 1
  total = 0
  for x in range(n):
    total = val1 + val2
    val1 += val2
    val2 += 1
  print({total})

# sum_to(6)
# sum_to(10) 



def largest(listOfNums=[]): 
  biggest=listOfNums[0]
  for x in listOfNums:
    if x > biggest:
      biggest = x
  print(biggest)

# largest([1, 2, 3, 4, 0])  # returns 4
# largest([10, 4, 2, 231, 91, 54])  # returns 231



def occurences(str1, str2):
  print(str1.count(str2))

# occurences('fleep floop', 'e')   # returns 2
# occurences('fleep floop', 'p')   # returns 2
# occurences('fleep floop', 'ee')  # returns 1
# occurences('fleep floop', 'fe')  # returns 0


def product(*args):
  total = 1
  for val in args:
    total = total * val
  print(total)

# product(-1, 4) # returns -4
# product(2, 5, 5) # returns 50
# product(4, 0.5, 5) # returns 10.0