hrs = raw_input("Enter Hours:")
try:
    h = float(hrs)
except:
    print 'Format exception'
    quit()

rate = 10.5

if h > 40:
    pay = 40 * 10.5 + (h - 40) * 10.5 * 1.5
else:
    pay = 40 * 10.5
print pay
