
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

#current: (x_real, y_real, yaw_real)
#target: (x_target, y_target, yaw_target)

def euler_modificado(V:float, omega:float, dt: float, target: dict) -> tuple:

   #Diminir a Linha pra n ficar grande
   dTheta = omega * dt
   Vxdt = V*dt

   #Euler Modificado
   x_k1 = target["x_k"] + math.cos(target["theta_k"] + dTheta/2)*Vxdt
   y_k1 = target["y_k"] + math.sin(target["theta_k"] + dTheta/2)*Vxdt
   theta_k1 = target["theta_k"] + dTheta

   return x_k1,y_k1,theta_k1
   
def calculate_velocity(target: tuple, current: tuple) -> tuple:

   vel = [0.0, 0.0]
    #   vx  omega

   return vel

valores = (0.0, 0.0, 0.0)
coordenates = ("x_k", "y_k", "theta_k")
target = dict(zip(coordenates, valores))

for i in range(1000):
    x_k1, y_k1, theta_k1 = euler_modificado(omega=0.3, V=1.0, dt=0.5, target=target)
    target = {"x_k": x_k1, "y_k": y_k1, "theta_k": theta_k1}

print(target)