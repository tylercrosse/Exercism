def to_rna(dna_strand):
    to_rna_dict = {
      'G': 'C',
      'C': 'G',
      'T': 'A',
      'A': 'U'
    }
    return ''.join(map(lambda d: to_rna_dict[d], dna_strand))
