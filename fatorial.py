def factorial(x):
  '''This is a function to find the factorial of the given number'''
  if x==0 or x==1:
    return 1
  else:
    return x*factorial(x-1)

print(factorial.__doc__)
fact= int(input("\nEnter the number: "))
print("The factorial of", fact,":", factorial(fact))