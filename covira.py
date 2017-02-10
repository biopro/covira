# -*- coding: utf-8 -*-

import shlex
import sys
import argparse

####FUNCTIONS

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

def process_file (file):

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

    for i,valores in enumerate(new_dataset):

        valores_programas[file][ids[i]] = valores[-1]

    for linha in [peso for peso in enumerate(pesos)]:

	yield linha

####VARIABLES

ids = []
valores_programas = {}

####MAIN

if __name__ == '__main__':

	argumentParser = argparse.ArgumentParser(description=(
	                 'CoVIRA: Consensus by Voting with Iterative '
                         'Re-weighting based on Agreement'))
	argumentParser.add_argument('-i','--input',required=True)
	argumentParser.add_argument('-o','--output')
	arguments = argumentParser.parse_args()
	input = arguments.input

	if arguments.output:

		sys.stdout = open(arguments.output,'w')

	try:

		for peso in process_file(input):

			sys.stdout.write('{0}\t{1}\n'.format(peso[0]+1,peso[1]))

	except:

		sys.stderr.write("""ERROR: Please, check your input file\n""".format(input))

