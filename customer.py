import os 
import fileinput 

def menuDisplay():
    print('==============================')
    print('== Customer Purchase Mgt Menu ===')
    print('==================================')
    print('(1) Add new Purchase Info')
    print('(2) Remove  Purchase Info ')
    print('(3)  Update purchase Info')
    print('(4)  search purchase Info ')
    print('(5)   print purchase info ')
    print('(99)  Quit')

    # ask the user Input or choice 
    CHOICE = int (input("Enter Choice: "))
      #method to handle the menu selection 
    menuSelection(CHOICE)
def menuSelection(CHOICE):
     # bunch of condition below 
     if CHOICE ==1:
         addPurchaseInfo()
     elif CHOICE == 2:
         removePurchaseInfo()
     elif CHOICE == 3:
         updatePurchaseInfo()
     elif CHOICE == 4:
          searchPurchaseInfo()
     elif CHOICE == 5:
          printPurchaseInfo()
     elif CHOICE == 99 :
           exit()
    
    # below we add the purchaseInfo to the system 
def addPurchaseInfo():
     PurchaseInfoFile = open('purchaseLedger.txt', 'a')
     print("Adding Purchase Info")
     print("======================")
     purchase_description = input("What was the reason of the  purchase : ")
     purchase_amount = input("Enter the amount of the purchase you made : ")
     PurchaseInfoFile.write(purchase_description +'\n')
     PurchaseInfoFile.write(purchase_amount + '\n')
     PurchaseInfoFile.close()        #close the file         
     CHOICE = int(input('Enter 98 to continue or 99 to exit:')) # message for the user to continue or to exit 
     # based on the user input this will happen 
     if CHOICE == 98 :
                menuDisplay()
     else:
          exit()
    # below is the method to remove a purchase history 
def removePurchaseInfo():
    print("Removing purchase Info")
    print("=======================")    
    purchase_description = input("Enter the name of the purchase you made:  ")
    # this will access what has been written to the file  
    file = fileinput.input('purchaseLedger.txt', inplace=True)
    #iterating through the file line by line to remove the purchase
    for line in file:
         if purchase_description in line:
              for i in range(1):
                   next(file,None)
         else:
             print(line.strip('\n') ,end='\n')
    purchase_description
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
         exit()
    #this method is to update the purchase info
def updatePurchaseInfo():
     print("Updating the  purchase Info")
     print("============================")
     purchase_description = input('Enter the purchase info you want to update: ')
     purchase_amount = input('Enter the  amount of the purchase  you want')

     # reading a file 
     with open('purchaseLedger.txt', 'r') as f:
          filedata = f.readlines()
     replace = ""
     line_number = 0
     count = 0
     # this opens the file so in order to be read
     f = open('purchaseLedger.txt','r')
     file = f.read().split('\n')

     #iterating through the file 
     for i, line in enumerate(file):
         if purchase_description in line:
              for b in file[i+2: i + 2]:
                   value = int(b)
                   change = value + (purchase_amount)
                   replace = b.replace(b,str(change))
                   line_number = count 
              count = i + 1
     f.close()  # closes the file 
     filedata[count] = replace + '\n'
    #again the the file will be opened to write the update info
     with open('purchaseLedger.txt', 'w') as f:
         for line in filedata:
              f.write(line)
     CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
     if CHOICE == 98:
               menuDisplay()
     else:
          exit()
    # below this method search the purchase info
def searchPurchaseInfo():
    print('Searching purchase info')
    print('===================')
    purchase_description = input('Enter the name for the purchase : ')

    # this opens the files so that it can be read 
    f = open ('purchaseLedger.txt', 'r')
    search = f.readlines()
    f.close
    for i , line in enumerate(search):
         if purchase_description in line:
              for b in search[i:i+1]:
                   print('Item:   ', b, end='')
              for c in search[i+1:i+2]:
                   print('Quantity:   ', b, end='')
                   print('----------')
                   
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()
        # this method will print the purchaseInfo
def printPurchaseInfo():
      PurchaseInfoFile = open('purchaseLedger.txt','r')
      purchase_description = PurchaseInfoFile.readline()
      print('Current Purchase')
      print('-----------------')
      while purchase_description != '':
             purchase_amount = PurchaseInfoFile.readline()
             purchase_description = purchase_description.rstrip('\n')
             purchase_amount= purchase_amount.rstrip('\n')
             print('Item:  ' , purchase_description)
             print('Quantity:  ' , purchase_amount)

             purchase_description = PurchaseInfoFile.readline()
             PurchaseInfoFile.close()   # close the file 

             CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
             if CHOICE == 98:
                menuDisplay()
             else:
                  exit()
menuDisplay()


     

         
                   