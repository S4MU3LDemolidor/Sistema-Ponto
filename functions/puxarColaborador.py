import json
import pandas as pd
import ast

def puxar_colaborador(nome, csv):

    df = pd.read_csv(csv)

    json_data = df.to_json(orient='records')

    info_existente = json.loads(json_data)

    for colaborador in info_existente:

        colaborador['informacao'] = ast.literal_eval(colaborador['informacao'])
        colaborador['info'] = ast.literal_eval(colaborador['info'])

        if colaborador["nome_colaborador"] == nome:
            entrada_horario = colaborador['informacao']['horario']
            saida_horario = colaborador['info']['horario']
            return (f"Nome: {colaborador['nome_colaborador']}, "
                    f"Entrada: {entrada_horario}, "
                    f"Saída: {saida_horario}")
