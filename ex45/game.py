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
