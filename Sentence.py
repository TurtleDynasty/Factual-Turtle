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
    print(pattern + 'end')
    pattern = re.sub(re.escape('noun'), lambda match: getRandomLine('noun.txt'), pattern)
    
    pattern.replace('\n', '')
    return(pattern + 'endl')

print(makeSentence('pattern.txt'))