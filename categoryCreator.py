import numpy as np
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import EnglishStemmer
from math import log10, sqrt
stemmer = EnglishStemmer()
ps = PorterStemmer()

topic_datacontrol = open("topics/datacontroller.txt", "r").read()
topic_datacontrol = topic_datacontrol.split("NEXT_POLICY_CODE")
del topic_datacontrol[-1]


topic_purpose = open("topics/purpose.txt", "r").read()
topic_purpose = topic_purpose.split("NEXT_POLICY_CODE")
del topic_purpose[-1]


topic_legalbasis = open("topics/legalbasis.txt", "r").read()
topic_legalbasis = topic_legalbasis.split("NEXT_POLICY_CODE")
del topic_legalbasis[-1]

topic_recipients = open("topics/recipients.txt", "r").read()
topic_recipients = topic_recipients.split("NEXT_POLICY_CODE")
del topic_recipients[-1]

topic_retention = open("topics/retention.txt", "r").read()
topic_retention = topic_retention.split("NEXT_POLICY_CODE")
del topic_retention[-1]

topic_request = open("topics/request.txt", "r").read()
topic_request = topic_request.split("NEXT_POLICY_CODE")
del topic_request[-1]

topic_profiling = open("topics/profiling.txt", "r").read()
topic_profiling = topic_profiling.split("NEXT_POLICY_CODE")
del topic_profiling[-1]

topic_personaldata = open("topics/personaldata.txt", "r").read()
topic_personaldata = topic_personaldata.split("NEXT_POLICY_CODE")
del topic_personaldata[-1]


def tokenizePolicy(textfile):
    policy_token = [word.lower()  for word in word_tokenize(textfile)]
    return(policy_token)

def stemmedToken(textfile):
    policy_token = [ps.stem(word.lower())  for word in word_tokenize(textfile)]
    return(policy_token)

def tokenizeTopic(topic):
    tokenizedPolicies = []
    for policy in topic:
        tokenizedPolicies.append([ps.stem(word.lower())  for word in word_tokenize(policy) if not word in stopwords.words() and word.isalnum()])
    return(tokenizedPolicies)

def createList(policies):
    totallist = []
    for policy in policies:
        totallist.append(policy)
    return(totallist)

def wordCounter(list, n):
    wordOccurence = dict()
    for policy in list:
        for word in policy:
            wordOccurence[word] = 0
            for policy in list:
                if word in policy:
                    wordOccurence[word] += 1
                wordOccurence[word] 
    return(sorted(wordOccurence.items(), key=lambda x: x[1])[-n:])



def topicFinal(topic):  
    tokenizedPolicies = tokenizeTopic(topic)
    wordsCounted = wordCounter(tokenizedPolicies, 15)
    return(wordsCounted)

topic_datacontrol = topicFinal(topic_datacontrol)
topic_purpose = topicFinal(topic_purpose)
topic_legalbasis = topicFinal(topic_legalbasis)
topic_recipients = topicFinal(topic_recipients)
topic_retention = topicFinal(topic_retention)
topic_request = topicFinal(topic_request)
topic_profiling = topicFinal(topic_profiling)
topic_personaldata = topicFinal(topic_personaldata)

import json
with open('example.json', 'w') as fp:
    json.dump([topic_datacontrol,topic_purpose, topic_legalbasis, topic_recipients, topic_retention, topic_request, topic_profiling, topic_personaldata],fp)



