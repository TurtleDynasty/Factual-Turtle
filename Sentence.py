import random, re

def getRandomLine(rsv):
    file_h = open(rsv)
    limit = file_h.readline()
    #limit.replace('\n', '')
    limit = int(limit)
    
    line = random.randint(1, limit)
    string = ''
    
    for x in range(line):
        string = file_h.readline()
    string.replace('\n', '')
    
    return(string)

def makeSentence(rsv):
    file_h = open(rsv)
    pattern = getRandomLine(rsv)
    pattern = re.sub(re.escape('noun'), lambda match: getRandomLine('noun.txt'), pattern)
    
    pattern.replace('\n', '')
    return(pattern)

print(makeSentence('pattern.txt'))