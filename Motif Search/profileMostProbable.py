"""
BA2c: Given string, k, and profile matrix, find kmer most likely to have been
generated by profile among all kmers in string.

Input: string\nk\nprofile matrix
Output: most probable kmer
"""

import os
input = open(os.path.abspath('../input/rosalind_ba2c.txt'))
vals = input.readlines()
text,k = vals[0:2]
matrix = vals[2:]

profile = {}
profile['A'] = [float(item) for item in matrix[0].split()]
profile['C'] = [float(item) for item in matrix[1].split()]
profile['G'] = [float(item) for item in matrix[2].split()]
profile['T'] = [float(item) for item in matrix[3].split()]

bestP = 0
mostProbable = ""
for i in range(len(text.strip()) - int(k.strip()) +1):
    window = text.strip()[i:i+int(k.strip())]
    currentP = 1
    for pos,base in enumerate(window):
        currentP *= profile[base][pos]
    if currentP > bestP:
        bestP = currentP
        mostProbable = window
        
print mostProbable