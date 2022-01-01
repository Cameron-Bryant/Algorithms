from sklearn.neural_network import MLPClassifier
from mlxtend.data import loadlocal_mnist

train_x, train_y = loadlocal_mnist(
    images_path = 'C://Users//camer//Desktop//MNIST_Data//train-images-idx3-ubyte',
    labels_path = 'C://Users//camer//Desktop//MNIST_Data//train-labels-idx1-ubyte'
                                 )
test_x, test_y = loadlocal_mnist(
    images_path='C://Users//camer//Desktop//MNIST_Data//t10k-images-idx3-ubyte', 
    labels_path='C://Users//camer//Desktop//MNIST_Data//t10k-labels-idx1-ubyte')

nn = MLPClassifier(max_iter=300, hidden_layer_sizes = (32,)).fit(train_x, train_y)
#784 x 32 x 10 neural network
print("Score/Accuracy:>" + str(nn.score(test_x, test_y)))
#gets acc of .94
