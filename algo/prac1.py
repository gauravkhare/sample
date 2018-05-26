words = ['cat', 'window', 'defenestrate']

for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
        words.append(w)
        #words.count(w)

print words
print words.count("window1")
print words.pop()
print words.pop()
print words.pop()
