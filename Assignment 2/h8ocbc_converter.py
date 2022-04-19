import os
from tokenize import String
clear = lambda: os.system('cls')

# C to K or K to C
def ck():
    clear()
    print('1. Choose Celcius to Kelvin or Kelvin to Celcius\n')
    print('Temperature[0-100, 273-373]: ', end='')
    temp = int(input())
    
    if (temp >= 0 and temp <= 100):
        print('Your input is Celcius')
        print('Result: ', temp+273.15, ' Kelvin')
    elif (temp >= 273 and temp <= 373):
        print('Your input is Kelvin')
        print('Result: ', temp-273.15, ' Celcius')
    else:
        print('Your input is not either Celcius or Kelvin')

# C to F or K to F
def cf():
    clear()
    print('2. Celcius or Kelvin to Fahrenheit?\n')
    print('Temperature[0-100, 273-373]: ', end='')
    temp = int(input())

    if (temp >= 0 and temp <= 100):
        print('Your input is Celcius')
        print('Result: ', (temp*9/5)+32, ' Fahrenheit')
    elif (temp >= 273 and temp <= 373):
        print('Your input is Kelvin')
        print('Result: ', (temp*9/5)-459.67, ' Fahrenheit')
    else:
        print('Your input is not either Celcius or Kelvin')

# F to C or F to K
def fk():
    clear()
    print('3. Fahrenheit to Kelvin or Celcius?\n')
    print('Temperature[32-212]: ', end='')

    temp = int(input())

    if (temp >= 32 and temp <= 212):
        print('Choose Celcius or Kelvin? [C or K]: ', end='')
        
        to = str(input())
        
        if (to == 'C' or to == 'c'): 
            print('You choose Celcius')
            print('Result: ', (temp-32)*5/9, ' Celcius')
        elif (to == 'K' or to == 'k'):
            print('You choose Kelvin')
            print('Result: ', (temp+459.67)*5/9, ' Kelvin')
        else:
            print('I cant process your choice')
    else:
        print('Temperature is not fahrenheit input type')

while(True):
    clear()
    print('Temperature Calculator\n')
    print('1. Choose Celcius to Kelvin or Kelvin to Celcius')
    print('2. Celcius or Kelvin to Fahrenheit?')
    print('3. Fahrenheit to Kelvin or Celcius?')
    print('4. Keluar')
    print('Pilih? [1-4]: ', end='')

    jawab = int(input())
    if (jawab == 1): ck(); input()
    elif (jawab == 2): cf(); input()
    elif (jawab == 3): fk(); input()
    else:
        print('Anda Keluar dari Program')
        input()
        break
    