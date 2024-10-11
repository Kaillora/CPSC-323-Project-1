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

#Create arrays for common keywords, operators, and separators that can be detected from the example code.
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
    
    #This tokenizes each keyword, operator, separator, identifier, and literal and puts them into their respective lists.
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
            
    #Print the tokenized code into a table without repeating tokens and print the total token count.
    print('Keywords: ', list(set(keyword)))
    print('Operators: ', list(set(operator)))
    print('Separators: ', list(set(separator)))
    print('Identifiers: ', list(set(identifier)))
    print('Literals: ', list(set(literal)))
    print('Token Count: ', total_tokens)

#Print the new output with comments and whitespaces removed.
new_code = remove_comments(file)
print('\nCode without comments and whitespaces: ')
for line in new_code:
    print(line)

#Print the function of the tokenized code and token count.  
tokenized_code = ' '.join(new_code)
print('\nTokenization and token count: ')
tokenizer(tokenized_code)

             
