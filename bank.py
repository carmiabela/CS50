a = input("greetings").strip().lower()
if (a[:5].strip())=="hello":
    print("$0")
elif a[0]=="h" and a[:5].strip()!="hello":
    print("$20")
else:
    print("$100")
