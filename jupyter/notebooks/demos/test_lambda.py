# lambda arguments : expression
x = lambda a : a + 10
print(x(5))


# Lambda functions can take any number of arguments:
x = lambda a, b : a * b
print(x(5, 6))

# Summarize argument a, b, and c and return the result
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


# lambda function
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


# Use if-else in Lambda Functions
 
# check if number is even or odd
result = lambda x : f"{x} is even" if x %2==0 else f"{x} is odd"
 
# print for numbers
print(result(12))
print(result(11))



# Use if-else in Lambda Functions
 
# check if two numbers is equal or greater or lesser
result = lambda x,y : f"{x} is smaller than {y}" \
if x < y else (f"{x} is greater than {y}" if x > y \
               else f"{x} is equal to {y}")
 
 
# print for numbers
print(result(12, 11))
print(result(12, 12))
print(result(12, 13))