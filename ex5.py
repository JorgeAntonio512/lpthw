name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about {}." .format(name)
print "He's {} inches tall." .format(height)
print "He's {} pounds heavy." .format(weight)
print "Actually that's not too heavy."
print "He's got {} eyes and {} hair." .format(eyes, hair)
print "His teeth are usually {} depending on the coffee." .format(teeth)

#this line is tricky, try to get it exactly right
print "If I add {}, {}, and {} I get {}." .format(
    age, height, weight, age + height + weight)
