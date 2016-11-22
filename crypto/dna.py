__author__ = 'ruiqin'

def decode_dna(string):
    pieces = []
    for i in range(0, len(string), 3):
        piece = string[i:i+3]
        pieces.append(mapping[piece])
    return "".join(pieces)

cipher = raw_input('Input the cipher: ')
mapping = {
        'CGA': 'A',
        'CCA': 'B',
        'GTT': 'C',
        'TTG': 'D',
        'GGC': 'E',
        'GGT': 'F',
        'TTT': 'G',
        'CGC': 'H',
        'ATG': 'I',
        'AGT': 'J',
        'AAG': 'K',
        'TGC': 'L',
        'TCC': 'M',
        'TCT': 'N',
        'GGA': 'O',
        'GTG': 'P',
        'AAC': 'Q',
        'TCA': 'R',
        'ACG': 'S',
        'TTC': 'T',
        'CTG': 'U',
        'CCT': 'V',
        'CCG': 'W',
        'CTA': 'X',
        'AAA': 'Y',
        'CTT': 'Z',
        'ATA': ' ',
        'TCG': ',',
        'GAT': '.',
        'GCT': ':',
        'ACT': '0',
        'ACC': '1',
        'TAG': '2',
        'GCA': '3',
        'GAG': '4',
        'AGA': '5',
        'TTA': '6',
        'ACA': '7',
        'AGG': '8',
        'GCG': '9'
}
print 'The plaintext: ' + decode_dna(cipher)