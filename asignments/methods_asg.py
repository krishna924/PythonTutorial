
fed_tax = 10

state_tax = {
    "texas" : 0,
    "illinois" : 6,
    "new yorck" : 5,
    "ohio" : 3
}


def netIncome (state, gross):
    """
    method should return net income =
    :param state:
    :param gross:
    :return:
    """

    fed_cut = (gross) * (fed_tax/100)
    st_tax = state_tax[state]
    if state_tax == 0:
        state_cut = gross
    else:
        state_cut = (gross) * (st_tax/100)

    net = gross - (fed_cut + state_cut)

    return net

def netIncome_new (state,gross):
    fed_cut_net = gross - (gross *0.1)
    st_tax = state_tax[state]
    if state in state_tax :
        net = fed_cut_net - (fed_cut_net * (st_tax/100))
        print('The net income of '+state+' with gross as '+str(gross)+' is: ')
        return net

a = netIncome('ohio', 100)
a1 = netIncome_new('ohio', 100)
print(a)
print(a1)
b = netIncome('texas', 100)
b1 = netIncome_new('texas', 100)
print(b)
print(b1)