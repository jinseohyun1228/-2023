# 백준 10870번

def fibonacci(n): 
  if(n == 0):
    return 0
  elif(n == 1):
    return 1
  return fibonacci(n-1) + fibonacci(n-2)

x = int(input())
print(fibonacci(x))