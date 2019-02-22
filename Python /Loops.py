#for i=0;i<=10;i++: print i

for i in xrange(10): print(i)

for j in range(0,10):
    for k in range(0,j):
        print("*")
    print("\n\r")


for letter in 'Python':
   if letter == 'h':
      pass
      print 'This is pass block'
   print 'Current Letter :', letter

print "Good bye!"


import time

#use time.time() on Linux

start = time.clock()
for x in range(10000000):
    pass
stop = time.clock()

print stop - start

start = time.clock()
for x in xrange(10000000):
    pass
stop = time.clock()

print stop - start

for i in range(10):
    print "hi"+ str(i)