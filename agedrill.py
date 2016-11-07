print ("Let's see how long you have lived in days, minutes and seconds.")
name = input("name: ")
age = int(input("age: "))
days = age * 365
minutes = (age * 525948) - (days * 24 * 60)
seconds = (age * 31556926) - (days * 86400)
print(name, "has been alive for", days, "days", minutes, "minutes and", seconds, "seconds!")
