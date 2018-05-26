'''
NOTE : string ops
 5 5 5 5 5
  4 4 4 4
   3 3 3
    2 2
     1
'''
# n=int(raw_input('Enter number'))
for i in range(5):
    print ' ' * i,
    for j in range(5 - i):
        print 5 - i,
    print
