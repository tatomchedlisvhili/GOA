# 0)კომენტარის სახით ახსენით append/insert/pop/len/upper/lower/capitalize/find და დაწერეთ ინფორმაცია მათი არგუმენტების შესახებ

# append - amatebs siis bolos axal element
# insert - amatebs konkretul indeqsze konkretul element
# pop - agdebs siidan elements
# len - sigrdzes tvlis
# upper - didi asoebit wers
# lower - patara asoebit wers
# capitalize - pirvel asos adidebs danachens apataravebs
# find - poulobs romel indeqszea elementi


# 1)შექმენით სია, შეიყვანეთ 5 გვარი, შემდეგ მომხმარებელს შემოატანინეთ მისი სახელი, თუ სახელი შეიცავს 7-ზე მეტ სიმბოლოს მაშინ ჩაამატეთ სახელების სიაში

surnames = ["mchedlishvili","odisharia","jiqia","dvali","goletiani"]

m = input("sheiyvanet tkveni saxeli")

if len(m) > 7:
    print(surnames.append(m))
print(surnames)


# 2)შექმენით სია 10 ელემენტით და გამოიტანეთ მხოლოდ ლუწ ინდექსზე მდგომი ელემენტები.

sia = ["nika",1,3,"giorgi",23,5,6,7,"ana",]
print(sia[::2])


# 3)შექმენით ცვლადი რომელშიც შენახული იქნება სტრინგი შემდეგ კი გაიგეთ ამ სტრინგის სიმბოლოების რაოდენობა.

name = "tarieli"
print(len(name))

# 4) მომხმარებელს შემოატანინეთ მისი სახელი დიდი ასოებით და შეინახეთ ცვლადში სახელად name და .lower() ფუნქციის მეშვეობით გადააქციეთ ცვლადის მნიშვნელობა  პატარა ასოებად. 

name = input("sheiyvanet tkveni saxeli didi asoebit: ")
print(name.lower())

# 5) ცვლადში შეინახეთ თქვენი გვარი პატარა ასოებით, შემდეგ .upper() ფუნქციის მეშვეობით გადააქციეთ ცვლადის მნიშვნელობა  დიდ ასოებად.


sname = "mchedlishvili"
print(sname.upper())


# 6) ცვლადში შეინახეთ სტრინგი პატარა ასოებით, შემდეგ .capitalize() ფუნქციის მეშვეობით გადააქციე პირველი ასო დიდ ასოდ.

nam = "tato"
print(name.capitalize())
