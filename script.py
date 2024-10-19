from contractions import fix
from collections import Counter
import socket

# Read text files
text1 = open('IF.txt', 'r').read()
text2 = open('AlwaysRememberUsThisWay.txt', 'r').read()
# Create a results text file in the /home/data/output directory
result = open('/home/data/output/result.txt', 'w')

# Count words in each text file
words1 = text1.split()
wordCount1 = len(words1)
result.write("Words in IF.txt: ")
result.write(str(wordCount1))
result.write("\n")

words2 = text2.split()
wordCount2 = len(words2)
result.write("Words in AlwaysRememberUsThisWay.txt: ")
result.write(str(wordCount2))
result.write("\n")

# Combine word counts in both text files
result.write("Total words: ")
result.write(str(wordCount1 + wordCount2))
result.write("\n")

# Split contractions in text files
uncontractedText2 = fix(text2)
newWords2 = uncontractedText2.split()

# Count most frequent words in each document
wordFrequency1 = Counter()
for x in words1:
    wordFrequency1[x] = wordFrequency1[x] + 1
result.write("Three most frequent words in IF.txt: ")
result.write(str(wordFrequency1.most_common(3)))
result.write("\n")

wordFrequency2 = Counter()
for x in newWords2:
    wordFrequency2[x] = wordFrequency2[x] + 1
result.write("Three most frequent words in AlwaysRememberUsThisWay.txt, splitting contractions: ")
result.write(str(wordFrequency2.most_common(3)))
result.write("\n")

# Find the machine's IP address
ipAddress = socket.gethostbyname(socket.gethostname())
result.write("This machine's IP address: ")
result.write(ipAddress)
result.write("\n")