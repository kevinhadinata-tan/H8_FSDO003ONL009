# x = 0
# y = 5

# if x < y:                            # Truthy
#     print('yes')

# if y < x:                            # Falsy
#     print('yes')

# if x:                                # Falsy
#     print('yes')

# if y:                                # Truthy
#     print('yes')

# # apakah huruf aul ada pada grault
# if 'aul' in 'grault':                # Truthy
#     print('yes')

# if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
#     print('yes')

# weather = 'nice'
# if weather == 'nice':
#     print('Mow the lawn')
#     print('Weed the garden')
#     print('Take the dog for a walk')

# raining = False
# print("Let's go to the", 'beach' if not raining else 'library')

# n = 5
# while n > 0:
#     n -= 1
#     print(n)
#     if n == 2:
#         break
# else:
#     print('Loop done.')

a = ['foo', 'bar']

while len(a):
    print(a.pop(0))
    
    b = ['baz', 'qux']
    
    while len(b):
        print('>', b.pop(0))