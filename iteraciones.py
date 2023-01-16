contador_externo = 0 # es recomendable utilizar contadores para iteraciones
contador_interno = 0

while contador_externo < 5:
    while contador_interno < 6: # primero se ejecutará esta iteración y luego la otra
        print(contador_externo, contador_interno)
        contador_interno += 1 # notar que estamos en el loop del contador_interno
        if contador_interno >= 3:
             break

    contador_externo += 1 # se vuelve a la identación del loop del contador_externo
    contador_interno = 0# si no regresa a 0, el primer ciclo while no será ejecutado   

# while_contador_externo no se ejecutará hasta que while_contador_interno
#  se ejecute, notar que el print está en el interno