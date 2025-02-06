# 1)შექმენით ფუნქცია რომელსაც გადაეცემა არგუმენტად რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ლუწია ეს რიცხვი თუ კენტი.

def luwiatukenti(num):
    if num % 2 == 0:
        return "luwia"
    else:
        return "kentia"

print(luwiatukenti(11))
print(luwiatukenti(12))   


# 2)შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა სახელი და დაბეჭდავს მისთვის მიესალმებას (მაგალითად: "Hello Giorgi"). გამოძახეთ ეს ფუნქცია 2-ჯერ და გადაეცით სხვადასხვა სახელი.

def misalmeba(word):
    return "hello " + word

print(misalmeba("nika"))
print(misalmeba("tazo"))


# 3)შექმენით ფუნქცია, რომელიც იღებს ორ სტრინგს და მოახდინეთ კონკატენაცია.


def konkatinacia(word1,word2):
    return word1 + word2

print(konkatinacia("vashli da ","xe"))
