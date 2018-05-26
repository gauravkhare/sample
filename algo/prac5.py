'''
       1
      2 2
     3 3 3
    4 4 4 4
   5 5 5 5 5
'''
# n=int(raw_input('Enter number'))
for i in range(5):
    print ' ' * (5 - i + 1),
    for j in range(i + 1):
        print i + 1,
    print

# print range(4,40,2)
