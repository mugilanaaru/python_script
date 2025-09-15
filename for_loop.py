######################### For Loop ######################
"""
for i in "apple":
    print(i)
"""
################################
"""
##### Range function ######
for i in range(5):
    print(i)
"""    
##################################
"""
#### Print a range function between 1 to 4 #####
for i in range(1,5):
    print(i)
"""
############################
"""
####### range function to print variable ##############
for i in range(1,11):
    print("emc")     ### it will print emc for 10 times
"""
###################################
"""
### Range function #####
for i in range(1,11):
    print("emc")  ## print emc 10 times
    print(i)     ### print 1 to 10
"""
###############################################
"""
##### Two Tables ################
for i in range(1,11):
    print(i,"*2", "=",i*2)   ### values comes inside "" are to print as it is. values given without "" will print values from variable
"""
###############################
"""
### Get the input from user to get the tables
table=int(input("Give the number for table :"))
for i in range(1,11):
    print(i,"*2", "=",i*table)
"""
#########################################
"""
#### Print even numbers between 1 to 10 ###
for i in range(1,11):
    if(i%2==0):
        print(i)
"""
####################################
"""
#### Count the number of even numbers from 1 to 10 ###########
count=0
for i in range(1,11):
    if(i%2==0):
        count=count+1
print(count)
"""
#############################################
"""
#### Print count of even number and odd number
e_count=0
o_count=0
for i in range(1,11):
    if(i%2==0):
        e_count=e_count+1
    else:
        o_count=o_count+1
print(e_count)
print(o_count)
"""
###################################################
"""
### Addition of first 5 natural numbers #####
sum=0
for i in range(1,6):
    sum=sum+i
print(sum)
"""
#####################################################

#### Get input for 10 numbers and sum of that 10 numbers and find avg #
#### List = [] list
a=[1,2,3,4,5]
for i in a:
    print(i)

##################################################
"""
##### appending values in list
a=[]                   ##### it is a list and adding values inside the list
a.append(10)
a.append(20)
a.append(30)
print(a)
"""
###################################################
"""
a=[]                   ##### it is a list and adding values inside the list
a.append(10)
a.append(20)
a.append(30)
b=int(input("Enter a number to append in list :"))
a.append(b)
print(a)
"""
###################################################
"""
#### Get input for 10 numbers and sum of that 10 numbers and find avg
a=[]
print("Enter 10 numbers : ")        ##### This loop is to fill the list
for i in range(10):
    num=int(input("Enter "+str(i+1)))
    a.append(num)
print(a)

sum=0
for i in a:                     #### This loop is to sum from the list
    sum=sum+i
print(sum)
"""
######################################################
### Get the n number of natural numbers and their sum


