#Program to understand sets concept
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(type(it_companies))
print('Length of IT companies is',len(it_companies))                    #length of IT companies
print(it_companies)

it_companies.add('Twitter')                                              #adding twitter to IT companies
print('\nIT companies set after adding Twitter', it_companies )

it_companies.update(['Accenture','Wipro'])                               #adding 2 companies at a time
print('\nIT companies set after adding 2 companies', it_companies)

it_companies.remove('IBM')
print('\nIT companies set after removing IBM ', it_companies)            # the remove() method will raise an error if the specified item does not exist, and the discard() method will not
print('\nJoining A and B:\t', A.union(B))                                #using union as update will modify A

print('\nIntersection of A and B',A.intersection(B))                     #A intersection B

print('\nIs A subset of B:',A.issubset(B))                               #subset

print('\nAre A and B disjoint sets:', A.isdisjoint(B))                   #Two sets are said to be disjoint when their intersection is null.

print('\nA union B and B union A respectively:')
print(A.union(B) ,B.union(A))
print('\nSymmetric difference of A and B is', A.symmetric_difference(B))  #symmetricdifference between A and B
del A                                                                     #deleted set A
del B                                                                     #deleted set B
ageset = set(age)                                                         #converting list to set
print('\nAge list is :',age)
print('Age set is:',ageset)
print('length of age list is', len(age),'while age set is ', len(ageset)) #Comparing length of list and set



