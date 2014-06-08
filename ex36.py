def angry_customer():
    print "The customer is angry because you are out of nacho cheese."
    print "What do you say?"
    print "1. What are you, a dirty Mexican?"
    print "2. Look, sir, I'll give you this small dog if you stfu and go away"
    print "3. NEXT IN LINE!"
    print "Please enter 1, 2, or 3"

    say = raw_input("> ")

    if say == "1":
        fired("The angry customer calls the complaints hotline.")
    elif say == "2":
        small_dog()
    elif say == "3":
        significant_other()
    else:
        fired("You stood silently and tried to stare down the angry customer.")


def trophy_wife():
    print "The trophy wife wants a pack of Marlboro Lights."
    print "What do you do?"
    print "1. Grab a pack and throw it at her heavily modified face"
    print "2. Squeeze her titties. HONK HONK."
    print "3. Ask if she wants to be your bottom bitch"
    print "Please enter 1, 2, or 3"

    action = raw_input("> ")

    if action == ("1", "2", "3"):
        fired("That's inappropriate.")
    else:
        fired("Follow the prompt, cunt.")


def significant_other():
    print "Your significant other comes up to you at the register, across the counter."
    print "She insists you have hot & sweaty sex with her right there, on the floor of the store"
    fired("Everyone that stood around and watched y'all have sex got herpes.")

def police():
    print "Hey, cunt, y'all are out of coffee and donuts."
    print "What do you say to the pigs?"
    print "1. OINK OINK"
    print "2. I'm sorrry sir the other fat shits bought it all"
    print "3. Don't you have something to do? Like earn your pay?"
    print "Please enter 1, 2, or 3"

    pigs = raw_input("> ")

    if pigs == ("1", "2", "3"):
        fired("You were a dick to the fuckin' pigs.")
    else:
        fired("You said something to the cops that can't even be put on the screen.")


def underage_drink_buyers():
    print "UHHH, yeah, I'm 21. I want this 54 pack of Steel Reserve"
    print "What do you say to this obviously 13 year old?"
    print "1. Dumbshit, Steel Reserve is sold by the can."
    print "2. Sure, sonny, here's your alcohol."
    print "3. You're obviously underage, but here's a small dog you can have."

    backtalk = raw_input("> ")

    if backtalk == "1":
        print "The underage wanna be drinker runs away. Good job, you win!"
        exit(0)
    elif backtalk == "2":
        fired("The police saw you sell. Them and the underage boy beat the shit out of you.")
    elif backtalk == "3":
        small_dog()

def small_dog():
    print "As you pick up the small dog, it shits everywhere."
    fired("Everyone that got shit on sued 7-Eleven.")

def fired(why):
    print why, "You're fired, bitch!"
    exit(0)


def start():
    print "Welcome to 7-Eleven! You are a clerk."
    print "You are ringing up customers."
    print "BUT, this is a special 7-Eleven. You get to choose who to ring up first."
    print "Do you choose:"
    print "1. Angry Customer"
    print "2. Trophy Wife"
    print "3. The Police"
    print "4. Underage Drink Buyers"
    print "Please enter 1, 2, 3, or 4"

    customer = raw_input("> ")

    if customer == "1":
        angry_customer()
    elif customer == "2":
        trophy_wife()
    elif customer == "3":
        police()
    elif customer == "4":
        underage_drink_buyers()
    else:
        fired("The store exploded because you choose a number that wasn't offered!")


start()
