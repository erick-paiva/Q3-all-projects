
def corresponding_parenthesis(text):
    return ")" * (text.count(")") - text.count("(")) if text.count(")") - text.count("(") > 0 else "(" * (text.count("(") - text.count(")"))

def remove_more_than_two_repetitions(text):
    text = list(text); i = 0
    while i < len(text)-2:
        if text[i] == text[i+1] and text[i] == text[i+2]: text.pop(i); i -= 1
        i += 1
    return "".join(text)

print(remove_more_than_two_repetitions("aaaabbbbaacaaaxxxxii"))