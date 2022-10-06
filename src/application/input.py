# 1) Faça um programa que  leia um arquivo json abaixo e calcule o saldo diário da
# quantidades de moedas.
# a) saldo inicial deve ser 0
import json
from typing import List


def pega_arquivo()->List[dict]:
       with open("transactions.json") as arquivo_json:
              arquivo_transactions = json.load(arquivo_json)
       return arquivo_transactions
