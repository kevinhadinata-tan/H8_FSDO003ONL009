# try:
#     f = open('Hack8_sample_text.txt', encoding = 'utf-8')
# except FileNotFoundError as error:
#     print(error)
# finally:
#     print('Executing the else clause')


import sys

def os_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    assert ('windows' in sys.platform), "This code runs on Windows only."
    print('Doing something.')
try:
    os_interaction()
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as error:
    print(error)
    print('os_interaction() function was not executed')