p=["college","sonata","software"]
for e in p:
	print(e,len(p))

for i in range(2,10,2):
	print(i)
#to check prime number between 1 to 1000
for no in range(2, 1001):
    if no > 1:
        for i in range(2, no):
            if (no % i) == 0:
                break
        else:
            print(no)