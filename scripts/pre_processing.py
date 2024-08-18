import pandas as pd
import create_dim_prato as dim_prato

def pre_processing_data(data):

    pre_processed_data = data

    # Replacing all '-' values with NaN

    pre_processed_data = pre_processed_data.replace('-', pd.NA) 

    # Removing all rows with NaN in 'Prato' column

    pre_processed_data = pre_processed_data.dropna(subset=['Prato'])

    # Removing rows with NaN in 'Turno' column

    pre_processed_data = pre_processed_data.dropna(subset=['Turno'])

    # Replacing NaN values in 'Valor R$', 'à Pagar', 'Taxa', 'Frete' columns with 0

    pre_processed_data['Valor R$'] = pre_processed_data['Valor R$'].fillna(0)
    pre_processed_data['à Pagar'] = pre_processed_data['à Pagar'].fillna(0)
    pre_processed_data['Taxa'] = pre_processed_data['Taxa'].fillna(0)
    pre_processed_data['Frete'] = pre_processed_data['Frete'].fillna(0)

    # Replacing 'OK' values in 'pedido_pago' column with 1, and other values with 0

    pre_processed_data['Pago'] = pre_processed_data['Pago'].replace('OK', 1)
    pre_processed_data['Pago'] = pre_processed_data['Pago'].replace(pd.NA, 0)


    # change data types

    pre_processed_data['Data'] = pd.to_datetime(pre_processed_data['Data'], errors='coerce')

    pre_processed_data['Valor R$'] = pd.to_numeric(pre_processed_data['Valor R$'], errors= 'coerce').fillna(0)

    pre_processed_data['à Pagar'] = pd.to_numeric(pre_processed_data['à Pagar'], errors= 'coerce')

    pre_processed_data['Taxa'] = pd.to_numeric(pre_processed_data['Taxa'], errors= 'coerce')

    pre_processed_data['Frete'] = pd.to_numeric(pre_processed_data['Frete'], errors= 'coerce')

    pre_processed_data['Pago'] = pd.to_numeric(pre_processed_data['Pago'], errors= 'coerce')

    # Changing column names
    pre_processed_data = pre_processed_data.rename(columns={
        'Prato': 'prato', 
        'Turno': 'turno', 
        'Data': 'data_venda', 
        'Valor R$': 'valor_prato', 
        'à Pagar': 'valor_pendente', 
        'Taxa': 'valor_adicional', 
        'Frete': 'valor_frete',
        'Pago': 'pedido_pago'})
    
    # Creating dimension 'prato'
    pre_processed_data = dim_prato.create_dim_prato(pre_processed_data)

    return pre_processed_data

if __name__ == '__main__':

    data = pd.read_excel('../data/food_service_data.xlsx', sheet_name= 'vendas_loja')

    processed_data = pre_processing_data(data)

    processed_data.to_csv('../data/outputs/processed_data.csv', index=False, sep=';')




