# Template 1: compose(composer, verb, music, at-time, at-loc)

from nltk.corpus import wordnet as wn

from script.task4_utils import filter_by_verb as fs
from script.task4_utils.pickle_if_not import _pickle_keyword_sents_if_not
# from script.task4_utils.pickle_if_not import _pickle_keyword_groves_if_not

# This is important to unpickle class Sentence.
import sys
from script import sentence
sys.modules['sentence'] = sentence

##################################
keyword = "study"
synset_str = "learn.v.01"

excludes = []
synwords = fs.getCandidateWords(synset_str, excludes)
print('synwords:', synwords)

##################################
# Step 1: filter sentences by verb
sents = fs._filter_by_verb(synwords)
print("number of filtered sentences:", len(sents))

# pickle keyword sents if never pickled
sents_pickle = _pickle_keyword_sents_if_not(keyword, sents)
print("Create sents pickle:", sents_pickle)

# get or wrap trees if trees do not exist
# this section below doesn't work!
# error: AttributeError: Can't pickle local object 'DependencyGraph.__init__.<locals>.<lambda>'
# groves_pickle = _pickle_keyword_groves_if_not(keyword, sents)
# print("Create groves pickle:", groves_pickle)

# unpickle groves
# groves = pu._get_groves(keyword)
# print("length of groves", len(groves))

####################################
# sample
# idx = 1
# sentence = sentences[1]
# pos_tag = pos_tags[1]
#
# trees = Trees(sentence, pos_tag)
# ctree = trees.cp
# dtree = trees.dp
# netree = trees.ne
#
# print("print ctree:")
# # ctree.pretty_print()
#
# print("print dtree:")
# # print(dtree.to_conll(4))
#
# print("print ner tree:")
# # print(netree)

######################################
# # Step 2: find subject and object
from script.templates import subject as sub
# subjects_all = sub._subject(synwords, sents[:10])
#
# # TEST PRINT
# # for subjects in subjects_all:
# #     print(subjects)
#
# objects_all = sub._object(synwords, sents[:10])
#
# # TEST PRINT
# for objects in objects_all:
#     print(objects)

#### Person and Location
from script.templates import entity
# persons = entity.extractEnt(sents, 'PERSON')
# print('Person:', persons)
# locations = entity.extractEnt(sents, ['GPE','GSP','PERSON','ORGANIZATION'])
# print('Location:', locations)



size = 20 # len(sents)
from script.templates import geo
tolocs = geo._getLocation(sents[10:size], synwords)
print(tolocs)

######################################
# Step 3: extract temporal information
# from script.templates import temporal as time
# time._extract_static_time(sents[100:110])

######################################
# Step 4: extract temporal information