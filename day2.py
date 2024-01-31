
 str = "yash_balpande"
print(len(str))
 str = "yash balpande"
 ch = str[4:]
print(ch)
 print(str.upper())
print(str.replace("yash", "Gau"))
 print(str.find("a")) 



 #Q,1

name = input("Enter Your Name :- ")
 print(len(name))



# Q.2

 print(name.find("p"))

# # ------------------------------------------------------------------------------

 x = int(input("Your age :-"))

 if x >= 18:
     print("Your are eligible for voting card")
 else:
     print("You r not eligible for votting card wait till 18th birthday")



 x = int(input("Enter The Number :- "))
 rev = x % 2

if (rev == 0):
     print("x is even number")
 else:
     print("x is odd number")


a = int(input('Enter The value of a :- '))
b = int(input('Enter The value of b :- '))
c = int(input('Enter The value of c :- '))


if (a>=b and a>= c):
    print(" a is greater then b")
elif(b>=a and b>= c):
     print(" a is greater then C")
else:
  print(" c is greater then b")
