

subtotal=0
salary=0
monthly_salary=0
monthly_price=0
#monthy subcription allowed

sub_list=[]
price_list=[]

while True:
    subscription = input("Please input a subscription you have subscribed to: ")
    sub_list.append(subscription)
    if subscription.upper() == ("X"):
        sub_list=sub_list[:-1]
        print(sub_list)




#while True:
#    list1["sub"] = (input("Please input the product identifier: "))
#    userreceipt.append(userproduct) #put this at the end
#    if userproduct.upper() == ("DONE"): #it has to be done and gotta do .upper but put this if first before everything else
#        userreceipt=userreceipt[:-1] #found a page on stackoverflow on it
#        print_rinfo() #printing out the previously defined receipt information
#        for userproduct in userreceipt: #everything in the for statement is based on Professor Rosetti's walkthrough
#            receiptproduct=[i for i in products if str(i["id"]) == str(userproduct)]
#            receiptproduct=receiptproduct[0]
#            subtotal =subtotal+receiptproduct["price"]
#            priceusd= (receiptproduct["price"])
#            print("..." + receiptproduct["name"] +  to_usd (priceusd) )
#        print_totals()
#        break
#    elif ((userproduct)) not in str(productlist) or int(userproduct)==0:
#        print ("Ensure it is a valid product identifier")
#        userreceipt=userreceipt[:-1]
#
#
#  
#
#
#
#
#