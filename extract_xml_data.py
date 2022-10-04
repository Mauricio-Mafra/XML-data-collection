import xml.etree.ElementTree as ET
from xml.dom import minidom
import csv
import os

def main():
    directory = os.fsencode("./")
    arquivo_csv = open('./cadastro_clientes.csv', 'w')
    writer = csv.writer(arquivo_csv, quoting=csv.QUOTE_ALL)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".xml"):
            #Config raiz do XML
            root = ET.parse(filename).getroot()
            nsNFE = {'ns': "http://www.portalfiscal.inf.br/nfe"}

            #Coleta e tratamento de dados
            #Razao Social
            razao_social = root.find('ns:NFe/ns:infNFe/ns:dest/ns:xNome', nsNFE).text
            print("Razão Social:", razao_social)

            #Endereço
            logradouro = root.find('ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:xLgr', nsNFE).text
            logr_numero = root.find('ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:nro', nsNFE).text
            print("Logradouro:", logradouro, " ", logr_numero)

            #Bairro
            bairro = root.find('ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:xBairro', nsNFE).text
            print("Bairro:", bairro)

            #CNPJ / CPF
            #cnpj = root.find('ns:NFe/ns:infNFe/ns:dest/ns:CNPJ', nsNFE)
            #if cnpj is None:
            #    root.find('ns:NFe/ns:infNFe/ns:dest/ns:CPF', nsNFE)
            #    print("CNPJ:", cnpj)

            #Cidade
            cidade = root.find('ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:xMun', nsNFE).text
            print("Cidade:", cidade)

            #UF
            uf = root.find('ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:UF', nsNFE).text
            print("UF:", uf)

            #CNPJ / CPF
            cnpj_cpf = root.find('ns:NFe/ns:infNFe/ns:dest/ns:CNPJ', nsNFE)
            if cnpj_cpf is None:
                cnpj_cpf = root.find('ns:NFe/ns:infNFe/ns:dest/ns:CPF', nsNFE)
            cnpj_cpf = cnpj_cpf.text


            #NF
            numero_nfe = root.find('ns:NFe/ns:infNFe/ns:ide/ns:nNF', nsNFE).text
            print("NF:", numero_nfe)

            #CEP
            cep = root.find('ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:CEP', nsNFE).text
            print("CEP:", cep)

            #Telefone
            telefone = root.find('ns:NFe/ns:infNFe/ns:dest/ns:enderDest/ns:fone', nsNFE)
            if telefone is not None:
                print("Telefone:", telefone.text)

                telefone_format = "({DDD:}) {Numero:}"
                telefone = telefone_format.format(DDD = telefone.text[:2], Numero = telefone.text[2:])
                print("Telefone:", telefone)
            else: 
                telefone = "-"

            dados_cliente = (numero_nfe, razao_social, cnpj_cpf, logradouro, logr_numero, bairro, cidade, uf, cep, telefone)
            writer.writerow(dados_cliente)

    arquivo_csv.close()



def save_CSV(csv_data):
    arquivo_csv = open('./cadastro_clientes.csv', 'w')
    writer = csv.writer(arquivo_csv, quoting=csv.QUOTE_ALL)
    

    for linha in range(csv_data):
        writer.writerow(csv_data[linha])
    
    arquivo_csv.close()

if __name__ == "__main__":
    main()