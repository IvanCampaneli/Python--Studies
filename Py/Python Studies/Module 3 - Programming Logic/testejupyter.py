import pyautogui
from selenium import webdriver
import smtplib
import time

#COMANDS
#pyautogui.click
#pyautogui.write
#pyautogui.press
#pyautogui.hotkey

pyautogui.PAUSE = 1

# Passo 1: Acessar o sistema da empresa
pyautogui.press("win")
pyautogui.click(x=824, y=162)
pyautogui.write("Microsoft Edge")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")

time.sleep(5)

# Passo 2: Fazer login no sistema
pyautogui.click(x=811, y=431)
pyautogui.write("login")

pyautogui.click(x=883, y=532)
pyautogui.write("senha123")

pyautogui.click(x=863, y=620)

time.sleep(5)

# Passe 3: Baixar a base de dados
pyautogui.click(x=454, y=385)
pyautogui.click(x=881, y=204)
pyautogui.click(x=959, y=670)

# Passe 4: Calcular os indicadores
import pandas as pd

# importar base de dados
arquivo = pd.read_csv(r"C:\Users\ivanc\Downloads\Compras.csv", sep=";") #r = raw
print(arquivo)

# calculo dos indicadores

# total gasto -> somar os itens da columa valor final
total_gasto = arquivo["ValorFinal"].sum()

# quantidade -> soomar a coluna quantidade
quantidade = arquivo["Quantidade"].sum()

# preço médio -> total gasto / quantidade
preco_medio = total_gasto / quantidade

import pyperclip
# Passe 5: Enviar o email para o destinatário
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://outlook.live.com/mail/0/")
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=214, y=222)
pyautogui.click(x=929, y=352)
pyautogui.write("ivancampaneli.dev@hotmail.com")
pyautogui.press("tab")
pyautogui.press("tab")
pyperclip.copy("Relatório de Despesas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
texto = f"""Caro Ranieri,

Espero que esta mensagem o encontre bem. Gostaria de compartilhar com você um resumo das despesas recentes. Segue abaixo o relatório detalhado:

Total Gasto: R$ ${total_gasto:,.2f}
Quantidade Total: ${quantidade:,}
Preço Médio: R$ ${preco_medio:,.2f}

Essas informações fornecem uma visão geral das despesas recentes e podem ser úteis para análise e planejamento financeiro.

Se você tiver alguma dúvida ou precisar de mais informações, por favor, não hesite em entrar em contato.

Atenciosamente,
Dev Ivan Campaneli
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# Enviar Email
pyautogui.hotkey("ctrl", "enter")