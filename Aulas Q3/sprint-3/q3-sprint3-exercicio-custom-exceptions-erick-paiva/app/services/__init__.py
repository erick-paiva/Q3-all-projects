import csv
from msilib.schema import Error
# Importe suas classes de exceções

FILENAME='dados_pessoas.csv'

def read_csv():
    with open(FILENAME) as fp:
        reader = csv.DictReader(fp)
        peoples = list(reader)

    if len(peoples) > 0:
        return peoples
    else:
        raise {"error": "The list is empty!"}

    # Faça o raise do seu erro


def create_people(data_body):
    peoples = read_csv()

    filter_cpf_exists = [people for people in peoples if people['cpf'] == str(data_body['cpf'])]

    if filter_cpf_exists:
        # Faça o raise do seu erro
        
        pass

    fieldnames=['nome', 'idade', 'cpf']
    
    with open(FILENAME, 'a') as fp:
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writerow(data_body)