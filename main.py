import random


9966699999966699999966699966669996699999996699666996699
9966999999996999999996666996699666699666996699666996699 
9966699999999999999966666699996666699666996699666996699 
9966666999999999999666666669966666699666996699666996699 
9966666669999999966666666669966666699666996699666996699 
9966666666699996666666666669966666699666996699666996666 
9966666666669966666666666669966666699999996699999996699






class Player(object):

	def __init__(self,name,currentLocation):
		self.name = name
		self.currentLocation = currentLocation
		self.currentPlace = currentLocation
		self.race = None
		self.inventory = {}
		self.purse = random.randint(100,1000)
		self.wordDefinition ={
		"go":["verb",self.move,[["direction"]]],#general for keyword: ["type",functions only for verbs, [[list of argument types],[list of argument types]etc.]
		"enter":["verb",self.enter,[["shop"]]],
		"leave":["verb",self.leave,[["shop"]]],
		"buy":["verb",self.buy,[["weapon","food","drink"]]],
		"attack":["verb",self.attack,[["person","creature"],["weapon"]]],
		"north":["direction"], 
		"east":["direction"], 
		"south":["direction"], 
		"west":["direction"],
		"axe":["weapon"],
		"sword":["weapon"],
		"dagger":["weapon"],
		"chicken":["creature"],
		"dog":["creature"],
		"bread":["food"],
		"blacksmith":["shop"],
		"tavern":["shop"],
		} 



		

	def move(self, directionlist):
		if self.currentLocation.__class__.__name__ != "Shop":
			if self.currentLocation.directions[directionlist[0]] != None:
				self.currentLocation = self.currentLocation.directions[directionlist[0]]
				self.currentPlace = self.currentLocation
				print "Welcome to " + self.currentLocation.name + " \n"

			else:
				print "You can't go that way \n"
		else:
			print "leave shop first then pick a direction"


	def buy(self, objectToBuy):
		if self.currentLocation.__class__.__name__ == "Shop":
			try:
				self.purse -= self.currentLocation.inventory[objectToBuy[0]][1]
				self.inventory[objectToBuy[0]]=self.currentLocation.inventory[objectToBuy[0]][0]
				print self.inventory
			except:
				print "Sorry we don't sell that here"
		else:
			print "Nah mate this aint a shop"


	def enter(self, typeOfShop):
		try:
			self.currentLocation =  self.currentLocation.listOfShops[typeOfShop[0]]
			print "You enter the " + typeOfShop[0] + "\n"
		except:
			print "Sorry there is no shop like that here"

	def leave(self, typeOfShop):
		if self.currentLocation.__class__.__name__ == "Shop":
			print "you leave the shop and come back into " + self.currentPlace.name
			self.currentLocation = self.currentPlace
		else:
			print "You can't leave because you're outside"



	def attack(self, weaponAndAttackee):

		try:
			self.currentLocation.listOfEntites[weaponAndAttackee[0]]

			try:
				self.inventory[weaponAndAttackee[1]]
			
				if self.currentLocation.__class__.__name__ != "Shop":
					print "You sure fucked up that " +weaponAndAttackee[0] #Need to add fighting mechanics here.
				else:
					print "You can't start a fight in a shop!!"
			except:
				print "You don't have a " +weaponAndAttackee[1]
		except:
			print "there is no " +weaponAndAttackee[0]+" here"
			



class Place(object):

	def __init__(self,name,description,listOfShops):
		self.directions = {"north":None, "east":None, "south":None, "west":None}
		self.name = name
		self.population = random.randint(20,100)
		self.description = description
		self.listOfShops = listOfShops
		self.listOfEntites = {"chicken":Creature("chicken")}



class Weapon(object):

	def __init__(self,weaponType):
		self.name = weaponType




class Shop(object):

	def __init__(self,shopType):
		self.shopType = shopType
		self.shopTypeToInventory = {"blacksmith":{"sword":[Weapon("sword"),10],"axe":[Weapon("axe"),10],"dagger":[Weapon("dagger"),10]}}
		self.inventory = self.shopTypeToInventory[self.shopType]

class Creature(object):

	def __init__(self,creatureType):
		self.creatureType = creatureType
		self.health = 100






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
					typeOfArgumentlist = player.wordDefinition[command[0]][2][counter]
					
					if not player.wordDefinition[command[counter+1]][0] in typeOfArgumentlist :
						invalidArgumentType = True
					counter +=1
					
				
				if invalidArgumentType == False:
					player.wordDefinition[command[0]][1](command[1:])
					

				else:
					print "Invalid syntax arguments of the wrong type \n "



			else:
				print "wrong amount of arguments \n "


		else:
			print "Commands must start with a verb \n "

	else:
		print "Basically nonsense \n " #basically they typed a nonsense word to begin with
	
	





Azalea = Place("Azalea","Shithole",{"blacksmith":Shop("blacksmith")})

VioletCity = Place("Violet City","Shithole",{"blacksmith":Shop("blacksmith")})

Olivine = Place("Port Olivine","Shithole",{"blacksmith":Shop("blacksmith")})

'''
<MAP SET UP>
'''

Azalea.directions["south"] = VioletCity

VioletCity.directions["north"] = Azalea
VioletCity.directions["south"] = Olivine

Olivine.directions["north"] = VioletCity

'''
</MAP SET UP>
'''


ourPlayer = Player(None,Azalea)
'''
print "Good morrow Adventurer! What is your name? \n"
ourPlayer.name = raw_input()
print " \n Nice to meet you "+ourPlayer.name+". What race are you? \n"
ourPlayer.race = raw_input()
print "\n Oh so you're a "+ourPlayer.race+". Let me tell you about the world. \n"
print"filler text \n"
'''

#print ourPlayer.currentLocation.description


while True:

	command = raw_input()
	print ""
	command = command.split("then")
	for c in command:
		c = c.strip()
		processCommand(ourPlayer,c)




