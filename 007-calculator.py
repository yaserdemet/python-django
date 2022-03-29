
## Solution with def : 
def calculator(x, y, opr) :
    """DOCTYPE : 
    This function generates a math result 
    according to given parameters and opr.

    Args:
        x (_int_): 
        y (_int_): 
        opr (_str_): 
    """
    
    if opr == "+" :
        return(x + y)
        
    elif opr == "-" :
        return(x - y)
        
    elif opr == "*" :
        return(x * y)
        


    elif opr == "/" :
        return(x / y)
        
    else :
        return("Enter a valid operator.")

calculator(5,4,"+") print(help(calculator))

