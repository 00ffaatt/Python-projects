# translates a DNA sequence to RNA or protein sequences

transcription = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
start_codons_coding = ['ATG', 'GTG', 'TTG']
start_codons_template = ['TAC', 'CAC', 'AAC']

def dna_rna(seq):
    rna_seq = ''
    
    for complementary_base_number in range(len(seq)-1, -1, -1):
        rna_seq += transcription[seq[complementary_base_number]]
    
    return rna_seq



print (dna_rna('AATTC'))