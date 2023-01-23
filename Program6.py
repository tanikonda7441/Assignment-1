#Program to find the unique words in a sentence

sentence='I am a teacher and I love to inspire and teach people'
unique=set(sentence.split(' '))                                   #split() method splits string into list
print('Unique words:',unique)