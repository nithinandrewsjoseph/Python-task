def Sum(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
n = 52
print(Sum(n))