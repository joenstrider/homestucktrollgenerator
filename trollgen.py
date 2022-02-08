import time
import random
from random import randrange

a = ["Doom","Light","Rage","Space","Time","Mind","Blood","Heart", "Breath", "Life", "Hope", "Void"]
c = ["Knight", "Sylph", "Thief","Bard", "Page", "Mage", "Prince","Heir", "Rogue", "Seer", "Witch", "Maid", "Lord", "Muse"]

fafirst = ["Dracin","Nivida", "Sesses", "Imerii", "Timita", "Manali", "Riikar", "Inhrta", "Aenvie", "Malkai", "Rigity", "Posida"]
fbfirst = ["Ilmien", "Aricia", "Sintir","Astien", "Derell", "Elkiva", "Raltin", "Enrien", "Scrien", "Marynn", "Reniel", "Keliea"]
cafirst = ["Aradia", "Tavros","Sollux","Karkat","Nepeta", "Kanaya", "Terezi", "Vriska", "Gamzee", "Eridan", "Feferi"]
cbfirst = ["Damara", "Rufioh", "Mituna", "Kankri", "Meulin", "Porrim", "Latula", "Aranea", "Kurloz", "Cronus", "Meenah"]
miscfirst = ["Tezzak","Aliive","Oliive"]

fantrollsur = ["Miituu","Betici", "Choram", "Vurees", "Triyen", "Nakame", "Ivlane", "Accide", "Rilepi", "Licien","Citrin","Tefinn"]
canonsur = ["Medigo","Nitram", "Captor", "Vantas", "Lejion", "Maryam", "Pyrope", "Serket", "Makara", "Ampora", "Peixes"]
misclast = ["Ixodes","Raiden","Gardin"]

bloodcolor = ["rust","bronze","gold","mutant","olive","jade","teal","cerulean","indigo","purple","violet","fuschia"]
mutantblood =["lime","red","pink","blue","yellow","green"]

fftrollian = ["taciturn","scholarly","sargent","fevrent","paranoid","mindful","caliginous","hapless","truthful","deathly", "gently", "ambitious","terepid","supersitious","serene","frightful","preoccupied","medicinal","conspicuous","heated","teased","defiant","grave","aggrieved"]
fstrollian = ["Sorrow","Hermit","Sarcasm","Warden","Clockwork","Mishap","Critique","Romantic","Agressor","Degenerate", "Therapeutic","Armament","Suspension","Heretic","Sermon","Wit","Calamity","Miracle","Criminal","Relations","Aristocrat","Demons","Terrorizer","Anarchist"]
cftrollian = ["carcino","apocalypse","adios","twin","arsenic","grim","gallows","arachnids","centaurs","terminally","caligulas","cuttlefish"]
cstrollian = ["Geneticist","Arisen","Toreador","Armageddons","Catnip","Auxillatrix","Callibrator","Grip","Testicle","Capracious","Aquarium","Culler"]
firsttrollian = fftrollian + cftrollian
secondtrollian = fstrollian + cstrollian

land1 = ["Frost","Clockwork","Woods","Bridges","Wind","Shade","Light","Rain","Cats","Hope","Angels","Dust","Crypts","Puzzles"]
land2 = ["Heat","Nitrogen","Arsenic","Krypton","Nobles","Rivers","Lakes","Oceans","Rats","Crabs","Blood","Rust","Circles","Tea"]
landgen = randrange(len(land1))
landf = land1[landgen]
if a == "Space":
    lands = "Frogs"
else:
    landgens = randrange(len(land2))
    lands = land2[landgens]

landabbrv = 'LO'+landf[:1]+'A'+lands[:1]

firstnames = fafirst+fbfirst+cafirst+cbfirst+miscfirst
lastnames = fantrollsur+canonsur+misclast

namegen = randrange(len(firstnames)) 
sgen = randrange(len(lastnames))

namegen = randrange(len(firstnames)) 
sgen = randrange(len(lastnames))
namegen = randrange(len(firstnames))

fname = firstnames[namegen]
sname = lastnames[sgen]
name = fname+' '+sname


firstt = randrange(len(firsttrollian))
secondd = randrange(len(secondtrollian))
firstt = firsttrollian[firstt]
secondd = secondtrollian[secondd]
handle = firstt+secondd


nicknames = [fname[:3],fname[:1]*2,sname[:1]*2,fname[:1]+sname[:1],firstt[:1]*2,secondd[:1]*2,firstt[:1].capitalize()+secondd[:1]]
nick = randrange(len(nicknames))
nick = nicknames[nick]

dersepit = ["derse", "prospit", "dual dreamer"]
dreamer = randrange(len(dersepit))
dreamer = dersepit[dreamer]
if dreamer == dersepit[2]:
    dreamer = "both Derse and Prospit"
    moon = "dual dreamer"
else: 
    dreamer = dreamer.capitalize()
    moon = dreamer
    
    
    
    
likes = ["movies", "archeology", "palentology", "coding", "romance", "murder", "Faygo", "the law", "roleplaying", "playing instruments", "doing your lusus", "building weapons", "conquering worlds"]
stronglikes = False
dislikes = ["war", "revolution", "people", "hope", "love", "their kismesis", "romance", "murder", "the law", "Faygo", "playing with grubs", "digging", "mutants", "geology", "lances", "violence", "fighting"]
strongnolikes = False

print("Generating random troll...")
time.sleep(1)
aspectgen = randrange(len(a))
classgen = randrange(len(c))

aspect = a[aspectgen]
classy = c[classgen]
classpect = classy+' of '+aspect

firstt = randrange(len(firsttrollian))
secondd = randrange(len(secondtrollian))
firstt = firsttrollian[firstt]
secondd = secondtrollian[secondd]
handle = firstt+secondd

blood = randrange(len(bloodcolor))
blood = bloodcolor[blood]
bloodtype = blood
if blood == "mutant":
    bloodtype = randrange(len(mutantblood))
    bloodtype = mutantblood[bloodtype]
likegen = randrange(len(likes))
likey = likes[likegen]

quadname = handle
moirail = quadname
kismesis = quadname
aus = False
auspitice = quadname
matesprit = quadname
sayme = True
    
    
    
### lololololololololol
dislikegen = randrange(len(dislikes))
dislike = dislikes[dislikegen]


### swag etc etc etc
print("Your troll's name is",name+".")
chance = random.choice([True,False])
time.sleep(1)
print(fname+"'s trollian handle is",handle+".")
if chance == True:
    time.sleep(1)
    print(fname+"'s nickname is",nick+".")
time.sleep(1)
print("Your troll likes",likey+", but dislikes",dislike+".")
time.sleep(1)
print(fname+" is a", bloodtype+"blood.")
time.sleep(1)
chance = random.choice([True,False])
if chance == True:
    while sayme == True:
        random.shuffle(firstnames)
        random.shuffle(lastnames)
        swag = firstnames
        sus = lastnames
        swagg = randrange(len(swag))
        swag = swag[swagg]
        swagg = randrange(len(sus))
        sus = sus[swagg]
        if fname != swag:
            pass
            if sname != sus:
                sayme = False
    quadname = swag+' '+sus 
    sayme = True
    print(fname+"'s moirail is named",quadname+".")
    moirail = quadname
    time.sleep(1)
else:
    pass
chance = random.choice([True,False])
if chance == True:
    while sayme == True:
        random.shuffle(firstnames)
        random.shuffle(lastnames)
        swag = firstnames
        sus = lastnames
        swagg = randrange(len(swag))
        swag = swag[swagg]
        swagg = randrange(len(sus))
        sus = sus[swagg]
        if fname != swag:
            pass
            if sname != sus:
                sayme = False
    quadname = swag+' '+sus 
    sayme = True
    print(fname+"'s kismesis is named",quadname+".")
    kismesis = quadname
    time.sleep(1)
    chance = random.choice([True,False])
    if chance == True:
        while sayme == True:
            random.shuffle(firstnames)
            random.shuffle(lastnames)
            swag = firstnames
            sua = lastnames
            swagg = randrange(len(swag))
            swag = swag[swagg]
            swagg = randrange(len(sus))
            sus = sua[swagg]
            if fname != swag:
                pass
                if sname != sus:
                    sayme = False
        quadname = swag+' '+sus 
        sayme = True
        print(fname+"'s auspitice is",quadname+".")
        auspitice = quadname
        time.sleep(1)
    else:
        pass
else:
    pass
chance = random.choice([True,False])
if chance == True:
    while sayme == True:
        random.shuffle(firstnames)
        random.shuffle(lastnames)
        swagy = firstnames
        sua = lastnames
        swagg = randrange(len(swagy))
        swag = swagy[swagg]
        sussy = randrange(len(sua))
        sus = sua[sussy]
        if fname != swag and swag not in quadname:
            pass
            if sname != sus and sus not in quadname:
                sayme = False
        else:
            swagg = randrange(len(swagy))
            swag = swagy[swagg]
            sus = randrange(len(sua))
            sussy = sua[sus]
    quadname = swag+' '+sus 
    sayme = True
    print(fname+"'s matesprit is",quadname+".")
    matesprit = quadname
    time.sleep(1)
else:
    pass
aa = 2
p = ""
while sayme == True:
    random.shuffle(firstnames)
    random.shuffle(lastnames)
    swagy = firstnames
    sua = lastnames
    swagg = randrange(len(swag))
    swag = swagy[swagg]
    swagg = randrange(len(sus))
    sus = sua[swagg]
    if fname != swag and swag not in quadname:
        pass
        if sname != sus and sus not in quadname:
            sayme = False
    else:
        swagg = randrange(len(swagy))
        swag = swagy[swagg]
        sus = randrange(len(sua))
        sussy = sua[sus]
    
quadname = swag+' '+sus 
sayme = True
p = quadname
while sayme == True:
    random.shuffle(firstnames)
    random.shuffle(lastnames)
    swag = firstnames
    sus = lastnames
    swagg = randrange(len(swag))
    swag = swagy[swagg]
    swagg = randrange(len(sus))
    sus = sus[swagg]
    if fname != swag and swag not in quadname:
        pass
        if sname != sus and sus not in quadname:
            sayme = False
    else:
        swagg = randrange(len(swagy))
        swag = swagy[swagg]
        sus = randrange(len(sua))
        sussy = sua[sus]

quadname = swag+' '+sus 
sayme = True
print(fname+"'s favourite troll is",quadname+". However, they hate",p+", as they enjoy",dislike+".")
time.sleep(1)
print("\nSBURB:")
time.sleep(1)
print(fname,"is a",classpect+".")
time.sleep(1)
print(fname,"dreams on",dreamer+".")
time.sleep(1)
print(fname+"'s land is",landabbrv+"; the Land of",landf.capitalize(),"And",lands.capitalize()+".")


