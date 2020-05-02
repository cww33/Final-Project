
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
    if (total_salary .isalpha()) or total_salary == "":
        print("Please Input a Number")
    else:
        break
    
while True:
    percentage= input("Input what percentage to allocate for monthly subscriptions: ")
    if (percentage .isalpha()):
        print("Please Input a Number")
    else:
        break

allowance = float(total_salary)*(float(percentage)/100)
while True:
    subscription = input("Please input a subscription you have subscribed to: ")
    sub_list.append(subscription)
    if subscription.upper() == ("DONE"):
        sub_list=sub_list[:-1]
        
        break
    while True:
        price = input("Please input the monthly price of the subscription: ")
        if (price .isalpha()):
            print("Please Input A Valid Number")  
            #price_list=price_list[:-1] 
        else:
            price_list.append(float(price))
            break
        
        

new_sub_list=sub_list
new_price_list=price_list

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
    space()
    print("You still have room in your allowance to add a subscription")
    print("The subscription must cost no more than " + to_usd(allowance-current_sub_price))
    new_sub_price=current_sub_price
    print("Would you like to add another subscription? ")
    dash()
    new= input("Input Y for yes and any other key for no: ")
    space()
    if new.upper() == ("Y"):
        while True:
           
            new_sub=input("What is the new subscription: ")
            new_sub_list.append(new_sub)
            while True:
                price = input("Please input the monthly price of the subscription: ")
                if (price .isalpha()):
                    print("Please Input A Valid Number")  
                    #price_list=price_list[:-1] 
                    break
                else:
                    new_price_list.append(float(price))
                    break
            new_sub_price=sum(new_price_list)
            price_str= to_usd(allowance-new_sub_price)

            if new_sub_price == allowance:
                space()
                print("You have budgeted well! You can afford this new subscription")
                break
            elif new_sub_price > allowance:
                space()
                print("You cannot afford this subscription!")
                break

            else:
                space()
                print("You can afford this new subscription and still have allowance!")
                print("You still have $" + (price_str) + " of allowance")
                space()
                print("Would you like to add an additional subscription?")
                dash()
                new= input("Input Y for yes and any other key for no: ")
                if new.upper() != ("Y"):
                    break

                       
    price_str= str(allowance-new_sub_price)   
    info2={new_sub_list[i]:new_price_list[i] for i in range(len(new_sub_list))}
    space()
    print("Your Current Subscriptions are: ")
    line()
    for new_sub_list, new_price_list in info2.items():
        print(new_sub_list, to_usd(new_price_list))
    dash()
    print("Total: " + to_usd(new_sub_price))
    line()
    print("Allowance left $" +(price_str))
    line()
    space()
    print("Hope this application helped! Have a nice day!")
        


    


 




