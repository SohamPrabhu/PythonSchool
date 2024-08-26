'''
Honor Code Statement
Name: Soham Prabhu
Assignment: PA 4
Due Date: 10/22/23
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by professor and class syllabus.

Comments and Assumptions: A note to the grader as to any problems or
uncompleted aspects of the assignment, as well as any assumptions.
You can write in N/A if you don’t have any comments/assumptions.

NOTE:   width of source code should be <=80 characters to be readable on-screen.
12345678901234567890123456789012345678901234567890123456789012345678901234567890
'''

# Goes through each name and find outs wheather the values are above the threshold
#It createes a list based on that and then returns the listen
def filter_popular(reacts_2D, names, threshold):
    # The body of your function goes here
    pop_list = []
    for j in range(len(reacts_2D)):
        num_total = 0
        for i in range(len(reacts_2D[j])):
            num_total += reacts_2D[j][i]
        if num_total >= threshold:
            pop_list.append(names[j])
    
    return pop_list

#Adds the name first to a list and then adds the proper number of values after it
def gather_engagement(names, reacts, grouping):
    # The body of your function goes here
    
    list_name =[]
    grouping_colum = 0 
    reacts_index = 0

    while grouping_colum < len(names):
        upper = []
        upper.append(names[grouping_colum])
        count = 0
        while reacts_index < len(reacts):
            if count >= grouping [grouping_colum]:
                break
            upper.append(reacts[reacts_index])
            reacts_index+=1
            count+=1
        grouping_colum +=1
        list_name.append(upper)



    
        
        
    

    return list_name 
print(gather_engagement(["crazy_guy", "solid321", "amicoolyet"], [4, 9, 6, 5, 1, 2, 3, 5, 8, 17, 2, 9], [4, 5, 3]))
    
#delets all of the zeros in the 2d array
def clear_zeros(reacts_2D):
    # The body of your function goes here
    colum_index = 0
    while colum_index < len(reacts_2D):
        row_index =0
        
        while row_index < len(reacts_2D[colum_index]):


            if reacts_2D[colum_index][row_index] == 0:
                reacts_2D[colum_index].remove(reacts_2D[colum_index][row_index])
                row_index -= 1
            row_index+=1
        if len(reacts_2D[colum_index]) == 0:
            reacts_2D.remove(reacts_2D[colum_index])
            colum_index -=1
        colum_index +=1
    return reacts_2D

#combines two dictionaires
#if they have the same key then the values add
#if they don't have the same key then it is added to the final list
def form_reactions_list(react_dict1, react_dict2):
    # The body of your function goes here
    first_list = []
    for react_dict2_key, react_dict2_value in react_dict2.items():
        if react_dict2_key in react_dict1:
           react_dict1[react_dict2_key] = react_dict1[react_dict2_key] + react_dict2_value
        else:
           react_dict1[react_dict2_key] = react_dict2_value
           

    
    final_list = []
    for dict_index, dict_value in react_dict1.items():
        upper = []
        upper.append(dict_index)
        upper.append(dict_value)
        final_list.append(upper)
    return final_list
#puts the list in on dictionary
def form_reactions_dict(reacts_2D):
    # The body of your function goes here
    final_dict = {}
    dict_colum = 0
    total = 0

    for colum_index in range(len(reacts_2D)):
        upper =[]
        upper_dict = {}
        for row_index in range(len(reacts_2D[colum_index])):
           
            upper.append(reacts_2D[colum_index][row_index])
        total += upper[1]
        upper_dict[upper[0]] = upper[1]
        
        #final_dict.update(upper_dict)
        for keys in upper_dict:
            final_dict[keys] = upper_dict[keys]
    
    final_dict['total'] = total
  
    
    return final_dict
#print(form_reactions_dict([['like', 10], ['comment', 10], ['share', 3], ['love', 10], ['wow', 2]]))
