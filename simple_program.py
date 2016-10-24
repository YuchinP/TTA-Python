'''epic_programmer_dict = {
    'Tim Berners-Lee' : 'tbl@gmail.com',
    'Guido Van Rossum' : 'gvr@gmail.com',
    'Linus Torvalds' : 'lt@gmail.com',
    'Larry Page' : 'lp@gmail.com',
    'Sergey Brin' : 'sb@gmail.com',
    }
print (epic_programmer_dict)'''

epic_programmer_dict = {
    'tim berners-lee' : ['tbl@gmail.com', 111],
    'guido van rossum' : ['gvr@gmail.com', 222],
    'linus torvalds' : ['lt@gmail.com', 333],
    'larry page' : ['lp@gmail.com', 444],
    'sergey brin' : ['sb@gmail.com', 555]
    }
print (epic_programmer_dict)

#print (epic_programmer_dict['Tim Berners-Lee'],['tbl@gmail.com',111])

#print (epic_programmer_dict['Tim Berners-Lee'],['tbl@gmail.com',111][1])

programmer = epic_programmer_dict['tim berners-lee']
print (programmer)

personsName = input('Please enter a name: ').lower()
print (personsName)

#personsInfo = epic_programmer_dict[personsName]
#print (personsInfo)

try:
    personsInfo = epic_programmer_dict[personsName]
    print ('Name: ' + personsName.title())
    print ('Email: ' + personsInfo[0])
    print ('Number: ' + str(personsInfo[1]))
except:
    print ('No Information found for that name')
