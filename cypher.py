
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'č', 'r', 's', 't', 'u', 'v', 'š', 'đ', 'ž', 'z'," ",".",",","?","!","ć","0","1","2","3","4",
"5","6","7","8","9","q","w","x","y",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Č', 'R', 'S', 'T', 'U', 'V', 'Š', 'Đ', 'Ž', 'Z',"Q","W","X","Y","Ć",
"#","$","%","&","/","(",")","=","*","+","-","_",":",";","<",">","[","]","{","}","€","@","|",'"',
]

lista_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lista_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lista_number = ["0","1","2","3","4","5","6","7","8","9"]
lista_symbols = ["!","?","@","_","#","$","€"]

lista_password = [lista_lower,lista_upper,lista_number,lista_symbols]

def encode(tekst):
    key = tekst
    kljuc = []
    for letter in key:
        for i in range(len(lista)):
            if lista[i] == letter:
                kljuc.append(i)
    return kljuc

def encrypt(codeword,message):
    key = encode(codeword)
    cypher = encode(message)
    duljina_key = len(key)-1
    count = 0
    new_cypher = []
    for number in cypher:
        if count > duljina_key:
            count = 0
        new_number = number + key[count]
        new_cypher.append(new_number)
        count +=1
    encrypted_message = ""
    for i in range(len(new_cypher)):
        if new_cypher[i] > 45:
            new_cypher[i] = new_cypher[i] - 46
        encrypted_message = encrypted_message + lista[new_cypher[i]]
    return encrypted_message

def decrypt(codeword,message):
    key = encode(codeword)
    cypher = encode(message)
    duljina_key = len(key)-1
    count = 0
    new_cypher = []
    for number in cypher:
        if count > duljina_key:
            count = 0
        new_number = number - key[count]
        new_cypher.append(new_number)
        count +=1
    encrypted_message = ""
    for i in range(len(new_cypher)):
        if new_cypher[i] < 0:
            new_cypher[i] = new_cypher[i] + 46
        encrypted_message = encrypted_message + lista[new_cypher[i]]
    return encrypted_message

#upit = 0
#while upit < 3:
#    upit = int(input("Šifrirati(1), Dešifrirati(2) ili Kraj(3)?\n"))
#    if upit == 1:
#        encrypt()
#    elif upit == 2:
#        decrypt()

   
