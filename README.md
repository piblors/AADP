# Instruções de instalação e dependências
 - Lista todos os pré-requisitos, como a versão da linguagem eprogramação (ex: Python 3.9+) e outros softwares necessários > 1
 - Inclui um arquivo de gerenciamento de pacotes (ex: requirements.txt para Python) que permite a instalação automatizada de todas as bibliotecas > 2
 - Apresenta os comandos exatos e sequenciais para criar e configurar o ambiente (ex: criação de ambiente virtual, instalação de dependências) > 1

# 2. Instruções de Execução
 - Fornece o(s) comando(s) exato(s) para executar o modelo/script, incluindo exemplos de argumentos, se houver > 2
 - Descreve claramente o formato de dados esperado na entrada e o formato dos dados que serão gerados na saída > 1

# 3. Clareza e Organização
 - Contém um arquivo principal de texto (ex: README.md) que descreve o objetivo da solução e a função de cada arquivo importante no projeto > 1
 - O código-fonte possui comentários em trechos complexos ou em funções chave, explicando a lógica implementada. > 1
 - A estrutura de arquivos do projeto é lógica e organizada (ex: separando dados, scripts, modelos, etc.) > 1

---

# 🔍 Detecção de Dados Pessoais em Textos Públicos

## 📌 Introdução

Com o fortalecimento da transparência pública e da participação social digital, surge também a necessidade de proteger adequadamente os dados pessoais dos cidadãos. No contexto do **Participa DF**, plataforma oficial de participação social do Governo do Distrito Federal, pedidos de acesso à informação podem conter informações sensíveis que, se divulgadas indevidamente, violam a **Lei Geral de Proteção de Dados (LGPD – Lei nº 13.709/2018)**

Este projeto foi desenvolvido no âmbito do **1º Hackathon em Controle Social – Desafio Participa DF**, na categoria **Acesso à Informação**, e tem como objetivo **identificar automaticamente textos que contenham dados pessoais**, como nomes próprios, CPF, RG, telefones e endereços de e-mail. A solução auxilia na classificação automática de pedidos que deveriam ser tratados como **não públicos**, contribuindo para a proteção da privacidade do cidadão e para a eficiência dos serviços públicos

## 🎯 Objetivo do Projeto

- Identificar automaticamente textos que contenham **dados pessoais**
- Auxiliar na **classificação correta** de pedidos de acesso à informação
- Reduzir riscos de exposição indevida de dados sensíveis
- Apoiar a conformidade com a **LGPD**
- Facilitar a integração com fluxos de análise automatizada

## 📁 Estrutura do Projeto
```bash
├── data/
│ ├── input_exemplo.txt # Exemplo de texto de entrada
│ └── output_exemplo.json # Exemplo de saída gerada pelo modelo
│
├── setup.bat # Executavel para criação de ambiente no Windows
├── setup.sh # Executavel para criação de ambiente no Linux/MacOS
│
├── detector.py # Lógica principal de detecção de dados pessoais
├── main.py # Script principal de execução
├── requirements.txt # Dependências do projeto
└── README.md # Documentação do projeto
```
---

## 1. Instruções de Instalação e Dependências

### Pré-requisitos

Antes de executar o projeto, certifique-se de que o ambiente atende aos seguintes requisitos:

- **Python 3.9 ou superior**
- Sistema operacional: Linux, macOS ou Windows
- `pip` instalado (Gerenciador de pacotes do python)
- Git (para a clonagem do repositório)
- `venv` para isolamento do ambiente

##  Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`
Você tem 2 opções: instalar manualmente ou com o arquivo de instalação automática (setup.sh ou .bat, dependendo do sistema)

> 0. Antes de tudo, clone e entre na pasta do projeto (recomendo clonar na pasta de documentos do seu computador, para fins de organização)
>```bash
> git clone https://github.com/piblors/AADP.git
> cd deteccao-dados-pessoais # Comando para Linux/MacOS
> dir deteccao-dados-pessoais # Comando para Windows
>```

### Opção 1: Instalação automática

1. Se estiver no **Windows**, digite no terminal: `setup.bat`
2. Caso esteja no **Linux/MacOS**, digite no terminal: `bash setup.sh`
2. Espere a instalação terminar
3. Continue com o passo a passo aqui neste README

### Opção 2: Instalação manual
1. Crie o ambiente virtual
```bash
python3 -m venv venv
```
2. Ative o ambiente virtual
```bash
venv\Scripts\activate # Uso no Windows
source venv/bin/activate # Uso no Linux/MacOS
```
3. Instale as dependências
```bash
pip install -r requirements.txt
```

## 2. Instruções de Uso
Você tem 2 opções aqui: 
- Colar o texto a ser analizado no documento `texto_para_busca.txt` na pasta `data/` e executar o programa
OU
- Inserir o texto a ser analizado após executar o programa

## OPÇÃO 1 (RECOMENDADO): Texto no documento para análise
1. Cole o texto no documento `texto_para_busca.txt` na pasta `data`

2. abra o terminal e digite isso para ir para a pasta do projeto: 
```bash 
dir **caminho_onde_o_projeto_foi_clonado**\AADP # No Windows
cd **caminho_onde_o_projeto_foi_clonado**/AADP # No Linux/MacOS
```

3. Execute o programa digitando ` python3 main.py` e clicando enter no terminal

4. **IMPORTANTE**: O programa irá perguntar se deseja usar o "documento de análise" ou o terminal, nesse caso, apenas clique enter sem digitar nada, para o programa utilizar o documento como entrada de dados

5. Pronto!! O resultado no terminal entrega se o texto possui ou não dados pessoais e, caso possua, diz quais tipos de dados (CPF, RG, Email...)

## OPÇÃO 2: Texto no terminal para análise
1. Abra o terminal e digite isso para ir para a pasta do projeto: 
```bash 
dir **caminho_onde_o_projeto_foi_clonado**\AADP # No Windows
cd **caminho_onde_o_projeto_foi_clonado**/AADP # No Linux/MacOS
```
3. Execute o programa digitando `python3 main.py` e clicando enter no terminal

4. **IMPORTANTE**: O programa irá perguntar se deseja usar o "documento de análise" ou o terminal, nesse caso, cole o texto no terminal e clique enter

5. Pronto!! O resultado no terminal entrega se o texto possui ou não dados pessoais e, caso possua, diz quais tipos de dados (CPF, RG, Email...)