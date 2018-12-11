import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import Tkinter as Tk
import matplotlib.pyplot as plt


rigidity = ctrl.Antecedent(np.arange(0, 11, 1), 'rigidity')
weight = ctrl.Antecedent(np.arange(0, 11, 1), 'weight')
force = ctrl.Consequent(np.arange(0, 26, 1), 'force')

rigidity.automf(5)
weight.automf(5)

force['low'] = fuzz.trimf(force.universe, [0, 0, 13])
force['medium'] = fuzz.trimf(force.universe, [0, 13, 25])
force['high'] = fuzz.trimf(force.universe, [13, 25, 25])

# rigidity['average'].view()
# weight.view()
# force.view()

rule1 = ctrl.Rule(rigidity['poor'] | weight['poor'], force['low'])
rule2 = ctrl.Rule(weight['average'], force['medium'])
rule3 = ctrl.Rule(weight['good'] | rigidity['good'], force['high'])
# rule1.view()

gripping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
gripping = ctrl.ControlSystemSimulation(gripping_ctrl)


# gripping.input['rigidity'] = 3
# gripping.input['weight'] = 2
# gripping.compute()
# gripping.output['force']
# force.view(sim=gripping)
#
# gripping.input['rigidity'] = 4
# gripping.input['weight'] = 6
# gripping.compute()
# gripping.output['force']
# force.view(sim=gripping)
#
# gripping.input['rigidity'] = 8
# gripping.input['weight'] = 10
# gripping.compute()
# gripping.output['force']
# force.view(sim=gripping)

# =============== experiment ===============

for rigidity_fixed in range(1, 10):
    x_rigidity = []
    y_rigidity = []
    for weight_current in range(1, 10):
        gripping.input['rigidity'] = rigidity_fixed
        gripping.input['weight'] = weight_current
        gripping.compute()
        x_rigidity.append(weight_current)
        y_rigidity.append(gripping.output['force'])
    plt.plot(x_rigidity, y_rigidity, label=rigidity_fixed)

plt.xlabel('rigidity')
plt.ylabel('force')
plt.legend()
plt.show()


# Tk.mainloop()
