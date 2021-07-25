
from tkinter import *

import sqlite3

root=Tk()
root.title('Livre de contacts')
root.geometry("400x600") 


 # CREATING DATA BASE

'''cont = sqlite3.connect('Livre_de_contacts.db')
c = cont.cursor()

c.execute("""CREATE TABLE contacts(
            name text ,
            adress text ,
            number integer,
            mail text 

            )""")

'''
 # ADDING A CONTACT

def submit():
    cont = sqlite3.connect('Livre_de_contacts.db')
    cur = cont.cursor()
    cur.execute("INSERT INTO contacts VALUES (:name, :adress, :number, :mail)",
                {
                    'name': name.get(),
                    'adress' : adress.get(),
                    'number' : number.get(),
                    'mail' : mail.get()
                })

    
    cont.commit()
    cont.close()

    
    name.delete(0,END)
    adress.delete(0,END) 
    number.delete(0,END)
    mail.delete(0,END)

 # SHOWING CONTACTS
    
def query():
    cont = sqlite3.connect('Livre_de_contacts.db')
    cur = cont.cursor()
    show=Tk()
    show.title("Sort a record")
    show.geometry("400x500")
    cur.execute("SELECT *,oid FROM contacts")
    records=cur.fetchall()
    print(records)
   
    print_records=''
    for record in records:
        print_records+=str(record[0])+ " " +str(record[1]) + " " +"\t" + str(record[4]) + "\n"
    query_label=Label(show, text=print_records)
    query_label.grid(row=2, column=0, columnspan=2)
    
    show_btn= Button(show, text="Return" , command=show.destroy)
    show_btn.grid(row=1 ,column=0,columnspan=2,pady=10,padx=10,ipadx=165)
    cont.commit()
    cont.close()

    
def delete():
    cont = sqlite3.connect('Livre_de_contacts.db')
    cur = cont.cursor()
    cur.execute("DELETE FROM contacts WHERE oid= " + delete_box.get())  
    cont.commit()
    cont.close()

#UPDATE A CONTACT

def save_update():
    cont = sqlite3.connect('Livre_de_contacts.db')
    cur = cont.cursor()
    record_id=delete_box.get()
    cur.execute('UPDATE contacts SET name =?,adress =?,number =?,mail =? WHERE oid = ?',(name_update.get(),adress_update.get(),number_update.get(),mail_update.get(),int(record_id)))

    cont.commit()
    cont.close()
    update.destroy()

def update():
    global update
    update=Tk()
    update.title("Update a contact")
    update.geometry("400x400")

    cont = sqlite3.connect('Livre_de_contacts.db')
    cur = cont.cursor()

    record_id=delete_box.get()
    cur.execute("SELECT *,oid FROM contacts WHERE oid="+record_id)
    records=cur.fetchall()

    global name_update
    global adress_update
    global number_update
    global mail_update
    
    

    name_update = Entry(update, width=30)
    name_update.grid(row=0, column=1 , padx=20 , pady=(10,0))
    adress_update = Entry(update, width=30)
    adress_update.grid(row=1, column=1)
    number_update= Entry(update, width=30)
    number_update.grid(row=2, column=1)
    mail_update = Entry(update, width=30)
    mail_update.grid(row=3, column=1)
    
    name_label=Label(update, text="Name")
    name_label.grid(row=0, column=0 , pady=(10,0))                   
    adress_label=Label(update, text="Adress")
    adress_label.grid(row=1, column=0)
    number_label=Label(update, text="Number")
    number_label.grid(row=2, column=0)
    mail_label=Label(update, text="Mail")
    mail_label.grid(row=3, column=0)
    
    for record in records:
        name_update.insert(0,record[0])
        adress_update.insert(0,record[1])
        number_update.insert(0,record[2])
        mail_update.insert(0,record[3])
        
    update_btn= Button(update, text="Save Contact" , command=save_update)
    update_btn.grid(row=6 ,column=0,columnspan=2,pady=10,padx=10,ipadx=145)


# SORT THE CONTATS
    
def tri_alpha():
    cont = sqlite3.connect('Livre_de_contacts.db')
    cur = cont.cursor()
    tri_alpha=Tk()
    tri_alpha.title("Sort By Alphabetic Order")
    tri_alpha.geometry("440x500")
    cur.execute("SELECT *,oid FROM contacts")
    records=cur.fetchall()
    print(records)
    T1=[]
    T2=[]
    for ij in range(len(records)):
        T1.append(records[ij][0])
        T2.append(records[ij])
    for i in range(len(T1)):
        aux =T1[i]
        ind=i
        for j in range(i+1,len(T2)):
            if (T1[j]<aux):
                aux=T1[j]
                ind=j
        T2[ind],T2[i]=T2[i],T2[ind]
        T1[ind],T1[i]=T1[i],T1[ind]
    
    update_btn= Button(tri_alpha, text="Return" , command=tri_alpha.destroy)
    update_btn.grid(row=1 ,column=0,columnspan=2,pady=10,padx=1,ipadx=80)
    
    print_records=''
    for record in T2:
        print_records+=str(record[0])+ " " +str(record[1]) + " "+str(record[2])+ " " +"\t" + str(record[4]) + "\n"
    tri_alpha_label=Label(tri_alpha, text=print_records)
    tri_alpha_label.grid(row=2, column=0,columnspan=2,pady=10,padx=1,ipadx=145)
    
    cont.commit()
    cont.close()
    tri.destroy()


def tri_num():
    cont = sqlite3.connect('Livre_de_contacts.db')
    cur = cont.cursor()
    tri_num=Tk()
    tri_num.title("Sort By Phone Number")
    tri_num.geometry("440x500")
    
    cur.execute("SELECT *,oid FROM contacts")
    records=cur.fetchall()
    print(records)
    T1=[]
    T2=[]
    for ij in range(len(records)):
        T1.append(records[ij][2])
        T2.append(records[ij])
    for i in range(len(T1)):
        aux =T1[i]
        ind=i
        for j in range(i+1,len(T2)):
            if (T1[j]<aux):
                aux=T1[j]
                ind=j
        T2[ind],T2[i]=T2[i],T2[ind]
        T1[ind],T1[i]=T1[i],T1[ind]

    print_records=''
    for record in T2:
        print_records+=str(record[0])+ " " +str(record[1]) + " " + str(record[2]) + " "+"\t" + str(record[4]) + "\n"
    tri_alpha_label=Label(tri_num, text=print_records)
    tri_alpha_label.grid(row=2, column=0, columnspan=2,pady=10,padx=10,ipadx=145)
    
    cont.commit()
    cont.close()
    tri.destroy()
    
    update_btn= Button(tri_num, text="Retour" , command=tri_num.destroy)
    update_btn.grid(row=0 ,column=0,columnspan=2,pady=10,padx=1,ipadx=80)

def tri():
    global tri
    tri=Tk()
    tri.title("Sort a record")
    tri.geometry("400x100")
    cont = sqlite3.connect('Livre_de_contacts.db')
    cur = cont.cursor()
    Alphabetic_btn= Button(tri,text="Alphabetic Order" , command=tri_alpha)
    Alphabetic_btn.grid(row=2 ,column=0,columnspan=10,pady=10,padx=30,ipadx=120)
    Numeric_btn= Button(tri,text="Numeric Order" , command=tri_num)
    Numeric_btn.grid(row=4 ,column=0,columnspan=10,pady=10,padx=10,ipadx=126)

# OUR MAIN FONCTION

cont = sqlite3.connect('Livre_de_contacts.db')
name = Entry(root, width=30)
name.grid(row=0, column=1 , padx=20 , pady=(10,0))

adress = Entry(root, width=30)
adress.grid(row=1, column=1)

number= Entry(root, width=30)
number.grid(row=2, column=1)

mail = Entry(root, width=30)
mail.grid(row=3, column=1)

delete_box = Entry(root,width=30)
delete_box.grid(row=9,column=1,pady=5)

name_label=Label(root, text="Name")
name_label.grid(row=0, column=0 , pady=(10,0))                   

adress_label=Label(root, text="Adress")
adress_label.grid(row=1, column=0)

number_label=Label(root, text="Number")
number_label.grid(row=2, column=0)

mail_label=Label(root, text="Mail")
mail_label.grid(row=3, column=0)

delete_box_label=Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)

submit_btn = Button(root, text="add record to database", command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=107)
                
query_btn = Button(root, text="show records" , command=query)
query_btn.grid(row=7 ,column=0,columnspan=2,pady=10,padx=10,ipadx=132)

delete_btn= Button(root, text="Delete Record" , command=delete)
delete_btn.grid(row=10 ,column=0,columnspan=2,pady=10,padx=10,ipadx=132)

update_btn= Button(root, text="Update Record" , command=update)
update_btn.grid(row=11 ,column=0,columnspan=2,pady=10,padx=10,ipadx=130)

tri_btn= Button(root, text="Sort Records" , command=tri)
tri_btn.grid(row=12 ,column=0,columnspan=2,pady=10,padx=10,ipadx=136)

cont.commit()
cont.close()

root.mainloop()
