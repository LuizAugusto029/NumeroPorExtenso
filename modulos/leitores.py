# BASE 1
def zero_a_nove(n):
    num_zero_a_dez = ['Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove']
    for c, i in enumerate(num_zero_a_dez):
        if c == n:
            numero = num_zero_a_dez[c]
            return str(numero)


# BASE 2
def dez_a_dezenove(n):
    num_onze_a_dezenove = ['Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
                           'Dezenove']
    for c, i in enumerate(num_onze_a_dezenove):
        if c == (n - 10):
            numero = num_onze_a_dezenove[c]
            return str(numero)


# 20 a 29
def vinte(n):
    if n == 20:
        return 'Vinte'
    else:
        n -= 20
        return 'Vinte e ' + zero_a_nove(n).lower()


# 30 a 39
def trinta(n):
    if n == 30:
        return 'Trinta'
    else:
        n -= 30
        return 'Trinta e ' + zero_a_nove(n).lower()


# 40 a 49
def quarenta(n):
    if n == 40:
        return 'Quarenta'
    else:
        n -= 40
        return 'Quarenta e ' + zero_a_nove(n).lower()


# 50 a 59
def cinquenta(n):
    if n == 50:
        return 'Cinquenta'
    else:
        n -= 50
        return 'Cinquenta e ' + zero_a_nove(n).lower()


# 60 a 69
def sessenta(n):
    if n == 60:
        return 'Sessenta'
    else:
        n -= 60
        return 'Sessenta e ' + zero_a_nove(n).lower()


# 70 a 79
def setenta(n):
    if n == 70:
        return 'Setenta'
    else:
        n -= 70
        return 'Setenta e ' + zero_a_nove(n).lower()


# 80 a 89
def oitenta(n):
    if n == 80:
        return 'Oitenta'
    else:
        n -= 80
        return 'Oitenta e ' + zero_a_nove(n).lower()


# 90 a 99
def noventa(n):
    if n == 90:
        return 'Noventa'
    else:
        n -= 90
        return 'Noventa e ' + zero_a_nove(n).lower()


# Função para repetição: UM até NOVENTA e NOVE
def um_a_noventanove(num_principal, nome_geral=''):
    if 1 <= num_principal <= 9:
        return f'{nome_geral}' + zero_a_nove(num_principal).lower()
    elif 10 <= num_principal <= 19:
        return f'{nome_geral}' + dez_a_dezenove(num_principal).lower()
    elif 20 <= num_principal <= 29:
        return f'{nome_geral}' + vinte(num_principal).lower()
    elif 30 <= num_principal <= 39:
        return f'{nome_geral}' + trinta(num_principal).lower()
    elif 40 <= num_principal <= 49:
        return f'{nome_geral}' + quarenta(num_principal).lower()
    elif 50 <= num_principal <= 59:
        return f'{nome_geral}' + cinquenta(num_principal).lower()
    elif 60 <= num_principal <= 69:
        return f'{nome_geral}' + sessenta(num_principal).lower()
    elif 70 <= num_principal <= 79:
        return f'{nome_geral}' + setenta(num_principal).lower()
    elif 80 <= num_principal <= 89:
        return f'{nome_geral}' + oitenta(num_principal).lower()
    elif 90 <= num_principal <= 99:
        return f'{nome_geral}' + noventa(num_principal).lower()


# 100 a 199
def cem(n):
    if n == 100:
        return 'Cem'
    else:
        n -= 100
        retorno = um_a_noventanove(num_principal=n, nome_geral='Cento e ')
        return retorno


# 200 a 299
def duzentos(n):
    if n == 200:
        return 'Duzentos'
    else:
        n -= 200
        retorno = um_a_noventanove(num_principal=n, nome_geral='Duzentos e ')
        return retorno


# 300 a 399
def trezentos(n):
    if n == 300:
        return 'Trezentos'
    else:
        n -= 300
        retorno = um_a_noventanove(num_principal=n, nome_geral='Trezentos e ')
        return retorno


# 400 a 499
def quatrocentos(n):
    if n == 400:
        return 'Quatrocentos'
    else:
        n -= 400
        retorno = um_a_noventanove(num_principal=n, nome_geral='Quatrocentos e ')
        return retorno


# 500 a 599
def quinhentos(n):
    if n == 500:
        return 'Quinhentos'
    else:
        n -= 500
        retorno = um_a_noventanove(num_principal=n, nome_geral='Quinhentos e ')
        return retorno


# 600 a 699
def seissentos(n):
    if n == 600:
        return 'Seiscentos'
    else:
        n -= 600
        retorno = um_a_noventanove(num_principal=n, nome_geral='Seiscentos e ')
        return retorno


# 700 a 799
def setecentos(n):
    if n == 700:
        return 'Setecentos'
    else:
        n -= 700
        retorno = um_a_noventanove(num_principal=n, nome_geral='Setecentos e ')
        return retorno


# 800 a 899
def oitocentos(n):
    if n == 800:
        return 'Oitocentos'
    else:
        n -= 800
        retorno = um_a_noventanove(num_principal=n, nome_geral='Oitocentos e ')
        return retorno


# 900 a 999
def novecentos(n):
    if n == 900:
        return 'Novecentos'
    else:
        n -= 900
        retorno = um_a_noventanove(num_principal=n, nome_geral='Novecentos e ')
        return retorno


# Função para repetição: Números que estão entre CEM e NOVECENTOS e NOVENTA e NOVE
def cem_a_novecentos_e_noventanove(num_principal, nome_geral=''):
    if 100 <= num_principal <= 199:
        return f'{nome_geral}' + cem(num_principal).lower()
    elif 200 <= num_principal <= 299:
        return f'{nome_geral}' + duzentos(num_principal).lower()
    elif 300 <= num_principal <= 399:
        return f'{nome_geral}' + trezentos(num_principal).lower()
    elif 400 <= num_principal <= 499:
        return f'{nome_geral}' + quatrocentos(num_principal).lower()
    elif 500 <= num_principal <= 599:
        return f'{nome_geral}' + quinhentos(num_principal).lower()
    elif 600 <= num_principal <= 699:
        return f'{nome_geral}' + seissentos(num_principal).lower()
    elif 700 <= num_principal <= 799:
        return f'{nome_geral}' + setecentos(num_principal).lower()
    elif 800 <= num_principal <= 899:
        return f'{nome_geral}' + oitocentos(num_principal).lower()
    elif 900 <= num_principal <= 999:
        return f'{nome_geral}' + novecentos(num_principal).lower()


# Função de repetição: números que estão entre [X-MIL] até [X-MIL e NOVENTA e NOVE]
def milnovenove(num_principal=0, x_mil=0, x_mil_nome_int='', x_mil_nome_geral=''):
    if num_principal == x_mil:
        return x_mil_nome_int
    else:
        num_principal -= x_mil
        retorno = um_a_noventanove(num_principal=num_principal, nome_geral=x_mil_nome_geral)
        return retorno


# Função de repetição: números que estão entre [X-MIL e MIL] até o [X-MIL NOVECENTOS e NOVENTA e NOVE]; ex.: 1100 ate 1999
def xmil_ate_xmil(num_principal, x_mil=0, x_mil_nome=''):
    if num_principal == x_mil + 100:
        return f'{x_mil_nome}e cem'
    elif num_principal == x_mil + 200:
        return f'{x_mil_nome}e duzentos'
    elif num_principal == x_mil + 300:
        return f'{x_mil_nome}e trezentos'
    elif num_principal == x_mil + 400:
        return f'{x_mil_nome}e quatrocentos'
    elif num_principal == x_mil + 500:
        return f'{x_mil_nome}e quinhentos'
    elif num_principal == x_mil + 600:
        return f'{x_mil_nome}e seiscentos'
    elif num_principal == x_mil + 700:
        return f'{x_mil_nome}e setecentos'
    elif num_principal == x_mil + 800:
        return f'{x_mil_nome}e oitocentos'
    elif num_principal == x_mil + 900:
        return f'{x_mil_nome}e novecentos'
    else:
        if (x_mil + 101) <= num_principal <= (x_mil + 999):
            num_principal -= x_mil
            retorno = cem_a_novecentos_e_noventanove(num_principal=num_principal, nome_geral=x_mil_nome)
            return retorno


def xmil_a_xmil_upgrade(n_principal, x_mil=0, nome_solo='', nome_geral=''):
    """
    -> Função com o objetivo de mostrar por extenso os números de 1.000 em 1.000 digitos
    :param n_principal: Número digitado pelo usuário
    :param x_mil: Valor número onde iniciará o intervalo, ex.: se for um intervalo de 1.000 a 2.000
    o parâmetro receberar 1.000 como valor
    :param nome_solo: Nome que o valor receberá quando o valor for igual ao inicio do intervalo, ex.: se
    for 1.000 a 2.000, esse param receberá 'Mil'
    :param nome_geral: Valor dado ao param nome_solo adicionando em seguida 'e', ex.: se
    for 1.000 a 2.000, esse param receberá 'Mil e '
    :return: Nome por extenso do valor recebido
    """
    # if x_mil <= n < x_mil + 1000:
    if x_mil <= n_principal <= x_mil + 99:
        retorno = milnovenove(num_principal=n_principal, x_mil=x_mil, x_mil_nome_int=nome_solo,
                              x_mil_nome_geral=nome_geral)
        return retorno
    else:
        retorno = xmil_ate_xmil(num_principal=n_principal, x_mil=x_mil, x_mil_nome=nome_solo)
        return retorno


# Função para ler os valores 1.000 a 9.999
def mil_ate_dezmil(n):
    # 1.000 a 1.999
    if 1000 <= n < 2000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=1000, nome_solo='Mil ', nome_geral='Mil e ')
        return retorno

    # 2.000 a 2.999
    elif 2000 <= n < 3000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=2000, nome_solo='Dois mil ', nome_geral='Dois mil e ')
        return retorno

    # 3.000 a 3.999
    elif 3000 <= n < 4000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=3_000, nome_solo='Três mil ', nome_geral='Três mil e ')
        return retorno

    # 4.000 a 4.999
    elif 4000 <= n < 5000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=4_000, nome_solo='Quatro mil ', nome_geral='Quatro mil e ')
        return retorno

    # 5.000 a 5.999
    elif 5000 <= n < 6000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=5_000, nome_solo='Cinco mil ', nome_geral='Cinco mil e ')
        return retorno

    # 6.000 a 6.999
    elif 6000 <= n < 7000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=6_000, nome_solo='Seis mil ', nome_geral='Seis mil e ')
        return retorno

    # 7.000 a 7.999
    elif 7000 <= n < 8000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=7_000, nome_solo='Sete mil ', nome_geral='Sete mil e ')
        return retorno

    # 8.000 a 8.999
    elif 8000 <= n < 9000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=8_000, nome_solo='Oito mil ', nome_geral='Oito mil e ')
        return retorno

    # 9.000 a 9.999
    elif 9000 <= n < 10000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=9_000, nome_solo='Nove mil ', nome_geral='Nove mil e ')
        return retorno


# Função para ler os valores de 10.000 a 19.999
def dezmil_a_vintemil(n):
    # 10.000 a 10.999
    if 10_000 <= n < 11_000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=10_000, nome_solo='Dez mil ', nome_geral='Dez mil e ')
        return retorno

    # 11.000 a 11.999
    elif 11_000 <= n < 12000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=11_000, nome_solo='Onze mil ', nome_geral='Onze mil e ')
        return retorno

    # 12.000 a 12.999
    elif 12_000 <= n < 13_000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=12_000, nome_solo='Doze mil ', nome_geral='Doze mil e ')
        return retorno

    # 13.000 a 13.999
    elif 13_000 <= n < 14_000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=13_000, nome_solo='Treze mil ', nome_geral='Treze mil e ')
        return retorno

    # 14.000 a 14.999
    elif 14_000 <= n < 15_000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=14_000, nome_solo='Quatorze mil ',
                                      nome_geral='Quatorze mil e ')
        return retorno

    # 15.000 a 15.999
    elif 15_000 <= n < 16_000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=15_000, nome_solo='Quinze mil ', nome_geral='Quinze mil e ')
        return retorno

    # 16.000 a 16.999
    elif 16_000 <= n < 17_000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=16_000, nome_solo='Dezesseis mil ',
                                      nome_geral='Dezeseis mil e ')
        return retorno

    # 17.000 a 17.999
    elif 17_000 <= n < 18_000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=17_000, nome_solo='Dezessete mil ',
                                      nome_geral='Dezessete mil e ')
        return retorno

    # 18.000 a 18.999
    elif 18_000 <= n < 19_000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=18_000, nome_solo='Dezoito mil ',
                                      nome_geral='Dezoito mil e ')
        return retorno

    # 19.000 a 19.999
    elif 19_000 <= n < 20_000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=19_000, nome_solo='Dezenove mil ',
                                      nome_geral='Dezenove mil e ')
        return retorno


# Função para repetição dos valores de 20.000 até 99.999
def funçao_mil_ate_dezmil(n):
    if 1000 <= n < 2000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=1000, nome_solo='Um mil ', nome_geral='Mil e ')
        return retorno

    elif 2000 <= n < 3000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=2000, nome_solo='Dois mil ', nome_geral='Dois mil e ')
        return retorno

    elif 3000 <= n < 4000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=3_000, nome_solo='Três mil ', nome_geral='Três mil e ')
        return retorno

    elif 4000 <= n < 5000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=4_000, nome_solo='Quatro mil ', nome_geral='Quatro mil e ')
        return retorno

    elif 5000 <= n < 6000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=5_000, nome_solo='Cinco mil ', nome_geral='Cinco mil e ')
        return retorno

    elif 6000 <= n < 7000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=6_000, nome_solo='Seis mil ', nome_geral='Seis mil e ')
        return retorno

    elif 7000 <= n < 8000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=7_000, nome_solo='Sete mil ', nome_geral='Sete mil e ')
        return retorno

    elif 8000 <= n < 9000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=8_000, nome_solo='Oito mil ', nome_geral='Oito mil e ')
        return retorno

    elif 9000 <= n < 10000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=9_000, nome_solo='Nove mil ', nome_geral='Nove mil e ')
        return retorno


# Função para repetição dos valores de dezenas de milhares
def xdezenas_mil(n_principal=0, x_dezena=0, x_dezena_nome='', x_dezena_geral=''):
    """
    -> Função com objetivo de mostrar por extenso os números de 10_000 em 10_000 digitos
    :param n_principal: Número digitado pelo usuário
    :param x_dezena: Valor numerico onde começará o intervalo, ex.: se o valor digitado estiver no intervalo de 20.000 a 30.000,
     esse parâmetro irá receber 20.000 como valor
    :param x_dezena_nome: Mostrará o nome inicial que essa dezena recebera nos valores que estão dentro do interva-lo
    da [x_dezena + 999], ex.: se o valor for 20.000 mostrará o nome que esse parâmetro receberá durante o intervalo de
    20.000 até 20.999 que será 'Vinte mil'
    :param x_dezena_geral: Nome inicial que receberá nos valores posteriores a [x_dezena + 1000]
    :return: Nome por extenso do valor recebido
    """
    if n_principal == x_dezena:
        return x_dezena_nome
    else:
        if x_dezena < n_principal < x_dezena + 1000:
            retorno = xmil_a_xmil_upgrade(n_principal=n_principal, x_mil=x_dezena,
                                          nome_solo=x_dezena_nome, nome_geral=x_dezena_nome+'e ')
            return retorno

        elif x_dezena + 1000 <= n_principal < x_dezena + 10_000:
            n_principal -= x_dezena
            retorno = funçao_mil_ate_dezmil(n_principal)
            return x_dezena_geral + retorno


# Função para ler os valores de 20.000 a 99.999
def vinte_a_cem_mil(n):
    # 20.000 a 29.999
    if 20_000 <= n < 30_000:
        retorno = xdezenas_mil(n_principal=n, x_dezena=20_000, x_dezena_nome='Vinte mil ', x_dezena_geral='Vinte e ')
        return retorno

    # 30.000 a 30.999
    elif 30_000 <= n < 40_000:
        retorno = xdezenas_mil(n_principal=n, x_dezena=30_000, x_dezena_nome='Trinta mil ', x_dezena_geral='Trinta e ')
        return retorno

    # 40.000 a 40.999
    elif 40_000 <= n < 50_000:
        retorno = xdezenas_mil(n_principal=n, x_dezena=40_000, x_dezena_nome='Quarenta mil ', x_dezena_geral='Quarenta e ')
        return retorno

    # 50.000 a 50.999
    elif 50_000 <= n < 60_000:
        retorno = xdezenas_mil(n_principal=n, x_dezena=50_000, x_dezena_nome='Cinquenta mil ', x_dezena_geral='Cinquenta e ')
        return retorno

    # 60.000 a 60.999
    elif 60_000 <= n < 70_000:
        retorno = xdezenas_mil(n_principal=n, x_dezena=60_000, x_dezena_nome='Sessenta mil ', x_dezena_geral='Sessenta e ')
        return retorno

    # 70.000 a 70.999
    elif 70_000 <= n < 80_000:
        retorno = xdezenas_mil(n_principal=n, x_dezena=70_000, x_dezena_nome='Setenta mil ', x_dezena_geral='Setenta e ')
        return retorno

    # 80.000 a 80.999
    elif 80_000 <= n < 90_000:
        retorno = xdezenas_mil(n_principal=n, x_dezena=80_000, x_dezena_nome='Oitenta mil ', x_dezena_geral='Oitenta e ')
        return retorno

    # 90.000 a 99.999
    elif 90_000 <= n < 100_000:
        retorno = xdezenas_mil(n_principal=n, x_dezena=90_000, x_dezena_nome='Noventa mil ', x_dezena_geral='Noventa e ')
        return retorno


# Função para ler os valores de 100.000 a 199.999
def cem_mil(n):
    if 100_000 <= n < 101000:
        retorno = xmil_a_xmil_upgrade(n_principal=n, x_mil=100_000, nome_solo='Cem mil ', nome_geral='Cem mil e ')
        return retorno
    elif 101_000 <= n < 110_000:
        n -= 100_000
        retorno = funçao_mil_ate_dezmil(n)
        return 'Cento e ' + retorno
    elif 110_000 <= n < 120_000:
        n -= 100_000
        retorno = dezmil_a_vintemil(n)
        return 'Cento e ' + retorno
    elif 120_000 <= n < 200_000:
        n -= 100_000
        retorno = vinte_a_cem_mil(n)
        return 'Cento e ' + retorno


# Função para repetição dos valores de centena de milhares
def centena_mil(num_principal, x_centena=0, x_centena_nome_a='', x_centena_nome_b=''):
    """
    -> Função com o objetivo de mostrar po rextenso os números de 100.000 em 100.000 digitos
    :param num_principal: Número digitado pelo usuário
    :param x_centena: Valor número onde iniciará o intervalo, ex.: 200.000 a 300.000, esse param
    receberar 200.000 como valor
    :param x_centena_nome_a: Nome inicial que o valor receberá, nesse caso esse nome ficará presente
    de 1 a 999
    :param x_centena_nome_b: Segundo nome inicial que o valor receberá, nesse caso esse nome se
     nos valores posteriores a 999
    :return: Nome por extenso do valor recebido
    """
    if x_centena <= num_principal < x_centena + 1000:
        retorno = xmil_a_xmil_upgrade(n_principal=num_principal, x_mil=x_centena,
                                      nome_solo=x_centena_nome_a, nome_geral=x_centena_nome_a+'e ')
        return retorno

    elif x_centena + 1000 <= num_principal < x_centena + 10_000:
        num_principal -= x_centena
        retorno = funçao_mil_ate_dezmil(num_principal)
        return x_centena_nome_b + retorno

    elif x_centena + 10_000 <= num_principal < x_centena + 20_000:
        num_principal -= x_centena
        retorno = dezmil_a_vintemil(num_principal)
        return x_centena_nome_b + retorno

    elif x_centena + 20_000 <= num_principal < x_centena + 100_000:
        num_principal -= x_centena
        retorno = vinte_a_cem_mil(num_principal)
        return x_centena_nome_b + retorno



def duzentos_a_um_milão(n):
    if 200_000 <= n < 300_000:
        retorno = centena_mil(num_principal=n, x_centena=200_000,
                              x_centena_nome_a='Duzentos mil ', x_centena_nome_b='Duzentos e ')
        return retorno

    elif 300_000 <= n < 400_000:
        retorno = centena_mil(num_principal=n, x_centena=300_000,
                              x_centena_nome_a='Trezentos mil ', x_centena_nome_b='Trezentos e ')
        return retorno

    elif 400_000 <= n < 500_000:
        retorno = centena_mil(num_principal=n, x_centena=400_000,
                              x_centena_nome_a='Quatrocentos mil ', x_centena_nome_b='Quatrocentos e ')
        return retorno

    elif 500_000 <= n < 600_000:
        retorno = centena_mil(num_principal=n, x_centena=500_000,
                              x_centena_nome_a='Quinhentos mil ', x_centena_nome_b='Quinhentos e ')
        return retorno

    elif 600_000 <= n < 700_000:
        retorno = centena_mil(num_principal=n, x_centena=600_000,
                              x_centena_nome_a='Seiscentos mil ', x_centena_nome_b='Seiscentos e ')
        return retorno

    elif 700_000 <= n < 800_000:
        retorno = centena_mil(num_principal=n, x_centena=700_000,
                              x_centena_nome_a='Setecnetos mil ', x_centena_nome_b='Setecentos e ')
        return retorno

    elif 800_000 <= n < 900_000:
        retorno = centena_mil(num_principal=n, x_centena=800_000,
                              x_centena_nome_a='Oitocentos mil ', x_centena_nome_b='Oitocentos e ')
        return retorno

    elif 900_000 <= n < 1_000_000:
        retorno = centena_mil(num_principal=n, x_centena=900_000,
                              x_centena_nome_a='Novecentos mil ', x_centena_nome_b='Novecentos e ')
        return retorno


def um_milhao(n):
    if n == 1_000_000:
        return 'Um milão'


# FUNÇÃO PRINCIPAL onde ORGANIZA todas as CONDIÇÕES POSSÍVEIS do número digitado.
def leitor_extenso(num):
    if num == 0:
        return 'Zero'
    elif 1 <= num < 100:
        return um_a_noventanove(num).capitalize()
    elif 100 <= num < 1000:
        return cem_a_novecentos_e_noventanove(num).capitalize()
    elif 1000 <= num < 10000:
        return mil_ate_dezmil(num)
    elif 10_000 <= num < 20_000:
        return dezmil_a_vintemil(num)
    elif 20_000 <= num < 100_000:
        return vinte_a_cem_mil(num)
    elif 100_000 <= num < 200_000:
        return cem_mil(num)
    elif 200_000 <= num < 1_000_000:
        return duzentos_a_um_milão(num)
    elif 1_000_000 <= num < 2_000_000:
        return um_milhao(num)


def leitura():
    try:
        numero = str(input('Número: ')).replace('.', '')
        tnumero = int(numero)
        extenso = leitor_extenso(tnumero)

        if tnumero > 1_000_000:
            print('\033[31mATÉ O MOMENTO SÓ ACEITA NÚMEROS <= 1.000.000\033[m')
            return leitura()

    except:
        print('\033[31mDIGITE UM NÚMERO n, ONDE n seja, 0 <= n <= 1.000.000\033[m')
        return leitura()
    else:
        return extenso


def continuar():
    try:
        ctn = str(input('Continuar? [S/N] > ')).upper().strip()[0]
        if ctn not in 'SN':
            print('INFORME sim[S] ou não[N]!')
            return continuar()
        else:
            return ctn
    except:
        print('INFORME sim[S] ou não[N]!')
        return continuar()
    else:
        return ctn
