from sklearn.externals.six import StringIO
from sklearn import tree
import pydotplus
import matplotlib.pyplot as plt
X = [[1,1,1,0], [1,1,1,1], [2,1,1,0], [2,3,2,1], [1,2,1,0], [1,3,2,0], [3,2,1,0],
[3,3,2,0], [3,3,2,1], [3,2,2,0], [1,2,2,1], [2,2,1,1], [2,1,2,0], [3,2,1,0]]

Y = [0,0,1,1,0,1,1,1,0,1,1,1,1,0]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

graph.write_pdf('datavis/game.pdf')

#branchNode = dict(boxstyle='sawtooth', fc='0.8')
#leafNode = dict(boxstyle = 'round4', fc='0.8')
#startNode = dict(boxstyle='sawtooth', fc='0.9')
#def createPlot():
#    fig = plt.figure(1, facecolor='white')
#    fig.clf()
#    createPlot.ax1 = plt.subplot(111, frameon=False)
#    plotNode =('from here', (0.3,0.8), (0.3, 0.8), startNode)
#    plotNode =('a decision node', (0.5, 0.1), (0.3, 0.8), branchNode)
#    plotNode = ('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
#    plt.show()
    
createPlot()