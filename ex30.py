#give values to variables
people = 30
cars = 40
buses = 15

# if there are more cars than people, print sentence
if cars > people:
    print "we should take the cars."
# else if there are more people than cars, print sentence
elif cars < people:
    print "we should not take the cars."
# failing both, print "We can't decide."
else:
    print "we can't decide."

# if there are more buses than cars...
if buses > cars:
    print "That's too many buses."
# else if ther are more cars than buses....
elif buses < cars:
    print "Maybe we could take the buses."
# failing both...
else:
    print "we still can't decide."

# if people are greater than buses...
if people > buses:
    print "Alright, let's just take the buses."
# otherwise...
else:
    print "Fine, let's stay home then."
