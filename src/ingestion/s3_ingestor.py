# S3 Ingestion Helper Functions
# test 
class Person:
    def __init__(self, name:str, age:int, super:float, income:float):
        # Validate age and super inputs
        if age < 0:
            raise ValueError("Age cannot be negative.")
        if super is None:
            raise ValueError("Super cannot be None.")
        
        # Initialize attributes
        self.age = age
        self.super = super
        self.name = name
        self.income = income
        
    
    # Method to calculate super after 5 years assuming a 11% contribution rate
    # and that income is provided
    def super_after_5_years(self):
        if self.income is None:
            raise ValueError("Income cannot be None.")
        else:
            return self.super + (self.income* 0.11 * 5)
        

    