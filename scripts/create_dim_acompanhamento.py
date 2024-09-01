import pandas as pd

def create_column_acompanhamento(data):
    # Create 'acompanhamento' column
    data['acompanhamento'] = data['prato'].str.split('+').str[1]

    # Remove leading/trailing whitespace
    data['acompanhamento'] = data['acompanhamento'].str.strip()

    data['acompanhamento'] = data['acompanhamento'].astype(str).replace({
        'Maionese': str.upper('maionese'),
        'Purê': str.upper('purê de batata'),
        'Batata': str.upper('batata frita'),
        'Salada': str.upper('salada de alface e tomante'),
        'nan': str.upper('sem acompanhamento'),
        'Couve': str.upper('couve'),
        'Batata Corada': str.upper('batata frita'),
        'Batata Frita': str.upper('batata frita'),
        'Mainese': str.upper('maionese'),
        'Salada de Alface e Tomate': str.upper('salada de alface e tomante'),
        'Bastante Macarrão': str.upper('sem acompanhamento'),
        'Aipim': str.upper('aipim frito'),
        'Salada de Legumes': str.upper('salada de legumes'),
        'Linguiça': str.upper('sem acompanhamento'),
        'Batata Frira': str.upper('batata frita'),
        'Couve-Flor': str.upper('salada de couve-flor'),
        'Fritas': str.upper('batata frita'),
        'Purê de batatas': str.upper('purê de batata'),
        'Calabresa': str.upper('sem acompanhamento'),
        'Aipim Frito': str.upper('aipim frito'),
        'Batatinha': str.upper('batatinha palha'),
        'fritas': str.upper('batata frita'),
        'batatinha': str.upper('batatinha palha'),
        'Molho branco': str.upper('molho branco'),
        'maionese': str.upper('maionese'),
        'calabresa':pd.NA,
        'calabresa (meia)': str.upper('sem acompanhamento'),
        'Costela (apenas)': str.upper('sem acompanhamento'),
        'Macarrão': str.upper('sem acompanhamento'),
        'Legumes': str.upper('salada de legumes'),
        'legumes': str.upper('salada de legumes'),
        'aipim': str.upper('aipim frito'),
        'alface e tomate': str.upper('salada de alface e tomante'),
        'purê': str.upper('purê de batata'),
        'salada verde': str.upper('salada de alface e tomante'),
        'Salada verde': str.upper('salada de alface e tomante'),
        'Grelhado': str.upper('sem acompanhamento'),
        'Coca': str.upper('sem acompanhamento'),
        'Salada Verde': str.upper('salada de alface e tomante'),
        'Ovos': str.upper('ovo frito'),
        'fritass': str.upper('batata frita'),
        'legumes -3': str.upper('salada de legumes'),
        'fritas e Calabresa': str.upper('batata frita'),
        'fritas e A. Parmegiana': str.upper('batata frita'),
        'maionesw': str.upper('maionese'),
        'docinhos 2': str.upper('sem acompanhamento'),
        'fritas e parmegiana': str.upper('batata frita'),
        'maiô': str.upper('maionese'),
        'maionese e f. parmê': str.upper('maionese'),
        'fritas e guaraná 350ml': str.upper('batata frita'),
        'maiô e 2-> alcatra': str.upper('maionese'),
        'fritas e coca 350ml': str.upper('batata frita'),
        'maiô e fritas etras e grelhado etra': str.upper('maionese'),
        'maionese e parmê': str.upper('maionese'),
        'fritas , strogonoff e coca 2L': str.upper('batata frita'),
        'fritas , alcatra': str.upper('batata frita'),
        'fritas e 1 parmê': str.upper('batata frita'),
        'fritas e parmê etra': str.upper('batata frita'),
        'fritas, 1-> grelhado': str.upper('batata frita'),
        'maiô e 1-> empanado': str.upper('maionese'),
        'purê e calabresa': str.upper('purê de batata'),
        'fitas e um com maionese': str.upper('maionese'),
        'purê > etra': str.upper('purê de batata'),
        'fritas e alcatra': str.upper('batata frita'),
        'salada': str.upper('salada de alface e tomante'),
        'fritas e outra salaada': str.upper('batata frita'),
        'aipim.': str.upper('aipim frito'),
        '2 etras parmegiana': str.upper('sem acompanhamento'),
        'maionese.': str.upper('maionese'),
        'guaracamp': str.upper('sem acompanhamento'),
        'omelete': str.upper('sem acompanhamento'),
        'fritas e empanada': str.upper('batata frita'),
        'fritas e strogonoff': str.upper('batata frita'),
        'fritas 2': str.upper('batata frita'),
        'salada e parmê': str.upper('salada de alface e tomante'),
        'fritas e parmê': str.upper('batata frita'),
        'fritas e maionese': str.upper('maionese'),
        'legumes e 1 porção de fritas': str.upper('batata frita'),
        'coca 2L': str.upper('sem acompanhamento'),
        'maiô e grelhado': str.upper('maionese'),
        'fritas e a. parmê': str.upper('batata frita'),
        'salada e omelete': str.upper('salada de alface e tomante'),
        'maiÔ': str.upper('maionese'),
        'fritas/maionese e costelinha': str.upper('maionese'),
        'fritas e 2 trufas': str.upper('batata frita'),
        'salada de legume': str.upper('salada de alface e tomante'),
        'maionesa': str.upper('maionese'),
        'legumes/maionese': str.upper('maionese'),
        'fritas e empanado': str.upper('batata frita'),
        'fritas, grelhado': str.upper('batata frita'),
        'batata doce': str.upper('salada de batata doce'),
        'macarrão': str.upper('sem acompanhamento'),
        'fritas.': str.upper('batata frita'),
        'friras': str.upper('batata frita'),
        'legumes e parmê': str.upper('salada de legumes'),
        'coca 350ml': str.upper('sem acompanhamento'),
        'fritas e omelete de queijo': str.upper('batata frita'),
        'fritas , empanado': str.upper('batata frita'),
        'maiô e fanta 350ml': str.upper('maionese'),
        'fritas 3': str.upper('batata frita'),
        'salada, costelinha, parmê': str.upper('salada de alface e tomante'),
        'fritas e guarana 1L': str.upper('batata frita'),
        'fritas e 2 guaracamp': str.upper('batata frita'),
        'beterraba': str.upper('salada de beterraba'),
        'trufa': str.upper('sem acompanhamento'),
        'purê/legumes': str.upper('purê de batata'),
        'legumes e costela': str.upper('salada de legumes'),
        'ovo': str.upper('ovo frito'),
        'fritas e costelinha': str.upper('batata frita'),
        'batatinha palha': str.upper('batatinha palha'),
        '<NA>': str.upper('sem acompanhamento')
    })

    data['acompanhamento'].fillna('SEM ACOMPANHAMENTO', inplace= True)

    return data

def create_dim_acompanhamnento(data):

    data = create_column_acompanhamento(data)

    dim_acompanhamento = pd.DataFrame()

    dim_acompanhamento['acompanhamento'] = sorted(data['acompanhamento'].unique())

    dim_acompanhamento['id_acompanhamento'] = dim_acompanhamento.index + 1

    data = data.merge(dim_acompanhamento, on='acompanhamento', how='left')

    data = data.drop(columns=['acompanhamento'])

    dim_acompanhamento.to_csv('../data/outputs/dim_acompanhamento.csv', index=False, sep=';')

    return data


