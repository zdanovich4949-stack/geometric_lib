def area(a, h):  

    '''
    Returns the area of triangle for a giver parameters.

    Parameters:
        a (float): Lenght of a triangle's side.
        h (float): Lenght of the altitude drawn to a given side.
    
    Return values:
        a * h / 2 (float): Area of triangle.
    
    Example:
        area(4,2): 4
    '''

    return a * h / 2  

 

def perimeter(a, b, c):  

    '''
    Returns the perimeter of triangle for a giver parameters.

    Parameters:
        a (float): Lenght of a first triangle's side.
        b (float): Lenght of a second triangle's side.
        c (float): Lenght of a third triangle's side.
    
    Return values:
        a + b + c (float): Perimeter of triangle.
    
    Example:
        perimeter(5,11,23): 39
    '''
    
    return a + b + c