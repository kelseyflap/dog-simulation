#! /usr/bin/env python

import time
import random
import multiprocessing 

bingo_age = random.randint(1,8)
bingo_gender = random.choice(['male','female'])

bingo_moods = ['hungry ascii placeholder', 'needs to pee placeholder','thirsty placeholder','tired placeholder', 'restless placeholder'] # put ascii art for hungry, thirsty, needs to pee, tired, etc here to represent moods
      
class Dog():
    def __init__(self, age, gender):
        
        print("Bingo's Portfolio:\nage: " + str(age) + " year(s) old\ngender: " + str(gender))
        
        # BINGO NEEDS VARIABLES
        
        self.fullness_capacity = 10.0 # hunger levels
        self.fullness = 5.0
        
        self.bladder_capacity = 10.0
        self.bladder = 5.0
        
        self.thirst_capacity = 10.0
        self.thirst = 5.0
        
        self.restlessness_capacity = 15.0
        self.restlessness = 5.0
        
        self.energy_capacity = 15.0
        self.energy = 5.0
        
        # BINGO NEEDS FULFILL FUNCTIONS
        
        def bedtime(self, energy, energy_capacity):
          energy = energy_capacity
          print("Bingo goes to sleep!\n...")
          dreams = ['Bingo is dreaming...\n','He finds a sirloin steak...\n','What a great dream! Bingo awakens feeling rested.']
          
          
        def drink(self,thirst,thirst_capacity):
          thirst = thirst_capacity
          print("You give Bingo a bowl of water; he drinks it all up!")
        
        def feed(self, fullness,fullness_capacity):
            print("Bingo has been fed!")
            fullness = fullness_capacity
        
        def walk(self,bladder,restlessness): # returns bladder & restlessness to 0
          bladder = 0
          restlessness = 0
          statements = ['Bingo admires the scenery.\n...','Was that a squirrel? Bingo is curious.\n...', 'Someone walks by. They pet Bingo!\n...']
          print("You take Bingo for a walk!\n...")
          y = True # y changes to False when finished running through list of statements
          while y == True:
            for x in range(3):
              time.sleep(2)
              print (statements[x])
              if x == 2:
                y = False
            
        
    # add functions for hungry, thirsty, etc here

bingo = Dog(bingo_age,bingo_gender)

# NEEDS DECAY FUNCTIONS

def restlessess_decay(restlessness,restlessness_capacity):
  while True:
    time.sleep(1.8)
    restlessness += .2
    
    if restlessness == 12.0:
      print("Bingo is restless! Take him for a walk.")
      
    elif restlessness == restlessness_capacity:
      print("Bingo has lashed out and bit someone! Now he must be put down.")
      exit()

def bladder_decay(bladder,bladder_capacity): # decays .5 from bingo's bladder lvl
  while True:
    time.sleep(2)
    bladder += 0.5
  
    if bladder == 1.0:
      print("Bingo needs to use the bathroom soon!")
    
    elif bladder == bladder_capacity:
      print("Oh no! Bingo just died from... bladder accident?")
      exit()
   
def hunger_decay(fullness): 
    while True:
        time.sleep(1.8)
        fullness -= 0.5
        
        if fullness == 3.0:
            print("Bingo is hungry and should be fed soon!")
            print(bingo_moods[0])
        
        elif fullness == 0:
            print("Bingo has died from starvation!")
            exit()
            
def thirst_decay(thirst,thirst_capacity):
  while True:
    time.sleep(1.4)
    thirst -= 0.5
    
    if thirst == 3:
      print("Bingo is thirsty!")
    
    elif thirst == 0:
      print ("Bingo has died from dehydration!")
      exit()
      
def energy_decay(energy, energy_capacity):
  while True:
    time.sleep(2.7)
    energy -= 0.5
      
    if energy == 3:
      print("Bingo is tired! He needs to rest soon.")
        
    elif energy == 0:
      print("Bingo has died from, uh, sleep deprivation! Oh no.")
      exit()
        
# INTERFACE
        
def interact(): 
    fulfill_needs = {'placeholder' : 1}
    action = (input("Type a command from the following list to help Bingo:\n"))
    for i in fulfill_needs:
      print(i)
    # put something here like 'if action is i in fulfill_needs, run action as function name in class, if that makes sense'
    
# TEST ZONE (run functions here for testing)
thirst_decay(bingo.thirst,bingo.thirst_capacity)

    

        
