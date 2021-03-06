from numpy import exp, array, random, dot

class NeuralNetwork():
    def __init__(self):
        # seed the number generator
        random.seed(1)

        # assign random weights to the synapses
        self.synaptic_weights = 2 * random.random((3, 1)) - 1

    # the sigmoid function
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # gradient of the sigmoid curve
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in xrange(number_of_training_iterations):
            # pass the training set through the neural net
            output = self.think(training_set_inputs)

            # calculate the error
            error = training_set_outputs - output

            # multiply the error by the input ad again by the gradient of the sigmoid curve
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

            # adjust weights
            self.synaptic_weights += adjustment

    def think(self, inputs):
        # pass inputs through our single neuron neural network
        return self.__sigmoid(dot(inputs, self.synaptic_weights))


if __name__ == '__main__':

    # initialize a single neuron neural network
    neural_network = NeuralNetwork()

    print 'Random starting synaptic weights:'
    print neural_network.synaptic_weights

    # the training set
    training_set_inputs = array([[0,0,1], [1,1,1], [1,0,1], [0,1,1]])
    training_set_outputs = array([[0,1,1,0]]).T

    # train the neural network using a training set
    neural_network.train(training_set_inputs, training_set_outputs, 10000)

    print 'New synaptic weights after training:'
    print neural_network.synaptic_weights

    # test neural network
    print('predicting... new situation [1, 0, 0]')
    print neural_network.think(array([1,0,0]))
