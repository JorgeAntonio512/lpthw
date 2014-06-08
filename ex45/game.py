from sys import exit


class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        print "Engine __init__ has scene_map", scene_map
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        print "Play's first scene", current_scene

        while True:
            print "\n---------"
            next_scene_name = current_scene.enter()
            print "next scene", next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)
            print "map returns new scene", current_scene


class Start(Scene):

    def enter(self):
        print "You are Cowboy George."
        print "You must wake from a dream that takes place in a Wild"
        print "West setting. To do so, you must get out of the town"
        print "that you find yourself in."
        print "You find yourself in a saloon. Looking around, do you:"
        print "1. Go with a good looking prostitute up to a room"
        print "2. Get in a fight with one of the bar denizens"
        print "3. Walk outside of the saloon"

        action = raw_input("> ")

        if action == "1":
            print "The prostitute talks you into tying you up and"
            print "blindfolding you. She strangles you and takes all"
            print "your money. Failure. Game over."
            exit(1)

        elif action == "2":
            print "Being an experienced bar fighter yourself, you get"
            print "a little banged up, but beat the other guy into a"
            print "bloody pulp. The Sheriff hauls your ass to jail."
            return 'jail_cell'

        elif action == "3":
            return 'town_streets'

        else:
            print "Sorry, Cowboy George, try again."
            return 'start'


class JailCell(Scene):

    def enter(self):
        print "You are in a grungy jail cell. Boy, the Sheriff"
        print "really hates you."
        print "You:"
        print "1. Look around"
        print "2. Lay down on the suprisingly comfortable bed"

        action = raw_input("> ")

        if action == "1":
            print "You see a crack in the cement. As you peel at it, it"
            print "comes up in a block. You discover a tunnel that the"
            print "previous prisoners started. You finish digging your"
            print "way out. You come up outside the town."
            print "Congratulations! You win!"

            return 'finished'

        elif action == "2":
            print "You fall asleep, wake up to find that you have turned"
            print "into an old man, and spend the rest of your days"
            print "begging on the town's streets. Failure. You lose."
            exit(1)

        else:
            print "A wild band of gorillas descends on you and nibbles"
            print "you to death. Follow instructions next time. Goodbye"
            exit(1)


class TownStreets(Scene):

    def enter(self):
        print "Walking into the town's streets, you see that you only have"
        print "two options:"
        print "1. Buy a horse from a sketchy guy in an alley"
        print "2. Enter the post office"

        action = raw_input("> ")

        if action == "1":
            print "The guy and his goons beat you to death, and take"
            print "all of your money. You lose. Don't do things in"
            print "sketchy places."
            exit(1)

        elif action == "2":
            return 'post_office'


class PostOffice(Scene):

    def enter(self):
        print "Do you:"
        print "1. Talk to the gentleman sending a package"
        print "2. Send a letter to your Mother begging her to send help"

        action = raw_input("> ")

        if action == "1":
            print "The gentleman is a wealthy merchant, and agrees"
            print "to get you out of town on one of his stagecoaches."
            print "Congratulations! You win!"

            return 'finished'

        elif action == "2":
            print "You write the letter, and wait to hear back."
            print "Unfortunately, the stagecoach that was carrying"
            print "your letter was ambushed by a band of Indians."
            print "The Indians come to the town and kill everyone."
            print "You lose."
            exit(1)

        else:
            print "The post office building collapses on top of you."
            print "You are the only fatality."
            print "Follow instructions next time."
            exit(1)


class Map(object):

    scenes = {
        'start': Start(),
        'jail_cell': JailCell(),
        'town_streets': TownStreets(),
        'post_office': PostOffice()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
        print "start_scene in __init__", self.start_scene

    def next_scene(self, scene_name):
        print "start_scene in next_scene"
        val = Map.scenes.get(scene_name)
        print "next_scene returns", val
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('start')
a_game = Engine(a_map)
