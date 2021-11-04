# Atousa Niazi -98440127-python-Store-OSLab


PRODUCTS=[]

def load():
    f=open('database.csv','r')
    
    for row in f:
        info = row[:-1].split(',')
        PRODUCTS.append({'code':info[0],'name':info[1],'price':info[2],'count':info[3]})
    print()


def add():
    print("\033[38;5;76madding:")
    print("to add a new item: ")
    print('code:')
    code_in=int(input())
    print('name:')
    name_in=input()
    print('price')
    price_in=int(input())
    print('count:')
    count_in=int(input())
    adding=[code_in,name_in,price_in,count_in]
    PRODUCTS.append({'code':adding[0],'name':adding[1],'price':adding[2],'count':adding[3]})
    print('do you want to see new list ? (y for yes,n for no)')
    answer_1=input()
    if answer_1=='y':
        show_list()
    print()
    
    

def edit():
    print("\033[38;5;30mediting :")
    print('find item by name:')
    name_in=input()
    for product in PRODUCTS:
        if name_in==product['name']:
            print('found it!')
            print('item info: ')
            print(product['code'],'\t',product['name'],'\t',product['price'],'\t',product['count'])
            print('enter new info for item:')
            print('code:')
            code_in=int(input())
            print('name:')
            name_in=input()
            print('price')
            price_in=int(input())
            print('count:')
            count_in=int(input())
            editing=[code_in,name_in,price_in,count_in]
            product['code']=code_in
            product['name']=name_in
            product['price']=price_in
            product['count']=count_in
            print('item new info: ')
            print(product['code'],'\t',product['name'],'\t',product['price'],'\t',product['count'])
            break
    else :
        print('item does not exist in list. enter 1 in menu for adding a new item in list or try again.')
    print()



def delete():
    print("\033[38;5;168mdeleting :")
    print('find item by name:')
    name_in=input()
    for product in PRODUCTS:
        if name_in==product['name']:
            print('found it!')
            print('item info: ')
            print(product['code'],'\t',product['name'],'\t',product['price'],'\t',product['count'])
            print('are sure you want to delete this item ?(y for yes,n for no)')
            answer=input()
            while answer!='y' and answer!='n':
                print('try again')
                answer=input()
            if answer=='y':
                PRODUCTS.remove(product)
                print('successful deleting!')
                print('do you want to see new list ? (y for yes,n for no)')
                answer_1=input()
                if answer_1=='y':
                    show_list()
            elif answer=='n':
                break
    print()


def show_list():
    print("\033[38;5;6mLsit:")
    print('================================')
    print('code\tname\tprice\tcount')
    for product in PRODUCTS:
        print(product['code'],'\t',product['name'],'\t',product['price'],'\t',product['count'])
    print('================================')
    
def search():
    print("\033[38;5;214m search by item name: ")
    print('enter name: ')
    name_in=input()
    for product in PRODUCTS:
        if name_in==product['name']:
            print('found it!')
            print('item info: ')
            print(product['code'],'\t',product['name'],'\t',product['price'],'\t',product['count'])
            break
    else :
        print('item does not exist in list. enter 1 in menu for adding a new item in list.')
    print()


def buy():
    print("\033[38;5;80mshopping:")
    print('item name: ')
    name_in=input()
    for product in PRODUCTS:
        if name_in==product['name']:
            print('item exist!')
            print('item info: ')
            print(product['code'],'\t',product['name'],'\t',product['price'],'\t',product['count'])
            print('do you want to buy it ? (y for yes,n for no)')
            answer=input()
            while answer!='y' and answer!='n':
                print('try again')
                answer=input()
            if answer=='y':
                print('how many do you want: ')
                count_in=int(input())
                while count_in>int(product['count']):
                    print('Unsuccessful purchase!. Not available in stock. ')
                    print('try again')
                    count_in=int(input())
                if count_in<=int(product['count']):
                    count_list=int(product['count'])
                    count_list=count_list - count_in
                    product['count']=srt(count_list)
                    print('successful purchase!')
                    print('updated info: ')
                    print(product['code'],'\t',product['name'],'\t',product['price'],'\t',product['count'])
            elif answer=='n':
                print('shopping stoped!')
                break
            break
    else :
        print('Unsuccessful purchase!item does not exist in list. enter 1 in menu for adding a new item in list.')
    print()



def save():
    print("\033[38;5;135msaving: ")
    print('do you want to save the changs ? (y for yes,n for no)')
    answer=input()
    while answer!='y' and answer!='n':
        print('try again')
        answer=input()
    if answer=='y':
        f=open('database.csv','w') # i opened the file with w to prevent overwritting
        for element in PRODUCTS:
            f.write(element + "\n")
        f.close()
    print()
    
def show_menu():
    print("\033[1;95m~~~~~~~~~~~~~~~~~~~~~~")
    print('Welcome to Sadjad Store!')
    print('1- Add')
    print('2- Edit')
    print('3- Delete')
    print('4- Show list')
    print('5- Search')
    print('6- Buy')
    print('7- Save and Exit')
    print("\033[1;95m~~~~~~~~~~~~~~~~~~~~~~\n")
    
print("\033[1;93mloading... \n")
load()
show_list()
print("\033[1;93m\ndatabase loaded. app is ready to use.\n")
while True:
    show_menu()
    print("\033[1;93mEnter your choice:")
    choice=int(input())
    
    
    if choice==1:
        add()
    elif choice==2:
        edit()
    elif choice==3:
        delete()
    elif choice==4:
        show_list()
    elif choice==5:
        search()
    elif choice==6:
        buy()
    elif choice==7:
        save()
        break