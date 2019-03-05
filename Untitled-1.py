#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'ads1-notebooks'))
	print(os.getcwd())
except:
	pass

#%%
# define a new sequence
seq = 'ACGT'


#%%
# define a new sequence
seq = "ACGT"


#%%
# Get a character from a string
seq[1]


#%%
# get the length of a sequence
len(seq)


#%%
# empty string (epsilon)
e = ''


#%%
len(e)


#%%
# concatenation
seq1 = 'AACC'
seq2 = 'GGTT'
print(seq1 + seq2)


#%%
seqs = ['A', 'C', 'G', 'T']
print(''.join(seqs))


#%%
# generate a random nucleotide
import random
random.choice('ACGT')


#%%
# generate a random sequence
seq = ''
for _ in range(10):
    seq += random.choice('ACGT')
print(seq)


#%%
# another way to generate a random sequence
seq = ''.join([random.choice('ACGT') for _ in range(10)])
print(seq)


#%%
# get a substring
seq[1:3]


#%%
# get a prefix
seq[:3]


#%%
# get a suffix
seq[7:]


#%%
# another way to get a suffix
seq[-3:]


