def addition(n1,n2):
    result=n1+n2
    return result

def substration(n1,n2):
    result=n1-n2
    return result

#TASK -- write function for *, /, %, //, **
def multiplication(n1,n2):
          result=n1*n2
          return result

def division(n1,n2):
          result=n1/n2
          return result

def floor_divison(n1,n2):
          result=n1//n2
          return result

def modulus(n1,n2):
          result=n1%n2
          return result

def exponentiation(n1,n2):
          result=n1**n2
          return result


#print Menu
print("Welcome to My Calculator Demo")
print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Floor Division\n7.Exponent")

#asking for choice in numeric format
choice=int(input("Enter your choice between 1 to 7"))

#input number
n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))

if(choice==1):
   add=addition(n1,n2)  
   print(f'{n1}+{n2}={add}')  
elif(choice==2):
    sub=substration(n1,n2)   
    print(f'{n1}-{n2}={sub}')
elif(choice==3):
      mul=multiplication(n1,n2)  
      print(f'{n1}*{n2}={mul}')
elif(choice==4):
       div=division(n1,n2)
       print(f'{n1}/{n2}={div}')
elif(choice==5):
       mod=modulus(n1,n2)
       print(f'{n1}%{n2}={mod}')
elif(choice==6):
       fdiv=floor_divison(n1,n2)
       print(f'{n1}//{n2}={fdiv}')
elif(choice==7):
       exp=exponentiation(n1,n2)
       print(f'{n1}**{n2}={exp}')
else:
       print("Wrong Choice !!!")

print("Thankyou !!!!!")
