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
    total_tokens = 0
    keywords = ['int', 'char', 'float', 'if', 'else', 'for', 'while', 'return', 'void', 'print', 'def']
    operators = ['+', '-', '*', '/', '%', '=']
    separators = ['(', ')', '[', ']', '{', '}', ';', ':', ',']
    keyword = []
    operator = []
    separator = []
    identifier = []
    literal = []
    
    tokens = tokenize.generate_tokens(StringIO(code).read)
    for toknum, tokval, _, _, _, in tokens:
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
            
    print('Keywords: ', list(set(keyword)))
    print('Operators: ', list(set(operator)))
    print('Separators: ', list(set(separator)))
    print('Identifiers: ', list(set(identifier)))
    print('Literals: ', list(set(literal)))
    print('Token Count: ', total_tokens)
    
new_code = remove_comments(file)
print('\nCode without comments and whitespaces: ')
for line in new_code:
    print(line)
    
tokenized_code = ' '.join(new_code)
print('\nTokenization and token count: ')
tokenizer(tokenized_code)

             
