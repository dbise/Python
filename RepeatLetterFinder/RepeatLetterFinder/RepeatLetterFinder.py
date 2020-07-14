#The start of NonRepeat function
#This function will take a string, find the number of occurences of each char, find the first char that is not repeated, finally take the string and sort it by least number of occurences
def NonRepeat(str):
    strLow = str.lower()
    count = {}

#Count the number of occurences of each char in a dictionary
    for c in strLow:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

#Find the first occurence of a char in the string that is not repeated
    for c in strLow:
        if count[c] == 1:
            print(c)
            break

#Rebuild the string by finding the least number of occurences to the highest number of occurences
    highestOccur = max(count.values())
    newStr = ""
    for i in range(1, highestOccur +1):
        for c in str:
            if count[c.lower()] == i:
                newStr += c
    print(newStr)


#Get input from user and run input through NonRepeat function
print("Enter a string: ")
input = input()
NonRepeat(input)
