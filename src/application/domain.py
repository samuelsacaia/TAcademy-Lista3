
from dataclasses import dataclass
from datetime import date
from typing import List

@dataclass
class Transaction:
    date : date
    type : str
    qty : float
    price : float
    cost : float

@dataclass
class Saldo:
    date :date
    qty : float

def converter_em_class( arquivo_transactions): 
    lista_trasanctions : List[Transaction]=[]

    for i in  arquivo_transactions:
            transaction = Transaction(**i)
            lista_trasanctions.append(transaction)
    return lista_trasanctions


def pegar_saldo(lista_trasanctions):
    saldo =0
    lista_saldo = []

    if len(lista_trasanctions)>0:
        data_inicial = lista_trasanctions[0].date
        for transaction in lista_trasanctions:
            if transaction.date !=data_inicial:
                lista_saldo.append(Saldo( date = data_inicial, qty = saldo))

                data_inicial= transaction.date
            if transaction.type =="BUY":
                saldo +=transaction.qty

            if transaction.type =="SELL":
                saldo -= transaction.qty

        lista_saldo.append(Saldo(date = data_inicial, qty=saldo))   
    return lista_saldo                