# AISupport chatbot model 0.1

## Requisites
```
Python 3.6 with these packages:
* nltk
* nltk.stem.lancaster
* tflearn
* numpy
* tensorflow
* random
* pickle
* json
* matplotlib.pyplot
```

## How does it work?

1. Train model 
    * Make sure to have your text corpus in "intents.json" file
    * We loop through all our sentences and stem them (divide into individual words) and create dictionary out of them (each word in dictionary is unique)
    * Then create Bag of Words for each sentence 
    * Then we send our vectors (features) that came out of BoW model into our deep neural network
    * Last step is saving everything into pickle file

2. Use model for prediction
    * We start by reconstructing our data structures (that we saved in last step of training)
    * Then we rebuild our deep Neural net model 
    * And after this we can already use it for prediction
    
    
     


## Built with these components
*  Python
* TFlearn framework with Tensorflow backend
