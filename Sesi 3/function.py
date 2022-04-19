# def printme( str_input ):
#    '''This prints a passed string into this function'''
#    print(str_input)

# Now you can call printme function
# printme("I'm first call to user defined function!")
# printme("Again second call to the same function")

# Function definition is here
# def changeme( mylist ):
#    '''This changes a passed list into this function'''
#    mylist = [1, 2, 3, 4] # This would assign new reference in mylist
#    print("Values inside the function  : ", mylist)

# Now you can call changeme function
# mylist = [10, 20, 30]
# changeme( mylist )
# print("Values outside the function : ", mylist)

# Function definition is here
# def printinfo( name, age = 26 ):
#    '''This prints a passed info into this function'''
#    print("Name : ", name)
#    print("Age  : ", age)
#    print("")

# Now you can call printinfo function
# printinfo( age=50, name="hacktiv8" )

def print_pets( name, *pets ):
    pass
 
print_pets('Amy', 'cats')
print_pets('Abby', 'cats', 'dogs', 'rabbits')
print_pets('Ady')

def print_bought_items(name, **bought_items):
  '''Create a function to print which items somebody bought'''
  print('Name : ', name)
 
  for key, value in bought_items.items():
    print('key   : ', key)
    print('value : ', value)
 
  print('')
 
print_bought_items("Ani", first="egg", second="sugar", third="salt", fourth="baking powder")
print_bought_items("Ali", first="thread", second="hoop", third="neddle")
print_bought_items("Cici", fruit="Apple", milk='oatmilk')

# Function definition is here
def printinfo( arg1, *vartuple ):
# def printinfo(arg1, arg2, arg3, arg4):
   '''This prints a variable passed arguments'''
   print('arg1     : ', arg1)
   print('vartuple : ', vartuple)
   print('')
   
   for var in vartuple:
      print('isi vartuple : ', var) 

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, "a" )

# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2

# That lambda function will be equal to :
# def sum(arg1, arg2):
#     return arg1+arg2

# Now you can call sum as a function
print("Value of total : ", sum( 10, 20 ))
print("Value of total : ", sum( 20, 20 ))

# Example of docstring in a function

def sum_number(num1, num2):
  '''
  This function is used to sum of 2 variables.
  :param num1: Input number 1 | int or float
  :param num2: Input number 2 | int or float
  
  :return: num3: Sum of number | int or float
  '''

  num3 = num1 + num2
  return num3

# Syntax to get explanation/docstring from a particular module/function/class

print(sum_number.__doc__)