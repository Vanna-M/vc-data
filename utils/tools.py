def top_words(wordList, num, minimum=1):
    ret = {}
    words= {}
    for i in str(wordList).seperate(" "):
        print i 
        if i in words:
            words[i]+=1
        else:
            words[i] = 1

    i = 0
    for key, value in sorted(words.iteritems(), key=lambda (k,v): (v,k))[::-1]:
        if i > num or minimum > value:
            return ret
        i += 1
        ret[key] = value
    return ret

def textify(text):
    ret = ""
    ignore = False
    openers = ["<","{"]
    closers = [">","{"]

    for i in text:
        if i in closers:
            ignore = False
            ret += " "
        elif i in openers:
            ignore = True
        elif not ignore:
            ret += i
    return ret

def addAll(d, inp, arg):
    for el in inp:
        if el in d:
            if arg not in d[el]:
                d[el].append(arg)
        else:
            d[el] = [arg]
    return d
