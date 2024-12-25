
# 1)მომხმარებელს შემოატანინეთ მისი სახელი, შემდეგ შეეკითხეთ როგორ უნდა სახელის შეცვლა (lower/upper/capitalize) თუ შემოიტანს upper, მაშინ დაუბეჭდეთ სახელი გადიდებულად, თუ შემოიტანს lower, მაშინ დაუბეჭდეთ სახელი დაპატარავებულად და თუ შემოიტანს capitalize, მაშინ სახელის პირველი ასო გაუდიდეთ.

momx = input("sheiyvanet tkveni saxeli: ")
momx1 = input("sheiyvanet shriftis zoma: ")

if momx1 == "upper":
    print(momx.upper())

if momx1 == "lower":
    print(momx.lower())

else:
    print(momx.capitalize())


# 2)მომხმარებელს შემოატანინეთ მისი გვარი და შეამოწმეთ თუ გვარი შეიცავს სიმბოლოებს "shvili" მაშინ დაუბეჭდეთ "როგორ ხარ?" თუ შეიცავლს "ia" მაშინ დაუბეჭდეთ "მუჭო რექ?" სხვა შემთხვევაში "Bye".

gvari = input("sheiyvanet tkveni gvari: ")

if "shvili" in gvari:
    print("rogor xar")
elif "ia" in gvari:
    print("მუჭო რექ")
else:
    print("bye")
 

# 3)შექმენით სახელების სია, შემდეგ მომხმარებელს შემოატანინეთ სახელი და თუ სახელის იწყება ასო "d"-თი და ბოლოვდება ასო "i"-თ, მაშინ დაამატეთ სახელების სიაში, სხვა შემთხვევაში დაუბეჭდეთ "invalid".


names = ["nika", "lado"]

mo = input("sheiyvanet saxeli: ") 


if mo[0] == "d" and mo[-1] == "i":
    print(names.append(mo))

else:
    print("invalid")

# 4)შექმენით 10 ელემენტიანი სია, შემდეგ მომხმარებელს შემოატანინეთ რიცხვი და ამოაგდეთ ამ რიცხვის ინდექსზე მდგომი ელემენტი სიიდან, ბოლოს დაბეჭდეთ სია.

numbers = [1,2,3,4,55,53,51,66,10,11]

num = int(input("sheiyvanet 1dan 10amde cipri: "))

numbers.pop(num)

print(numbers)

# 5)შექმენით 5 ელემენტიანი სია, მომხმარებელს შემოატანინეთ რიცხვი და შემდეგ მისი საყვარელი საჭმელი, შემდეგ ამ შემოტანილი რიცხვის ინდექსზე დაამატეთ მისი საყვარელი საჭმელი და დაბეჭდეთ სია.

numb = ["lomi","mgeli","kata","dzagli","zvigeni"]

m = input("sheiyvanet tkveni sayavreli sachmeli: ")
m2 = int(input("sheiyvanet nebismieri cipri: "))

numb.insert(m2,m)
print(numb)





