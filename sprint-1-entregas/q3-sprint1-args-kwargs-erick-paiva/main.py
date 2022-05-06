def sum_numbers(*args):
    return sum(list(args))

print(sum_numbers(*[1, 2, 3, 4, 5, 6]))

def get_multiplied_amount(multiplier, *args):
    return multiplier * sum(list(args))

def word_concatenator(*args):
    return " ".join(list(args))


def inverted_word_factory(*args):
    return " ".join(list(args))[::-1]

print(inverted_word_factory(*"eae", "amigão", "belezinha?"))

def dictionary_separator(**kwargs):
    return ([*kwargs.keys()], [*kwargs.values()])

def dictionary_creator(*args, **kwargs):
    if len(args) < len(kwargs): return None
    return { args[i] : list(kwargs.values())[i] for i in range(len(list(kwargs.values())))   }

def purchase_logger(**kwargs):
    desc = ["Product", "costs", "and was bought"]
    return " ".join([f"{desc[i]} {list(kwargs.values())[i]}" for i in range(len(kwargs.values()))])

def world_cup_logger(country, *args):
    args = sorted(list(args))
    return f'{country} - {" ".join([ f"{list(args)[i]}," if i < len(list(args))-2 else f"{list(args)[i]} e {list(args)[i+1]}" for i in range(len(list(args))-1)])}'
 
