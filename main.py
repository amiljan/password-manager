from tkinter import *
from cypher import decrypt, lista_password, encrypt
import random
import pandas as pd
from os.path import exists

ekran = Tk()
ekran.title("Password Manager")

if exists("passwords.csv") != True:
    pd.DataFrame({"Website":[],"Email":[],"Password":[]}).to_csv("passwords.csv",index=False)


def generate_password():
    gen_pass = ""
    for i in range(16):
        if i == 0:
            lista = random.choice(lista_password[1])
            gen_pass += random.choice(lista)
        elif i == 4:
            lista = random.choice(lista_password[0])
            gen_pass += random.choice(lista)
        elif i == 8:
            lista = random.choice(lista_password[2])
            gen_pass += random.choice(lista)
        elif i == 12:
            lista = random.choice(lista_password[3])
            gen_pass += random.choice(lista)
        else:
            lista = random.choice(lista_password)
            gen_pass += random.choice(lista)
    password_input.delete(0,END)
    password_input.insert(0,str(gen_pass))

def save_add():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    key = retrive_input.get()
    email_crypt = encrypt(key,email)
    password_crypt = encrypt(key,password)
    input_table = pd.read_csv("passwords.csv")
    table = input_table.to_dict()
    free_row = len(table["Website"])
    table["Website"][free_row] = website
    table["Email"][free_row] = email_crypt
    table["Password"][free_row] = password_crypt
    output_table = pd.DataFrame(table)
    output_table.to_csv("passwords.csv",index=False)
        


def retrive_passwords():
    text = Text()
    text.grid(row=6,column=1)
    input_passwords = pd.read_csv("passwords.csv").to_dict()
    print(input_passwords)
    num_of_rows = len(input_passwords["Website"])
    for row in range(num_of_rows):
        input_passwords["Email"][row] = decrypt(retrive_input.get(),input_passwords["Email"][row])
        input_passwords["Password"][row] = decrypt(retrive_input.get(),input_passwords["Password"][row])
    output_password = pd.DataFrame(input_passwords)
    text.insert(END,output_password.to_string)
    

canvas = Canvas(width=300, height=300)
canvas.grid(row=0,column=1)
img = PhotoImage(file="lock.png")
canvas.create_image(150,150,image=img)

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
website_input = Entry()
website_input.grid(row=1,column=1)

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)
email_input = Entry()
email_input.grid(row=2,column=1)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)
password_input = Entry()
password_input.grid(row=3,column=1)
password_generate = Button(text="Generate Password",command=generate_password)
password_generate.grid(row=3,column=2)

add_button = Button(text="Add",command=save_add)
add_button.grid(row=4,column=1)

retrive_label = Label(text="Key:")
retrive_label.grid(row=5,column=0)
retrive_input = Entry()
retrive_input.insert(0,"Please enter key:")
retrive_input.grid(row=5,column=1)
retrive_button = Button(text="Retrive", command=retrive_passwords)
retrive_button.grid(row=5,column=2)



ekran.mainloop()