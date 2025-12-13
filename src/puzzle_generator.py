import random
def generate_puzzle(level): #this function works as a brain of the project which generates puzzles based on the level of the user.
    if level == 1:
        # Level 1: Add/Sub (1-10)
        n1 = random.randint(1, 10)
        n2 = random.randint(1, 10)
        op = random.choice(['+', '-'])
        
    elif level == 2:
        # Level 2: Add/Sub/Mul (1-50)
        n1 = random.randint(1, 50)
        n2 = random.randint(1, 50)
        op = random.choice(['+', '-', '*'])
        
    else:
        # Level 3: Mixed Ops
        n1 = random.randint(50, 100)
        n2 = random.randint(2, 10) # Smaller second number for division
        op = random.choice(['+', '-', '*', '/'])

    # This method ensures that there is no negative numbers 
    if (op == '-' or op == '/') and n1 < n2:
        n1, n2 = n2, n1

    # Ensure division results in whole numbers
    if op == '/':
        # Adjusting n1 so it is perfectly divisible by n2
        n1 = n1 - (n1 % n2) 
        # To Avoid division by zero or 1
        if n2 <= 1: n2 = 2
        # Re-calculate n1 to ensure it's still a multiple
        n1 = n2 * random.randint(2, 10) 

    return n1, n2, op