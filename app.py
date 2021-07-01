# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 09:05:31 2021

@author: Adm
"""

#!/usr/bin/env python3
# -- coding: utf-8 --
"""
PF008

Objetivos:
Desenvolver um bot para desempenhar as seguintes funções:
- Acompanhar a rentabilidade das aplicações do fundo, e as porcentagens em cada tipo de investimento (ex: 60% em FI, 20% em RV, 10 em Cripto e etc).
- Armazenar as ações dos “traders” e rapidamente atualizasse a plataforma em detrimento das mudanças (ex: 5% de FI para RV).
- Monitorar os investimentos e ações do fundo constantemente para oferecer os dados aos clientes
- Monitorar os serviços e ter noção de como o seu dinheiro está sendo administrado.
- Disponibilizar as informações por meio de mensagens a um grupo de telegram ou whatsapp.

"""

import ast
import pandas as pd
import pandas_datareader.data as web 
import yfinance as yf

clientes = pd.read_excel('programação.xlsx')
listaAcoes = []
acoes = clientes['ação']
[listaAcoes.append(ast.literal_eval(i)) for i in acoes]

all_data =[]
for atual in listaAcoes:
    all_data.append({ticker: yf.Ticker(ticker) for ticker in atual})

arquivo = open('texto.txt','a')
iter = 0
for cliente in all_data:
    iter += 1
    arquivo.write('\n\t'+'Cliente ' + str(iter))
    for empresa in cliente:
        arquivo.write('\n\t'+'Empresa nova: ' + empresa)
        try:
            arquivo.write('\n\t previousClose: '+ str(cliente[empresa].info['previousClose']))
        except:
            print('erro')

arquivo.close()