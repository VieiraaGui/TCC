#!/usr/bin/env python
# coding: utf-8

# In[119]:


import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl



#  Definição dos ranges


processador = ctrl.Antecedent(np.arange(0, 5), 'processador')
placaVideo = ctrl.Antecedent(np.arange(0, 5), 'placaVideo')
ram = ctrl.Antecedent(np.arange(0, 32), 'ram')

desempenho = ctrl.Consequent(np.arange(0, 7), 'desempenho')


# Definição dos valores dos conjuntos de entrada

processador['baixo'] = fuzz.trapmf(processador.universe, [0, 0, 1, 1.5])
processador['medioBaixo'] = fuzz.trapmf(processador.universe, [1, 1.5, 2, 2.5])
processador['medio'] = fuzz.trapmf(processador.universe, [2, 2.5, 3, 3.5])
processador['medioAlto'] = fuzz.trapmf(processador.universe, [3, 3.5, 4, 4.5])
processador['alto'] = fuzz.trapmf(processador.universe, [4, 4.5, 5, 5])
processador.view()

placaVideo['baixo'] = fuzz.trapmf(placaVideo.universe,  [0, 0, 1, 1.5])
placaVideo['medioBaixo'] = fuzz.trapmf(placaVideo.universe,  [1, 1.5, 2, 2.5])
placaVideo['medio'] = fuzz.trapmf(placaVideo.universe,  [2, 2.5, 3, 3.5])
placaVideo['medioAlto'] = fuzz.trapmf(placaVideo.universe,  [3, 3.5, 4, 4.5])
placaVideo['alto'] = fuzz.trapmf(placaVideo.universe,  [4, 4.5, 5, 5])
placaVideo.view()

ram['baixo'] = fuzz.trapmf(ram.universe, [0, 0, 4, 8])
ram['medio'] = fuzz.trapmf(ram.universe, [6, 8, 10, 12])
ram['alto'] = fuzz.trapmf(ram.universe, [10, 12, 32, 32])
ram.view()


# Definição dos valores dos conjuntos de saída


desempenho['alto'] = fuzz.trapmf(desempenho.universe,  [0, 0, 1, 1.5])
desempenho['medioAlto'] = fuzz.trapmf(desempenho.universe,  [1, 1.5, 2, 2.5])
desempenho['medio'] = fuzz.trapmf(desempenho.universe,  [2, 2.5, 3, 3.5])
desempenho['medioBaixo'] = fuzz.trapmf(desempenho.universe,  [3, 3.5, 4, 4.5])
desempenho['baixo'] = fuzz.trapmf(desempenho.universe,  [4, 4.5, 7, 7])
desempenho.view()


# Regras de inferência


regra1 = ctrl.Rule(processador['baixo'] & ram['baixo'] & placaVideo['baixo'], desempenho['baixo']  )
regra2 = ctrl.Rule(processador['baixo'] & ram['baixo'] & placaVideo['medioBaixo'], desempenho['baixo']  )
regra3 = ctrl.Rule(processador['baixo'] & ram['baixo'] & placaVideo['medio'], desempenho['baixo']  )
regra4 = ctrl.Rule(processador['baixo'] & ram['baixo'] & placaVideo['medioAlto'], desempenho['baixo']  )
regra5 = ctrl.Rule(processador['baixo'] & ram['baixo'] & placaVideo['alto'], desempenho['baixo']  )
regra6 = ctrl.Rule(processador['baixo'] & ram['medio'] & placaVideo['baixo'], desempenho['baixo']  )
regra7 = ctrl.Rule(processador['baixo'] & ram['medio'] & placaVideo['medioBaixo'], desempenho['medioBaixo']  )
regra8 = ctrl.Rule(processador['baixo'] & ram['medio'] & placaVideo['medio'], desempenho['medioBaixo']  )
regra9 = ctrl.Rule(processador['baixo'] & ram['medio'] & placaVideo['medioAlto'], desempenho['medioBaixo']  )
regra10 = ctrl.Rule(processador['baixo'] & ram['medio'] & placaVideo['alto'], desempenho['medioBaixo']  )
regra11 = ctrl.Rule(processador['baixo'] & ram['alto'] & placaVideo['baixo'], desempenho['baixo']  )
regra12 = ctrl.Rule(processador['baixo'] & ram['alto'] & placaVideo['medioBaixo'], desempenho['medioBaixo']  )
regra13 = ctrl.Rule(processador['baixo'] & ram['alto'] & placaVideo['medio'], desempenho['medioBaixo']  )
regra14 = ctrl.Rule(processador['baixo'] & ram['alto'] & placaVideo['medioAlto'], desempenho['medioBaixo']  )
regra15 = ctrl.Rule(processador['baixo'] & ram['alto'] & placaVideo['alto'], desempenho['medioBaixo']  )

regra16 = ctrl.Rule(processador['medioBaixo'] & ram['baixo'] & placaVideo['baixo'], desempenho['baixo']  )
regra17 = ctrl.Rule(processador['medioBaixo'] & ram['baixo'] & placaVideo['medioBaixo'], desempenho['baixo']  )
regra18 = ctrl.Rule(processador['medioBaixo'] & ram['baixo'] & placaVideo['medio'], desempenho['baixo']  )
regra19 = ctrl.Rule(processador['medioBaixo'] & ram['baixo'] & placaVideo['medioAlto'], desempenho['baixo']  )
regra20 = ctrl.Rule(processador['medioBaixo'] & ram['baixo'] & placaVideo['alto'], desempenho['baixo']  )
regra21 = ctrl.Rule(processador['medioBaixo'] & ram['medio'] & placaVideo['baixo'], desempenho['baixo']  )
regra22 = ctrl.Rule(processador['medioBaixo'] & ram['medio'] & placaVideo['medioBaixo'], desempenho['medioBaixo']  )
regra23 = ctrl.Rule(processador['medioBaixo'] & ram['medio'] & placaVideo['medio'], desempenho['medioBaixo']  )
regra24 = ctrl.Rule(processador['medioBaixo'] & ram['medio'] & placaVideo['medioAlto'], desempenho['medioBaixo']  )
regra25 = ctrl.Rule(processador['medioBaixo'] & ram['medio'] & placaVideo['alto'], desempenho['medioBaixo']  )
regra26 = ctrl.Rule(processador['medioBaixo'] & ram['alto'] & placaVideo['baixo'], desempenho['baixo']  )
regra27 = ctrl.Rule(processador['medioBaixo'] & ram['alto'] & placaVideo['medioBaixo'], desempenho['medioBaixo']  )
regra28 = ctrl.Rule(processador['medioBaixo'] & ram['alto'] & placaVideo['medio'], desempenho['medioBaixo']  )
regra29 = ctrl.Rule(processador['medioBaixo'] & ram['alto'] & placaVideo['medioAlto'], desempenho['medioBaixo']  )
regra30 = ctrl.Rule(processador['medioBaixo'] & ram['alto'] & placaVideo['alto'], desempenho['medioBaixo']  )

regra31 = ctrl.Rule(processador['medio'] & ram['baixo'] & placaVideo['baixo'], desempenho['baixo']  )
regra32 = ctrl.Rule(processador['medio'] & ram['baixo'] & placaVideo['medioBaixo'], desempenho['baixo']  )
regra33 = ctrl.Rule(processador['medio'] & ram['baixo'] & placaVideo['medio'], desempenho['baixo']  )
regra34 = ctrl.Rule(processador['medio'] & ram['baixo'] & placaVideo['medioAlto'], desempenho['baixo']  )
regra35 = ctrl.Rule(processador['medio'] & ram['baixo'] & placaVideo['alto'], desempenho['baixo']  )
regra36 = ctrl.Rule(processador['medio'] & ram['medio'] & placaVideo['baixo'], desempenho['baixo']  )
regra37 = ctrl.Rule(processador['medio'] & ram['medio'] & placaVideo['medioBaixo'], desempenho['medioBaixo']  )
regra38 = ctrl.Rule(processador['medio'] & ram['medio'] & placaVideo['medio'], desempenho['medio']  )
regra39 = ctrl.Rule(processador['medio'] & ram['medio'] & placaVideo['medioAlto'], desempenho['medio']  )
regra40 = ctrl.Rule(processador['medio'] & ram['medio'] & placaVideo['alto'], desempenho['medio']  )
regra41 = ctrl.Rule(processador['medio'] & ram['alto'] & placaVideo['baixo'], desempenho['baixo']  )
regra42 = ctrl.Rule(processador['medio'] & ram['alto'] & placaVideo['medioBaixo'], desempenho['medioBaixo']  )
regra43 = ctrl.Rule(processador['medio'] & ram['alto'] & placaVideo['medio'], desempenho['medio']  )
regra44 = ctrl.Rule(processador['medio'] & ram['alto'] & placaVideo['medioAlto'], desempenho['medio']  )
regra45 = ctrl.Rule(processador['medio'] & ram['alto'] & placaVideo['alto'], desempenho['medio']  )

regra46 = ctrl.Rule(processador['medioAlto'] & ram['baixo'] & placaVideo['baixo'], desempenho['baixo']  )
regra47 = ctrl.Rule(processador['medioAlto'] & ram['baixo'] & placaVideo['medioBaixo'], desempenho['baixo']  )
regra48 = ctrl.Rule(processador['medioAlto'] & ram['baixo'] & placaVideo['medio'], desempenho['baixo']  )
regra49 = ctrl.Rule(processador['medioAlto'] & ram['baixo'] & placaVideo['medioAlto'], desempenho['baixo']  )
regra50 = ctrl.Rule(processador['medioAlto'] & ram['baixo'] & placaVideo['alto'], desempenho['baixo']  )
regra51 = ctrl.Rule(processador['medioAlto'] & ram['medio'] & placaVideo['baixo'], desempenho['baixo']  )
regra52 = ctrl.Rule(processador['medioAlto'] & ram['medio'] & placaVideo['medioBaixo'], desempenho['medioBaixo']  )
regra53 = ctrl.Rule(processador['medioAlto'] & ram['medio'] & placaVideo['medio'], desempenho['medioAlto']  )
regra54 = ctrl.Rule(processador['medioAlto'] & ram['medio'] & placaVideo['medioAlto'], desempenho['medioAlto']  )
regra55 = ctrl.Rule(processador['medioAlto'] & ram['medio'] & placaVideo['alto'], desempenho['medioAlto']  )
regra56 = ctrl.Rule(processador['medioAlto'] & ram['alto'] & placaVideo['baixo'], desempenho['baixo']  )
regra57 = ctrl.Rule(processador['medioAlto'] & ram['alto'] & placaVideo['medioBaixo'], desempenho['medio']  )
regra58 = ctrl.Rule(processador['medioAlto'] & ram['alto'] & placaVideo['medio'], desempenho['medioAlto']  )
regra59 = ctrl.Rule(processador['medioAlto'] & ram['alto'] & placaVideo['medioAlto'], desempenho['medioAlto']  )
regra60 = ctrl.Rule(processador['medioAlto'] & ram['alto'] & placaVideo['alto'], desempenho['medioAlto']  )

regra61 = ctrl.Rule(processador['alto'] & ram['baixo'] & placaVideo['baixo'], desempenho['baixo']  )
regra62 = ctrl.Rule(processador['alto'] & ram['baixo'] & placaVideo['medioBaixo'], desempenho['baixo']  )
regra63 = ctrl.Rule(processador['alto'] & ram['baixo'] & placaVideo['medio'], desempenho['baixo']  )
regra64 = ctrl.Rule(processador['alto'] & ram['baixo'] & placaVideo['medioAlto'], desempenho['baixo']  )
regra65 = ctrl.Rule(processador['alto'] & ram['baixo'] & placaVideo['alto'], desempenho['baixo']  )
regra66 = ctrl.Rule(processador['alto'] & ram['medio'] & placaVideo['baixo'], desempenho['baixo']  )
regra67 = ctrl.Rule(processador['alto'] & ram['medio'] & placaVideo['medioBaixo'], desempenho['medioAlto']  )
regra68 = ctrl.Rule(processador['alto'] & ram['medio'] & placaVideo['medio'], desempenho['alto']  )
regra69 = ctrl.Rule(processador['alto'] & ram['medio'] & placaVideo['medioAlto'], desempenho['alto']  )
regra70 = ctrl.Rule(processador['alto'] & ram['medio'] & placaVideo['alto'], desempenho['alto']  )
regra71 = ctrl.Rule(processador['alto'] & ram['alto'] & placaVideo['baixo'], desempenho['baixo']  )
regra72 = ctrl.Rule(processador['alto'] & ram['alto'] & placaVideo['medioBaixo'], desempenho['alto']  )
regra73 = ctrl.Rule(processador['alto'] & ram['alto'] & placaVideo['medio'], desempenho['alto']  )
regra74 = ctrl.Rule(processador['alto'] & ram['alto'] & placaVideo['medioAlto'], desempenho['alto']  )
regra75 = ctrl.Rule(processador['alto'] & ram['alto'] & placaVideo['alto'], desempenho['alto']  )


# Sistema de controle de regras


tipping_ctrl = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9,
regra10, regra11, regra12, regra13, regra14, regra15, regra16, regra17, regra18, regra19, regra20, regra21,
regra22, regra23, regra24, regra25, regra26, regra27, regra28, regra29, regra30,regra31,regra32,regra33,
regra34,regra35,regra36,regra37,regra38,regra39,regra40,regra41,regra42,regra43,regra44,regra45,regra46,
regra47,regra48,regra49,regra50,regra51,regra52,regra53,regra54,regra55,regra56,regra57,regra58,regra59,
regra60,regra61,regra62,regra63,regra64,regra65,regra66,regra67,regra68,regra69,regra70,regra71,regra72,
regra73,regra74,regra75])

tipping = ctrl.ControlSystemSimulation(tipping_ctrl)


# Valores de entrada


tipping.input['processador'] = 2
tipping.input['placaVideo'] = 3
tipping.input['ram'] = 8

tipping.compute()


# Saída


print(tipping.output['desempenho'])
desempenho.view(sim=tipping)





