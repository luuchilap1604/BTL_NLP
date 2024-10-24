import os
import nltk
from nltk import CFG
from nltk.parse.generate import generate
import sys

class task2_2:
    def __init__(self):
        #print(f"Task 2.2: {sys.path}")
        # Define the grammar from 2.1
        with open('output/grammar_rules.txt', 'r') as grammar_file:
            grammar_text = grammar_file.read()
            
        grammar = CFG.fromstring(grammar_text)
        # Define the output directory and filename
        output_dir = 'output'
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, 'samples.txt')
        
        # Generate sentences with a limit of 10,000
        max_sentences = 10000
        generated_sentences = []
        output_file = 'output/samples.txt'
        # Use NLTK to generate sentences based on the grammar
        with open(output_file, 'w') as f:
            for i, sentence in enumerate(generate(grammar, n=max_sentences)):
                generated_sentence = ' '.join(sentence)
                f.write(generated_sentence + '\n')
                generated_sentences.append(generated_sentence)
                if i >= max_sentences - 1:
                    break

        print(f"Generated {len(generated_sentences)} sentences and saved them to {output_file}")
