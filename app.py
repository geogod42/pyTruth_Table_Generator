# app.py
from flask import Flask, render_template, request
import itertools
import re

app = Flask(__name__)

# Logical operations
def NOT(x):
    return not x

def AND(x, y):
    return x and y

def OR(x, y):
    return x or y

def XOR(x, y):
    return bool(x) ^ bool(y)

def IMPLIES(x, y):
    return not x or y

def EQUIVALENT(x, y):
    return x == y

# Mapping of symbols to function names
OPERATION_MAP = {
    '¬': 'NOT', 'not': 'NOT', '!': 'NOT', '~': 'NOT',
    '∧': 'AND', 'and': 'AND', '&': 'AND', '*': 'AND',
    '∨': 'OR', 'or': 'OR', '|': 'OR', '+': 'OR', 'v': 'OR',
    '⊕': 'XOR', '^': 'XOR',
    '→': 'IMPLIES', '->': 'IMPLIES', '➡': 'IMPLIES',
    '↔': 'EQUIVALENT', '<->': 'EQUIVALENT'
}

def replace_symbols(expression):
    """Replace operation symbols with their corresponding function names, ensuring correct syntax."""
    # Handle NOT explicitly to wrap the following variable or expression
    expression = re.sub(r'¬\s*([a-zA-Z])', r'NOT(\1)', expression)
    expression = re.sub(r'[!~]([a-zA-Z])', r'NOT(\1)', expression)

    # Add parentheses around binary operations to ensure correct evaluation
    expression = re.sub(r'(\b[a-zA-Z]+\b)\s*(∧|and|&|\*)\s*(\b[a-zA-Z]+\b)', r'AND(\1, \3)', expression)
    expression = re.sub(r'(\b[a-zA-Z]+\b)\s*(∨|or|\||\+|v)\s*(\b[a-zA-Z]+\b)', r'OR(\1, \3)', expression)
    expression = re.sub(r'(\b[a-zA-Z]+\b)\s*(⊕|\^)\s*(\b[a-zA-Z]+\b)', r'XOR(\1, \3)', expression)
    expression = re.sub(r'(\b[a-zA-Z]+\b)\s*(→|->|➡)\s*(\b[a-zA-Z]+\b)', r'IMPLIES(\1, \3)', expression)
    expression = re.sub(r'(\b[a-zA-Z]+\b)\s*(↔|<->)\s*(\b[a-zA-Z]+\b)', r'EQUIVALENT(\1, \3)', expression)

    print(f"Replaced expression: {expression}")  # Debug: show replaced expression
    return expression

def evaluate(expression, env):
    """Safely evaluate the logical expression using the provided environment."""
    try:
        # Replace variable names with their boolean values
        for var, value in env.items():
            expression = re.sub(rf'\b{var}\b', str(value), expression)
        
        return eval(expression, {"__builtins__": None}, {
            "NOT": NOT, "AND": AND, "OR": OR, "XOR": XOR, "IMPLIES": IMPLIES, "EQUIVALENT": EQUIVALENT
        })
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def home():
    result_table = None
    variables = set()
    expression = ''
    
    if request.method == 'POST':
        expression = request.form['expression']
        
        # Replace operation symbols with function names
        parsed_expression = replace_symbols(expression)
        
        # Extract variables using regex
        variables = sorted(set(re.findall(r'\b[a-zA-Z]\b', expression)))  # Fix to detect all variables
        print(f"Extracted variables: {variables}")  # Debug: show extracted variables
        
        num_vars = len(variables)
        
        # Generate all possible truth values for the variables
        truth_values = list(itertools.product([False, True], repeat=num_vars))
        print(f"Truth values: {truth_values}")  # Debug: show truth value combinations
        
        # Evaluate the expression for each combination of truth values
        result_table = []
        for values in truth_values:
            env = {var: value for var, value in zip(variables, values)}
            result = evaluate(parsed_expression, env)
            result_table.append((*values, result))
    
    return render_template('index.html', result_table=result_table, variables=variables, expression=expression)

if __name__ == '__main__':
    app.run(debug=True)

