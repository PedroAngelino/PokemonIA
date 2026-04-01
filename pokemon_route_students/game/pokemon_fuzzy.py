import numpy as np

from skfuzzy import control as ctrl

# 1. Definição do Universo e Variáveis (Mantendo o que o teu colega fez)
level = ctrl.Antecedent(np.arange(-10, 11, 1), "level")
effect = ctrl.Antecedent(np.arange(0.0, 4.25, 0.25), "effect")
prob = ctrl.Consequent(np.arange(0.0, 1.05, 0.05), "prob")

# 2. Funções de Pertença (Arrays do teu colega)
level["low"] = np.array([1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.5,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
level["medium"] = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.2,0.4,0.6,0.8,1.0,0.8,0.6,0.4,0.2,0.0,0.0,0.0,0.0,0.0,0.0])
level["high"] = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.5,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0])

effect["low"] = np.array([1.0,1.0,1.0,1.0,0.5,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
effect["medium"] = np.array([0.0,0.0,0.0,0.5,1.0,0.5,0.5,0.5,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
effect["high"] = np.array([0.0,0.0,0.0,0.0,0.5,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0])

prob["low"] = np.array([1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.5,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
prob["medium"] = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.2,0.4,0.6,0.8,1.0,0.8,0.6,0.4,0.2,0.0,0.0,0.0,0.0,0.0,0.0])
prob["high"] = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.2,0.4,0.6,0.8,1.0,1.0,1.0,1.0,1.0,1.0])

# 3. Regras (As 9 regras lógicas do teu colega estão ótimas)
rules = [
    ctrl.Rule(level["low"] & effect["low"], prob["low"]),
    ctrl.Rule(level["low"] & effect["medium"], prob["low"]),
    ctrl.Rule(level["low"] & effect["high"], prob["medium"]),
    ctrl.Rule(level["medium"] & effect["low"], prob["low"]),
    ctrl.Rule(level["medium"] & effect["medium"], prob["medium"]),
    ctrl.Rule(level["medium"] & effect["high"], prob["high"]),
    ctrl.Rule(level["high"] & effect["low"], prob["medium"]),
    ctrl.Rule(level["high"] & effect["medium"], prob["high"]),
    ctrl.Rule(level["high"] & effect["high"], prob["high"])
]

# 4. Criação do Sistema de Controlo (Isto faltava para automatizar o cálculo)
prob_ctrl = ctrl.ControlSystem(rules)
prob_sim = ctrl.ControlSystemSimulation(prob_ctrl)

def calculate_prob(level_input, effect_input):
    # Ajustar inputs para os limites do universo (segurança)
    level_input = np.clip(level_input, -10, 10)
    effect_input = np.clip(effect_input, 0, 4)

    # Passar os valores para o simulador
    prob_sim.input['level'] = level_input
    prob_sim.input['effect'] = effect_input

    # Computar o resultado
    prob_sim.compute()

    return prob_sim.output['prob']


