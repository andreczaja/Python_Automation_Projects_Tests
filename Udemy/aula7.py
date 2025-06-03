import os
import PyPDF2
import pathlib

caminho_pasta_downloads = os.path.join(pathlib.Path.home(), r'Downloads')

for arquivo in os.listdir(caminho_pasta_downloads):
    if os.path.isdir(arquivo):
        continue
    if arquivo == "Cartola_159 _2024 (1).pdf":
        # os.startfile(os.path.join(caminho_pasta_downloads,arquivo))
        # break
        with open(os.path.join(caminho_pasta_downloads,arquivo),'rb') as f:
            dados_do_pdf = PyPDF2.PdfReader(f)
            pagina1 = dados_do_pdf.pages[0]
            texto_da_pagina = pagina1.extract_text()
            print(texto_da_pagina)

