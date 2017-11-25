import numpy as np
import matplotlib.pyplot as plt

def attemptThree():
    if np.random.randint(0,100) < threePtPercent:
        if np.random.randint(0,100) < overtimePercent:
            return True
    return False
    
def attemptTwo():
    havePossession = True
    pointsDown = 3

    timeLeft = 30
    while (timeLeft > 0):
        if havePossession:
            if pointsDown >= 3:
                timeLeft -= timeToShoot2
            else:
                timeLeft = 0
            if np.random.randint(0,100) < twoPtPercent:
                pointsDown -= 2
                havePossession = False
        else:
            if np.random.randint(0,100) >= offenseReboundPercent:
                havePossession = False
            else:
                if pointsDown > 0:
                    timeLeft -= timeToFoul
                    if np.random.randint(0,100) < oppFtPercent:
                        pointsDown += 1
                    if np.random.randint(0,100) < oppFtPercent:
                        pointsDown += 1
                        havePossession = True
                else:
                    if np.random.randint(0, 100) >= ftReboundPercent:
                        havePossession = True
                    else:
                        if np.random.randint(0,100) < oppTwoPtPercent:
                            pointsDown += 2
                        timeLeft = 0
    if pointsDown > 0:
        return False
    else:
        if pointsDown < 0:
            return True
        else:
            if np.random.randint(0,100) < overtimePercent:
                return False
            else:
                return True
plt.figure(figsize=(14, 14))
names = ['Lebron James', 'Kyrie Irving', 'Steph Curry', 'Kyle Krover', 'Dirk Nowitzki']
threePercents = [35.4, 46.8, 44.4, 49.2, 38.0]
twoPercents = [53.6, 49.1, 52.8, 47.0, 48.6]
colind = 0

colors = [tuple(np.random.randint(1, 256, 3)/255.0) for i in range(20)]

for i in range(5):
    x = []
    y1 = []
    y2 = []
    trials = 400
    threePtPercent = threePercents[i]
    twoPtPercent = twoPercents[i]
    oppTwoPtPercent = 40
    oppFtPercent = 70
    timeToShoot2 = 5
    timeToFoul = 5
    offenseReboundPercent = 25
    ftReboundPercent = 15
    overtimePercent = 50
    
    winsTakingThree = 0
    lossTakingThree = 0
    winsTakingTwo = 0
    lossTakingTwo = 0
    curTrial = 1
    
    while curTrial < trials:
        if attemptThree():
            winsTakingThree += 1
        else:
            lossTakingThree += 1
            if attemptTwo() == True:
                winsTakingTwo += 1
            else:
                lossTakingTwo += 1
            x.append(curTrial)
            y1.append(winsTakingThree)
            y2.append(winsTakingTwo)
            curTrial += 1
    plt.plot(x, y1, color=colors[colind], label=names[i]+' Wins Taking Three Point', linewidth=2)
    plt.plot(x, y2, color=colors[colind+1], label=names[i]+' Wins Taking Two Point', linewidth=2)
    colind += 2

legend = plt.legend(loc='upper left', shadow=True)
for legobj in legend.legendHandles:
    legobj.set_linewidth(2.6)
plt.show()
     
                            
                
                
            
        