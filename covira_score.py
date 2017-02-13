# -*- coding: utf-8 -*-

import shlex
import sys
import argparse
import csv

####FUNCTIONS

def parseInput(input):
	inputCsvHandle = open(input)
	inputCsvParser = csv.reader(inputCsvHandle,
                                    delimiter='\t')
	for linha in inputCsvParser:
		yield linha[:1] + [int(field) for field in linha[1:]]

def parseWeights(input):
	weightsCsvHandle = open(input)
	weightsCsvParser = csv.reader(weightsCsvHandle, 
                                      delimiter='\t')
	weightsList = []
	for linha in weightsCsvParser:
		weightsList.append(float(linha[1]))
	return weightsList

def calculate_vote(linha,weights,threshold=0.5):
	if len(linha) != len(weights)+1:
		print linha, weights
		sys.stderr.write("ERROR: Wrong number of fields\n")
		sys.exit()
	entryId = linha.pop(0)
	votingSum = sum(map(lambda x:x[0]*x[1], zip(linha, weights)))
	if votingSum > threshold:
		finalVote = 1
	else:
		finalVote = 0
	linha.insert(0,entryId)
	linha.append(votingSum)
	linha.append(finalVote)
	return linha

		

def process(linhas,weights,threshold=0.5):

	processedLinha = []
	
	for linha in linhas:
		
		processedLinha = calculate_vote(linha,weightsList,
                                                threshold=threshold)

		yield processedLinha

def ranking(linhas):

	for linha in sorted(linhas,key=lambda l:l[-2], reverse=True):
	
		yield linha

def printLine(linha):

	print '\t'.join([str(field) for field in linha])

####VARIABLES

ids = []
valores_programas = {}

####MAIN

if __name__ == '__main__':

	argumentParser = argparse
	argumentParser = argparse.ArgumentParser(description=(
	'CoVIRA Score: Voting and Re-ranking based on CoVIRA'))
	argumentParser.add_argument('-i','--input',required=True)
	argumentParser.add_argument('-w','--weights',required=True)
	argumentParser.add_argument('-o','--output')
	argumentParser.add_argument('-t','--threshold',type=float,default=0.5)
	argumentParser.add_argument('-r','--ranking',action='store_true')
	arguments = argumentParser.parse_args()
	input = arguments.input
	weights = arguments.weights
	threshold = arguments.threshold
	weightsList = parseWeights(weights)
	linhasList = parseInput(input)
		
	#define output file (file or STDOUT)
	
	if arguments.output:

		sys.stdout = open(arguments.output,'w')
		
	if arguments.ranking:
		
		for linha in ranking(process(linhasList,weightsList,
                                             threshold=threshold)):

			printLine(linha)
	else:

		for linha in process(linhasList,weightsList,
                                     threshold=threshold):

			printLine(linha)

		
