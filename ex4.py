# setting cars variable equal to 100
cars = 100
# setting space_in_a_car variable equal to 4.0
space_in_a_car = 4.0
# setting drivers variable equal to 30
drivers = 30
# setting passengers variable equal to 90
passengers = 90
# setting cars_not_driven equal to cars minus drivers
cars_not_driven = cars - drivers
# setting cars_driven variable equal to drivers
cars_driven = drivers
# setting carpool_capacity equal to cars_driven times space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# setting average_passengers_per_car equal to passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven

# printing shit
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
