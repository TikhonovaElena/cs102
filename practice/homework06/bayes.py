from collections import Counter
import math
class NaiveBayesClassifier:

    def __init__(self, alpha):
        self.alpha = 0.05

    def fit(self, x_train, y_train):
        """ Fit Naive Bayes classifier according to X, y. """
        self.labels = set(y_train)
        self.number_of_words = 0
        self.words_of_type = {}
        self.label_of_title = dict(zip(x_train, y_train))
        self.counted_words = []
        self.counted_w_of_type = {}
        self.model = {}
        self.feature_vector = set()
        self.feature_vector_size = 0

        words = ''
        for title in x_train:
            words += title
        self.counted_words = Counter(words.split())

        for title in self.label_of_title:
            try:
                self.words_of_type[self.label_of_title[title]] += title
            except KeyError:
                self.words_of_type[self.label_of_title[title]] = title

        for label in self.words_of_type:
            self.words_of_type[label] = self.words_of_type[label].split()
            self.number_of_words += len(self.words_of_type[label])
            self.feature_vector = self.feature_vector|set(self.words_of_type[label])
            self.counted_w_of_type[label] = {}
        self.feature_vector_size = len(self.feature_vector)

        for label in self.words_of_type:
            self.counted_w_of_type[label] = Counter(self.words_of_type[label])

        for word in self.feature_vector:
            #в model кортеж - (количество слов, логарифмированная вероятность)
            self.model[word] = {label: self.word_likelihood(word, label) for label in self.labels}
        return [self.labels, self.model]

    def predict(self, x):
        """ Perform classification on an array of test vectors X. """
        words = x.split()
        probability_label_word = [[],[]]
        counter = 0
        for label in self.labels:
            probability_label_word[0].append(label)
            probability_label_word[1].append(math.log(len(self.words_of_type[label])/self.number_of_words))
            for word in words:
                try:
                    probability_label_word[1][counter] += self.model[word][label][1]
                except KeyError:
                    pass
            counter += 1
        log = probability_label_word[1][0]
        label = probability_label_word[0][0]
        for counter in range(0, len(probability_label_word[1])):
            if probability_label_word[1][counter] > log:
                log = probability_label_word[1][counter]
                label = probability_label_word[0][counter]
        return label

    def score(self, x_test, y_test):
        """ Returns the mean accuracy on the given test data and labels. """
        pass

    def word_likelihood(self, word, label):
        probability_word_label = math.log(self.counted_w_of_type[label][word] + self.alpha) - \
            math.log(self.counted_words[word] + self.alpha*self.feature_vector_size)
        return(self.counted_w_of_type[label][word], probability_word_label)
