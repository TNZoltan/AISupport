# things we need for NLP
import nltk
from nltk.stem.lancaster import LancasterStemmer
from sklearn.model_selection import train_test_split

stemmer = LancasterStemmer()

# things we need for Tensorflow
import numpy as np
import tflearn
import tensorflow as tf
import random
import json
import pickle

# import our intents file
with open('intents1.json') as json_data:
    intents = json.load(json_data)

words = []
classes = []
documents = []
ignore_words = ['?', '(', ')', '\'', ',', '/', '.', '-']

# loop through each sentence in our intents patterns
for intent in intents['Intents']:
        # tokenize each word in the sentence
        w = nltk.word_tokenize(intent['Question'])
        # add to our words list
        words.extend(w)
        # add to documents in our corpus
        documents.append((w, intent['Question']))
        # add to our classes list
        if intent not in classes:
            classes.append(intent['Question'])

# stem and lower each word and remove duplicates
for myword in words:
    print(myword)

words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
print("dictionary length: ", len(words))

for myword in words:
    print(myword)

# create our training data
training = []
output = []
# create an empty array for our output
output_empty = [0] * len(classes)

# training set, bag of words for each sentence
for doc in documents:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # stem each word
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    # create our bag of words array
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# shuffle our features and turn into np.array
random.shuffle(training)
training = np.array(training)

# create train and test lists
x_data = list(training[:, 0])
y_data = list(training[:, 1])

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2)

x = np.random.randint(0, len(x_train))

# reset underlying graph data
tf.reset_default_graph()
# Build neural network
net = tflearn.input_data(shape=[None, len(x_train[0])])
# net = tflearn.fully_connected(net, 128, activation="relu")
# net = tflearn.dropout(net, 0.5)
net = tflearn.fully_connected(net, 512, activation="relu", regularizer='L2')
net = tflearn.fully_connected(net, 128, activation="relu", regularizer='L2')
net = tflearn.fully_connected(net, len(y_train[0]), activation='softmax')
net = tflearn.regression(net)

# Define model and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
# Start training (apply gradient descent algorithm)
model.fit(x_train, y_train, validation_set=(x_test, y_test), n_epoch=100, batch_size=8, show_metric=True)

model.save('model.tflearn')

pickle.dump({'words': words, 'classes': classes, 'train_x': x_train, 'train_y': y_train}, open("training_data", "wb"))
