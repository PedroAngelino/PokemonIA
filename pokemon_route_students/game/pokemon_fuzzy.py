import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

'''
Cria um sistema Fuzzy que recebe como input a diferença dos niveis
e o efeito do ataque e devolve como input a probabilidade de ganhar
'''

def calculate_prob(level_input, effect_input):
    # TO DO
    l_pos = np.where(level.universe == level_input)[0][0]
    l_low = level["low"].mf[l_pos]
    l_medium = level["medium"].mf[l_pos]
    l_high = level["high"].mf[l_pos]
    e_pos = np.where(effect.universe == effect_input)[0][0]
    e_low = effect["low"].mf[e_pos]
    e_medium = effect["medium"].mf[e_pos]
    e_high = effect["high"].mf[e_pos]


    rule1_and = min(l_low,e_low)
    rule2_and = min(l_low,e_medium)
    rule3_and = min(l_low,e_high)
    rule4_and = min(l_medium,e_low)
    rule5_and = min(l_medium,e_medium)
    rule6_and = min(l_medium,e_high)
    rule7_and = min(l_high,e_low)
    rule8_and = min(l_high,e_medium)
    rule9_and = min(l_high,e_high)
    #rule2_or = max(l_low,e_low)
    #rule3_and = min(l_medium,e_medium)


    #low_activation = np.minimum(rule1_and, prob["low"].mf)
    #medium_activation = np.minimum(rule2_or, prob["medium"].mf)

    #low_activation = np.minimum(rule1_and, rule2_and, rule4_and, prob["low"].mf)
    #medium_activation = np.minimum(rule3_and, rule5_and, rule7_and, prob["medium"].mf)
    #high_activation = np.minimum(rule6_and, rule8_and, rule9_and, prob["high"].mf)

    low_agg = np.maximum(rule1_and, np.maximum(rule2_and, rule4_and))
    low_activation = np.minimum(low_agg, prob["low"].mf)
    medium_agg = np.maximum(rule3_and, np.maximum(rule5_and, rule7_and))
    medium_activation = np.minimum(medium_agg, prob["medium"].mf)
    high_agg = np.maximum(rule6_and, np.maximum(rule8_and, rule9_and))
    high_activation = np.minimum(high_agg, prob["high"].mf)


    aggregated =np.maximum(low_activation, np.maximum(medium_activation, high_activation))


    prob_output = fuzz.defuzz(
        prob.universe,
        aggregated,
        "centroid"
    )
    
    return prob_output



#forma correta de level
#level = ctrl.Antecedent(np.arange(-100,101,1), "level")

level = ctrl.Antecedent(np.arange(-10,11,1), "level")
#effect = ctrl.Antecedent([0,0.25,0.5,1,2,4], "effect")
effect = ctrl.Antecedent(np.arange(0.0,4.25,0.25), "effect")

prob = ctrl.Consequent(np.arange(0.0,1.05,0.05), "prob")

#effect["low"] = np.array([1.0,1.0,0.8,0.5,0.0,0.0])

level["low"] = np.array([1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.5,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
level["medium"] = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.2,0.4,0.6,0.8,1.0,0.8,0.6,0.4,0.2,0.0,0.0,0.0,0.0,0.0,0.0])
level["high"] = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.5,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0])

effect["low"] = np.array([1.0,1.0,1.0,1.0,0.5,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,])
effect["medium"] = np.array([0.0,0.0,0.0,0.5,1.0,0.5,0.5,0.5,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,])
effect["high"] = np.array([0.0,0.0,0.0,0.0,0.5,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,])

prob["low"] = np.array([1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.5,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

prob["medium"] = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.2,0.4,0.6,0.8,1.0,0.8,0.6,0.4,0.2,0.0,0.0,0.0,0.0,0.0,0.0])

prob["high"] = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.2,0.4,0.6,0.8,1.0,1.0,1.0,1.0,1.0,1.0])



#low & low = low
rule1 = ctrl.Rule(
    level["low"] & effect["low"],
    prob["low"]
)
rule2 = ctrl.Rule(
    level["low"] & effect["medium"],
    prob["low"]
)
rule3 = ctrl.Rule(
    level["low"] & effect["high"],
    prob["medium"]
)
rule4 = ctrl.Rule(
    level["medium"] & effect["low"],
    prob["low"]
)
rule5 = ctrl.Rule(
    level["medium"] & effect["medium"],
    prob["medium"]
)
rule6 = ctrl.Rule(
    level["medium"] & effect["high"],
    prob["high"]
)
rule7 = ctrl.Rule(
    level["high"] & effect["low"],
    prob["medium"]
)
rule8 = ctrl.Rule(
    level["high"] & effect["medium"],
    prob["high"]
)
rule9 = ctrl.Rule(
    level["high"] & effect["high"],
    prob["high"]
)



