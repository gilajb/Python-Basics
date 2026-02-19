greeting = "Hello"
course = "SOFTWARE ENGINEERING"

#Shorten -- counts all spaces too
print(greeting[0],greeting[1])
print(greeting[0:2])#1st 2
print(greeting[2:]) #emit 1st 2
print(greeting[:2]) #1st 2
print(greeting[-1]) #write in reverse
print(greeting[::-1]) #reverse whole thing
print(greeting[::2])#2nd of each
print(len(greeting))

#changing capital and small
print(course.lower()) #--- Evth small
print(greeting.upper()) #---Evth big
print(greeting.capitalize()) #---1st letter big

#string concatenation
print(greeting + course)
print(greeting + " " + course)

#finding length
result = len(greeting)
print(result)

#find space positions
result2 = greeting.find("H") #rfind - in opp direction
print(result2)

#confirmation
print(greeting.isdigit()) #digit
print(greeting.isalpha()) #alpha(spaces make false)
print(greeting.count("l"))#how many similar characters
print(greeting.replace("e", "3"))
