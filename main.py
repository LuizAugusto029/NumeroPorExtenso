from modulos import leitores

print("""
——————————————————————————————————————————————————————————————————————————————————————————————
NÚMERO POR EXTENSO:
Mostrará um número qualquer inteiro entre 0 (zero) a 1.000.000 (um milhão) escrito por extenso. 
Ex.: 
Número: 33                  ou     Número: 8.765
Output >>> Trinta e três           Output >>> Oito mil setecentos e sessenta e cinco

Ao digitar o qualquer número acima de 1.000 (mil) é opcional digita-lo com um ponto "." ou sem
Ex.: 
Número: 13768 ou 13.768 são válidos
Output >>> Treze mil setecentos e sessenta e oito
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
""")

while True:
    valor = leitores.leitura()
    print(f'\033[33m{valor}\033[m\n')
    saida = leitores.continuar()
    if saida == 'S':
        continue
    if saida == 'N':
        break

print('\n\033[31m ⋯⋯⋯⋯⋯⋯ ENCERRADO ⋯⋯⋯⋯⋯⋯ \033[m')
