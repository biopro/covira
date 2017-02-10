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
		yield linha

def parseWeights(input):
	weightsCsvHandle = open(input)
	weightsCsvParser = csv.reader(weightsCsvHandle, 
                                      delimiter='\t')
	weightsList = []
	for linhaIndex, linha in enumerate(weightsCsvParser):
		if linhaIndex == 0:
			continue
		weightsList.append(linha[1])
	return weightsList

def calculate_vote(linha,weights,threshold):
	pass

def ranking():
	pass

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
	argumentParser.add_argument('-t','--threshold',default=0.5)
	argumentParser.add_argument('-r','--ranking')
	arguments = argumentParser.parse_args()
	input = arguments.input
	weights = arguments.weights	
	#define output file (file or STDOUT)
	
	if arguments.output:

		sys.stdout = open(arguments.output,'w')

	try:
		
	except:
		sys.stderr.write(("ERROR: Please, check your "
                                  "input file\n").format(input))
		sys.exit()


