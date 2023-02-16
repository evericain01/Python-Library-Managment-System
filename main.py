f = open('myfile.txt', 'w')
f.write('2-Level\nText')
f = open('myfile.txt', 'r')
for line in f:
  print(repr(line)) 
f.close()