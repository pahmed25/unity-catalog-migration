# S3 Ingestion Helper Functions
# test 
class Person:
    def __init__(self, name, age, super, income=None):
        self.name = name
        self.age = age
        self.super = super
        self.income = income
    
    # Method to calculate super after 5 years assuming a 11% contribution rate
    # and that income is provided
    def super_after_5_years(self):
        if self.income is not None:
            return self.super + (self.income* 0.11 * 5)
        else:
            raise ValueError("Income must be provided to calculate super after 5 years.")


    