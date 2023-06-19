# DNA='TACGGCGTTAGACAAGTGCGTGAGTACACA'

# task1
dnaseq = input("Enter DNA sequence :")

for i in dnaseq:
    if ((i!='A') and (i!='T') and (i!='G') and (i!='C')) :
        print("not a dna sequence")
        break
    else:
        seq=dnaseq.upper()
        GC_percent = (seq.count('C') + seq.count('G')) / len(seq) * 100    
        print("{:.6f}".format(GC_percent))   
        break
    
    
# task2
dnaseq=input("Enter Dna Sequence:")
for i in range(len(dnaseq)):
    if(dnaseq[i]=='G')and(dnaseq[i+1]=='T'):
            print("%s is found at index %d"%(dnaseq[i],i),"%s is found at index %d"%(dnaseq[i+1],(i+1)))    
            

# task3
dnaseq=input("Enter Dna Sequence:")
for i in range(len(dnaseq)):
    if(dnaseq[i]=='A')or(dnaseq[i]=='C')or(dnaseq[i]=='G')or(dnaseq[i]=='T'):
        pass
    else :
        print("not dna seq")
        break
else:  
    print("%s is found %d times in dna seq  "%('A',dnaseq.count('A')))
    print("%s is found %d times in dna seq  "%('C',dnaseq.count('C')))
    print("%s is found %d times in dna seq  "%('G',dnaseq.count('G')))
    print("%s is found %d times in dna seq  "%('T',dnaseq.count('T')))            
    
#task4    
def central_dogma(DNA):
    comp={'A':'T' , 'T':'A' , 'C':'G' , 'G':'C'}
    trans={'A':'A' , 'T':'U' , 'C':'C' , 'G':'G'}
    table = {
            'AUG':'Met', 'CCG':'Pro', 'CAA':'Gin', 'UCU':'Ser',
            'GUU':'Val', 'CAC':'His', 'GCA':'Ala', 'CUC':'Leu',
            'AUG':'Met', 'UGU':'Cys',}

    complementDNA=''
    transcription=''
    protein =''
    for base_comp in DNA:
        complementDNA = complementDNA + comp[base_comp]
    print('Complement is',complementDNA)

    for base_trans in complementDNA:
        transcription = transcription + trans[base_trans]
    print('Transcription is',transcription)

    if len(transcription)%3 == 0:
        for i in range(0, len(transcription), 3):
            codon = transcription[i:i + 3]
            if codon == transcription[ -3 : ]:
                protein+= table[codon]
            else:
                protein+= table[codon]+'-'

            
    print('Translation is', protein)
DNA = input('please Enter your sequence : ')
central_dogma(DNA)
 
       
# task5
from collections import defaultdict 
f = open('C:\\Users\\SOFT\\Desktop\\sondos tasks\\sequence.fasta','r')
list=defaultdict(str)
name = ''
for line in f:
    if line.startswith('>'):
        name = line[1:-1]
        continue 
    list[name]+=line.strip()
print(list)          