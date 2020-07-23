
import math

class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        if type(real_part)==str and type(imaginary_part)!=str:
            raise ValueError("Invalid value for real part")
        if type(real_part)!=str and type(imaginary_part)==str:
            raise ValueError("Invalid value for imaginary part")
        if type(real_part)==str and type(imaginary_part)==str:
            raise ValueError("Invalid value for real and imaginary part")
        self.real_part=real_part
        self.imaginary_part=imaginary_part

    def conjugate(self):
        if self.imaginary_part>=0:
            return ComplexNumber(self.real_part, -(self.imaginary_part))
        else:
            return ComplexNumber(self.real_part, abs(self.imaginary_part))
    def __add__(self, other):
        if self.imaginary_part + other.imaginary_part>=0:
            return ComplexNumber(self.real_part + other.real_part,self.imaginary_part + other.imaginary_part)
        else:
            
            return ComplexNumber(self.real_part + other.real_part,self.imaginary_part + other.imaginary_part)
    
    def __sub__(self, other):
        if self.imaginary_part - other.imaginary_part>=0:
            return ComplexNumber(self.real_part - other.real_part,self.imaginary_part - other.imaginary_part)
        else:
            
            return ComplexNumber(self.real_part - other.real_part,self.imaginary_part - other.imaginary_part)
    
    def __abs__(self):
        return round(math.sqrt(self.real_part**2 + self.imaginary_part**2),3)
    
    def __mul__(self, other):
        if self.imaginary_part*other.real_part + self.real_part*other.imaginary_part>=0:
            return ComplexNumber(self.real_part*other.real_part - self.imaginary_part*other.imaginary_part,
                       self.imaginary_part*other.real_part + self.real_part*other.imaginary_part)
        else:
            
            return ComplexNumber(self.real_part*other.real_part - self.imaginary_part*other.imaginary_part,
                       self.imaginary_part*other.real_part + self.real_part*other.imaginary_part)
    def __truediv__(self, other):
        divider= other.real_part**2 + other.imaginary_part**2
        real,imaginary=((self.real_part*other.real_part)+(self.imaginary_part*other.imaginary_part))/divider, ((self.imaginary_part*other.real_part)-(self.real_part*other.imaginary_part))/divider
        
        if (other.real_part**2 + other.imaginary_part**2)<0 and (other.real_part**2 + other.imaginary_part**2)>-1:
            raise ZeroDivisionError("division by zero")
        else:
            if imaginary>=0:
                return ComplexNumber(real,imaginary)
            return ComplexNumber(real,imaginary)
        
    def __eq__(self, other):
        return self.real_part == other.real_part and self.imaginary_part == other.imaginary_part
    def __str__(self):
        if self.imaginary_part>=0:
            return '%g+%gi'%(self.real_part, self.imaginary_part)
        else:
            return '%g%gi' %(self.real_part, self.imaginary_part)
        


