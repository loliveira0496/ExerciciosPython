import os
import shutil

writer_dir = r'C:\Writer'
calc_dir = r'C:\Calc'
impress_dir = r'C:\Impress'

writer = ['.docx', 'odt']
calc = ['.xlsx', 'ods']
impress = ['.pptx', 'odp']

diretorio = r'C:\Users\Lorran\Downloads'
lista_dir = os.listdir(diretorio)

for item in lista_dir:
    caminho_arq = os.path.join(diretorio, item)
    if os.path.isfile(caminho_arq):  # Verificar se é um arquivo
        extensao = item.rsplit('.', 1)[1]
        if extensao in writer:
            novo_caminho = os.path.join(writer_dir, item)
            shutil.move(caminho_arq, novo_caminho)
            print(f'item {item} movido para {writer_dir}')
        elif extensao in calc:
            novo_caminho = os.path.join(calc_dir, item)
            shutil.move(caminho_arq, novo_caminho)
            print(f'item {item} movido para {calc_dir}')
        elif extensao in impress:
            novo_caminho = os.path.join(impress_dir, item)
            shutil.move(caminho_arq, novo_caminho)
            print(f'item {item} movido para {impress_dir}')
        else:
            print(f'item {item} não corresponde a nenhuma extensão conhecida')
