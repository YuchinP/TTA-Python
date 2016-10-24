#create a list of epic programmers
epic_programmer_list = ["Tim Berners-Lee",
                        "Guido van Rossum",
                        "Linus Torvalds",
                        "Larry Page",
                        "Sergey Brin",]
print ("An Epic Programmers: " + epic_programmer_list[0])
print ("An Epic Programmers: " + epic_programmer_list[1])
print ("An Epic Programmers: " + epic_programmer_list[2])
print ("An Epic Programmers: " + epic_programmer_list[3])
print ("An Epic Programmers: " + epic_programmer_list[4])

#epic_programmer_list[4] = "Me"
#print (epic_programmer_list)

epic_programmer_list.append ("Me")
print (epic_programmer_list)
print ("An Epic Programmers: " + epic_programmer_list[5])

#looping
for programmer in epic_programmer_list:
    #print (programmer)
    print ("An Epic Programmer: " + programmer)

#list of numbers

number_list = [1,2,3,4,5]
for x in number_list:
    print (x**2)
empty_number_list = []
for x in number_list:
    empty_number_list.append(x**2)
print (empty_number_list)
