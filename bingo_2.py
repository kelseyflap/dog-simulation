import time
import random

bingo_age = random.randint(1,8)
bingo_gender = random.choice(['male','female'])

bingo_moods = ['hungry ascii placeholder', 'needs to pee placeholder','thirsty placeholder','tired placeholder', 'restless placeholder'] # put ascii art for hungry, thirsty, needs to pee, tired, etc here

def walk(bladder,restlessness): # make this function run through a couple print statements at 2 second intervals, empty bladder +
    statements = ['Bingo admires the scenery.\n...','Was that a squirrel? Bingo is curious.\n...', 'Someone walks by. They pet Bingo!\n...']
    print("You take Bingo for a walk!\n...")
    for x in range(2):
        while True:
            time.sleep(2)
            print statements[x] # fix this
            if x == 2:
                break

walk(0,2)
        
        
    
class Dog():
    def __init__(self, age, gender):
        
        print("Bingo's Portfolio:\nage: " + str(age) + " year(s) old\ngender: " + str(gender))
        
        self.fullness_capacity = 10.0 # hunger levels
        self.fullness = 5.0
    
        def feed(self, fullness):
            print("Bingo has been fed!")
            fullness = fullness_capacity
        
        self.bladder_capacity = 10.0
        self.bladder = 5.0
        
        def go_pee(self, bladder):
        
        self.thirst_capacity = 15.0
        self.thirst = 5.0
        
        self.energy_capacity = 15.0
        self.energy = 5.0
        
        self.restlessness_capacity = 15.0
        self.restlessness = 5.0
        
    # add functions for hungry, thirsty, etc here

bingo = Dog(bingo_age,bingo_gender)
   
def hunger_decay(fullness): # decays .3 food pts from bingo's fullness lvl
    while True:
        time.sleep(5)
        fullness -= 1.0
        print("Fullness: " + str(fullness))
        
        if fullness == 3.0:
            print("Bingo is hungry and should be fed soon!")
            print(bingo_moods[0])
        
        elif fullness < 1.0:
            print("Bingo has died from starvation!")
            exit()
            

        
hunger_decay(bingo.fullness)
        
        
def interact():
    print("placeholder")
        
