import string
def check_password_strength(password:str) -> bool:
    return password!=None and len(password)>=8 and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password)  

result=check_password_strength("Welcom@1234")
if result:
    print("Good Password")
else:
    print("Please choose a strong password with\nminimum of 8 charachter \natleast one numeric\natleast one specialcharacter")
