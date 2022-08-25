import sys
import re
count = 0
lst = []
wrd_cunt = {}
print('Num of arguments', len(sys.argv))
if len(sys.argv) < 2:
    raise Exception(sys.argv[0], "requires a file path in the next argument")
print('first argument is:', sys.argv[1])


with open(sys.argv[1]) as f:
    lines = f.readlines()
    for line in lines:
        count +=1
        for word in line:
            if word.isalpha() == True:
                word = word.lower()
                if word not in wrd_cunt:
                    wrd_cunt[word] = 1
                else:
                    wrd_cunt[word] += 1
    print("Word Count\n****************************************")
    for w in sorted(wrd_cunt, key=wrd_cunt.get, reverse=True):
        print(w, wrd_cunt[w])
    print("***************\nLine Count:" + str(count))
        