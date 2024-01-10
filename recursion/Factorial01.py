def factorial_1(n):
  the_product = 1
  while n > 0:
    the_product *= n 
    n -= 1
  return the_product

def factorial_2(n):
  the_product = 1
  if n == 0: 
    return 1
  return n * factorial_2(n-1) 

print(str(factorial_2(3))) 


"""
🤔 중간 중간 결과는 어디에 저장될까? -> 내부스택에
n이 3일때의 내부 스택
  return n * factorial_2(n-1)   # n = 3
  return n * factorial_2(n-1)   # n = 2
  return n * factorial_2(n-1)   # n = 1
  1                             # factorial_2(0) = 1

  return n * factorial_2(n-1)   # n = 3
  return n * factorial_2(n-1)   # n = 2
  1

  return n * factorial_2(n-1)   # n = 3
  2 

  6  

return 6
"""