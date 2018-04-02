import os

#returns the top 50 companies according to crunchbase
def get_big_companies():
    resource = "data/CrunchbaseCompanies.html"
    key = 'href="/organization/'
    return search(resource,key)

def search(resource, key):
    directory = os.path.dirname(__file__)
    resource = os.path.join(directory,resource)
    ret = []
    inp = open(resource,'r')
    for line in inp.readlines():
        if key in line:
            word = ''
            done = False
            for letter in line[::-1]:
                if done:
                    if letter == key[-1]:
                        break
                    word = letter + word
                elif letter == '"':
                    done = True
            ret.append(word)
    return ret
