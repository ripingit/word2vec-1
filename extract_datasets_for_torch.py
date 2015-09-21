
import random
import numpy as np
from cs224d.data_utils import *


random.seed(1)
dataset = StanfordSentiment()
tokens = dataset.tokens()
nWords = len(tokens)
trainset = dataset.getTrainSentences()
nTrain = len(trainset)
trainLabels = [None for _ in range(nTrain)]
trainSentences = [None for _ in range(nTrain)]

for i in xrange(nTrain):
    trainWords, trainLabel = trainset[i]
    trainLabels[i] = str(trainLabel + 1) + '\n'
    trainSentences[i] = ' '.join(trainWords) + '\n'

with open('trainSentences_raw', 'w') as f:
    f.writelines(trainSentences)
with open('trainLabels', 'w') as f:
    f.writelines(trainLabels)

b = 1
pass


