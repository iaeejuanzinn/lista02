estoque = int(input('digite o estoque atual: '))
estoque2 = float(input('digite a quantidade maxima do estoque:')) 
estoque3 = float(input('digite a quantidade minima do estoque: '))
media = (estoque2 + estoque3) /2
if estoque >= media:
    print(media,'não efetuar compra')
else:
    print(media,'efetuar compra')