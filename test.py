#Authors: Alexander Black, Crystal Hwang, Kitt Mori, Hannah Smith (Section 3 Group 5)
#Data Structures Project
# Description: Randomly assigns burger orders to nine different customers at our burger restaurant,
# Outputs the number of burgers each customer orders
 
import random #allows us to generate random numbers and random element from list
 
class Order():
    def __init__(self):
        self.burger_count = self.randomBurgers() #assigns integer returned in randomBurgers() to burger_count instance variable
    def randomBurgers(self):
        randomInt = random.randint(1,20) #generates random integer between 1 and 20
        return randomInt
   
class Person():
    def __init__(self):
        self.customer_name = self.randomName() #assigns string returned in randomName() to customer_name instance variable
    def randomName(self):
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        randomName = random.choice(asCustomers) #gets random element from asCustomers list
        return randomName
 
class Customer(Person):
    def __init__(self):
        super().__init__() #call superclass's constructor
        self.order = Order() #order object created from Order Class as an instance variable of the Customer Class
 
queueCustomers = [] #make queue
numCustomers = 100 #variable for number of customers to put in queue

#append customers to queue; each customer in queue should have a name and order object as an attribute
for i in range(0, numCustomers):
    customer = Customer()
    queueCustomers.append(customer)
 
dictionaryCustomers = {} #create dictionary

#to add items to dictionaryCustomers
#loops through each customer in queue
#if customer_name is not in the dictionary, add it to the dictionary with customer_name as key and burger_count as value
#if customer_name is already in queue, update the value of that already existing key by adding the burger_count of currently accessed customer to the current value of the key
for i in queueCustomers:
    if i.customer_name not in dictionaryCustomers:
        dictionaryCustomers[i.customer_name] = i.order.burger_count
    elif i.customer_name in dictionaryCustomers:
        dictionaryCustomers[i.customer_name] = dictionaryCustomers[i.customer_name] + i.order.burger_count
 
lstSortedValues = sorted(dictionaryCustomers.values())[::-1] #sorts all dictionary values in descending order and adds to list

sorted_values_dict = {} #create new dictionary for sorting

#to sort dictionary in descending order by value
#loop through each value in sorted lstSortedValues
#loop through each key in dictionaryCustomers
#if the value of currently accessed dictionaryCustomer key is equal to currently accessed element in lstSortedValues
#then add to sorted_values_dict where the key is the currently accessed key from dictionaryCustomers
#and the value is the value of the currently accessed key from dictionary Customers
for i in lstSortedValues:
    for j in dictionaryCustomers.keys():
        if dictionaryCustomers[j] == i:
            sorted_values_dict[j] = dictionaryCustomers[j]
 
#output
new_line = '\n'
for i in sorted_values_dict.keys():
    print(f'{i:21}{str(sorted_values_dict[i])}{new_line}')