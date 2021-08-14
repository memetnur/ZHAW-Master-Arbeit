import os
import sys
folder = "/Users/memn/Desktop/Master Arbeit/Masterthesis_Memeti_B-Group"
folder2= "/Users/memn/Desktop/Master Arbeit/Masterthesis_Memeti_Rubus"
for filename in os.listdir(folder2):
    infilename = os.path.join(folder2,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.1.fsa_nt', '_1.fasta')
    newname = infilename.replace('.txt', '.fasta')
    output = os.rename(infilename, newname)
