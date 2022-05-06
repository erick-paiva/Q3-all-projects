
def standardize_names(character_name):
    character_name = character_name.strip().split()
    nomes_compostos = [p for p in character_name if p[0] == p[0].upper()]
    return "-".join(nomes_compostos) if len(nomes_compostos) > 0 else "".join(character_name)

def standardize_title(title):
    return " ".join([texto.capitalize() for texto in title.split()])

def standardize_text(text):
    text = text.split()
    return """ """.join([text[i].capitalize()
    if text[i-1][-1] == "." or i == 0 else text[i]
    for i in range(len(text))])
    
def title_creator(text):
    return f"{'-'*20}{' '.join([palavra.capitalize() for palavra in text.split()])}{'-'*20}"

def text_merge(text_of_blog_a, text_of_blog_b):
    text_of_blog_a = " ".join(text_of_blog_a.split())
    text_of_blog_b = " ".join(text_of_blog_b.split())
    text_of_blog_b = f"{text_of_blog_b[0].lower()}{text_of_blog_b[1:]}"
    if text_of_blog_a[-1] == ".": text_of_blog_a = text_of_blog_a[:-1]
    return standardize_text(" ".join([*text_of_blog_a.split(), *text_of_blog_b.split()]))
