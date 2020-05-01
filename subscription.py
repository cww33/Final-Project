

subtotal=0
salary=0
monthly_salary=0
monthly_price=0
#monthy subcription allowed

sub_list=[]
price_list=[]

while True:
    total_salary = (input("Input your total montly salary: "))
    if (total_salary .isdigit()):
        break
    else:
        print("Please Input a Number")
    pass
        
percentage= input("Input what percentage to allocate for monthly subscriptions")
print(total_salary)
while True:
    subscription = input("Please input a subscription you have subscribed to: ")
    sub_list.append(subscription)
    if subscription.upper() == ("X"):
        sub_list=sub_list[:-1]
        print(sub_list)
        break




