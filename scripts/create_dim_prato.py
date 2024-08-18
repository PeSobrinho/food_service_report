import pandas as pd

def create_column_quantidade(data):
    
    data['prato'] = data['prato'].str.replace('x', '', regex= False)

    data['quantidade'] = data['prato'].str.split().str[0]

    data['quantidade'] = data['quantidade'].replace({
        '-': '',
        '>': '',
        '1/2': '0.5',
        'parmê': '',
        '->': ''
    }, regex= True)

    data['quantidade'] = pd.to_numeric(data['quantidade'], errors= 'coerce').fillna(1)

    data['valor_prato'] = data['valor_prato']/data['quantidade']

    return data

def create_dim_prato(data):
    
    data = create_column_quantidade(data)

    return data



