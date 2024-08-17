import pandas as pd

def pre_processing_data(data):

    processed_data = data

    # Replacing all '-' values with NaN

    processed_data = processed_data.replace('-', pd.NA) 

    # Removing all rows with NaN in 'Prato' column

    processed_data = processed_data.dropna(subset=['Prato'])

    # Removing rows with NaN in 'Turno' column

    processed_data = processed_data.dropna(subset=['Turno'])

    # Replacing NaN values in 'Valor R$', 'à Pagar', 'Taxa', 'Frete' columns with 0

    processed_data['Valor R$'] = processed_data['Valor R$'].fillna(0)
    processed_data['à Pagar'] = processed_data['à Pagar'].fillna(0)
    processed_data['Taxa'] = processed_data['Taxa'].fillna(0)
    processed_data['Frete'] = processed_data['Frete'].fillna(0)

    # Replacing 'OK' values in 'pedido_pago' column with 1, and other values with 0

    processed_data['Pago'] = processed_data['Pago'].replace('OK', 1)
    processed_data['Pago'] = processed_data['Pago'].replace(pd.NA, 0)


    # change data types

    processed_data['Data'] = pd.to_datetime(processed_data['Data'], errors='coerce')

    processed_data['Valor R$'] = processed_data['Valor R$'].astype(float, errors='ignore')

    processed_data['à Pagar'] = processed_data['à Pagar'].astype(float, errors='ignore')

    processed_data['Taxa'] = processed_data['Taxa'].astype(float, errors='ignore')

    processed_data['Frete'] = processed_data['Frete'].astype(float, errors='ignore')

    processed_data['Pago'] = processed_data['Pago'].astype(int, errors='ignore')

    # Changing column names
    processed_data = processed_data.rename(columns={
        'Prato': 'prato', 
        'Turno': 'turno', 
        'Data': 'data_venda', 
        'Valor R$': 'valor_prato', 
        'à Pagar': 'valor_pendente', 
        'Taxa': 'valor_adicional', 
        'Frete': 'valor_frete',
        'Pago': 'pedido_pago'})


    return processed_data

if __name__ == '__main__':

    data = pd.read_excel('../data/food_service_data.xlsx', sheet_name= 'vendas_loja')

    processed_data = pre_processing_data(data)

    processed_data.to_csv('../data/outputs/processed_data.csv', index=False, sep=';')




