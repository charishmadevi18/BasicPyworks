from datetime import datetime
name=input("Enter your name::")
lists='''
rice      Rs 20/kg                  
sugar     Rs 30/kg
salt      Rs 20/kg
oil       Rs 80/litre
paneer    Rs 110/kg
maggi     Rs 50/kg
boost     Rs 90/each
colgate   Rs 85/each
'''
price=0
pricelist=[]
totalprice=0
ilist=[]
qlist=[]
plist=[]
items={'rice':20,'sugar':30,'salt':20,'oil':80,'paneer':110,'maggi':50,'boost':90,'colgate':85}
option=int(input("for list of items press1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items::")
        quantity=int(input("Enter quantity::"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no::")   
    if inp=='yes':
        pass
        if finalamount!=0:
            print(30*"=","SuperMarket",30*"=")
            print(28*" ","RJY",28*" ")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i+1, 8*" ",1*' ',ilist[i], 10*' ',qlist[i], 10*' ',plist[i])
            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print(50*" ","gst Amount:",0*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalamount:','Rs',finalamount)
            print(75*"-")
            print(20*" ","Thanks for visiting")
            print(75*"-")
                
        
    
    
    