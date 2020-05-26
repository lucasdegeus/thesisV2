import json
from collections import Counter

jsonfile = open('example.json')
jsonstr = jsonfile.read()

for category in json.loads(jsonstr):
    for word in category:
        print(word[0], ":" , word[1], end=', ')
    print(' ---- ')


# occurencesInCategories = Counter([word[0] for words in json.loads(jsonstr) for word in words])
# for word in sorted(occurencesInCategories.items() ,  key=lambda x: x[1], reverse=True):
#     print(word[0], word[1])