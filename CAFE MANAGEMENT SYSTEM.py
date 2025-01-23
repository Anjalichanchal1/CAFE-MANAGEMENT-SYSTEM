#!/usr/bin/env python
# coding: utf-8

# In[ ]:


menu={  
    'Pizza' : 110,
    'Pasta' : 150,
    'Burger': 200,
    'Salad' : 250,
    'Coffee': 100,   
}

print(" Welcome to the Restraunt")
print(" Pizza  : Rs 110,\n Pasta  : Rs 150,\n Burger : Rs 200,\n Salad  : Rs 250,\n Coffee : Rs 100")

order_total= 0
item_1= input("Enter the name of item which you want to order=  ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"order item {item_1} is not available yet")
another_order= input("do you want to add another order item(YES/NO)= ")
if another_order == "YES":
    item_2= input("Enter the name of second item=  ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your item {item_2} has been added to your order")
else:
    print(f"order item {item_2} is not available yet")
        
print(f"The total amounts of item to pay{order_total}")
    
    


# In[ ]:


menu={  
    'Pizza' : 110,
    'Pasta' : 150,
    'Burger': 200,
    'Salad' : 250,
    'Coffee': 100,   
}

print(" Welcome to the Restraunt")
print(" Pizza  : Rs 110,\n Pasta  : Rs 150,\n Burger : Rs 200,\n Salad  : Rs 250,\n Coffee : Rs 100")

order_total= 0
item_1= input("Enter the name of item which you want to order=  ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"order item {item_1} is not available yet")
another_order= input("do you want to add another order item(YES/NO)= ")
if another_order == "YES":
    item_2= input("Enter the name of second item=  ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your item {item_2} has been added to your order")
else:
    print(f"order item {item_2} is not available yet")
        
print(f"The total amounts of item to pay{order_total}")
    
    


# In[ ]:




