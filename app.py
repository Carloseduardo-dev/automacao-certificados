#Pegar os dados da planilha
import openpyxl
from PIL import Image, ImageDraw, ImageFont

workbook_alunos = openpyxl.load_workbook('planilha_alunos.xlsx')
sheet_alunos = workbook_alunos['Sheet1']

for indice, linha in enumerate(sheet_alunos.iter_rows(min_row=2)):
    #Acessando células que contém info
    nome_curso = linha[0].value
    nome_participante = linha[1].value
    tipo_participante = linha[2].value
    carga_horaria = linha[5].value

    data_inicio = linha[3].value
    data_final = linha[4].value

    data_emissao = linha[6].value

    #Transferir os dados da planilha para a imagem do certificado
    #Fonte a ser usada
    fonte_nome = ImageFont.truetype('./tahomabd.ttf',90)
    fonte_geral = ImageFont.truetype('./tahoma.ttf',80)
    fonte_data = ImageFont.truetype('./tahoma.ttf',49)

    image =Image.open('./certificado_padrao.jpg')
    desenhar = ImageDraw.Draw(image)

    desenhar.text((1020,825),nome_participante,fill='black',font=fonte_nome)
    desenhar.text((1062,950),nome_curso,fill='black',font=fonte_geral)
    desenhar.text((1435,1065),tipo_participante,fill='black',font=fonte_geral)
    desenhar.text((1480,1182),str(carga_horaria),fill='black',font=fonte_geral)

    desenhar.text((748,1785),data_inicio,fill="#0E093D",font=fonte_data)
    desenhar.text((750,1935),data_final,fill="#0E093D",font=fonte_data)

    desenhar.text((2230,1935),data_emissao,fill="#0E093D",font=fonte_data)

    image.save(f'./{indice} {nome_participante} certificado.jpg')
    
