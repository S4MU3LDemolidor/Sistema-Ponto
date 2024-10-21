import json
import pandas as pd

def puxar_colaborador(nome, csv):

    df = pd.read_csv(csv)

    json_data = df.to_json(orient='records')

    info_existente = json.loads(json_data)

    for colaborador in info_existente:
        if colaborador["nome_colaborador"] == nome:
            entrada_horario = colaborador['informacao']['horario']
            entrada_tipo = colaborador['informacao']['tipo']
            saida_horario = colaborador['info']['horario']
            saida_tipo = colaborador['info']['tipo']
            return (f"Nome: {colaborador['nome_colaborador']}, "
                    f"Entrada: {entrada_horario} ({entrada_tipo}), "
                    f"Saída: {saida_horario} ({saida_tipo})")

puxar_colaborador('Samuel', '2024-10-21.csv')