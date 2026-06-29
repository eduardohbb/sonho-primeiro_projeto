
# ISSO COM BASE NO EXERCICIO 4 DA LISTA 7 DE C++
#┌────────────────────────────────────────────────────────┐
#│                      SEU PROJETO                       │
#│ Posição Atual + Posição Alvo  ───>  Calcula V e ω      │
#└───────────────────────────┬────────────────────────────┘
#                            │
#                            ▼ (Comando enviado ao robô)
#┌────────────────────────────────────────────────────────┐
#│                 EXERCÍCIO DE ODOMETRIA                 │
#│ V e ω medidos pelas rodas    ───>  Calcula Nova Posição│
#└────────────────────────────────────────────────────────┘
#

import math

#target: (x_real, y_real, yaw_real)
#current: (x_target, y_target, yaw_target)

def calculate_velocity(target, current):
 
   x_target = target[0]
   y_target = target[1]
   yaw_target = target[2]

   x_real = current[0]
   y_real = current[1]
   yam_real = current[2]

   dy = y_target - y_real
   dx = x_target - x_real
   distancia = math.sqrt(dy**2 + dx**2)


   vel = [0.0, 0.0]
    #   vx  omega

   return vel