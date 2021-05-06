from collections import Counter

def groupStrings(input):

    dict = {}

    for word in input:
        wordDict=Counter(word)

        key = wordDict.keys()

        key  = sorted(key)

        key = ''.join(key)


        if key in dict.keys():
            dict[key].append(word)
        else:
            dict[key] = []
            dict[key].append(word)

    for (key, value) in dict.iteritems():
        print(','.join(dict[key]))

if  __name__ == "__main__":

    input=['may', 'student', 'students', 'dog', 'studentssess', 'god', 'cat', 'act','tab', 'bat', 'flow', 'wolf', 'lambs', 'amy', 'yam', 'balms', 'looped', 'poodle']
    groupStrings(input)


        
