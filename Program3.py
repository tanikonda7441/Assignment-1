#Program to create a tuple containing names of sisters and brothers

sisters=('Ahalya','Benny','Cutie')                           #sisters tuple
brothers=('Dino','Eshwar','Finn','George')                   #brothers tuple
print(type(sisters))                                         #confirming the created sisters list is a tuple
siblings=sisters+brothers                                    #appending sisters and brothers
print('\nSibling names are ', siblings)                      #printing the sibling names
print('\nTotal number of siblings are',len(siblings))        #number of siblings
modified_siblings=siblings[1:6]                              #modifying the sibling tuple
father_mother=('Henry','Nancy')
family_members=modified_siblings+father_mother               #adding father and mother names to modified siblings
print('\nThe family members are ',family_members)