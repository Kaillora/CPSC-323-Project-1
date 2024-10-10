import tokenize
from io import StringIO

#Inputting the name of the file you want to tokenize
file = input("Enter the name of the file you want to open: ")

#Remove the whitespaces and comments in the file and print the new output
def remove_comments(file):
    result = []
    with open(file) as f:
        for line in f:
            line = line.strip()
            if not line.startswith('#'):
                result.append(line)
    return result

#Tokenize the printed output and categorize it in tabular form
def tokenizer(code):
    tokens = code.split()
    total_tokens = 0
    keywords = ['int', 'char', 'float', 'if', 'else', 'for', 'while', 'return', 'void', 'print', 'def']
    operators = ['+', '-', '*', '/', '%', '=']
    separators = ['(', ')', '[', ']', '{', '}', ';', ':', ',']
    keyword = []
    operator = []
    separator = []
    identifier = []
    literal = []
    total_tokens = 0
    
    for token in tokens:
        tokens = tokenize.generate_tokens(StringIO(code).read)
        total_tokens += 1
        if token in keywords:
            keyword.append(token)
        elif token in operators:
            operator.append(token)
        elif token in separators:
            separator.append(token)
        elif (token.startswith("'") and token.endswith("'")) or token.isdigit():
            literal.append(token)
        else:
            identifier.append(token)
            
    print('Keywords: ', list(set(keyword)))
    print('Operators: ', list(set(operator)))
    print('Separators: ', list(set(separator)))
    print('Identifiers: ', list(set(identifier)))
    print('Literals: ', list(set(literal)))
    print('Token Count: ', total_tokens)
    
new_code = remove_comments(file)
for line in new_code:
    print(line)
    
tokenized_code = ' '.join(new_code)
tokenizer(tokenized_code)

             
