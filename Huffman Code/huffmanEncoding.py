# -*- coding: utf-8 -*-
# Author: Pawan Pinjarkar
# Applied Algorithms
# CSCI-B505 Fall 2017
# Programming Assignment 4

from collections import defaultdict
import heapq

# This method encodes the tree ( heap) as per Huffman encoding elgorithm
def encode(tree,path):
    try:
        goRight = False
        goLeft = False
        isChar = (tree[1]).keys()[0]=='char'
        
        if isChar is False:
            goLeft = (tree[1]).keys()[1]=='left'
            goRight = (tree[1]).keys()[0]=='right'
        if(goRight):
            encode(tree[1]['right'],path+"1")
        if(goLeft):
            encode(tree[1]['left'],path+"0")
        if isChar:
            output[tree[1]['char']]=path
        if len(output.keys())==32:
            return output 
    except TypeError as e :
        print(e.message)
        
####################################################################
# Program execution starts here
####################################################################
# Read the text file, replace newline characters into a blank and convert into a string variable
with open('The_Young_Train_Master_by_Burton_Egbert_Stevenson.txt', 'r') as myfile:
    word = myfile.read().replace('\n', '')

# convert all the text to lower case before counting the frequencies. This is necessary as we are using 32 bit encoding
wordLowerCase = word.lower()

letters = defaultdict(int)
output = defaultdict(int)
frequencies = defaultdict(int)
validChars = 0
path = ""

# Construct the valid character set, 32 chars long
charset =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
          'r','s','t','u','v','w','x','y','z','!',' ',',','.','!','?',"'"]

# Check every character from the input string 
# but count the frequency for only those characters which are present in the character set
for letter in wordLowerCase:
    letters[letter] += 1
    if letter in letters and letter in charset :
        frequencies[letter] = letters[letter]

# Count the number of valid characters
for l in frequencies:
    validChars = validChars+frequencies[l]

# Construct a list which contains the frequencies of each character. This becomes the base of heap
heap = [[value, {'char':key}] for key,value in frequencies.items()]

# Transform list named heap into a heap data structure, in-place, in linear time.
heapq.heapify(heap)

# Merge nodes
while(len(heap)>1):
    # Pop and return the smallest item from the heap, maintaining the heap invariant
    node1 = heapq.heappop(heap)
    node2 = heapq.heappop(heap)
    
    node = [node1[0]+node2[0],{'left':node1,'right':node2}]
    
    # Push the value item onto the heap, maintaining the heap invariant.
    heapq.heappush(heap,node )
    
encodedData = encode(heap[0],path)

print "Character".ljust(20)+"Frequency".ljust(20)+"Huffman Code".ljust(20)+"Bits"
result = {}

# Just some processing here
for key, huffmanCode in encodedData.items():
    for key1,freq in frequencies.items():
        if key == key1:
            result[key]= [freq,huffmanCode]

Totalbits = 0
# Print the result
for key,value in result.items(): 
    character = key
    freq = value[0]
    huff = value[1]
    bitsLength = len(value[1])
    bits = bitsLength*value[0]
    
    Totalbits = Totalbits + bits
    print character.ljust(20),str(freq).ljust(20),huff.ljust(20),bits
 

print "\n32 bit characters encoding was used."    
print "The text was encoded using",Totalbits,"bits."   
print "The text had ",validChars," valid characters."
print "Using a 5-bit fixed length encoding, this would have been",5*validChars,"bits long."
print "So we saved",((validChars*5)-Totalbits),"bits!"   
    
    
    
    
        