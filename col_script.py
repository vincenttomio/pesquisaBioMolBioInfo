#!/usr/bin/python
import json, textwrap
from glob import glob
import os

os.makedirs('output', exist_ok=True)

input_file_list = glob('./*.fas')

for input_file_path in input_file_list:

    especies = []
    especie = {}

    with open(input_file_path) as f:
        for line in f:
            if line.startswith('>'):
                if especie:
                    especies.append(especie)

                especie = {
                    'nome': line.strip(),
                    'gene': ''
                }
            else:
                especie['gene'] += line.strip()

    
    
    output_path = './output/' + input_file_path.split('/')[-1]
    with open(output_path, 'w') as output_file:
        
        for especie in especies:
            output_file.write(especie['nome'] + '\n')

            output_file.write('\n'.join(textwrap.wrap(especie['gene'], 60)))
            output_file.write('\n')



