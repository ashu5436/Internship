### Fake News Classifier
According to the some researchers, Fake news has become one of the biggest problems of our age. It has serious impact on our online as well as offline discourse. Fake news's simple meaning is to incorporate information that leads people to the wrong path. Nowadays fake news spreading like water and people share this information without verifying it. This is often done to further or impose certain ideas and is often achieved with political agendas.


Natural Language Process (NLP) and Deep Learning comes as a vital tool to solve almost any type of business problems to help companies optimize the standards resulting in overall revenue and profits growth. Moreover, it also improves their marketing strategies and demands focus on changing trends.


Now, if we talk about the Fake News Classifier project what I feel is that LSTM RNN would be the key recurrent neural network in identifying these fake news as the news title would be having too many words in each documents of its corpus and definitely it will help us to preserve the Long Term- Short Term Memory of each words in the system, so that we can get genuine prediction.


Also, implementation of Deep Learning and Deep NLP techniques like- Stemming, Stopwords, Tensorflow, Keras, Embedding, LSTM, Dense, Dropout, One_Hot encoder, Pad_Sequence, Sequential and Regular Expression would be really helpful while predicting the target variable. So, here in this project I’ll be using NLP with Deep Learning.


I'll be using here stemming technique not lemmatization as we are not making project for any particular text summarization or language translation where the output need to be well organized and meaningful.


Also, keras provides the one_hot() function that creates a hash/index of each word of a document as an efficient integer encoding. The Embedding has a vocabulary of 5000 and an input length of 50(Max documents length). We will choose an embedding space i.e. our output dimension as of 100 dimensions(any dimension). The model is a simple binary classification model. The output from the embedding layer will be 50 vectors of 100 dimension each, one for each word.


we have created our neural networks having input as length of 5000 vocabularies then we have added first hidden layer i.e. embedding layer having input length 50 and output dimension as 100. Then again added a second hidden layer as LSTM (300) it means that it will have a layer of 300 'smart neurons' and the output will be a vector of 300 dimensions as well. In the output layer I’ve applied the activation function as ‘sigmoid’ since it is a binary classification problem and will be getting only one output at a time. I’ve applied dropout= 30% it means that it will disconnect 30% impractical neurons to reduce the overfitting problem. 


Once the model is define will separate our target and feature variable and will convert it into array, so that we can fit our model with train_test_split method. I’ve selected epochs=10 and batch_size=100 while training the model. Also, I have taken the validation split over the test data to compare the accuracy and loss w.r.t. that of training data.Since, Classification metrics can't handle a mix of binary and continuous targets, so have applied the concept as - if y_pred>0.5 then convert it into 1 otherwise 0.


### Below are some inputs which were really helpful in this model building

### Embeddings-
Are a great way to deal with NLP problems because of two reasons! First it helps in dimensionality reduction over one-hot encoding as we can control the number of features. Second it is capable of understanding the context of a word so that similar words have similar embeddings.

### LSTM-
Long Short Term Memory Networks is an advanced RNN, a sequential network that allows information to persist. It is capable of handling the vanishing gradient problem faced by RNN. A recurrent neural network is also known as RNN and is used for persistent short term memory.

### Dense-
In any neural network, a dense layer is a layer that is deeply connected with its preceding layer which means the neurons of the layer are connected to every neuron of its preceding layer. This layer is the most commonly used layer in artificial neural network networks. In Keras, "dense" usually refers to a single layer.

### Dropout-
It refers to dropping out the nodes (input and hidden layer) in a neural network to control overfitting problem.

### One Hot Encoding-
Converts text into vector.

### Padding-
To ensure that all the input sequence data is having the same length we pad or truncate the input data points.

### Sequential-
In Keras it usually refers to an entire model, not just one layer. Sequential refers to the way we build models in Keras using the sequential API. Sequential API is used to create models layer-by-layer. In sequential models, the input, hidden and output layers are stacked in the model sequentially. The information propagates from the input to the output through hidden layers.


![image](https://user-images.githubusercontent.com/101721582/211142898-676977f7-af5c-48c6-beb9-6a107c11e475.png)

### In an LSTM network, basically three gates are present-

### Input gate-
discover which value from input should be used to modify the memory. Sigmoid function decides which values to let through 0, 1 and tanh function gives weightage to the values which are passed deciding their level of importance ranging from -1 to 1.

### Forget gate-
discover what details to be discarded from the block. It is decided by the sigmoid function. It looks at the previous state and the content input and outputs a number between 0 (omit this) and 1 (keep this) for each number in the cell state.

### Output gate-
the input and the memory of the block is used to decide the output. Sigmoid function decides which values to let through 0, 1; and tanh function gives weightage to the values which are passed deciding their level of importance ranging from -1 to 1 and multiplied with output of Sigmoid.

![image](https://user-images.githubusercontent.com/101721582/211142795-a84af071-aa32-42a7-bc61-8f2173c220b8.png)

At each epoch our model training loss is getting decreasing and training accuracy is getting increasing which shows that our model is performing well with LSTM RNN neural networks and it’s giving testing accuracy as 98% which is an excellent accuracy.

Also validation loss and validation accuracy is almost similar to that of Training loss and Training accuracy respectively, which indicates this model is a perfectly fit for predicting the fake news. Kindly see the below graph for clear understanding of how the LSTM RNN performs while predicting the fake news.

![image](https://user-images.githubusercontent.com/101721582/211142823-aefdfe10-0582-48bf-b27e-b7bc4e42d939.png)
