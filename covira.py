# -*- coding: utf-8 -*-

import shlex
import sys

####CONSTANTS

HELP_SCREEN = '''
--------------------------------------------------------
                         CoVIRA
--------------------------------------------------------
CoVIRA: Consensus by Voting with Iterative Re-weighting 
based on Agreement
--------------------------------------------------------
KREMER, F.S; GRASSMANN, A.A; MCBRIDE, A.J.A; PINTO, L.S.
--------------------------------------------------------
USAGE:

$ python covira.py input.txt


THE INPUT FILE:

The input file must be a tab-delimited file where the 
first field of each lines must be the id of the object 
that is analyzed and the following fields the results,
in binary format, from the different predictors. Ex:

PROTEIN_1	1	0	1	1
PROTEIN_2	1	1	1	0
PROTEIN_3	0	1	0	1

In this case, there are four different predictions for
each entry (protein). 
'''
min_score = 0.5

####FUNCTIONS

"""
read_file("csv file"):
    parses the CSV file and generate a list of lists. Ex:
    
    output: [
      ['protein_1',1,0],
      ['protein_2',0,0],
      ['protein_3',1,0],
      ['protein_4',1,1]
    ]
"""
def read_file(file):
    global ids
    global valores_programas
    valores_programas[file] = {}
    ids = []
    handle = open(file).read()
    handle = handle.split('\n')
    lines = []
    for line in handle:
        if line != '':
            line = line.split('\t')
            ids.append(line.pop(0))
            line = [int(i) for i in line]
            lines.append(line)
    return lines

def calcular_acuracia(dataset,pesos):
    acuracias = []
    for pesos_i,pesos_v in enumerate(pesos):
        acuracia_dividendo = 0
        acuracia_divisor = 0
        for linha_i, linha_v in enumerate(dataset):
            for valor_i, valor_v in enumerate(linha_v):
                if valor_i != pesos_i:
                    if valor_v == linha_v[pesos_i]:
                        acuracia_dividendo += 1 * pesos[pesos_i]
                    acuracia_divisor += 1 * pesos[pesos_i]
        acuracias.append(acuracia_dividendo/acuracia_divisor)
    return [float(i/sum(acuracias)) for i in acuracias]

"""
read_file("csv file"):
    parses the CSV file and generate a list of lists. Ex:
    
    output: [
      ['protein_1',1,0],
      ['protein_2',0,0],
      ['protein_3',1,0],
      ['protein_4',1,1]
    ]
"""

def process_file (file):
    global min_score
    dados = read_file(file)
    pesos = [float(1)/len(dados[0]) for i in range(len(dados[0]))]
    for i in range(10000):
        novos_pesos = calcular_acuracia(dados,pesos)
        if novos_pesos == pesos:
            break
        else:
            pesos = novos_pesos
    new_dataset = []
    for line in dados:
        score = 0
        scores = []
        for valor_i,valor_v in enumerate(line):
            score += valor_v * pesos[valor_i]
            if valor_v:
                scores.append(pesos[valor_i])
        line.append(score)
        new_dataset.append(line)
    lic_list = []
    for i,valores in enumerate(new_dataset):
        valores_programas[file][ids[i]] = valores[-1]
        if valores[-1] > min_score:
            lic_list.append(ids[i])
    for linha in [peso for peso in enumerate(pesos)]:
	yield linha

####VARIABLES

ids = []
valores_programas = {}

####MAIN

if __name__ == '__main__':
	if len(sys.argv) > 1:
		input = sys.argv[1]
		try:
			print 'PROGRAM\tWEIGHT'
			print '-------\t-------'
			for peso in process_file(input):
				print '{0}\t{1}'.format(peso[0]+1,peso[1])
		except:
			sys.stderr.write("""ERROR: Couldn't process the file "{0}"\n""".format(input))
	else:
		print HELP_SCREEN

