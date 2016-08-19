inputString = "reneessomba"
outputSting = "r1e3n1s2o1m1b1a1"

def stringCount (string):
    key = [i[0] for i in map(lambda x : x.split(),inputString)]
    
    dedupe_key = []           
    for i in range(len(key)):
        if key[i] not in dedupe_key:
            dedupe_key.append(key[i])
      
    x = []
    for j in range(len(dedupe_key)):
        x.append(dedupe_key[j])
        x.append(len([i for i in key if i == dedupe_key[j]]))
    
    x = ''.join(str(i) for i in x)
    return(x)

if __name__ == "__main__":
    print(stringCount(inputString))
