import matplotlib.pyplot as plt
def drawCurve(a,CurrentLevel):#a即前文中的系数a，CurrentLevel即Xn
    RegentLevel = []
    for i in range(30):
        RegentLevel.append(CurrentLevel)
        CurrentLevel = (a*CurrentLevel-a*(CurrentLevel**2) )
    Time = [i for i in range(30)]
    plt.plot(Time, RegentLevel)
for i in range(1,100):
    drawCurve(4,i/100)
plt.annotate('a = 6',xy = (5, 0.4),xytext = (6,0.9),arrowprops = dict(facecolor = 'black',shrink = 0.1))

