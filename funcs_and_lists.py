#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 18:00:15 2023

@author: monika
"""

sheLovesYou = ['she', 'loves', 'you', 'yeah', 'yeah', 'yeah', 'she', 'loves',
               'you', 'yeah', 'yeah', 'yeah', 'she', 'loves', 'you', 'yeah', 
               'yeah', 'yeah', 'yeah', 'verse', '1', 'paul', 'mccartney', '&',
               'john', 'lennon', 'you', 'think', "you've", 'lost', 'your', 
               'love', 'well', 'i', 'saw', 'her', 'yesterdayayayay', "it's",
               "you", "she's", "thinking", "of", "and", "she", "told", "me",
               "what", "to", "sayayayay", "refrain", "paul", "mccartney", 
               "&", "john", "lennon", "she", "says", "she", "loves", "you",
               "and", "you", "know", "that", "can't", "be", "bad", "yes"]

def lyrics_to_freq(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    print(myDict)
    return myDict

beatles = lyrics_to_freq(sheLovesYou)

def mostCommonWords(freq):
    values = freq.values()
    best = max(values)
    print("best:", best)
    words = []
    for k in freq:
        if freq[k] == best:
            words.append(k)
    print("words:",words)
    return (words, best)

def wordsOften(freq, minTimes):
    result = []
    done = False
    while not done:
        temp = mostCommonWords(freq)
        print("temp:", temp)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                print("w:", w,"freq[w]:", freq[w])
                del(freq[w])
        else:
            done = True
        print("result:", result)
    return result   



