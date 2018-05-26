a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print i, a[i]
    print str(i) + '|' + a[i]

# the noticable thing here is , restricts new line character after each iteration
print '************************************'
for i in range(len(a)):
    print a[i],
