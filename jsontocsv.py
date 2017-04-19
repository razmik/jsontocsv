import sys
import csv
import json

print('Initializing jsontocsv...')

#read input command
inputfile = None
outputfile = None

for index, item in enumerate(sys.argv):
	if(sys.argv[index] == '-i'):
		inputfile = sys.argv[index+1]
	elif(sys.argv[index] == '-o'):
		outputfile = sys.argv[index+1]
		
#validate input arguments
if(inputfile is None):
	print('Fail: Input file not found.')
	sys.exit()
if(outputfile is None):
	outputfile = 'output.csv'

print('Reading from '+ inputfile +'...')

with open(inputfile, 'r') as myfile:
    data=myfile.read().replace('\n', '')

x = """[""" + data + """]"""

x = json.loads(x)

print('Writing to '+ outputfile +'...')

f = csv.writer(open(outputfile, "w+", newline='', encoding="utf-8"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["Age", "Author", "Date", "EmotionKeywords", "AFRAID", "ALIVE", "ANGRY", "CONFUSED", "DEPRESSED", "GOOD", "HAPPY", "HELPLESS", "HURT", "INDIFFERENT", "INTERESTED", "LOVE", "OPEN", "POSITIVE", "SAD", "STRONG", "Gender", "Timeline"])

for x in x:
    f.writerow([x["Age"],
                x["Author"],
                x["Date"],
                x["EmotionInfo"]["EmotionInfo"]["EmotionKeywords"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["AFRAID"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["ALIVE"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["ANGRY"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["CONFUSED"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["DEPRESSED"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["GOOD"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["HAPPY"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["HELPLESS"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["HURT"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["INDIFFERENT"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["INTERESTED"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["LOVE"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["OPEN"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["POSITIVE"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["SAD"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["STRONG"],
                x["Gender"], x["Timeline"]])

print('Successfully created the csv output file.')
