i = 0
numbers = []
x = 6
y = 1

def while_go(i, x, y):
    while i < x:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + y
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

print while_go(i, x, y)

print "The numbers: "

for num in numbers:
    print num
