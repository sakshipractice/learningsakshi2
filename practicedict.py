D = {'name':'Drew', 'age': 32}
print(D)
print(D['age'])              #acessing the elements
print(D['name'])              #acessing the elements
D2 = {'prof' : D}
print(D2)
print(D2['prof']['age'])
D['height'] = 69                    #adding a element 
print(D)
D['job'] = 'teacher'                 #changing the element
print(D)
del D['job']                  #delete
print(D)
print(D.keys())                #print the keys
print(D.values())              #print the values
print(D.items())               #print items
print(len(D))                  #check the length
D.clear()                      #clear the dictionary
print(D)