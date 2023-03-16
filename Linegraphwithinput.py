import matplotlib.pyplot as plt


X = []
Y=[]
graph = {}


def update_graph(X, Y, graph):
    for x, y in zip(X, Y):
        graph[x] = y
    return graph



def xandyinp():
    while True:
        xinp = input("Input x coordinate: ")
        
        if xinp == "":
            break
        else:
            yinp = input("Input y coordinate: ")
            X.append(xinp)
            Y.append(yinp)
            graph[xinp] = yinp

def plot(X,Y):
    X = [int(x) for x in X]
    Y = [int(y) for y in Y]
    plt.plot(X,Y, color='blue')
    plt.title('Example Graph')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    plt.show()


graph = update_graph(X, Y, graph)
#print(graph)

xandyinp()
plot(X,Y)
print(graph)





