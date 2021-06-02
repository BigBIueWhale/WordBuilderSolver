#How many words of three or more letters, including plurals, can you make from the five letters, using each letter only once?
#No foreign words or words beginning with a capital are allowed. there's at least one five letter word.

import json
def getLettersInput():
    stringOfLetters = input("Enter The Letters You Were Given. (No Spaces): ")
    listOfLetters = []
    for letter in stringOfLetters:
        listOfLetters.append(letter.lower())
    return listOfLetters
def getWordListFromFile():
    try:
        wordListFile = open("list.json")
        wordList = json.load(wordListFile)
        wordListFile.close()
    except FileNotFoundError:
        print("list.json Not found!\nAborting program.")
        emptyList = {}
        return emptyList
    return wordList
def getWordDicFromFile():
    try:
        wordDicFile = open("dictionary.json")
        wordDic = json.load(wordDicFile)
        wordDicFile.close()
    except FileNotFoundError:
        print("dictionary.json Not found!\nAborting program.")
        emptyDic = {}
        return emptyDic
    return wordDic
lettersList = getLettersInput()
lettersDic = {}
for letter in lettersList:
    value = lettersDic.get(letter)
    if value == None: lettersDic[letter] = 1
    else: lettersDic[letter] += 1
wordDic = getWordDicFromFile()
wordList = getWordListFromFile()
validWords = []
for word in wordList:
    lenWord = len(word)
    toAdd = True
    lettersDicC = lettersDic.copy()
    letterCounter = 0
    for letter in word:
        if (letter == " ") or (letter == "-"): continue
        if letter == "\n": print("error, found new line!")
        letterCounter += 1
        letterLower = letter.lower()
        value = lettersDicC.get(letterLower)
        if (value == None) or (value == 0) or (letterCounter > 5):
            toAdd = False
            break
        lettersDicC[letterLower] -= 1
    if toAdd and (letterCounter >= 3):
        validWords.append(word)
threeLetterWords = []
fourLetterWords = []
fiveLetterWords = []
for word in validWords:
    lenWord = len(word)
    if lenWord == 3: threeLetterWords.append(word)
    elif lenWord == 4: fourLetterWords.append(word)
    elif lenWord == 5: fiveLetterWords.append(word)
print("Three letter words: " + str(threeLetterWords))
print("Four letter words: " + str(fourLetterWords))
print("Five letter words: " + str(fiveLetterWords))
input("\npress enter to exit")
