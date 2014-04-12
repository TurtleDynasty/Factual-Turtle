import random, re

def getRandomLine(rsv):
    file_h = open(rsv)
    limit = file_h.readline()
    limit = int(limit)
    
    line = random.randint(0, limit - 1)
    
    for x in range(line):
        file_h.readline()
   
    phrase = file_h.readline()
    phrase.strip('\n')
    
    return(phrase)

def makeSentence(rsv):
    pattern = getRandomLine(rsv)
    pattern.strip('\n')
    pattern = re.sub(re.escape('noun'), lambda x: getRandomLine('noun.txt'), pattern)
    pattern = re.sub(re.escape('adj'), lambda x: getRandomLine('adjective.txt'), pattern)
    pattern = re.sub(re.escape('verb'), lambda x: getRandomLine('verb.txt'), pattern)
    pattern = re.sub(re.escape('adv'), lambda x: getRandomLine('adverb.txt'), pattern)
    return(pattern)

print(makeSentence('pattern.txt'))