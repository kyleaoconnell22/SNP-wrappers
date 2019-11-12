import os
import sys
import subprocess as sp
import shutil
from Bio import SeqIO
import argparse
import numpy
import numpy as np
'''
############################################
Written for Python 2.7
############################################

Kyle O'Connell
kyleaoconnell22@gmail.com
Oct 2019

This script is not very fancy, it assumes you ran admixture 5x and will summarize k2-4. It would require more hard coding to do more than that.

'''

#prefix of the admixture output files, up to the k value
#full file for example is 'n77-m55-r96_u_maf.1.P.rep1'
prefix = 'maf_filt'

#max reps you want to summarize

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", "--max_reps", required=True, help="REQUIRED: Upper limit of reps, ex. 5")
    return parser.parse_args()


def sum_admix_k2(kval,maxreps):
	outfile = 'k{0}_average_{1}reps.txt'.format(kval,maxreps)
	fh_out = open(outfile,'a')
#list for summarizing runs
	kvalr1 = []
	kvalr2 = []
	kvalr3 = []
	kvalr4 = []
	kvalr5 = []

	#edit this, I want for this dataset k2-k4
	for i in range(1,int(maxreps)+1):
		fh = open(prefix+'.{0}.Q.rep{1}'.format(kval,i),'r')
		for line in fh:
			line=line.strip()
			if i == 1:
				kvalr1.append(line)
			elif i == 2:
				kvalr2.append(line)
			elif i == 3:
				kvalr3.append(line)
			elif i == 4:
				kvalr4.append(line)
			else:
				kvalr5.append(line)
				
	for a,b,c,d,e in zip(kvalr1,kvalr2,kvalr3,kvalr4,kvalr5):
		col0 = np.array([float(a.split(' ')[0]),float(b.split(' ')[0]),float(c.split(' ')[0]),float(d.split(' ')[0]),float(e.split(' ')[0])])
		col1 = np.array([float(a.split(' ')[1]),float(b.split(' ')[1]),float(c.split(' ')[1]),float(d.split(' ')[1]),float(e.split(' ')[1])])
		
		mean0 = np.mean(col0)
		mean1 = np.mean(col1)
		mean0 = str(round(mean0, 2))
		mean1 = str(round(mean1, 2))
		fh_out.write(mean0 + '\t' + mean1 + '\n')		

#k=3
def sum_admix_k3(kval,maxreps):
	outfile = 'k{0}_average_{1}reps.txt'.format(kval,maxreps)
	fh_out = open(outfile,'a')
#list for summarizing runs
	kvalr1 = []
	kvalr2 = []
	kvalr3 = []
	kvalr4 = []
	kvalr5 = []

	#edit this, I want for this dataset k2-k4
	for i in range(1,int(maxreps)+1):
		fh = open(prefix+'.{0}.Q.rep{1}'.format(kval,i),'r')
		for line in fh:
			line=line.strip()
			if i == 1:
				kvalr1.append(line)
			elif i == 2:
				kvalr2.append(line)
			elif i == 3:
				kvalr3.append(line)
			elif i == 4:
				kvalr4.append(line)
			else:
				kvalr5.append(line)
				
	for a,b,c,d,e in zip(kvalr1,kvalr2,kvalr3,kvalr4,kvalr5):
		col0 = np.array([float(a.split(' ')[0]),float(b.split(' ')[0]),float(c.split(' ')[0]),float(d.split(' ')[0]),float(e.split(' ')[0])])
		col1 = np.array([float(a.split(' ')[1]),float(b.split(' ')[1]),float(c.split(' ')[1]),float(d.split(' ')[1]),float(e.split(' ')[1])])
		col2 = np.array([float(a.split(' ')[2]),float(b.split(' ')[2]),float(c.split(' ')[2]),float(d.split(' ')[2]),float(e.split(' ')[2])])

		mean0 = np.mean(col0)
		mean1 = np.mean(col1)
		mean2 = np.mean(col2)
		mean0 = str(round(mean0, 2))
		mean1 = str(round(mean1, 2))
		mean2 = str(round(mean2, 2))
		fh_out.write(mean0 + '\t' + mean1 + '\t' + mean2 + '\n')	

#k=4		
def sum_admix_k4(kval,maxreps):
	outfile = 'k{0}_average_{1}reps.txt'.format(kval,maxreps)
	fh_out = open(outfile,'a')
#list for summarizing runs
	kvalr1 = []
	kvalr2 = []
	kvalr3 = []
	kvalr4 = []
	kvalr5 = []

	#edit this, I want for this dataset k2-k4
	for i in range(1,int(maxreps)+1):
		fh = open(prefix+'.{0}.Q.rep{1}'.format(kval,i),'r')
		for line in fh:
			line=line.strip()
			if i == 1:
				kvalr1.append(line)
			elif i == 2:
				kvalr2.append(line)
			elif i == 3:
				kvalr3.append(line)
			elif i == 4:
				kvalr4.append(line)
			else:
				kvalr5.append(line)
				
	for a,b,c,d,e in zip(kvalr1,kvalr2,kvalr3,kvalr4,kvalr5):
		col0 = np.array([float(a.split(' ')[0]),float(b.split(' ')[0]),float(c.split(' ')[0]),float(d.split(' ')[0]),float(e.split(' ')[0])])
		col1 = np.array([float(a.split(' ')[1]),float(b.split(' ')[1]),float(c.split(' ')[1]),float(d.split(' ')[1]),float(e.split(' ')[1])])
		col2 = np.array([float(a.split(' ')[2]),float(b.split(' ')[2]),float(c.split(' ')[2]),float(d.split(' ')[2]),float(e.split(' ')[2])])
		col3 = np.array([float(a.split(' ')[3]),float(b.split(' ')[3]),float(c.split(' ')[3]),float(d.split(' ')[3]),float(e.split(' ')[3])])

		mean0 = np.mean(col0)
		mean1 = np.mean(col1)
		mean2 = np.mean(col2)
		mean3 = np.mean(col3)
		mean0 = str(round(mean0, 2))
		mean1 = str(round(mean1, 2))
		mean2 = str(round(mean2, 2))
		mean3 = str(round(mean3, 2))
		fh_out.write(mean0 + '\t' + mean1 + '\t' + mean2 + '\t' + mean3 + '\n')			
		
			
def main():
	args = get_args()
	#define the arguments
	sum_admix_k2(2,args.max_reps)
	sum_admix_k3(3,args.max_reps)
	sum_admix_k4(4,args.max_reps)

	
if __name__ == '__main__':
    main()
	


	
		
	