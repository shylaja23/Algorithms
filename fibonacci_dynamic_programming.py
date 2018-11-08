def fib(n):
  i = 0
  j = 1
  if( n == 0):
    return i
  if(n == 1):
    return j 
  for i in range(2,n+1):
    k = i+j
    i = j
    j = k
  return j
