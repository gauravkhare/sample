'''
       1
      2 2
     3 3 3
    4 4 4 4
   5 5 5 5 5
0-1=i+
1-3
2-5
3-7
4-9
'''
n = int(raw_input('Enter number: '))
c = 0
for i in range(n):
    c = c + 1
    print '  ' * (n - i - 1),

    for j in range(i + c):
        print i + 1 - j if i + 1 - j > 0 else j + 1 - i,
    # for k in range(j):
    #	print

    print
