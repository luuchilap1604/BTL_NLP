
import os
from .grammar_rules import grammar_rules
import sys
# Define the grammar rules

#sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'grammar_rules'))

class task2_1:
    def __init__(self):
        #print(f"Task 2.1: {sys.path}")
        # Define the output directory and filename
        output = 'output/grammar_rules.txt'

        # Write the grammar to a file
        with open(output, 'w', encoding='utf-8') as f:
            f.write(grammar_rules)

        print(f"Grammar rules saved to {output}")
