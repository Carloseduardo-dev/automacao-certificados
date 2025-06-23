# 📜 Automação de Certificados

Sistema automatizado para geração de certificados de conclusão em massa a partir de dados de planilha Excel. O projeto lê informações dos participantes e gera certificados personalizados usando um template base.

## 🎯 Sobre o Projeto

Este script Python automatiza o processo de criação de certificados de conclusão, eliminando a necessidade de preenchimento manual. Ideal para instituições de ensino, empresas de treinamento e organizadores de eventos que precisam gerar múltiplos certificados de forma eficiente.

## ✨ Funcionalidades

- 📊 **Leitura automática** de dados do Excel
- 🎨 **Template personalizado** de certificado 
- ⚡ **Geração em lote** de certificados
- 🖼️ **Saída em alta qualidade** (formato JPG/PNG)
- 📝 **Campos personalizáveis**:
  - Nome do participante
  - Nome do curso
  - Tipo de participação
  - Carga horária
  - Datas de início e término
  - Data de emissão

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **OpenPyXL** - Manipulação de arquivos Excel
- **Pillow (PIL)** - Processamento de imagens
- **Fontes TTF** - Tahoma e Tahoma Bold

## 📋 Pré-requisitos

- Python 3.7+
- pip (gerenciador de pacotes)

## 🚀 Instalação

1. **Clone ou baixe o projeto**
   ```bash
   git clone https://github.com/Carloseduardo-dev/automacao-certificados.git
   cd automacao-certificados
   ```

2. **Instale as dependências**
   ```bash
   pip install openpyxl pillow
   ```

3. **Organize os arquivos necessários**
   ```
   projeto/
   ├── app.py                    # Script principal
   ├── planilha_alunos.xlsx     # Planilha com dados
   ├── certificado_padrao.jpg   # Template do certificado
   ├── tahoma.ttf              # Fonte regular
   └── tahomabd.ttf            # Fonte negrito
   ```

## 📊 Estrutura da Planilha

A planilha `planilha_alunos.xlsx` deve conter as seguintes colunas na **Sheet1**:

| Coluna A | Coluna B | Coluna C | Coluna D | Coluna E | Coluna F | Coluna G |
|----------|----------|----------|----------|----------|----------|----------|
| Nome do Curso | Nome Participante | Tipo Participante | Data Início | Data Término | Carga Horária | Data Emissão |

**Exemplo:**
```
Python Básico | João Silva | Aluno | 01/06/2025 | 15/06/2025 | 40 | 20/06/2025
Web Development | Maria Santos | Participante | 05/06/2025 | 25/06/2025 | 60 | 30/06/2025
```

## 🎨 Template do Certificado

O template `certificado_padrao.jpg` deve ser uma imagem com:
- **Resolução recomendada**: Alta resolução para impressão
- **Espaços em branco** nas posições onde os textos serão inseridos
- **Formato**: JPG ou PNG

### Posições dos Textos no Template:
- **Nome do Participante**: Posição (1020, 825) - Fonte: Tahoma Bold 90px
- **Nome do Curso**: Posição (1062, 950) - Fonte: Tahoma 80px  
- **Tipo de Participante**: Posição (1435, 1065) - Fonte: Tahoma 80px
- **Carga Horária**: Posição (1480, 1182) - Fonte: Tahoma 80px
- **Data Início**: Posição (748, 1785) - Fonte: Tahoma 49px
- **Data Término**: Posição (750, 1935) - Fonte: Tahoma 49px
- **Data Emissão**: Posição (2230, 1935) - Fonte: Tahoma 49px

## 💻 Como Usar

1. **Prepare sua planilha** com os dados dos participantes
2. **Coloque o template** do certificado no diretório
3. **Execute o script**:
   ```bash
   python app.py
   ```
4. **Os certificados serão gerados** automaticamente com o nome: `{índice} {nome_participante} certificado.jpg`

## ⚙️ Configurações

### Modificar Posições dos Textos
```python
# Exemplo para ajustar posição do nome
desenhar.text((1020,825), nome_participante, fill='black', font=fonte_nome)
#            ^posição X,Y
```

### Alterar Fontes e Tamanhos
```python
fonte_nome = ImageFont.truetype('./tahomabd.ttf', 90)  # Nome em negrito
fonte_geral = ImageFont.truetype('./tahoma.ttf', 80)   # Texto geral
fonte_data = ImageFont.truetype('./tahoma.ttf', 49)    # Datas
```

### Personalizar Cores
```python
desenhar.text((posicao), texto, fill='black', font=fonte)      # Preto
desenhar.text((posicao), texto, fill='#0E093D', font=fonte)   # Azul escuro
```

## 📁 Arquivos de Saída

Os certificados gerados seguem o padrão:
- **Nome**: `{índice} {nome_participante} certificado.jpg`
- **Formato**: JPG
- **Localização**: Mesmo diretório do script

Exemplo de saída:
```
0 João Silva certificado.jpg
1 Maria Santos certificado.jpg
2 Pedro Oliveira certificado.jpg
```

## 🔧 Solução de Problemas

### Erro: "No such file or directory"
```bash
# Verifique se todos os arquivos estão no diretório:
ls -la
# Devem estar presentes: app.py, planilha_alunos.xlsx, certificado_padrao.jpg, tahoma.ttf, tahomabd.ttf
```

### Erro: "OSError: cannot open resource"
- Verifique se as fontes TTF estão no diretório correto
- No Windows, você pode usar fontes do sistema: `C:/Windows/Fonts/tahoma.ttf`

### Textos desalinhados
- Ajuste as coordenadas X,Y nas funções `desenhar.text()`
- Use um editor de imagem para medir as posições corretas

### Planilha não encontrada
- Certifique-se de que o arquivo se chama exatamente `planilha_alunos.xlsx`
- Verifique se a aba se chama `Sheet1`

---

⭐ **Gostou do projeto? Deixe uma estrela no repositório!**
