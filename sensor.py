import serial
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Configurar la conexión serial
ser = serial.Serial('/dev/tty.usbserial-57670841031', 115200)  

# Crear las variables del universo y las funciones de membresía
ppm = ctrl.Antecedent(np.arange(0, 10001, 1), 'ppm')
air_quality = ctrl.Consequent(np.arange(0, 101, 1), 'air_quality')

# Definir las funciones de membresía para ppm (entrada)
ppm['muy_bajo'] = fuzz.trapmf(ppm.universe, [0, 0, 100, 500])
ppm['bajo'] = fuzz.trimf(ppm.universe, [100, 500, 2000])
ppm['moderado'] = fuzz.trimf(ppm.universe, [500, 2000, 5000])
ppm['alto'] = fuzz.trimf(ppm.universe, [2000, 5000, 7500])
ppm['muy_alto'] = fuzz.trapmf(ppm.universe, [5000, 7500, 10000, 10000])

# Definir las funciones de membresía para air_quality (salida)
air_quality['excelente'] = fuzz.trimf(air_quality.universe, [0, 0, 25])
air_quality['buena'] = fuzz.trimf(air_quality.universe, [0, 25, 50])
air_quality['regular'] = fuzz.trimf(air_quality.universe, [25, 50, 75])
air_quality['mala'] = fuzz.trimf(air_quality.universe, [50, 75, 100])
air_quality['muy_mala'] = fuzz.trimf(air_quality.universe, [75, 100, 100])

# Crear y agregar las reglas difusas
rules = [
    ctrl.Rule(ppm['muy_bajo'], air_quality['excelente']),
    ctrl.Rule(ppm['bajo'], air_quality['buena']),
    ctrl.Rule(ppm['moderado'], air_quality['regular']),
    ctrl.Rule(ppm['alto'], air_quality['mala']),
    ctrl.Rule(ppm['muy_alto'], air_quality['muy_mala'])
]

# Sistema de control y simulación
quality_control = ctrl.ControlSystem(rules)
quality_sim = ctrl.ControlSystemSimulation(quality_control)

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            ppm_value = int(line)
            quality_sim.input['ppm'] = ppm_value
            quality_sim.compute()
            print(f"Calidad del aire estimada: {quality_sim.output['air_quality']:.2f}")
except KeyboardInterrupt:
    print("Programa interrumpido por el usuario")
    ser.close()
