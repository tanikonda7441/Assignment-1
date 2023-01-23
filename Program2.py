#Program to create empty dictionary and add keys and values to it
dog_dictionary={}                                                                        #empty dog dictionary
print('Empty dictionary',dog_dictionary)
dog_dictionary={'name': 'Rex', 'color':'black', 'breed':'labrador', 'legs':4, 'age':3}   #adding keys and values to dog dictionary
print('Dog Dictionary:', dog_dictionary)


student={                                                                                #creating student dictionary

    'first_name':'Venkata',
    'last_name':'Tanikonda',
    'gender' : 'Male',
    'age':25,
    'marital_status':False,
    'skills':['SAP', 'Java', 'Python', 'Automation','C'],
    'country': 'India',
    'city':'Hyderabad',
    'address':'Overlandpark'

       }
print('\nLength of student dictionary is',len(student))                                 #length of student dictionary
print( '\nSkills of a student are', student['skills'])                                  # other way to print skills   print(student.get('skills'))
                                                                                        #print(type(student))
print('\nType of skills is',type(student['skills']))                                    #printing type of skills as list
student['skills'].append(['CSS','HTML'])                                                #adding two extra skills
print('\nList of student after appending 2 skills',student)
keys=student.keys()                                                                     #printing list of keys
print('\nList of keys in student dictionary is',keys)
values=student.values()
print('\nList of values in student dictionary is',values)                               #printing list of keys


