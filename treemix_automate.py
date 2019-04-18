import os
import sys
import subprocess as sp
import shutil
'''
####
hard code these parts
####

input files need to end in .treemix.gz (there can be multiples)
gzip file.treemix (outputs file.treemix.gz)
'''
#for setting the seed below
from random import randint
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

####
desired_migration_events = 10
root = "CV"
block_size = 500

####

m_list = []

for x in range(desired_migration_events):
	m_list.append(x)

for filetype in os.listdir('.'):
    if filetype.endswith(".treemix.gz"):
        prefix = filetype.split('.')[0]
        for mig in m_list:
        	seed = random_with_N_digits(5)
        	treemix1_call = "treemix -i {0} -noss -seed {1} -root {2} -m {3} -o {4}_m{5}_r1 -k {6}".format(filetype, seed, root, mig, prefix, mig, block_size)
        	proc_treemix1 = sp.call(treemix1_call, shell=True)
        	print "running treemix on {0}, with {1} mig edges, seed = {2} and run 1/3".format(prefix, mig, seed)
        	seed = random_with_N_digits(5)
        	treemix2_call = "treemix -i {0} -noss -seed {1} -root {2} -m {3} -o {4}_m{5}_r2 -k {6}".format(filetype, seed, root, mig, prefix, mig, block_size)
        	proc_treemix2 = sp.call(treemix2_call, shell=True)
        	print "running treemix on {0}, with {1} mig edges, seed = {2} and run 2/3".format(prefix, mig, seed)
        	seed = random_with_N_digits(5)
        	treemix3_call = "treemix -i {0} -noss -seed {1} -root {2} -m {3} -o {4}_m{5}_r3 -k {6}".format(filetype, seed, root, mig, prefix, mig, block_size)
        	proc_treemix3 = sp.call(treemix3_call, shell=True)
        	print "running treemix on {0}, with {1} mig edges, seed = {2} and run 3/3".format(prefix, mig, seed)
