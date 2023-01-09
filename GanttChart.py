import matplotlib.pyplot as plt
import random
fig, ax = plt.subplots()
plt.title('GanttChart')
def make_color(indexList):
    colorList=[]
    lengh_indexList=len(indexList)
    def random_color():
        rand_colors=["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
        return rand_colors
    while True:
        rand_colors=random_color()
        if rand_colors not in colorList:
            colorList.append(rand_colors)
        if len(colorList)==lengh_indexList:
            break
    return colorList
actIndexList=[]
actColorList=[]
def color(index,colorList):
    if index in actIndexList:
        i=actIndexList.index(index)
        color=actColorList[i]
        return color
    else:
        actIndexList.append(index)
        color=random.choice(colorList)
        actColorList.append(color)
        colorList.remove(color)
        return color
def gantt_chart(indexList,indexArray,completionArray,startPoint):
    colorList=make_color(indexList)
    firstPoint=startPoint
    startList=[]
    durationList=[]
    startList.append(startPoint)
    for value in completionArray:
        if value==completionArray[-1]:
            duration=value-startPoint
            durationList.append(duration)
        else:
            duration=value-startPoint
            durationList.append(duration)
            startPoint=value
            startList.append(startPoint)
    completionArray.insert(0,firstPoint)
    for start,duration,index in zip(startList,durationList,indexArray):
        ax.broken_barh([(start,duration)], (1, 0.5), facecolors=color(index,colorList),label=index)
        ax.set_ylim(1,5)
        ax.yaxis.set_visible(False)
        ax.set_xlim(0,max(completionArray))
        ax.set_xticks(completionArray)
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys())
    return plt.show()
def close():
    plt.close('all')