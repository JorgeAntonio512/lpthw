#set x variable equal to "There are 10 types of people" string
#10 takes the place of %d
x = "There are %d types of people." % 10
#set binary variable equal to "binary" string
binary = "binary"
#set do_not variable equal to "don't" string
do_not = "don't"
#set y variable equal to "Thos who know binary and those who don't." string
#binary and do_not variables take the place of their respective %s
y = "Those who know %s and those who %s." % (binary, do_not)

#print x variable
print x
#print y variable
print y

#print "I said: There are 10 types of people."
print "I said: %r." % x
#print "I also said: those who know binary and those who don't."
print "I also said: '%s'." % y

#set hilarious equal to boolean(?) value False
hilarious = False
#set joke_evaluation equal to "Isn't that joke so funny?! %r"
joke_evaluation = "Isn't that joke so funny?! %r"

#print "Isn't that joke so funny?! False"
print joke_evaluation % hilarious

#set w equal to "this is the left side of..."
w = "this is the left side of..."
#set e qual to "a string with a right side."
e = "a string with a right side."

#print "this is the left side of...a string with a right side."
print w + e
