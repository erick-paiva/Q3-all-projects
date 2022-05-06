def loose_change(cents):
    print(cents)
    quarters = 0
    nickels = 0
    dimes = 0
    pennies = 0
    
    while cents > 0 :
        if cents - 1 > 0:
            cents -= 1
            pennies+=1
        if cents - 5 > 0:
            cents -= 5
            nickels += 1
        if cents - 10 > 0:
            cents -= 10
            dimes+=1
        if cents - 25 > 0:
            cents -= 25
            quarters+=1
 
    resultado = {'Nickels': nickels, 'Pennies': pennies, 'Dimes': dimes, 'Quarters': quarters} 
    print(resultado)
    
loose_change(56)

# {'Nickels': 1, 'Pennies': 1, 'Dimes': 0, 'Quarters': 2}