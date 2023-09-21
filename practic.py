
def cost_delivery(quantity, *_, discount=0):
    result = (5 + 2 * (quantity - 1)) * (1 - discount)
    return result
print(cost_delivery(2, 1, 2, 3, discount=0.5))