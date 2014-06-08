print "You enter a circular dark room with three doors.   Do you go through door #1 or door #2 or door #3?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
    print "You enter a room made entirely out of gold, and come face-to-face with God. What do you say to Him?"
    print "1. God, why did you create mankind?"
    print "2. God, can I have both love and money?"
    print "3. God, have I been a good and faithful servant?"
    print "4. God, I've done the best I can. Every day I am tired. Every day I look around me and see a world I have less and less love for. Can you change it?"
    print "5. Give me a gold medal, please, God?"

    God_question = raw_input("> ")

    if God_question == "1":
        print "I thought that I could trust y'all. I fucked up there."
    elif God_question == "2":
        print "If you work your ass off, your whole life. Get crackin', boy."
    elif God_question == "3":
        print "Look inside yourself, and you'll have the answer."
    elif God_question == "4":
        print "No. It's y'all's world."
    elif God_question == "5":
        print "SURE! HAVE YOUR MEDAL!"
    else:
        print "What is your name?"

        name = raw_input("> ")

        print "YOU DIDN'T PICK ONE OF THE CHOICES, " + name + ", BURN IN HELL."

else:
    print "You stumble around and fall on a knife and die. Good job!"
