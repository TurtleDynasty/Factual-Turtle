import random

def mistype(letter):
    if letter == 'q':
        q = {'w':1,'s':2,'a':3}
        return random.choice(q.keys())
    elif letter == 'w':
        w = {'q':1,'e':2,'a':3,'s':4,'d':5}
        return random.choice(w.keys())
    elif letter == 'e':
        e = {'w':1,'s':2,'d':3,'f':4,'r':5, 'ee':6}
        return random.choice(e.keys())
    elif letter == 'r':
        r = {'e':1,'d':2,'f':3,'g':4,'t':5}
        return random.choice(r.keys())
    elif letter == 't':
        t = {'r':1,'f':2,'g':3,'h':4,'y':5}
        return random.choice(t.keys())
    elif letter == 'y':
        y = {'t':1,'g':2,'h':3,'j':4,'u':5,}
        return random.choice(y.keys())
    elif letter == 'u':
        u = {'y':1,'h':2,'j':3,'k':4,'i':5}
        return random.choice(u.keys())
    elif letter == 'i':
        i = {'u':1,'j':2,'k':3,'l':4,'o':5}
        return random.choice(i.keys())
    elif letter == 'o':
        o = {'i':1,'k':2,'l':3,'p':4, 'ooo':5}
        return random.choice(o.keys())
    elif letter == 'p':
        p = {'o':1,'l':2}
        return random.choice(p.keys())
    elif letter == 'a':
        a = {'aa':1,'aaa':2,'aaaa':3,'z':4,'x':5,'s':6,'w':7,'q':8}
        return random.choice(a.keys())
    elif letter == 's':
        s = {'q':1,'w':2,'e':3,'a':4,'s':5,'d':6,'z':7,'x':8,'c':9}
        return random.choice(s.keys())
    elif letter == 'd':
        d = {'w':1,'e':2,'r':3,'s':4,'d':5,'f':6,'x':7,'c':8,'v':9}
        return random.choice(d.keys())
    elif letter == 'f':
        f = {'e':1,'r':2,'t':3,'d':4,'f':5,'g':6,'c':7,'v':8,'b':9}
        return random.choice(f.keys())
    elif letter == 'g':
        g = {'r':1,'t':2,'y':3,'f':4,'g':5,'h':6,'v':7,'b':8,'n':9}
        return random.choice(g.keys())
    elif letter == 'h':
        h = {'t':1,'y':2,'u':3,'g':4,'h':5,'j':6,'b':7,'n':8,'m':9}
        return random.choice(h.keys())
    elif letter == 'j':
        j = {'y':1,'u':2,'i':3,'h':4,'j':5,'k':6,'n':7,'m':8}
        return random.choice(j.keys())
    elif letter == 'k':
        k = {'u':1,'i':2,'o':3,'j':4,'k':5,'l':6,'m':7}
        return random.choice(k.keys())
    elif letter == 'l':
        l = {'i':1,'o':2,'p':3,'k':4,'l':5}
        return random.choice(l.keys())
    elif letter == 'z':
        z = {'a':1,'s':2,'x':3}
        return random.choice(z.keys())
    elif letter == 'x':
        x = {'z':1,'a':2,'s':3,'d':4,'c':5}
        return random.choice(x.keys())
    elif letter == 'c':
        c = {'x':1,'s':2,'d':3,'f':4,'v':5}
        return random.choice(c.keys())
    elif letter == 'v':
        v = {'c':1,'d':2,'f':3,'g':4,'b':5}
        return random.choice(v.keys())
    elif letter == 'b':
        b = {'v':1,'f':2,'g':3,'h':4,'n':5}
        return random.choice(b.keys())
    elif letter == 'n':
        n = {'b':1,'g':2,'h':3,'j':4,'m':5}
        return random.choice(n.keys())
    elif letter == 'm':
        m = {'n':1,'h':2,'j':3,'k':4}
        return random.choice(m.keys())
    elif letter == ' ':
        space = {', ':1,'  ':2}
        return random.choice(space.keys())
    else:
        return letter
    
def mash(phrase, recur):
    recur -= 1
    value = str(phrase)
    L = list(value)
    
    R = random.choice(value)    #choose random element from string
    I = L.index(R)              #save index of that element
    M = mistype(R)              #chose a replacement character
    L.remove(R)                 #remove original character
    L.insert(I,M)               #insert new character at index
    
    J = ''.join(L)                  #turn the list back into a string
    if recur <=0:
        return(J)
    else:
        return mash(J, recur)
#print(mash('aba', 2))
