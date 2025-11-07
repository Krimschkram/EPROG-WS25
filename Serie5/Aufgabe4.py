from hashlib import sha256
def tresor(code):
    secret_code = ("b2b2f104d32c638903e151a9b20d6e27"
    + "b41d8c0c84cf8458738f83ca2f1dd744")
    m = sha256()
    m.update(code.encode())
    if m.hexdigest() == secret_code:
        print("Tresor geöffnet! Code ist:", code)


my_list = [0,1,2,3,4,5,6,7,8,9]


for a in my_list:
    for b in my_list:
        for c in my_list:
            for d in my_list:
                tresor(str(a) + str(b) + str(c) + str(d))