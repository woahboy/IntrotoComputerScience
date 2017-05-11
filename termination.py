def proc1(n): #terminates
   while True:
      n = n - 1
      if n == 0:
         break
   return 3

def proc2(n): # doesn't terminate
   if n == 0:
      return n
   return 1 + proc2(n - 2)

def proc3(n):
   if n <= 3:
      return 1
   return proc3(n - 1) + proc3(n - 2) + proc3(n - 3)


print proc3(10)
