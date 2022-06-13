# import necessary libraries
import tensorflow as tf
from src.utils.functions import mkdir_if_not_exists

# create class
class ClassificationModel:
    # defining variables
    def __init__(self, inputs, features, activation_functions, job):
        self.inputs = inputs
        self.features = features
        self.activation_functions = activation_functions
        self.job = job
        self.all_features = tf.keras.layers.concatenate(self.features)

        if self.job == "classification":
            #  create model to classifiy data (benign or darknet)
            self.x = tf.keras.layers.Dense(32, activation=self.activation_functions)(self.all_features)
            self.x = tf.keras.layers.Dropout(0.5)(self.x)
            self.output = tf.keras.layers.Dense(1)(self.x)
            self.model = tf.keras.Model(self.inputs, self.output)
            self.model.compile(optimizer='adam', loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), metrics=['accuracy'])

        elif self.job == 'characterization':
            # create model to characterize data (by traffic category)

            self.x = tf.keras.layers.Dense(128, activation=self.activation_functions)(self.all_features)
            self.x = tf.keras.layers.Dense(64, activation=self.activation_functions)(self.x)
            self.output = tf.keras.layers.Dense(8, activation='softmax')(self.x)
            self.model = tf.keras.Model(self.inputs, self.output)
            self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        else:
            raise InterruptedError("[!] - Job do not recognised. Select only classification or characterization")

    # load model from file
    def loadModel(self, job):
        if job == 'classification':
            return tf.keras.models.load_model('etc/trainModel/orgClassifier')
        elif job == 'characterization':
            return tf.keras.models.load_model('etc/trainModel/orgCharacterization')
        else:
            raise InterruptedError("[!] - Job do not recognised. Select only classification or characterization")

    # create a function to fit the model
    def fitModel(self, train, val, epochs = 20):
        self.history_model = self.model.fit(train, epochs=epochs, validation_data = val)
        mkdir_if_not_exists('etc/')
        mkdir_if_not_exists('etc/trainModel')
        if self.job == 'classification':
            self.model.save('etc/trainModel/orgClassifier')
        elif self.job == 'characterization':
            self.model.save('etc/train_model/orgCharacterization')
        else:
            raise InterruptedError("[!] - Job do not recognised. Select only classification or characterization")

    # model pointer
    def getModel(self):
        return self.model

    # create a function to evaluate model
    def evaluate(self, test):
        self.loss, self.acc = self.model.evaluate(test)
        print(f"[!] - Accuracy: {self.acc}")