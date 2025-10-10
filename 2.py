def matrix(key):
    key = key.upper().replace("J", "I")
    matrix=""
    for ch in key:
        if ch not in matrix and ch.isalpha():
            matrix += ch

    for ch in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if ch not in matrix:
            matrix += ch

    return [list (matrix[i:i+5]) for i in range(0, 25, 5)] #5x5 matrix banane k liye

def find_position(matrix,ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i,j
    return None

def encrypt(plaintext,matrix):
    text=plaintext.upper().replace("J","I")
    pairs=[]
    i=0
    while i < len(text):
        a=text[i]
        b=text[i+1] if i+1 < len(text) else 'X'
        if a==b:
            pairs.append((a,'X')) #agr same letter ho to 2nd letter ki jga X add krdeta
            i+=1
        else:
            pairs.append((a,b)) #agr different ho to as it is add krdeta
            i+=2
            
    cipher=""
    for a,b in pairs:
                r1, c1= find_position(matrix,a)
                r2, c2= find_position(matrix,b)
                if r1==r2:
                    cipher+=matrix[r1][(c1+1)%5] #agr same row m ho to next column ma shift krdeta
                    cipher+=matrix[r2][(c2+1)%5]
                elif c1==c2:
                    cipher+=matrix[(r1+1)%5][c1] #agr same column m ho to next row ma shift krdeta
                    cipher+=matrix[(r2+1)%5][c2]
                else:
                    cipher+=matrix[r1][c2] #agr same row or column m na ho to unka column swap krdeta
                    cipher+=matrix[r2][c1]
    return cipher
        
def decrypt(ciphertext,matrix):
    plain=""
    for i in range(0,len(ciphertext),2): #2 2 k pairs ma leta ha
        a,b=ciphertext[i],ciphertext[i+1]
        r1,c1=find_position(matrix,a)
        r2,c2=find_position(matrix,b)

        if r1==r2:
            plain+=matrix[r1][(c1-1)%5]  #agr same row m ho to previous column ma shift krdeta
            plain+=matrix[r2][(c2-1)%5]

        elif c1==c2:
            plain+=matrix[(r1-1)%5][c1] #agr same column m ho to previous row ma shift krdeta
            plain+=matrix[(r2-1)%5][c2]

        else:
            plain+=matrix[r1][c2]   #agr same row or column m na ho to unka column swap krdeta
            plain+=matrix[r2][c1]
    return plain


            
key="SECURITY"
plaintext="CYBERATTACK"

print("Plaintext:",plaintext)
print("Key:",key)

matrix=matrix(key)
ciphertext=encrypt(plaintext,matrix)
print("Ciphertext:",ciphertext)

decrypted_text=decrypt(ciphertext,matrix)
print("Decrypted Text:",decrypted_text)

