#!/bin/python3
import os, sys


# ------- Class Definition ---------
class MyApp:

    def __init__ (self, first_name, last_name, age):
        self.FirstName = first_name
        self.LastName = last_name
        self.Age = age

    def out(self):
        print(f'{self.FirstName} {self.LastName} {self.Age}')



# -------- End ---------------

if __name__ == "__main__":
    m = MyApp(sys.argv[1], sys.argv[2], sys.argv[3])
    m.out()
