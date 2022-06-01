""" 
Realizar un programa  que le solicite  a  3  usuarios ingresar por teclado información 
personal,  la  información  de  cada  usuario  se  debe  guardar  en  una  estructura  de 
colección  inmutable,  luego  mostrar  por  pantalla  la  información  de  los  usuarios 
agrupada en una estructura de colección mutable. 
 
La información para solicitar es:
 
    a. Nombres y apellidos. 
    b.  Ocupación. 
    c. Edad. 
    d.  Ciudad. 
    e. Número de contacto. 
    f. Correo electrónico
"""

# First user
## Request personal information
print("Enter the information for the first user") 
fullname_user_1 = input("Type your full name? \n")
occupation_user_1 = input("Type your occupation \n")
age_user_1 = int(input("Type your age \n"))
city_user_1 = input("Type your city \n")
contact_number_user_1 = int(input("Type your contact number \n"))
email_user_1 = input("Type your email \n")

## Save first user into a tuple
first_user = (
    fullname_user_1, 
    occupation_user_1, 
    age_user_1, city_user_1, 
    contact_number_user_1, 
    email_user_1)

# Second user
## Request personal information
print("Enter the information for the second user") 
fullname_user_2 = input("Type your full name? \n")
occupation_user_2 = input("Type your occupation \n")
age_user_2 = int(input("Type your age \n"))
city_user_2 = input("Type your city \n")
contact_number_user_2 = int(input("Type your contact number \n"))
email_user_2 = input("Type your email \n")

## Save second user into a tuple
second_user = (
    fullname_user_2, 
    occupation_user_2, 
    age_user_1, city_user_2, 
    contact_number_user_2, 
    email_user_2)

# Third user
## Request personal information
print("Enter the information for the third user") 
fullname_user_3 = input("Type your full name? \n")
occupation_user_3 = input("Type your occupation \n")
age_user_3 = int(input("Type your age \n"))
city_user_3 = input("Type your city \n")
contact_number_user_3 = int(input("Type your contact number \n"))
email_user_3 = input("Type your email \n")

## Save third user into a tuple
third_user = (
    fullname_user_3, 
    occupation_user_3, 
    age_user_1, city_user_3, 
    contact_number_user_3, 
    email_user_3)

# Show users information
print(f"The firs user is: \n {list(first_user)}")
print(f"The second user is: \n {list(second_user)}")
print(f"The third user is: \n {list(third_user)}")
