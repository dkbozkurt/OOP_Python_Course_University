# -*- coding: utf-8 -*-
"""
Created on Mon May 17 16:25:51 2021

@author: Doğukan Bozkurt
"""
import vehicles

def main():
    
    car = vehicles.Car('BMW',2001, 70000, 15000.0,4)
    truck = vehicles.Truck('Toyota', 2002, 40000,12000.0,'4WD')
    suv= vehicles.SUV('Volvo', 2000, 30000, 18500.0, 5)
    
    print('USED CAR INVENTORY')
    print("==================")
    
    print("The following car is in inventory:")
    print("Make:", car.get_make())
    print("Model:", car.get_model())
    print("Mileage:", car.get_mileage())
    print("Price:", car.get_price())
    print("Number of doors:",car.get_doors())
    print()
    
    print("The following truck is in inventory:")
    print("Make:", truck.get_make())
    print("Model:", truck.get_model())
    print("Mileage:", truck.get_mileage())
    print("Price:", truck.get_price())
    print("Drive type:",truck.get_drive_type())
    print()
    
    print("The following SUV is in inventory:")
    print("Make:", suv.get_make())
    print("Model:", suv.get_model())
    print("Mileage:", suv.get_mileage())
    print("Price:", suv.get_price())
    print("Passenger Capacity:",suv.get_pass_cap())
    print()

        
    
main()