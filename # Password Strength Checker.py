# Password Strength Checker

# Password ki length check karo.
# 8+ characters ho to Strong, warna Weak.

a = str(input("ENTER YOUR PASSWORDF :"))
b  = len(a)

if (b>=8):
    print("STRONG PASSWORD")
else:
    print("WEAK")
