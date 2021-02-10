s = input
tokens = s.split()
a = int(tokens[0])
b = int(tokens[1])

if a*b%2 == 0:
    print ('Even')
else:
    print('odd')