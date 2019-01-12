import math
print'max(95.5,64.8,-62.4):', max(95.5,64.8,-62.4)
print'min(95.5,64.8,-62.4):', min(95.5,64.8,-62.4)
a=max(95.5,64.8,-62.4)
b=min(95.5,64.8,62.4)
print a
print b
print "----------"
print math.ceil(a)
print math.floor(b)
c=math.ceil(a)*math.floor(b)
if (c<0):
	e=(-1)*c
	print math.sqrt(e)
	d=math.sqrt(e)
	print math.pow(d,3)
else: 
	print math.sqrt(c)
	d=math.sqrt(c)
	print math.pow(d,3)

