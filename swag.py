import time
import random
from random import randrange

a = ["Doom","Light","Rage","Space","Time","Mind","Blood","Heart", "Breath", "Life", "Hope", "Void"]
c = ["Knight", "Sylph", "Thief","Bard", "Page", "Mage", "Prince","Heir", "Rogue", "Seer", "Witch", "Maid", "Lord", "Muse"]

fafirst = ["Dracin","Nivida", "Sesses", "Imerii", "Timita", "Manali", "Riikar", "Inhrta", "Aenvie", "Malkai", "Rigity", "Posida"]
fbfirst = ["Ilmien", "Aricia", "Sintir","Astien", "Derell", "Elkiva", "Raltin", "Enrien", "Scrien", "Marynn", "Reniel", "Keliea"]
fantrollsur = ["Miituu","Betici", "Choram", "Vurees", "Triyen", "Nakame", "Ivlane", "Accide", "Rilepi", "Licien","Citrin","Tefinn"]

cafirst = ["Aradia", "Tavros","Sollux","Karkat","Nepeta", "Kanaya", "Terezi", "Vriska", "Gamzee", "Eridan", "Feferi"]
cbfirst = ["Damara", "Rufioh", "Mituna", "Kankri", "Meulin", "Porrim", "Latula", "Aranea", "Kurloz", "Cronus", "Meenah"]
canonsur = ["Medigo","Nitram", "Captor", "Vantas", "Lejion", "Maryam", "Pyrope", "Serket", "Makara", "Ampora", "Peixes"]
firstnames = fafirst+fbfirst+cafirst+cbfirst
lastnames = fantrollsur+canonsur

bloodcolor = ["rust","bronze","gold","mutant","olive","jade","teal","cerulean","indigo","purple","violet","fuschia"]
mutantblood =["lime","red","pink","blue","yellow","green"]

fftrollian = ["taciturn","scholarly","sargent","fevrent","paranoid","mindful","caliginous","hapless","truthful","deathly", "gently", "ambitious","",]
fstrollian = ["Sorrow","Hermit","Sarcasm","Warden","Clockwork","Mishap","Critique","Romantic","Agressor","Degenerate", "Therapeutic","Armament",""]


dersepit = ["derse", "prospit", "dual dreamer"]
likes = ["movies", "archeology", "palentology", "coding", "romance", "murder", "Faygo", "the law", "roleplaying", "playing instruments", "doing your lusus", "building weapons", "conquering worlds"]
stronglikes = False
dislikes = ["war", "revolution", "people", "hope", "love", "their kismesis", "romance", "murder", "the law", "Faygo", "playing with grubs", "digging", "mutants", "geology", "lances", "violence", "fighting"]
strongnolikes = False

print("Generating random troll...")
time.sleep(1)
aspectgen = randrange(len(a))
classgen = randrange(len(c))
namegen = randrange(len(firstnames)) 
sgen = randrange(len(lastnames))
def namegenerator():
    namegen = randrange(len(firstnames)) 
    sgen = randrange(len(lastnames))

namegenerator()
def othergen():
    onamegen = randrange(len(firstnames))
    ofname = firstnames[namegen]
    osname = lastnames[sgen]
    onamea = fname+' '+sname
namegen = randrange(len(firstnames))
aspect = a[aspectgen]
classy = c[classgen]
classpect = classy+' of '+aspect
fname = firstnames[namegen]
sname = lastnames[sgen]
name = fname+' '+sname
onamea = fname
blood = randrange(len(bloodcolor))
blood = bloodcolor[blood]
bloodtype = blood
if blood == "mutant":
    bloodtype = randrange(len(mutantblood))
    bloodtype = mutantblood[blood]
likegen = randrange(len(likes))
likey = likes[likegen]
same = True
### lololololololololol
dislikegen = randrange(len(dislikes))
dislike = dislikes[dislikegen]


### swag etc etc etc
print("Your troll's name is",name+".")
time.sleep(1)
print("Your troll likes",likey+", but dislikes",dislike+".")
time.sleep(1)
print("Your troll is a",classpect+".")
time.sleep(1)
print(fname+" is a", bloodtype+"blood.")
time.sleep(1)
print(fanme,"'s trollhandle is")
time.sleep(1)