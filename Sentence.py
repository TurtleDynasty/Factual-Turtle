import random, re

def getRandomLine(rsv):
    file_h = open(rsv)                  #a file handle for the .txt in question
    limit = file_h.readline()           #the number of lines to search per the .txt
    limit = int(limit)                  #the number literal converted to int
    line = random.randint(0, limit - 1) #which line to search
    
    for x in range(line):
        file_h.readline()               #parse through that shit until search reached
    phrase = file_h.readline()          #if you gotta big d*** lemme search it. 
    phrase = phrase.replace('\n', '')   #get rid of trailing returns cause those are gross
    
    return(phrase)

def makeSentence(rsv):
    pattern = getRandomLine(rsv)        #get a random pattern
    #replace keywords with random calls to a matching word from .txt
    pattern = re.sub(re.escape('noun'), lambda x: getRandomLine('noun.txt'), pattern)
    pattern = re.sub(re.escape('adj'), lambda x: getRandomLine('adjective.txt'), pattern)
    pattern = re.sub(re.escape('verb'), lambda x: getRandomLine('verb.txt'), pattern)
    pattern = re.sub(re.escape('adv'), lambda x: getRandomLine('adverb.txt'), pattern)
    
    return(pattern)