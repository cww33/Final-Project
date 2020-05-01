

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

print(sub_list)      
print(price_list)
print(allowance)
print(info)
        
    #if price.isalpha:
    #    print("Please Input      A Valid Number")
    #    price_list=price_list[:-1]
    #else:
    #    break
    #




