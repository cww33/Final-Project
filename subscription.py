
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Parameters: my_price (int or float)

    Example: to_usd(99999.99)

    Returns: $99,999.99
    """  
    return f" ${my_price:,.2f}"
def line():
    print("______________________________________________")
def space():
    print("\n")
def dash():
    print("----------------------------------")
subtotal=0
salary=0
monthly_salary=0
monthly_price=0
#monthy subcription allowed

sub_list=[]
price_list=[]

while True:
    total_salary = (input("Input your total monthly salary: "))
    if (total_salary .isdigit()):
        break
    else:
        print("Please Input a Number")
    pass
while True:
    percentage= input("Input what percentage to allocate for monthly subscriptions: ")
    if (percentage .isdigit()):
        break
    else:
        print("Please Input a Number")

allowance = float(total_salary)*(float(percentage)/100)
while True:
    subscription = input("Please input a subscription you have subscribed to: ")
    sub_list.append(subscription)
    if subscription.upper() == ("DONE"):
        sub_list=sub_list[:-1]
        
        break
    while True:
        price = input("Please input the monthly price of the subscription: ")
        price_list.append(float(price))
        if (price .isalpha()):
            print("Please Input A Valid Number")  
            price_list=price_list[:-1] 
        else:
            break

info={sub_list[i]:price_list[i] for i in range(len(sub_list))}
current_sub_price= sum(price_list)

#loop new subs
# format
#underscore problem
space()
print("Your Current Subscriptions are: ")
line()

for sub_list, price_list in info.items():
    print(sub_list, to_usd(price_list))
dash()
print("Total: " + to_usd(current_sub_price))
line()
    
if current_sub_price == allowance:
    print("You have already reached your maximum allowance for subscriptions")
    print("No new subscriptions for you!")
elif current_sub_price > allowance:
    print("You have already exceeded your allowance for subscriptions!")
    print("You need to remove a subscription that costs at least " + to_usd(current_sub_price-allowance))
else:
    print("You still have room in your allowance to add a subscription")
    print("The subscription must cost no more than " + to_usd(allowance-current_sub_price))

    print("Would you like to add another subscription? ")
    new= input("Input Y for yes and any other key for no")
    if new.upper() == ("Y"):
        while True:
            new_sub=input("What is the new subscription: ")
            sub_list.append(new_sub)
            if new_sub.upper() == ("DONE"):
                sub_list=sub_list[:-1]
                break
            while True:
                price = input("Please input the monthly price of the subscription: ")
                price_list.append(float(price))
                if (price .isalpha()):
                    print("Please Input A Valid Number")  
                    price_list=price_list[:-1] 
                else:
                    break
        if current_sub_price == allowance:
            print("You have budgeted well! You can afford this new subscription")
        elif current_sub_price > allowance:
            print("You cannot afford this subscription!")
           
        else:
            print("You have budgeted well! You can afford this new subscription")
            
        space()
        print("Your Current Subscriptions are: ")
        line()

        for sub_list, price_list in info.items():
            print(sub_list, to_usd(price_list))
        dash()
        print("Total: " + to_usd(current_sub_price))
        line()
    else:
        space()
        print("Your Current Subscriptions are: ")
        line()

        for sub_list, price_list in info.items():
            print(sub_list, to_usd(price_list))
        dash()
        print("Total: " + to_usd(current_sub_price))
        line()
        print("Hope this application helped! Have a nice day!")
        


    

#print(sub_list)      
#print(price_list)
#print(allowance)
#print(info)
#print(current_sub_price)
        
 




