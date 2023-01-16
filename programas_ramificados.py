# num_1 = int(input('por favor ingrese un número entero: '))
# num_2 = int(input(f'por favor ingrese un segundo número entero: '))
# if num_1 > num_2:
#     print(str(num_1) + " es mayor que  " + str(num_2))
# elif num_1 < num_2:
#     print(str(num_1) + " es menor que " + str(num_2))
# else:
#     print(str(num_1) + " es igual a " + str(num_2))

persona_1 = input(f'por favor ingrese su nombre (persona 1):  ')
edad_1 = int(input(f'por favor ingrese su edad: '))
persona_2 = input(f'por favor ingrese su nombre (persona 2): ')
edad_2 = int(input(f'por favor ingrese su edad: '))
if edad_1 > edad_2:
    print(persona_1 + f' es mayor que ' + persona_2)
elif edad_1 < edad_2:
    print(persona_2 + f' es mayor que ' + persona_1)   
else :
    print(f'¡ambos tienen la misma edad!') 