loop1 = True
loop2 = False
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')
filename1 = pd.read_csv("C:\\Users\\Hp\\Desktop\\users.csv")
filename2 = pd.read_csv("C:\\Users\\Hp\\Desktop\stock.csv")
filename3 = pd.read_csv("C:\\Users\\Hp\\Desktop\\orders.csv")
print("********************")
print(" WELCOME TO ONLINE ELECTRONIC SHOP ")
print("********************")
username = None
while loop1:
print("1. Login")
print("2. Register")
print("3. Exit")
choice = int(input("Enter your choice:"))
if choice == 1:
df = pd.read_csv("C:\\Users\\Hp\\Desktop\\users.csv",
index_col='user')
uname = input("Enter your name:")
passw = input("Enter your password:")
if uname in df.index:
login = True
print('\n')
print('Logged in successfully')
else:
login = False
if not login:
print("Incorrect username, Try again later")
else:
if passw == df.loc[uname, 'passw']:
login = True
else:
login = False
print("Incorrect password, Try again later")
if not login:

10

print("Login failed")
else:
loop1 = False
loop2 = True
username = uname
print("-------------------------------------------------------")
print("-------------------------------------------------------")

elif choice == 2:
uname = input("Enter your username:")
passw = input("Enter your password:")
email = input("Enter your email:")
print("Registered successfully")
df = pd.read_csv("C:\\Users\\Hp\\Desktop\\users.csv")
to_append = [uname, passw, email]
df_Length = len(df)
print(df_Length)
df.loc[df_Length] = to_append
df = df.set_index('user')
df.to_csv("C:\\Users\\Hp\\Desktop\\users.csv")
loop1 = False
loop2 = True
username = uname
elif choice == 3:
print("OK, bye. Thank you for for shopping with us")
loop1 = False

while loop2:
print("1. View available items")
print("2. Place an order")
print("3. View orders placed by a customer")
print("4. Add a new product to the store")
print("5. List out the products of a particular company")
print("6. To view details of any product")
print("7. List out the stock based on highest orders")
print("8. Data Analysis of the product and the orders of the product")
print("9. Data Analysis of the revenue from each Product")
print("10. Exit")
print("-------------------------------------------------------")
choice2 = int(input("Enter your choice:"))
print("-------------------------------------------------------")

if choice2 == 1:
df2 =
pd.read_csv("C:\\Users\\Hp\\Desktop\\stock.csv",index_col=0)
print(df2.iloc[:, :3])
print("-------------------------------------------------------")

11

elif choice2 == 2:
df3 = pd.read_csv("C:\\Users\\Hp\\Desktop\\orders.csv")
df2 = pd.read_csv("C:\\Users\\Hp\\Desktop\\stock.csv",
index_col='itemcode')
df2.fillna(0)
print(df2.iloc[:,:3])
print("-------------------------------------------------------")
itemcode = input("Enter item code of the product:")
if itemcode in df2.index:
qty = int(input("Enter quantity of the product:"))
astock = df2.loc[itemcode,'astock']
if astock>=qty:
orders=df2.loc[itemcode,'orders']
orders=orders+qty
astock=astock-qty
df2.loc[itemcode,'orders']=orders
df2.loc[itemcode,'astock'] = astock
amount=df2.loc[itemcode,'price']*qty
to_append3 = [username, itemcode, qty, amount]
df_length3 = len(df3)
df3.loc[df_length3+1] = to_append3
df3 = df3.set_index('corders')
df3.to_csv("C:\\Users\\Hp\\Desktop\\orders.csv")
df2.to_csv("C:\\Users\\Hp\\Desktop\\stock.csv")
print("Purchase successful. Amount of Rs. ", amount, "has been
charged")
print('\n')
else:
print("Insufficient stock")
else:
print("Invalid choice")
elif choice2==3:
df3=pd.read_csv("C:\\Users\\Hp\\Desktop\\orders.csv")
uname = input("Enter your name (admin): ")
passw = input("Enter your password: ")

if uname=='admin' and passw=='admin':
print("Logged in as admin.")
print("-------------------------------------------------------")
st=input("Name of customer: ")
print()

12

print("Orders Placed by ",st)
print()
dfcust=df3[df3['corders']==st]
dfcust.set_index('corders')
print(dfcust)
else:
print("You are not the admin")
elif choice2==4:
df2 = pd.read_csv("C:\\Users\\Hp\\Desktop\\stock.csv")
uname = input("Enter your name (admin): ")
passw = input("Enter your password: ")

if uname=='admin' and passw=='admin':
print("Logged in as admin.")
print("-------------------------------------------------------")
print("Add the new Product information")
print("-------------------------------------------------------")
length = len(df2.index)
code = input("Enter the Product code: ")
pro = input("Enter the Product name: ")
nm=input("Enter Company name : ")
pri = int(input("Enter cost per Product : "))
tot = int(input("Enter total stock: "))
print()
astock=tot
orders=0
length=length+1
df2.loc[length, ['itemcode', 'product','company', 'price',
'totalstock', 'astock', 'orders']] = [code, pro,nm, pri, tot, astock, orders]
df2.to_csv("C:\\Users\\Hp\\Desktop\\stock.csv")
print("New Product details added successfully")
print("--------------------------------------------------------")
else:
print("Invalid login. Admin access denied.")
print("--------------------------------------------------------")

elif choice2==5:
df2 = pd.read_csv("C:\\Users\\Hp\\Desktop\\stock.csv",
index_col='itemcode')
str=input("Enter the Company name:")
dfcompany=df2[df2['company']==str]
dfcompany.drop(dfcompany.columns[dfcompany.columns.str.contains('
Unnamed',case = False)],axis = 1, inplace = True)
print(dfcompany.iloc[:,:3])
print('\n')

13

elif choice2==6:
df2 = pd.read_csv("C:\\Users\\Hp\\Desktop\\stock.csv",
index_col='itemcode')
str=input("Enter the Product name:")
dfproduct=df2[df2['product']==str]
dfproduct.drop(dfproduct.columns[dfproduct.columns.str.contains('Un
named',case = False)],axis = 1, inplace = True)
print(dfproduct)
print('\n')
elif choice2==7:
df=pd.read_csv("C:\\Users\\Hp\\Desktop\\stock.csv")
df.drop(df.columns[df.columns.str.contains('Unnamed',case =
False)],axis = 1, inplace = True)
print(df.sort_values(by=['orders'],ascending=False))
print("-------------------------------------------------------")
elif choice2==8:
df=pd.read_csv("C:\\Users\\Hp\\Desktop\\stock.csv")
orders=df.groupby('product')[['orders']].sum()
plt.xlabel("Product Name")
plt.ylabel("Orders")
plt.title("Analysis of the orders of each Product")
plt.xticks(fontsize=10,rotation=90)
plt.plot(orders,color='r',marker='*',markersize=10,linestyle='dashdot')
plt.show()
elif choice2 ==9:
df = pd.read_csv("C:\\Users\\Hp\\Desktop\\orders.csv")
amount=df.groupby('itemcode')[['amount']].sum()
pcode=amount.index.to_list()
amt=amount.amount.to_list()
print(pcode)
print(amt)
plt.xlabel("Product Code")
plt.ylabel("Revenue")
plt.title("Analysis of the Revenue received from the sales of each
Product")
plt.bar(pcode,amt,color='g')
plt.show()

elif choice2 == 10:
print("********************************")
print(" Thank you . It was pleasant shopping with you. Have a
nice day BYE . ")
print("*******************************")
loop2 = False

14

else:
print("Invalid choice")
