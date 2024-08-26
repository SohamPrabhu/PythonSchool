'''
Honor Code Statement
Name: Soham Prabhu
Assignment: PA 6
Due Date: Deadline Date here
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by professor and class syllabus.

Comments and Assumptions: A note to the grader as to any problems or
uncompleted aspects of the assignment, as well as any assumptions.
You can write in N/A if you don’t have any comments/assumptions.

NOTE:   width of source code should be <=80 characters to be readable on-screen.
12345678901234567890123456789012345678901234567890123456789012345678901234567890
'''


def save_bookings(book_name, file_name): # opens the file and then takes all the strings. It then adds in all the lines of the string into one file and retrus the sum of all the characters
    
    with open(file_name, 'w') as file:
        for items in book_name:

            line = ':'.join(map(str, items)) + ':\n'

            file.write(line)


    file_characters = sum(len(line) for line in book_name) 
    return file_characters
    

# Example usage:
        
    #print(book_information)
    


#save_bookings([['CSHawks', 7, 30, 'AM', 8, 30, 'AM', 1, 5, 6]])

def load_lines(file_name): # finds all the lines of the file and then puts it all into a string. If the file is not fine then the error file could not be found is returned
    try:
        file_name = open(file_name, 'r')
        file_lines = file_name.readlines()
        file_name.close
        return file_lines

    except:
        return f'The file {file_name} could not be found'
#print(load_lines('bookings_file1.txt'))
def split_lines(booking_lines):# Removes all the coons and then puts all of the words intoa  string. If the value is not a string and it will oupout a string that say an int was expected instead
    final_list = []
    for book_index, book_value in enumerate(booking_lines):
        upper = book_value.split(':')

        try:
            upper.remove('\n')
        except:
            value = None
        for upper_index, upper_value in enumerate(upper):
            try:
                upper[upper_index] = int(upper_value)
            except:
                if upper_index == 2:
                    return f'An int was expected instead of {upper_value}'
                continue
        
        final_list.append(upper)
    
    return final_list
#print(split_lines(['CSHawks:7:BOO:AM:8:30:AM:1:5:6:\n']))
def check_schedule(booking_items, num_lanes):# This checks the schedules and if there were any problems then it will raise a valueError
    if booking_items == []:
        return None
    time = [0,15,30,45]
    for book_index, book_value in enumerate(booking_items):
        if len(book_value[0]) < 6:
            raise ValueError
        index = 1
        while(index < len(book_value)-2):
            if book_value[index] not in range(0,13):
                raise ValueError
            index += 3
        index =2
        while(index < len(book_value)-2):
            if book_value[index] not in time:
                raise ValueError
            index+=3
        index = 3
        while(index < len(book_value)):
            if book_value[index] != 'AM' and book_value[index]!= 'PM':
                raise ValueError
            index +=3
        if book_value[-1] > num_lanes:
            raise ValueError
    return None
        

#check_schedule([['CS 112 Lab', 9, 15, 'AM', 10, 45, 'AM', 2, 3],
 #               ['MECH Class', 11, 0, 'AM', 12, 0, 'PM', 2, 3],
 #               ['STAT Swimmers', 7, 0, 'AM', 4, 45, 'PM', 1]] , 5)           
        
        
        
        





def make_schedule(booking_items, num_lanes):# Will create a schedule based on a couple spefic values.
    final_string = ''
    final_string += 'LANES    '
    for i in range(1,num_lanes+1):
        final_string+= f'{i:^3} '
        #final_string += 'start'
    final_string += '\n'
    hour_time = 7
    min_time = 0
    time_stamp = ' AM '
    while hour_time != 5:
        hour_string = str(hour_time)
        min_string = str(min_time)
        if len(hour_string) ==1:
            hour_string = '0'+hour_string
        if len(min_string) ==1:
            min_string = '0'+min_string
        
        final_string+= hour_string+':'+min_string+time_stamp
        combined_time = hour_time*60+min_time

        if time_stamp == ' PM' and hour_time != 12:
            combined_time+= 60*12
        for i in range(1, num_lanes+1):
            
            value_num = None
            other_string = None
            for booking_index, booking_value in enumerate(booking_items):
                lower_value = booking_value[1]*60+ booking_value[2]
                upper_value = booking_value[4]*60+ booking_value[5]
                if booking_value[3] == 'PM' and booking_value[1] != 12:
                    lower_value += 60*12
                if booking_value[6] == 'PM' and booking_value[4] !=12:
                    upper_value += 60*12
                if lower_value <= combined_time < upper_value and (i == booking_value[-1] or i == booking_value[-2] or i == booking_value[-3]):
                    other_string = booking_value[0][:3]+' '
                else:
                    value_num = 1
            if other_string == None or booking_items == []:
                final_string += '~~~ '
            else:
                final_string+= other_string
        if num_lanes ==0:
            final_string +='\n'
        else:

            final_string +='\n' 
        
        min_time +=15
        if min_time ==60:
            min_time = 0
            hour_time+=1
        if hour_time > 11:
            time_stamp = ' PM '
        if hour_time >12:
            hour_time =1
    
    #file_info = open('info', 'w')
    #file_info.write(final_string)
    #file_info.close()

    return final_string

print(make_schedule([['CS 112 Lab', 9, 15, 'AM', 10, 45, 'AM', 2, 3],
                ['MECH Class', 11, 0, 'AM', 12, 0, 'PM', 2, 3],
                ['STAT Swimmers', 7, 0, 'AM', 4, 45, 'PM', 1]] , 3))