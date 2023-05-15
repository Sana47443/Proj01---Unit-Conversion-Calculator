################################################################################################################
#  Computer Project #1
#
#  Algorithm
#    prompts user for a floating-point value denoting a distance in rods(a unit of measurement of rods)
#    print the inputted distance value(rod) that the person had entered
#    do corresponding conversions for meters,feet, miles,furlongs and the time(in minutes) to walk that distance
#    print the computed conversions which is rounded upto 3 decimal places
################################################################################################################


rods_float= float(input("Input rods: "))  #user input in floating-point value for rods
print("\nYou input",rods_float,"rods.")

one_rod_in_m= 5.0292  #Symbolic constant("m" stands for meters)

one_foot_in_m= 0.3048 #Symbolic constant

one_mile_in_m= 1609.34 #Symbolic constant

one_furlong_in_rods= 40  #Symbolic constant

avg_walkspeed=3.1  #Symbolic constant(the avg_walkspeed is in miles/hour)


meter_float = (rods_float)*(one_rod_in_m  #Conversion of rods to meters 

feet_float = (rods_float)*(one_rod_in_m/one_foot_in_m)  #Conversion of rods to feet

mile_float = (rods_float)*(one_rod_in_m/one_mile_in_m)  #Conversion of rods to miles

furlong_float= (rods_float)/one_furlong_in_rods    #Conversion of rods to furlongs

time_taken_min = ((rods_float*(one_rod_in_m/one_mile_in_m))/avg_walkspeed)*60 #Calculating time taken to cover the inputed distance in minutes
#The above time was first calculated by converting rods to miles then calculating time by time=distance/speed formula and then converting the computed hours to minutes

print() #Printing an empty line
print("Conversions")    #Printing the above computed conversions (which are then rounded upto 3 decimal places(below))
print("Meters:",round(meter_float,3))
print("Feet:",round(feet_float,3))
print("Miles:",round(mile_float,3))
print("Furlongs:",round(furlong_float,3))
print("Minutes to walk",rods_float,"rods:",round(time_taken_min,3))


