'''A simple function for calculating the amount at the end of the deposit'''

def bank(x, y):
    '''
    The user makes a deposit in the amount of x rubles for a period of y years at 10% per annum.
    
    Args:
    x: Initial amount
    y: Number of years
    
    Returns:
    Total amount at the end of the deposit
    '''

    total = x
    for _ in range(y):
        total += total*0.1
    return total

print(bank(100, 10))
