#Python program to drop all digits from a string.

digits = [str(x) for x in range(16)]
#mystr = 'He12llo, Py00th55on! cour456se'
mystr = 'ayeno6786 helpme67 go89 to the market89'
chars = []
for x in mystr:
   if x not in digits:
      chars.append(x)
newstr = ''.join(chars)
print (newstr)