# -*- coding: utf-8 -*-

import shlex
import sys

####CONSTANTS

HELP_SCREEN = '''
--------------------------------------------------------
                      CoVIRA Score
--------------------------------------------------------
CoVIRA: Consensus by Voting with Iterative Re-weighting 
based on Agreement
--------------------------------------------------------
KREMER, F.S; GRASSMANN, A.A; MCBRIDE, A.J.A; PINTO, L.S.
--------------------------------------------------------
USAGE:

$ python covira_score.py input.txt covira_weights.txt


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

