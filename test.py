import random





class Player(object):

	def __init__(self,name,currentLocation):
		self.name = name
		self.currentLocation = currentLocation
		self.race = None
		self.inventory = []
		self.wordDefinition ={
		"go":["verb",self.move,["direction"]], #general for keyword: ["type",functions only for verbs, [argument types for verbs only]]
		"north":["direction"], 
		"east":["direction"], 
		"south":["direction"], 
		"west":["direction"]
		} 



		

	def move(self, directionlist):
		if self.currentLocation.directions[directionlist[0]] != None:
			self.currentLocation = self.currentLocation.directions[directionlist[0]]
			print "Welcome to " + self.currentLocation.name

		else:
			print "You can't go that way"


class Place(object):

	def __init__(self,name):
		self.directions = {"north":None, "east":None, "south":None, "west":None}
		self.name = name
		population = random.randint(0,100)


def processCommand(player,commandString):
	command = commandString.split(" ")
	command = [word for word in command if word != "with"] #for the kill command
	counter = 0
	invalidArgumentType = False
	commandSet = set(command)
	allowedWordsSet = set(player.wordDefinition.keys())


	if len(commandSet.intersection(allowedWordsSet)) == len(commandSet): #check all words are valid

		if player.wordDefinition[command[0]][0] == "verb": #check its first word is a verb

			if (len(command)-1) == len(player.wordDefinition[command[0]][2]): #check it has the right amount of arguments

				
				while counter < len(player.wordDefinition[command[0]][2]): #check arguments are all of the right type
					typeOfArgument = player.wordDefinition[command[0]][2][counter]
					if typeOfArgument != player.wordDefinition[command[counter+1]][0]:
						invalidArgumentType = True
					counter +=1
				
				if invalidArgumentType == False:
					player.wordDefinition[command[0]][1](command[1:])
					

				else:
					print "Sorry adventurer I didn't understand that" #Invalid syntax arguments of the wrong type


			else:
				print "Sorry adventurer I didn't understand that" #"wrong amount of arguments"


		else:
			print "Sorry adventurer I didn't understand that" #"Commands must start with a verb"

	else:
		print "Sorry adventurer I didn't understand that" #"Basically nonsense" #basically they typed a nonsense word to begin with
	
	





Azalea = Place("Azalea")

VioletCity = Place("Violet City")

Olivine = Place("Port Olivine")

'''
<MAP SET UP>
'''

Azalea.directions["south"] = VioletCity

VioletCity.directions["north"] = VioletCity
VioletCity.directions["south"] = Olivine

Olivine.directions["north"] = VioletCity

'''
</MAP SET UP>
'''


ourPlayer = Player("Dave",Azalea)


print "Hi " + ourPlayer.name +" you are in " + ourPlayer.currentLocation.name


while True:

	command = raw_input()
	processCommand(ourPlayer,command)




