#Program to convert weight's in lbs to kilograms

weights_in_lbs = list(input('Enter the weights in lbs in comma separated formated: ').split(','))
def lb_to_kilos(weight_in_lbs:list)->list:
    weight_in_kilos = []
    for lbs in weight_in_lbs:
        kgs = int(lbs)*0.453592                     #converting weight in lbs to kgs
        weight_in_kilos.append(round(kgs,2))
    return weight_in_kilos
print(lb_to_kilos(weights_in_lbs))
