from sys import argv

script, first, second = argv
age = int(raw_input("How old are you?"))
weight = int(raw_input("How much do you weigh?"))


print "The filename is {0}, your first variable is" \
" {1}, your second variable is {2}, your age is {3}" \
", your weight is {4}, and your weight and age added" \
" together is {5}".format(script, first, second, age, weight, (age+weight))
