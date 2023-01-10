class Fraction:
    def __init__(self,s,m):
        if m==0:
            print("Error!" ) 
        self.soorat=s
        self.makhraj=m

    def show(self):
       print(self.soorat,"/",self.makhraj)

    def sum(self,f1):
        result=Fraction(None,None)
        result.soorat=self.soorat*f1.makhraj+self.makhraj*f1.soorat
        result.makhraj=self.makhraj*f1.makhraj
        return result

    def subtraction(self,f1):
        result=Fraction(None,None)
        result.soorat=self.soorat*f1.makhraj-self.makhraj*f1.soorat
        result.makhraj=self.makhraj*f1.makhraj
        return result

    def division(self,f1):
        result=Fraction(None,None)
        result.soorat=self.soorat*f1.makhraj 
        result.makhraj=self.makhraj*f1.soorat   
        return result


faraction1=Fraction(2,9)
print("first Fraction: " ) 
faraction1.show()
faraction2=Fraction(3,3)
print("second Fraction: " ) 
faraction2.show()
m=faraction1.sum(faraction2)
print("sum of 2 fractions: " ) 
m.show()
tafrigh=faraction1.subtraction(faraction2)
print("Subtraction of 2 fractions: " ) 
tafrigh.show()
d=faraction1.division(faraction2)
print("Division of 2 fractions: " ) 
d.show()