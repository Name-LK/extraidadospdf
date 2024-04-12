import PyPDF2
import pandas

# OBS _> EXTRAIR O "HISTÓRICO DO CONSUMO"
        #Nº DO CLIENTE

def preço(pagina):

    #DEPOIS CRIAR UMA LOGICA DE FILTRAGEM PARA ARQUIVOS QUE NAO RETORNAREM O RESULTADO ESPERADO
    
    with open('contas.pdf', 'rb') as file:
        # Create a PDF file reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Get the first page of the PDF file
        page = pdf_reader.pages[pagina]

        # Extract the text from the page
        text = page.extract_text()

    # Split the text into lines
    lines = text.strip().split('\n')

    # Initialize an empty list to store the extracted data
    data = []

    # Loop through the lines and extract the relevant information
    for linha in lines:
        if 'TOTAL A PAGAR' in linha:
            index = lines.index(linha)

    return lines[index+1].split(' ')[-2]

def consumo(pagina):

    with open('contas.pdf', 'rb') as file:
        # Create a PDF file reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Get the first page of the PDF file
        page = pdf_reader.pages[pagina]

        # Extract the text from the page
        text = page.extract_text()

    # Split the text into lines
    lines = text.strip().split('\n')

    # Initialize an empty list to store the extracted data
    data = []

    # Loop through the lines and extract the relevant information
    for linha in lines:
        if 'Consumo Ativo(kWh)-TUSD' in linha:
            linha = linha.split(' ')
            linha = list(filter(None, linha))
            linha = linha[2].replace('DA',"")

            data.append(linha)
            return data[0]
        
pag = int(input("Digite o numero de paginas desejadas para consulta -->  "))

print("---------------------------------")

listaPreço = []
listaConsumo = []

for pagina in range(1,pag):
    num = int(pagina)

    # CRIAR LISTA COM TODOS OS DADOS
    listaPreço.append(preço(num))
    listaConsumo.append(consumo(num))

    '''
    print(f"|    TOTAL A PAGAR --> {preço(num)}    |")
    print(f"|    CONSUMO --> {consumo(num)}     |")
    print("---------------------------------")
    '''

data = {
    'Consumo':listaConsumo,
    'Preço':listaPreço
}

df = pandas.DataFrame(data)
print(df)
df.to_excel("Dados.xlsx", index=False)