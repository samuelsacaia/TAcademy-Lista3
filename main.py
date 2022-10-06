


from src.application.domain import converter_em_class, pegar_saldo
from src.application.input import pega_arquivo


if __name__=='__main__':
    arquivo_transactions = pega_arquivo()
    lista_trasanctions = converter_em_class(arquivo_transactions)
    lista_saldo = pegar_saldo(lista_trasanctions)
