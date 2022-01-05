from typing import runtime_checkable


def currency_conventer(conicoin):
    rub = conicoin*2.98
    ars = conicoin*0.82
    hnl = conicoin*0.17
    aud = conicoin*1.9622
    mad = conicoin*0.208
    print(f'I will get {round(rub, 2)} RUB from the sale of {float(conicoin)} conicoins.')
    print(f'I will get {round(ars, 2)} ARS from the sale of {float(conicoin)} conicoins.')
    print(f'I will get {round(hnl, 2)} HNL from the sale of {float(conicoin)} conicoins.')
    print(f'I will get {round(aud, 2)} AUD from the sale of {float(conicoin)} conicoins.')
    print(f'I will get {round(mad, 2)} MAD from the sale of {float(conicoin)} conicoins.')

conicoin = float(input())
currency_conventer(conicoin)