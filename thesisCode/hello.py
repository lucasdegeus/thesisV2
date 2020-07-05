import sys
sys.path.append('/media/lucasdegeus/Storage/thesisCode/thesisCode/venv/lib/python3.6/site-packages')
from flask import Flask, session, redirect, url_for, request, jsonify,abort
from markupsafe import escape
from werkzeug.utils import secure_filename
from flask import render_template
import numpy as np
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import EnglishStemmer
from math import log10, sqrt
import requests
import justext
from bs4 import BeautifulSoup
import os
import json

nltk.download('punkt')
nltk.download('stopwords')
stemmer = EnglishStemmer()
ps = PorterStemmer()

pinterest = open("policies/pinterest.txt",encoding="utf8").read()
reddit = open("policies/reddit.txt",encoding="utf8").read()
linkedin = open("policies/linkedin.txt",encoding="utf8").read()
yahoo = open("policies/yahoo.txt",encoding="utf8").read()
spotify = open("policies/spotify.txt",encoding="utf8").read()
tumblr = open("policies/tumblr.txt",encoding="utf8").read()
snapchat = open("policies/snapchat.txt",encoding="utf8").read()
flickr = open("policies/flickr.txt",encoding="utf8").read()
telegram = open("policies/telegram.txt",encoding="utf8").read()
########################################################################
whatsapp = open("policies/whatsapp.txt",encoding="utf8").read()
facebook = open("policies/facebook.txt",encoding="utf8").read()
twitter = open("policies/twitter.txt",encoding="utf8").read()
instagram = open("policies/instagram.txt",encoding="utf8").read()
google = open("policies/google.txt",encoding="utf8").read()
       
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
    
def checker(words, policy):
    word_index = dict()
    for word in words:
        index = np.where(np.array(policy) == word[0])[0]
        word_index[word[0]] = index
    return(word_index)    
    
    
def findIndex(checker, policy):
    indexcount = dict()
    for value in checker:
        occuredmost = []
        for index in checker[value]:
            counter=0
            for othervalue in checker:
                if value == othervalue:
                    continue
                else:
                    if othervalue in policy[index-15:index+15]:
                        counter+=1
                        indexcount[index] = counter
    return(indexcount)

def maxIndex(indexes):
    maxIndex = []
    for item,value in indexes.items():
        if value == indexes[max(indexes, key=indexes.get)]:
            maxIndex.append(item)
    return(maxIndex)

   


def removeDuplicates(indexes):
    finalIndex = [indexes[0]]
    for index in indexes:
        for location in finalIndex:
            if int(index) not in range(location-10,location+10):
                if location == finalIndex[-1:]:
                    finalIndex.append(index)
                else:
                    next
            else:
                break
    return(finalIndex)

def tf(policy,term):
    try:
        return(float(policy.count(term)))
    except:
        return(0)
    
def sortIndex(indexes, policy):
    sortedIndex = dict()
    for index in indexes:
        sortedIndex[index] = tf(policy, policy[index])
    return((sortedIndex))



# def ranker(sortedIndex, topicIndex):
#     rankedWords = dict()
#     maximum = dict()
#     for item,value in sortedIndex.items():
#         rankedWords[item] = topicIndex[item] / sortedIndex[item]
#     for item,value in rankedWords.items():
#         if value == rankedWords[max(rankedWords, key=rankedWords.get)]:
#             maximum[item] = value
#     return(maximum)

def ranker(sortedIndex, topicIndex, stemmedpolicy, wordcounted):
    rankedWords = dict()
    maximum = dict()
    for item,value in sortedIndex.items():
        for word in wordcounted:
            if word[0] == stemmedpolicy[item]:
                occurencesTraining = int(word[1])
        rankedWords[item] = topicIndex[item]**2 / sortedIndex[item] * occurencesTraining
    for item,value in rankedWords.items():
        if value == rankedWords[max(rankedWords, key=rankedWords.get)]:
            maximum[item] = value
            print(maximum[item], item)
    return(maximum)

def minimumFrequency(sortedIndexes):
    minimum = dict()
    for item,value in sortedIndexes.items():
        if value == sortedIndexes[min(sortedIndexes, key=sortedIndexes.get)]:
            minimum[item] = value
    return(minimum)

def printContext(indexes, full_policy):
    for index in indexes:
        return(" ".join(full_policy[index-20:index+20]))
        


# def alles2(topic, policy):
#     token_policy = tokenizePolicy(policy)
#     token_policy_stemmed = stemmedToken(policy)
    
    
#     tokenizedPolicies = tokenizeTopic(topic)
#     wordsCounted = wordCounter(tokenizedPolicies, 10)
#     checkedPolicy = checker(wordsCounted, token_policy_stemmed)
#     topicIndex = findIndex(checkedPolicy, token_policy_stemmed)
#     sortedIndex = sortIndex(topicIndex.keys(), token_policy)
#     rankedIndex = (ranker(sortedIndex,topicIndex))
#     printContext(rankedIndex, token_policy)
# #     print(topicIndex)
# #     print(sortedIndex, topicIndex)
# check = alles2(topic_datacontrol, reddit)

jsonfile = open('example.json')
jsonstr = jsonfile.read()
def topicDefiner(topic):
    if topic == 'datacontroller':
        return(json.loads(jsonstr)[0])
    if topic == 'purpose':
        return(json.loads(jsonstr)[1])
    if topic == 'legalbasis':
        return(json.loads(jsonstr)[2])
    if topic == 'recipients':
        return(json.loads(jsonstr)[3])
    if topic == 'retention':
        return(json.loads(jsonstr)[4])
    if topic == 'request':
        return(json.loads(jsonstr)[5])
    if topic == 'profiling':
        return(json.loads(jsonstr)[6])
    if topic == 'personaldata':
        return(json.loads(jsonstr)[7])

def returnTopIndex(topic, policy):
    token_policy = tokenizePolicy(policy)
    token_policy_stemmed = stemmedToken(policy)
    

    # jsonfile = open('example.json')
    # jsonstr = jsonfile.read()
    wordsCounted = topic
    checkedPolicy = checker(wordsCounted, token_policy_stemmed)
    topicIndex = findIndex(checkedPolicy, token_policy_stemmed)
    sortedIndex = sortIndex(topicIndex.keys(), token_policy)
    rankedIndex = (ranker(sortedIndex,topicIndex, token_policy_stemmed, wordsCounted))
#     print(topicIndex)
#     print(sortedIndex, topicIndex)
    # print(printContext(rankedIndex, policy))
    return(rankedIndex.keys())


def returnCategories(policy):
    try:
        categorizedPolicy = tokenizePolicy(policy)

        datacontroller = list(returnTopIndex(topicDefiner('datacontroller'), policy))
        datacontroller.append('datacontroller')

        purpose = list(returnTopIndex(topicDefiner('purpose'), policy))
        purpose.append('purpose')

        legalbasis = list(returnTopIndex(topicDefiner('legalbasis'), policy))
        legalbasis.append('legalbasis')

        recipients = list(returnTopIndex(topicDefiner('recipients'), policy))
        recipients.append('recipients')

        retention = list(returnTopIndex(topicDefiner('retention'), policy))
        retention.append('retention')

        request = list(returnTopIndex(topicDefiner('request'), policy))
        request.append('request')

        profiling = list(returnTopIndex(topicDefiner('profiling'), policy))
        profiling.append('profiling')

        personaldata = list(returnTopIndex(topicDefiner('personaldata'), policy))
        personaldata.append('personaldata')

        categories = [datacontroller, purpose, legalbasis, recipients, retention,request, profiling,personaldata ]
        for category in categories:
            value = category[-2]
                # try:
                #     categorizedPolicy[value-25] = "<h1> SECTION:" + category[-1] + "</h1>" + "<div id='" + category[-1] + "'>" + "<b>" + categorizedPolicy[value-25]
                # except:
                #     categorizedPolicy[value] = "<div id='" + category[-1] + "'>" + "<b>" + categorizedPolicy[value]
                # try:
                #     categorizedPolicy[value+25] = categorizedPolicy[value+25] + "</b></div>"
                # except:
                #     categorizedPolicy[value] = categorizedPolicy[value] + "</b></div>"

                
            try:
                categorizedPolicy[value-15] = "<h1 id=' SECTION:" + category[-1] + " '>" + categorizedPolicy[value-15]
            except:
                categorizedPolicy[value] = "<h1 SECTION:" + category[-1] + " >" + categorizedPolicy[value]
        print(categorizedPolicy[3023-25:3023])
        return(" ".join(categorizedPolicy))
    except:
        return(False)


    #     for value in category:

    #         if type(value) == str:
    #             next
    #         else:

    #             # try:
    #             #     categorizedPolicy[value-25] = "<h1> SECTION:" + category[-1] + "</h1>" + "<div id='" + category[-1] + "'>" + "<b>" + categorizedPolicy[value-25]
    #             # except:
    #             #     categorizedPolicy[value] = "<div id='" + category[-1] + "'>" + "<b>" + categorizedPolicy[value]
    #             # try:
    #             #     categorizedPolicy[value+25] = categorizedPolicy[value+25] + "</b></div>"
    #             # except:
    #             #     categorizedPolicy[value] = categorizedPolicy[value] + "</b></div>"

                
    #             try:
    #                 categorizedPolicy[value-15] = "<h1 id=' SECTION:" + category[-1] + " '>" + categorizedPolicy[value-15]
    #             except:
    #                 categorizedPolicy[value] = "<h1 SECTION:" + category[-1] + " >" + categorizedPolicy[value]
    # print(categorizedPolicy[3023-25:3023])
    # return(" ".join(categorizedPolicy))

    #//




def webScraper(url):
    response = requests.get(url)
    paragraphs = justext.justext(response.content, justext.get_stoplist('English'))
    returningParagraphs = list()
    for item in paragraphs:
        returningParagraphs.append(item.text)
    return(returningParagraphs)

def exists(var):
     var_exists = var in locals() or var in globals()
     return var_exists
names=['lucas', 'pieter' , 'geit']


app = Flask(__name__)
print("NewSession------------------")

@app.errorhandler(500)
def server_error(e):

    email_admin(message="Server error", url=request.url, error=e)

    app.logger.error(f"Server error: {request.url}")

    return "hi", 500


@app.route('/about')
def about():
    return(render_template('about.html'))


@app.route('/',  methods=['POST', 'GET'])
def mainIndex():
    if request.method == 'POST':
        print("POSTER")
        if 'file' not in request.files:
            if 'urlInput' in request.form:
                print("hi")
                return(render_template('checktext.html', type='get', checkText=webScraper(request.form['urlInput'])))
            else:
                policy = request.form['description']
                cleantext = BeautifulSoup(policy, "lxml").text
                text = returnCategories(cleantext)
                if text == False:
                    return("false")
                else:
                    return(render_template('navigationpage.html', content=text.split('<h1')))
    print(os.listdir('policies'))
    policies = []
    for policy in os.listdir('policies'):
        policies.append(policy.split(".")[0])
    return (render_template('index.html', topics=policies))

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    c = request.args.get('policy')
    policycontent = open("policies/" + c + ".txt",encoding="utf8").read()
    return jsonify(policycontent)


if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run(debug=True, host='0.0.0.0')
