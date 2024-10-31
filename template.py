import copy
# Exercise 1 - Spacemon Competition
def exercise1(roster1,roster2):
    rtn=None
    while(True):
        if(len(roster1))==0:
            rtn=False
            break
        if(len(roster2))==0:
            rtn=True
            break
        matchResult=matchRosters(roster1,roster2)
        roster1=matchResult[0]
        roster2=matchResult[1]
    return rtn
def tupleSet(tup,index,data):
    temp = list(tup)
    temp[index] = data
    return tuple(temp)
def fighterPlanet(fighter):
    return fighter[0]
def fighterEnergy(fighter):
    return fighter[1]
def fighterPower(fighter):
    return fighter[2]
def powerRate(planet1,planet2):
    if(planet1=='Mercury' and planet2=='Venus'):
        return 2
    if(planet1=='Mercury' and planet2=='Mars'):
        return 0.5
    if(planet1=='Venus' and planet2=='Earth'):
        return 2
    if(planet1=='Venus' and planet2=='Mercury'):
        return 0.5
    if(planet1=='Earth' and planet2=='Mars'):
        return 2
    if(planet1=='Earth' and planet2=='Venus'):
        return 0.5
    if(planet1=='Mars' and planet2=='Mercury'):
        return 2
    if(planet1=='Mars' and planet2=='Earth'):
        return 0.5
    return 1
def matchRosters(roster1,roster2):
    if(len(roster1)==0):
        return roster1,roster2,False
    if(len(roster2)==0):
        return roster1,roster2,True
    fighter1=roster1[0]
    fighter2=roster2[0]
    while(True):
        powerRate1=powerRate(fighterPlanet(fighter1),fighterPlanet(fighter2))
        fighter2=tupleSet(fighter2,1,fighterEnergy(fighter2)-powerRate1*fighterPower(fighter1))
        if fighterEnergy(fighter2)<=0:
            roster2.pop(0)
            roster1[0]=fighter1
            break
        powerRate2=powerRate(fighterPlanet(fighter2),fighterPlanet(fighter1))
        fighter1=tupleSet(fighter1,1,fighterEnergy(fighter1)-powerRate2*fighterPower(fighter2))
        if fighterEnergy(fighter1)<=0:
            roster1.pop(0)
            roster2[0]=fighter2
            break
    return roster1,roster2
# Exercise 2 - Five Letter Unscramble
def exercise2(s):
    return None

# Exercise 3 - Wordle Set
def exercise3(green,yellow,gray):
    return None

# Exercise 4 - 2D Most Rewarding Shortest Path
def exercise4(env):
    return None

# Exercise 5 - Social Network Analysis
def exercise5(network):
    return None

