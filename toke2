import tokenize
from io import StringIO

# Inputting the name of the file to tokenize
file = input("Enter the name of the file you want to open: ")

# Remove the whitespaces and comments in the file and print the new output
def remove_comments(file):
    result = []
    try:
        with open(file) as f:
            for line in f:
                line = line.strip()
                # Ignore lines that start with '#' or are empty
                if not line.startswith('#') and line:
                    result.append(line)
        return result
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
        return []

# Tokenize the printed output and categorize it in tabular form
def tokenizer(code):
    keywords = {'int', 'char', 'float', 'if', 'else', 'for', 'while', 'return', 'void', 'print', 'def'}
    operators = {'+', '-', '*', '/', '%', '='}
    separators = {'(', ')', '[', ']', '{', '}', ';', ':', ','}
    
    keyword = []
    operator = []
    separator = []
    identifier = []
    literal = []
    total_tokens = 0

    try:
        tokens = tokenize.generate_tokens(StringIO(code).readline)
        for toknum, tokval, _, _, _ in tokens:
            total_tokens += 1
            if tokval in keywords:
                keyword.append(tokval)
            elif tokval in operators:
                operator.append(tokval)
            elif tokval in separators:
                separator.append(tokval)
            elif toknum == tokenize.NAME:
                identifier.append(tokval)
            elif toknum == tokenize.NUMBER or toknum == tokenize.STRING:
                literal.append(tokval)
    except tokenize.TokenError:
        print("Tokenization error encountered.")
    
    print('Keywords:', list(set(keyword)))
    print('Operators:', list(set(operator)))
    print('Separators:', list(set(separator)))
    print('Identifiers:', list(set(identifier)))
    print('Literals:', list(set(literal)))
    print('Token Count:', total_tokens)

# Process file and tokenize content
new_code = remove_comments(file)
if new_code:
    print("\nProcessed code without comments and whitespace:")
    for line in new_code:
        print(line)

    tokenized_code = '\n'.join(new_code)
    print("\nTokenization results:")
    tokenizer(tokenized_code)
