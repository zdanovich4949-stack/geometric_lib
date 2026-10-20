import math


def area(r):

    '''
    Returns the area of a circle for a given radius.

        Parameters:
            r (float): Radius of a circle.

        Return value:
            math.pi * r * r (float): Area of a circle.
        
        Example:
            area(228): 163 229,76
    '''

    return math.pi * r * r


def perimeter(r):

    '''
    Returns the circumference for a given radius.

        Parameters:
            r (float): Radius of a circle.
        
        Return value:
            2 * math.pi * r (float): circumference.

        Example:
            perimeter(322): 2 022,16
    '''

    return 2 * math.pi * r