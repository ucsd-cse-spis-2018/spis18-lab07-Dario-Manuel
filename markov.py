import random
def train(s):
    wordsList = s.split()
    prob = {}

    for loc, word in enumerate(wordsList):
        if word not in prob and loc < len(wordsList) - 1:
            prob[word] = [wordsList[loc+1]]
        elif loc < len(wordsList) - 1:
            prob[word].append(wordsList[loc+1])
        elif word not in prob:
            prob[word] = [wordsList[0]]
        else:
            prob[word].append(wordsList[0])
    return prob

def generate(model, firstWord, numWords):
    sentence = firstWord
    currWord = firstWord

    for i in range(numWords):
        currWord = random.choice(model[currWord])
        sentence += " " + currWord
    print(sentence)

def generateFile(filename, numWords):
    f = open("data/"+filename, "r")
    text = f.read()
    f.close()

    wordList = train(text)

    generate(wordList, text.split(maxsplit=1)[0], numWords)
    return

testString = "Yeah baby I like it like that You gotta believe me when I tell you I said I like it like that"

modelDictionary = train(testString)

generate(modelDictionary, "Yeah", 90)
print("\n")
generateFile("frozen.txt", 300)
print("\n")
generateFile("hannah_montana.txt", 300)
print("\n")
generateFile("trump_tweet.txt", 300)
print("\n")
generateFile("tangled.txt", 300)
print("\n")
generateFile("bruno_mars.txt", 300)
