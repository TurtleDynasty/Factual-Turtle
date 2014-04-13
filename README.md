Factual Turtle
==============
The factual turtle twitter application by David, Alec, Jered, and Ben.  

Dependencies
------------
Python 2.7.6  
Twitter-Python (https://code.google.com/p/python-twitter/)  
bootstrap  
Simple json  
ajax  

Sentence.py
-----------
Generates sentences based on patterns pulled from .txt  
getRandomLine(rsv) returns a single trimmed line from a return-separated-value .txt file.  
makeSentence(rsv) returns a generated sentence from one item from a return-separated-value .txt file. Recommend using pattern.txt

*.txt
----
All .txt start with a number indicating the number of lines to follow.  
Each line after is a word or phrase which can be used for generation of english nonsense.  
The last line is an empty line. 
 
'pattern.txt' defines sentences patterns which the application can use for generation of english nonsense.  
'noun.txt' defines a list of nouns that can be used for generation of english nonsense.  
'verb.txt' defines a list of verbs that can be used... and so on.  

mistype.py
----------
Recursive string scrambler  
mistype(letter) returns a single char of a random keystroke close to letter, restricted to a-z.  
mash(phrase, recur) replaces recurn number of characters in phrase one at a time through recursive calls.  
