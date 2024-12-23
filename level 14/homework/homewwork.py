# 1)შექმენით სია, რომელშიც მოცემულია კვირის დღეები:["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
# ამოიღეთ და დაბეჭდეთ: კვირის პირველი დღე.ბოლო დღე.
# შეცვალეთ სიის მესამე ელემენტი ("Wednesday") ახალ მნიშვნელობაზე "Midweek".



week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(week[0], week[6])

week[2] = "midweek"

print(week)


# 2)მომხმარებელს სთხოვეთ, რომ შეიყვანოს ხუთი საყვარელი ცხოველის სახელები. სახელები შეინახეთ სიაში.
# მომხმარებლის მიერ შეყვანილი სიის მიხედვით:დაბეჭდეთ პირველი და ბოლო ცხოველის სახელი.შეცვალეთ სიის მეორე ცხოველის სახელი და მომხმარებლისგან მოითხოვეთ ახალი 
# მნიშვნელობა.დაბეჭდეთ განახლებული სია.

fav_animal1 = input("shieyvanet pirveli sayvareli cxoveli: ")
fav_animal2 = input("shieyvanet meore sayvareli cxoveli: ")
fav_animal3 = input("shieyvanet mesame sayvareli cxoveli: ")
fav_animal4 = input("shieyvanet mesame sayvareli cxoveli: ")
fav_animal5 = input("shieyvanet mesame sayvareli cxoveli: ")

s = [fav_animal1,fav_animal2,fav_animal3,fav_animal4,fav_animal5]

print(s[0],s[4])

s[0] = input("sheiyvanet axali cxoveli: ")
s[4] = input("sheiyvanet axali cxoveli: ")

print(s)

# 3)შექმენით სია: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12].
# ამოიღეთ სიის ყოველი მესამე ელემენტი. ამოიღეთ სია უკუღმა. სიის შუა 6 ელემენტი გადაიტანეთ ახალ სიაში.

i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(i[0:11:3])

print(i[::-1])

f =i[3:9]

print(f)

# 4)შექმენით სია, რომელიც შეიცავს ათასიდან ათიათასამდე ყველა რიცხვს, რომლებიც იყოფა 500-ზე.
# გამოიყენეთ სლაისინგი, რათა ამოიღოთ:პირველი ხუთი რიცხვი.ყოველი მესამე რიცხვი.დაითვალეთ, რამდენი ელემენტია საბოლოო სიაში.

nums = []

for i in range(1000,10000):
    nums.append(i)


print(nums[0:5])
print(nums[0::3])
print(len(nums))

# 5)მომხმარებელს სთხოვეთ, რომ შეიყვანოს 10 რიცხვი მძიმით გამოყოფილად. შეინახეთ ეს რიცხვები სიაში.
# ამ სიის მიხედვით:ამოიღეთ და დაბეჭდეთ მომხმარებლის შეყვანილი პირველი სამი რიცხვი.სიის შუა ოთხი ელემენტი გადააკოპირეთ ახალ სიაში და დაბეჭდეთ ის.შეამოწმეთ, თუ სიის ბოლო ელემენტი არის ციფრი 10.

nums = []

for i in range(10):
    nums.append(input("sheiyvanet" + str(i) + "ricxvi: "))


print(nums[0:3])

numbers = nums[4:8]
print(numbers)


print(numbers[-1] == 10)
