import random, re

def getRandomLine(rsv):
    file_h = open(rsv)
    limit = file_h.readline()
    limit = int(limit)
    
    line = random.randint(0, limit - 1)
    
    for x in range(line):
        file_h.readline()
    string = file_h.readline()
    #string.replace('\n', '')
    
    return(string)

def makeSentence(rsv):
    pattern = getRandomLine(rsv)
    print(pattern)
    pattern = re.sub(re.escape('noun'), lambda match: getRandomLine('noun.txt'), pattern)
    
    pattern.replace('\n', '')
    return(pattern)

print(makeSentence('pattern.txt'))