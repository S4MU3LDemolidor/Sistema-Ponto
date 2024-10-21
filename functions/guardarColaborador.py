import pandas as pd
import json
from datetime import date
import os

def guardar_colaborador():

    arquivo = "json/data.json"
    data = date.today().strftime('%Y-%m-%d')

    with open(arquivo, 'r') as json_file:
        info_existente = json.load(json_file)

    df = pd.DataFrame(info_existente)

    csv_file = f'{data}.csv'
    df.to_csv(csv_file, index=False)
