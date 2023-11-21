from math import sqrt


class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        '''
        This method checks if the triangle is valid.
        
        Args: 
            No
        Returns:
            bool: True if the triangle is valid, False otherwise
        '''
        return (self.a>0 and self.b>0 and self.c>0)
    
    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.

        Note: typies are 'Teng yonli', 'Teng tomonli', 'Turli tomonli'
        '''
        if self.a==self.b or self.b==self.c or self.a==self.c:
            return "Isosceles triangle"
        elif self.a==self.b and self.b==self.c:
            return "equilateral triangle"
        else:
            return "scalene triangle"
        
    def perimeter(self) -> float:
        '''
        This method finds the perimeter of the triangle.
        Args:
            No
        Returns:
            float: return perimeter of the triangle if the triangle is valid, 0 otherwise
        '''
        return self.a+self.b+self.c

    def area(self) -> float:
        '''
        This method finds the area of the triangle.
        Args:
            NO
        Returns:
            float: return area of the triangle if the triangle is valid, 0 otherwise
        '''
        p=self.perimeter()/2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
