def first_program():
    vl = ['A', 'E', 'I', 'O', 'U']
    kv = []
    sv = []
    kevin = ""
    stuart = ""

    s = input("Enter any name for string:")
    if len(s)>10 :
        print("Lenght is more then 10 character")
        exit()
    elif s.islower():
        print("string is in lower case")
        exit()

    print("Kevin words start with vowels")
    for i in range(0,len(s)):
        if s[i] in vl:
            sh=s[i:len(s)]
            # sk = s[i:len(s)-1]
            print(sh)

            sk = s[i:len(s) - 1]
            print(sk)



    print("Stuart words start with Consonent")
    for i in range(len(s)-1,0,-1):
        if s[i] not in vl:
            sh = s[i:len(s)]
            # sk = s[i:len(s)-1]
            print(sh)
            sk = s[0:len(s)-i]
            print(sk)



first_program()
