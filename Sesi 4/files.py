# try:
#    f = open("Hack8_sample_text.txt", encoding = 'utf-8')
#    # perform file operations
# finally:
#    f.close()

# with open("Hack8_sample_text.txt",'w',encoding = 'utf-8') as f:
#    f.write("my first file\n")
#    f.write("This file\n\n")
#    f.write("contains three lines\n")

f = open("Hack8_sample_text.txt",'r',encoding = 'utf-8')
print(f.read(4)) # read the first 4 data
print(f.read(4))    # read the next 4 data
print(f.read())