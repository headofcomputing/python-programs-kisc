#assign rate
rateBurger=500
ratePizza=2500

#get number of burgers and pizzas from the user
orderBurger=int(input("how many burger"))
orderPizza=int(input("how many Pizza?"))


#calculate the total by multiplying order and rate of each
total=orderBurger * rateBurger + orderPizza * ratePizza

#if total is over 5000, print elligible. Else, print not elligible.
if(total > 5000):

    print("Your total is", total)
    print("You are elligible for discount!")

else:

    print("Your total is", total)
    print("You are not elligible for discount!")

