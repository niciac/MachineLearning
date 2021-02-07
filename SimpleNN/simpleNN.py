import numpy as np

def neural_network(X,y):
    W1 = np.random.rand(2,4)
    W2 = np.random.rand(4,1)
    output = np.zeros((4,1))

    for epochs in range(10000):
        layer = 1 / (1 + np.exp(-np.dot(X, W1)))
        output = 1 / (1 + np.exp(-np.dot(layer, W2)))
        error = (y-output)
        W2 += np.dot(layer.T, (2 * error * output * (1 - output)))
        W1 += np.dot(X.T, (np.dot(2 * error * output * (1-output), W2.T) * layer * (1 - layer)))

    return np.round(output).flatten().dtype(int)

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

print("OR", neural_network(X, np.array([[0, 1, 1, 1]]).T))
print("AND", neural_network(X, np.array([[0, 0, 0, 1]]).T))
print("XOR", neural_network(X, np.array([[0, 1, 1, 0]]).T))
print("NAND", neural_network(X, np.array([[0, 1, 1, 1]]).T))
print("NOR", neural_network(X, np.array([[1, 0, 0, 0]]).T))