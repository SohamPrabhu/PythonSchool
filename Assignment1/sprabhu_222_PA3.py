'''
Honor Code Statement
Name: Soham Prabhu
Assignment: PA 3
Due Date: 10/9/23
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by professor and class syllabus.

Comments and Assumptions: A note to the grader as to any problems or
uncompleted aspects of the assignment, as well as any assumptions.
You can write in N/A if you don’t have any comments/assumptions.

NOTE:   width of source code should be <=80 characters to be readable on-screen.
12345678901234567890123456789012345678901234567890123456789012345678901234567890
'''
#-------------------------------------------------------
# Task1
#-------------------------------------------------------
import time
def empty_or_full(parking_lane, capacity): 
    # The body of your function goes here
    # Finds out which lane the empty spot is in and then prints out full or empty
    empty_spots = 0
    for i in range(capacity):
        try:
            parking_lane[i]
        except:
            empty_spots+=1
        
    if empty_spots ==0 :
        return 'full'
    elif empty_spots == capacity:
        return 'empty'
    else:
        return 'neither'
    
    
          
            
        
 
    return 

# parks the car in the specific lane that is asked
def park_cars(parking_lane, capacity, cars_to_park):
    for x in cars_to_park:
        parking_lane.append(x)
    return parking_lane[0:capacity]
    
# Goes through all of the cars and finds the one that it has to retrive
def retrieve_cars(parking_lane, cars_to_retrieve):
    for row_index, car_parked in enumerate(parking_lane):
        
        for colume_index, car_retrive in enumerate(cars_to_retrieve):
            
            
            if car_parked == car_retrive :
                
                parking_lane.pop(row_index)

    return parking_lane

#First finds wheather the cars are in the lane and then compares to how many cars are being asked. Then it returns either true or false
def check_cars(parking_lane, cars_to_check):
    # The body of your function goes here
    cars = 0
    lenght_check = len(cars_to_check)
    #print(len(cars_to_check))
    for row_index, cars_checked in enumerate(cars_to_check):

        if cars_checked in parking_lane:

            cars += 1

    if cars >= lenght_check:
        return True
    else:
        return False



#-------------------------------------------------------
# Task 2
#-------------------------------------------------------
#shift value moves the value from the parking lane or to the service lane and then adds o to the move list
# It first finds the index of the  gap after that it changes value with adjacent lane

moves = []
def shift_Value (parking_lane, service_lane):
    gapIndex = -1
    which_lane = 0
    moves.append('O')
    for car_index, license_plate in enumerate(parking_lane):
        if license_plate == '': 
            
            gapIndex =  car_index
            
            which_lane +=1
    for car_index, license_plate in enumerate(service_lane):
        if license_plate == '':
            gapIndex =  car_index
            which_lane += 2
    if which_lane == 1:
        parking_lane[gapIndex] = service_lane[gapIndex]
        service_lane [gapIndex] = ''
        return parking_lane, service_lane
    elif which_lane == 2:

        service_lane[gapIndex] = parking_lane[gapIndex]
        parking_lane [gapIndex] = ''
        return parking_lane, service_lane
# This first finds the buble then changes value with the bottom value and switches it with the bubble at the end it appends the value H to it
def shift_up_value(parking_lane, service_lane):
    gapIndex = -1
    which_lane = 0
    moves.append('H')
    for car_index, license_plate in enumerate(parking_lane):
        if license_plate == '': 
            
            gapIndex =  car_index
            
            which_lane +=1
    for car_index, license_plate in enumerate(service_lane):
        if license_plate == '':
            gapIndex =  car_index
            which_lane += 2
    if which_lane == 1:
        parking_lane[gapIndex] = parking_lane[gapIndex+1]
        parking_lane[gapIndex +1] = ''
        return parking_lane, service_lane
    elif which_lane == 2:

        service_lane[gapIndex] = service_lane[gapIndex+1]
        service_lane[gapIndex +1] = ''
        return parking_lane, service_lane
#find the index of the bubble then lower take the value higher than the bubble and switch it with the bubble vlaue
def lower_value(parking_lane, service_lane):
    
    gapIndex = -1
    which_lane = 0
    moves.append('L')
    for car_index, license_plate in enumerate(parking_lane):
        if license_plate == '': 
            
            gapIndex =  car_index
            
            which_lane +=1
    for car_index, license_plate in enumerate(service_lane):
        if license_plate == '':
            gapIndex =  car_index
            which_lane += 2
    if which_lane == 1:
        parking_lane[gapIndex] = parking_lane[gapIndex-1]
        parking_lane[gapIndex - 1] = ''
        return parking_lane, service_lane
    elif which_lane == 2:

        service_lane[gapIndex] = service_lane[gapIndex-1]
        service_lane[gapIndex - 1] = ''
        return parking_lane, service_lane
#Finds out which lane a specfic car is in and then return either a 1 or 0 to represent which lane
def which_lane(parking_lane, service_lane, car):
    gapIndex = -1
    which_lane = 0
    for car_index, license_plate in enumerate(parking_lane):
        if license_plate == car: 
            
            gapIndex =  car_index
            
            return 1
    for car_index, license_plate in enumerate(service_lane):
        if license_plate == car:
            gapIndex =  car_index
            return 2
def car_index (parking_lane, service_lane, car):
    if which_lane(parking_lane, service_lane, car) == 1:
        for car_index, car_plat in enumerate(parking_lane):
            if car_plat == car:
                return car_index
    elif which_lane(parking_lane, service_lane,car) ==2:
        for car_index, car_plat in enumerate(service_lane):
            if car_plat == car:
                return car_index

# Gets car to the front
def swap_to_front(parking_lane, service_lane, car):
    while(car_index(parking_lane, service_lane, car) != 0):# Keeps on running until car index is equal to 0
        
        if which_lane(parking_lane, service_lane, car) == which_lane(parking_lane, service_lane, '') and car_index(parking_lane, service_lane,'')> car_index(parking_lane, service_lane, car):# switches the bubble to be the opposite of the car
            parking_lane, service_lane = shift_Value(parking_lane, service_lane)
        
        while(car_index(parking_lane, service_lane,'')!=(car_index(parking_lane, service_lane,car)-1)): # while moves keeps going until the index of the bubble is one above the car index
            
            if(car_index(parking_lane, service_lane,'')>(car_index(parking_lane, service_lane,car)-1)):
        
                
                parking_lane, service_lane =lower_value(parking_lane, service_lane)
             
            
            elif(car_index(parking_lane, service_lane,'')<(car_index(parking_lane, service_lane,car)-1)):
    
                parking_lane, service_lane =shift_up_value(parking_lane, service_lane)
        if(car_index(parking_lane, service_lane,'')==(car_index(parking_lane, service_lane,car)-1)):# Once it has left the if statment the value will move 
            
            parking_lane, service_lane = shift_Value(parking_lane, service_lane)
            parking_lane, service_lane = shift_up_value(parking_lane, service_lane)
    # if not moves:
    #     moves.append('') 

    return moves # returns all of the moves
'''def apply_trace(lane_A, lane_B, trace, car):
    
    Assumptions:
    * Parameters lane_A, laneB, trace, are lists of strings
    * lane_A and lane_B have the same length and are full except for the bubble
    * trace contains only move codes ('O', 'L', 'H').
    * The moves are legitimate, that is, we would not require
    * Parameter car is a string contained in either list_A or list_B
    the bubble to go to negative indices or over the length of a list
    Guarantees:
    * Makes the bubble move according to the move codes in the list trace
    * Returns the final index of parameter car after the bubble moves 

    # locate the bubble
    bubble = ''
    if bubble in lane_A:
        bubble_index = lane_A.index(bubble)
        bubble_lane = 0
    if bubble in lane_B:
        bubble_index = lane_B.index(bubble)
        bubble_lane = 1

    # execute the moves that are encoded in trace
    for i in range(len(trace)):
        if trace[i] == 'O':
            # move the bubble
            bubble_lane = 1 - bubble_lane
            # move a car into the freed slot where the bubble used to be
            if bubble_lane == 0: # after bubble switches lanes
                lane_B[bubble_index] = lane_A[bubble_index]
            else: # bubble_lane == 1 after bubble switches lanes
                lane_A[bubble_index] = lane_B[bubble_index]
        elif trace[i] == 'L':
            # move the bubble
            bubble_index -= 1
            # move a car into the freed slot where the bubble used to be
            if bubble_lane == 0:
                lane_A[bubble_index + 1] = lane_A[bubble_index]
            else: # bubble_lane == 1
                lane_B[bubble_index + 1] = lane_B[bubble_index]
        else: #trace[i] == 'H'
            # move the bubble
            bubble_index += 1
            # move a car into the freed slot where the bubble used to be
            if bubble_lane == 0:
                lane_A[bubble_index - 1] = lane_A[bubble_index]
            else: # bubble_lane == 1
                lane_B[bubble_index - 1] = lane_B[bubble_index]

    # locate the car and return its index
    if car in lane_A:
        car_index = lane_A.index(car)
    if car in lane_B:
        car_index = lane_B.index(car)

    return car_index'''

#print(swap_to_front(['ABC-1234'], [''], 'ABC-1234'))
#print(swap_to_front(['ABC-1234', 'XYZ-5678', 'KLM-9012'], ['RST-2468', 'JKL-4680', ''], 'ABC-1234'))
#print(apply_trace(['ABC-1234', 'XYZ-5678', 'KLM-9012'],['', 'RST-2468', 'JKL-4680'], swap_to_front(['ABC-1234', 'XYZ-5678', 'KLM-9012'], ['', 'RST-2468', 'JKL-4680'], 'KLM-9012'),'KLM-9012'))
#print(swap_to_front(['ABC-1234', 'XYZ-5678', ''], ['RST-2468', 'JKL-4680', 'KLM-9012'], 'KLM-9012'))
