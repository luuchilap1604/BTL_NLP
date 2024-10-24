import nltk
from nltk import CFG
import sys

class task2_3:
    def __init__(self):
        #print(f"Task 2.3: {sys.path}")
        # Step 1: Read the grammar rules from output/grammar.txt
        with open('output/grammar_rules.txt', 'r') as grammar_file:
            grammar_rules = grammar_file.read()

        # Step 2: Read the sentences from input/sentences.txt
        with open('input/sentences.txt', 'r') as sentences_file:
            sentences = sentences_file.readlines()

        # Step 3: Parse the sentences using the grammar rules
        grammar = CFG.fromstring(grammar_rules)
        parser = nltk.ChartParser(grammar)

        parse_results = []
        for sentence in sentences:
            sentence = sentence.strip()
            if sentence:
                words = sentence.split()
                try:
                    parse_trees = list(parser.parse(words))
                    for tree in parse_trees:
                        parse_results.append(tree)
                except ValueError as e:
                    parse_results.append(f"Error parsing sentence: {sentence}\n{e}")

        # Step 4: Write the parse results to output/parse-result.txt
        with open('output/parse-result.txt', 'w') as output_file:
            for result in parse_results:
                output_file.write(' '.join(str(result).split()) + '\n')