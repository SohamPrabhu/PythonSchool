# Insert your header comment here

def update_inventory(inventory, restock = None):  # Figure out the parameters and add to the function signature
    # Put your function body here
    if restock == None:
        return inventory
    for colume_index, colum_value in enumerate(restock):# Goes through the the inventory and adds any desciprtions to the inventory based on tehr restock value. It will only do this if there is key that is equal to one of the restock vaulues. 
        for inventory_keys in inventory.keys():
            if restock[colume_index][0] == inventory_keys:
                total = restock[colume_index][2][0] + inventory[restock[colume_index][0]][1][0]
                inventory[restock[colume_index][0]][1][0] = total
                if restock[colume_index][2][1] != '':# if it's not blank than it will add a number
                    
                    if len(restock[colume_index][2]) == 1:
                        inventory[restock[colume_index][0]][1].append(restock[colume_index][2][1])
                    else:
                        con_string = inventory[restock[colume_index][0]][1][1]+' '+restock[colume_index][2][1]
                        inventory[restock[colume_index][0]][1][1] = con_string

    for colume_index, colum_value in enumerate(restock):# This adds any value that isn't there 
        if restock[colume_index][0] in inventory:
            
            for index, values in enumerate(restock[colume_index][1]):
                if values != '':
                    inventory[restock[colume_index][0]][0].append(values)
        else:

            inventory[restock[colume_index][0]] = [restock[colume_index][1], restock[colume_index][2]]
    
    for inventory_keys, inventory_value in inventory.items(): #checks if there re two values tht are int in a specific locaiotns. If they are ints then  this for loop will concatinate all of hte numbers into one 
        for spec_index, spec_values in enumerate(inventory_value[0]):
        
            if type(spec_values) == float:
                
                
                if spec_index != len(inventory_value[0])-1:
                    
                    buffer_value = inventory_value[0][-1]
                    inventory_value[0].remove(spec_values)
                    inventory_value[0].append(spec_values)
                    if type(inventory_value[0][-1]) ==float and type(inventory_value[0][-2]) == float:
                        if inventory_value[0][-1] > inventory_value[0][-2]:
                            buffer_value = inventory_value[0][-2]
                            inventory_value[0][-2] = inventory_value[0][-1]
                            inventory_value[0][-1] = buffer_value
                    #inventory_value[0][-1] = spec_values
                    #inventory_value[0][spec_index] = buffer_value
                    
    

    return inventory



def merge_inventory (inventory, new_inventory = None):  # Figure out the parameters and add to the function signature
    # Put your function body here
    final_inventory = {}
    final_newinventory =[]
    if new_inventory != None:# if the enventory is none then this if statment will run which will onnly work if the inventory has a value and the new_inventory is none

        
        for keys_newinv, value_newinv in new_inventory.items():
            lower =[]
            uppper = []
            uppper.append(keys_newinv)
            for spec_key, spec_value in enumerate(value_newinv):
                uppper.append(spec_value)
            

            final_newinventory.append(uppper)
        
        
        for inventory_index, inventory_value in enumerate(inventory):
            final_inventory[inventory[inventory_index][0]] = [inventory[inventory_index][1],inventory[inventory_index][2]]
    
        
        return update_inventory(final_inventory, final_newinventory)
    else:# This will switch inventory into a dictionary and new inventory in a list suo it can be pasedd
        for inventory_index, inventory_value in enumerate(inventory):
            final_inventory[inventory[inventory_index][0]] = [inventory[inventory_index][1],inventory[inventory_index][2]]
        return update_inventory(final_inventory)



def products_info (products, product_detail, new_product_detail = None):  # Figure out the parameters and add to the function signature
    # Put your function body here
    final_product_detail = []
    final_new_product_detal = {}
    if new_product_detail == None:# what should happen if the product detail has no values
        for product_detail_index, product_detail_value in enumerate(product_detail):
            upper = []
            upper.append(products[product_detail_index])
            upper.append
            for spec_index, spec_value in enumerate(product_detail_value):
                upper.append(spec_value)
            final_product_detail.append(upper)
        return merge_inventory(final_product_detail)
    for product_detail_index, product_detail_value in enumerate(product_detail): # this will put proudct  detail into final product detail so that it can be put into another list beause this is alread a tuple so it cannot be changed
        upper = []
        upper.append(products[product_detail_index])
        upper.append
        for spec_index, spec_value in enumerate(product_detail_value):
            upper.append(spec_value)
        final_product_detail.append(upper)
    product_index = 0
    for product_detail_index, product_detail_value in enumerate(new_product_detail):
        
        if product_detail_value != []:
            final_new_product_detal[products[product_detail_index]] = [product_detail_value[0],product_detail_value[1]]
            product_index+=1

        
    

    
    
    return merge_inventory(final_product_detail, final_new_product_detal)





def digits_summation (n):# interates everytime finding a specfic value and adding it
    # Put your function body here
    if n == 0:
        return 0
    elif n != 0:
        return (n %10)+ digits_summation(n//10)
    
    


def vowel_counts (some_str, results={}): # goes thhrought the first letter in a name and then adds it to a dicitonary to see if itsn't in the vowels. It delets that word and then keep siterating thorug the entire word
    # Put your function body here
    vowels ='AEIOUaeiou'
    if len(results) == 0:
        results = {}
    if some_str =='':
        return results
    else:
        
        #print(some_str[:1])
        if some_str[0] in vowels:
            if results.get(some_str[0])!= None:
                results[some_str[:1]] += 1
            else:
                results[some_str[:1]] = 1
        
        return vowel_counts(some_str[1:], results)

 
    
    
#products = ('Apple',)
#products_detail =([['',0.0],[0,'']],)
#new_products_detail = ([['c','j', 'k'], [33,'15F']],)
#print(products_info(products, products_detail, new_products_detail))
