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

def create_colunm_prato_principal(data):

    # Create 'prato_principal' column
    data['prato_principal'] = data['prato'].str.split('+').str[0]

    # Remove leading/trailing whitespace
    data['prato_principal'] = data['prato_principal'].str.strip()

    # Remove quantities and special characters from the beginning of 'prato_principal'
    data['prato_principal'] = data['prato_principal'].str.replace(r'^(\d+(\s*\/\s*\d+)?|\d+\/\d+|\-|\->|>)\s*', '', regex=True)

    # Remove any remaining leading/trailing whitespace
    data['prato_principal'] = data['prato_principal'].str.strip()

    data['prato_principal'] = data['prato_principal'].replace({
        '-':'',
        '->':'',
        '>':'',
    }, regex=True).str.strip()

    data['prato_principal'] = data['prato_principal'].replace({
        '*****': pd.NA,
        '******': pd.NA,
        'A. Parmegiana': str.upper('alcatra parmegiana'),
        'A. empanada': str.upper('alcatra empanada'),
        'A. paremegiana': str.upper('alcatra parmegiana'),
        'A. parmegiana': str.upper('alcatra parmegiana'),
        'Aipim': str.upper('porção de aipim'),
        'Alcatra': str.upper('alcatra acebolada'),
        'Alcatra (parmegiana)': str.upper('alcatra parmegiana'),
        'Alcatra a parmegiana': str.upper('alcatra parmegiana'),
        'Alcatra acebolada': str.upper('alcatra acebolada'),
        'Alcatra parmegiana': str.upper('alcatra parmegiana'),
        'Almôndega': str.upper('almôdega'),
        'Batata Frita': str.upper('porção de batata frita'),
        'Bife': str.upper('alcatra acebolada'),
        'Bife a Parmegiana': str.upper('alcatra parmegiana'),
        'Bife a rolé carne': str.upper('bife a rolé bovino'),
        'Bife a rolé frango': str.upper('bife a rolé frango'),
        'Bife de Alcatra': str.upper('alcatra acebolada'),
        'Bife de Alcatra a Parmegiana': str.upper('alcatra parmegiana'),
        'Bife à Rolé': str.upper('bife a rolé bovino'),
        'Bolo de pote':pd.NA,
        'Bolonhesa': str.upper('macarrão a bolonhesa'),
        'Calabresa': str.upper('calabresa acebolada'),
        'Calabresa Acebolada': str.upper('calabresa acebolada'),
        'Calabresas': str.upper('calabresa acebolada'),
        'Carne Assada': str.upper('carne assada'),
        'Carne Assada com Molho': str.upper('carne assada'),
        'Carne Asssada': str.upper('carne assada'),
        'Carne Picadinha': str.upper('carne assada'),
        'Carne ao molho': str.upper('carne assada'),
        'Carne assada': str.upper('carne assada'),
        'Carne de Panela': str.upper('carne de panela'),
        'Carne de panela': str.upper('carne de panela'),
        'Carne moída': str.upper('carne moída'),
        'Carre': str.upper('carré suíno'),
        'Carré': str.upper('carré suíno'),
        'Carré etra': str.upper('carré suíno'),
        'Coca 2,0L': pd.NA,
        'Coca 2,5L': pd.NA,
        'Coca 2L': pd.NA,
        'Coca 350ml': pd.NA,
        'CocaCola 2,5L': pd.NA,
        'CocaCola 2L': pd.NA,
        'CocaCola Lata': pd.NA,
        'Costela': str.upper('costelinha suína'),
        'Costelinha': str.upper('costelinha suína'),
        'Costelinha Frita': str.upper('costelinha suína'),
        'Cubinho Emanado': str.upper('cubinho de frango empanado'),
        'Drumet': str.upper('drumet de frango'),
        'Empanada': str.upper('filé de frango empanado'),
        'Empanado': str.upper('filé de frango empanado'),
        'Empanado (etra)': str.upper('filé de frango empanado unidade'),
        'Empanado (unidade)': str.upper('filé de frango empanado unidade'),
        'Empanado de frango': str.upper('filé de frango empanado'),
        'Empanadp (só)': str.upper('filé de frango empanado'),
        'Ensopado': str.upper('frango ensopado'),
        'Ensopado de Frango': str.upper('frango ensopado'),
        'Ensopado de frango': str.upper('frango ensopado'),
        'Estrogonofe': str.upper('strogonoff de frango'),
        'Estrogonofe de Carne': str.upper('strogonoff de carne'),
        'Estrogonofe de Carne (completo)': str.upper('strogonoff de carne'),
        'Etras': pd.NA,
        'F. de panela': str.upper('frango ensopado'),
        'Fanta 2 Lt.': pd.NA,
        'Fanta 2L': pd.NA,
        'Fanta 350ml': pd.NA,
        'Fanta Uva 2L': pd.NA,
        'Fanta Uva 350ml': pd.NA,
        'Fanta guaraná 350ml': pd.NA,
        'Feijoada': str.upper('feijoada'),
        'Feijão': str.upper('feijão unidade'),
        'Filé de Frango Empanado': str.upper('filé de frango empanado'),
        'Frando ensopado': str.upper('frango ensopado'),
        'Frango': str.upper('filé de frango empanado'),
        'Frango Empanado': str.upper('filé de frango empanado'),
        'Frango Grelhado': str.upper('filé de frango grelhado'),
        'Frango Parmegiana': str.upper('frango a parmegiana'),
        'Frango a parmegiana': str.upper('frango a parmegiana'),
        'Frango ao Molho': str.upper('frango ensopado'),
        'Frango empanado': str.upper('filé de frango empanado'),
        'Frango ensopado': str.upper('frango ensopado'),
        'Frangos Empanados': str.upper('filé de frango empanado'),
        'Frangos a parmegiana': str.upper('frango a parmegiana'),
        'Fritas': str.upper('porção de batata frita'),
        'Gorjäoes de Frango': str.upper('Gorjão de Frango'),
        'Grelhado': str.upper('filé de frango grelhado'),
        'Guaracamp': pd.NA,
        'Guaracamps': pd.NA,
        'Guaraná 350ml': pd.NA,
        'Kaut 2L': pd.NA,
        'Kuat 2L': pd.NA,
        'Kuat 2l': pd.NA,
        'Lasanha': pd.NA,
        'Liguiça Acebolada': str.upper('calabresa acebolada'),
        'Linguiça': str.upper('calabresa acebolada'),
        'Linguiça Acebolada': str.upper('calabresa acebolada'),
        'Lombo': str.upper('lombo suíno'),
        'Macarrão': str.upper('macarrão a bolonhesa'),
        'Macarrão à Bolonhesa': str.upper('macarrão a bolonhesa'),
        'Mouse Chocolate c/Maracujá': pd.NA,
        'Mousse': pd.NA,
        'Nuggets': str.upper('Nuggets'),
        'P. Calabresa': str.upper('calabresa acebolada'),
        'Panqueca': str.upper('panqueca a bolonhesa'),
        'Panqueca a Bolonhesa': str.upper('panqueca a bolonhesa'),
        'Parm\~e': str.upper('frango a parmegiana'),
        'Parmegiana': str.upper('frango a parmegiana'),
        'Parmegiana (etra)': str.upper('frango a parmegiana unidade'),
        'Parmegiana de alcatra': str.upper('alcatra parmegiana'),
        'Parmegiana de frango': str.upper('frango a parmegiana'),
        'Parmê': str.upper('frango a parmegiana'),
        'Peie': str.upper('Peixe empanado'),
        'Peie Empanado': str.upper('Peixe empanado'),
        'Picadinho de Carne': str.upper('picadinho de carne'),
        'Porçâo Cubinhos de Frango': str.upper('cubinho de frango empanado'),
        'Porção  Fritas': str.upper('porção de batata frita'),
        'Porção Aipim': str.upper('porção de aipim'),
        'Porção Calabresa': str.upper('calabresa acebolada'),
        'Porção Cubinho Emanado': str.upper('cubinho de frango empanado'),
        'Porção Frango a Passarinho': str.upper('frango a passarinho'),
        'Porção Fritas': str.upper('porção de batata frita'),
        'Porção Salgadinho': str.upper('porção de salgadinhos'),
        'Porção Salgadinhos': str.upper('porção de salgadinhos'),
        'Porção Sardinha': str.upper('porção de sardinha'),
        'Porção aipim': str.upper('porção de aipim'),
        'Porção de Fritas': str.upper('porção de batata frita'),
        'Porção de Salgadinho': str.upper('porção de salgadinhos'),
        'Porção de Sardinha': str.upper('porção de sardinha'),
        'Porção de aipim': str.upper('porção de aipim'),
        'Pote Sorvete 2L': pd.NA,
        'Pudim':pd.NA,
        'Refri 2L': pd.NA,
        'Refrigerante 2L': pd.NA,
        'Refrigerante Sabores 1,5L': pd.NA,
        'Sobrecoa': str.upper('sobrecoxa assada'),
        'Sobrecoa Assada': str.upper('sobrecoxa assada'),
        'Sobrecoa Frita': str.upper('sobrecoxa frita'),
        'Sobremesa':pd.NA,
        'Sprit Lata': pd.NA,
        'Sprit Lata 350ml': pd.NA,
        'Stogronofe de Frango': str.upper('strogonoff de frango'),
        'Strogonofe de Carne': str.upper('strogonoff de carne'),
        'Strogonofe de Frango': str.upper('strogonoff de frango'),
        'Strogonoff': str.upper('strogonoff de frango'),
        'Strogonoff (puro)': str.upper('strogonoff de frango unidade'),
        'Strogonoff Carne': str.upper('strogonoff de carne'),
        'Strogonoff Frango': str.upper('strogonoff de frango'),
        'Strogonoff carne': str.upper('strogonoff de carne'),
        'Strogonoff de Carne': str.upper('strogonoff de carne'),
        'Strogonoff de carne': str.upper('strogonoff de carne'),
        'Strogonoff de frango': str.upper('strogonoff de frango'),
        'Strogonoff frango': str.upper('strogonoff de frango'),
        'Toscana': str.upper('linguiça de churrasco acebolada'),
        'UBER': pd.NA,
        'Uber': pd.NA,
        'a. parmegiana': str.upper('alcatra parmegiana'),
        'a. parmê': str.upper('alcatra parmegiana'),
        'a.parmegiana': str.upper('alcatra parmegiana'),
        'a.parmê': str.upper('alcatra parmegiana'),
        'abóbora':pd.NA,
        'acebolado':pd.NA,
        'acumulo': pd.NA,
        'alcatra': str.upper('alcatra acebolada'),
        'alcatras': str.upper('alcatra acebolada'),
        'bolo de pote':pd.NA,
        'calabresa': str.upper('calabresa acebolada'),
        'carne': str.upper('carne de panela'),
        'carne de panela': str.upper('carne de panela'),
        'carne moída': str.upper('carne de panela'),
        'carne picadinha': str.upper('picadinho de carne'),
        'carré': str.upper('carré suíno'),
        'coca 2L': pd.NA,
        'coca 350ml': pd.NA,
        'contrafile': str.upper('contrafilé bovino'),
        'costeliha': str.upper('costelinha suína'),
        'costelinha': str.upper('costelinha suína'),
        'costelinha salada/fritas/maionese': str.upper('costelinha suína'),
        'empanado': str.upper('filé de frango empanado'),
        'empanado e parmê':pd.NA,
        'empanado etra': str.upper('filé de frango empanado unidade'),
        'empanados': str.upper('filé de frango empanado'),
        'escondidinho': str.upper('escondidinho'),
        'etra f. parmegiana': str.upper('frango a parmegiana unidade'),
        'f. parmegiana': str.upper('frango a parmegiana'),
        'f. parmergiana': str.upper('frango a parmegiana'),
        'f. parmê': str.upper('frango a parmegiana'),
        'feijão': str.upper('feijão unidade'),
        'feijão branco': str.upper('feijão branco'),
        'filé empanado': str.upper('filé de frango empanado'),
        'frango': str.upper('filé de frango empanado'),
        'frango a parmegiana': str.upper('frango a parmegiana'),
        'frango assado': str.upper('frango assado'),
        'fritas': str.upper('porção de batata frita'),
        'fritas etras': str.upper('porção de batata frita'),
        'fígado': str.upper('fígado bovino acebolado'),
        'grelhado': str.upper('filé de frango grelhado'),
        'kuat 2L': pd.NA,
        'ling.churrasco': str.upper('linguíça de churrasco acebolada'),
        'linguiça': str.upper('calabresa acebolada'),
        'maracrrão': str.upper('macarrão a bolonhesa'),
        'nuggets': str.upper('Nuggets'),
        'omelete': str.upper('omelete de queijo'),
        'omelete de espinafre': str.upper('omelete de espinafre'),
        'omelete de queijo': str.upper('omelete de queijo'),
        'omelete etra e omelete': str.upper('omelete de queijo'),
        'p. aipim frito': str.upper('porção de aipim'),
        'p. fritas': str.upper('porção de batata frita'),
        'p.fritas': str.upper('porção de batata frita'),
        'pagou': pd.NA,
        'parmegiana': str.upper('frango a parmegiana'),
        'parmegiana etra': str.upper('frango a parmegiana unidade'),
        'parmegiana etra 2': pd.NA,
        'parmegianas': str.upper('frango a parmegiana unidade'),
        'parmê': str.upper('frango a parmegiana'),
        'parmê e omelete etra': pd.NA,
        'parmê e salada verda': str.upper('frango a parmegiana'),
        'parmê etra': str.upper('frango a parmegiana unidade'),
        'pavê de kitkat': pd.NA,
        'pavê de kitkat e 1 de limão': pd.NA,
        'pavê kitkat': pd.NA,
        'pavê kitkat e 1  pavê morango': pd.NA,
        'pavê morango': pd.NA,
        'pavês': pd.NA,
        'picadinho': str.upper('picadingo de carne'),
        'porçao calabresa': str.upper('calabresa acebolada'),
        'porção de fritas': str.upper('porção de batata frita'),
        'quentinhas': pd.NA,
        'quentinhas de empanado': str.upper('filé de frango empanado'),
        'salgadinhos': str.upper('porção de salgadinhos'),
        'strogonoff': str.upper('strogonoff de frango'),
        'strogonoff de carne': str.upper('strogonoff de carne'),
        'strogonoff de frango': str.upper('strogonoff de frango'),
        'strogonoff e carré': pd.NA,
        'strogonoff e parmegiana': pd.NA,
        'só parmê': str.upper('frango a parmegiana unidade'),
        'trufas': pd.NA,
        'trufas 2': pd.NA
        })

    data = data.dropna(subset=['prato_principal'])

    return data

def create_dim_prato(data):
    
    data = create_column_quantidade(data)

    data = create_colunm_prato_principal(data)

    dim_prato = pd.DataFrame()

    dim_prato['prato_principal'] = sorted(data['prato_principal'].unique())

    dim_prato['id_prato_principal'] = dim_prato.index + 1

    data = data.merge(dim_prato, on='prato_principal', how='left')

    data = data.drop(columns=['prato_principal'])

    dim_prato.to_csv('../data/outputs/dim_prato.csv', index=False, sep=';')

    return data



