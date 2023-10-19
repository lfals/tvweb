# Sua lista de texto
lista_texto = """
03:00   WXV Rugby: England x Australia | https://v2.sportsonline.so/channels/pt/sporttv3.php
06:00   ATP World Tour 500: Tokyo | https://v2.sportsonline.so/channels/pt/sporttv2.php
07:00   ATP World Tour 250: Stockholm | https://v2.sportsonline.so/channels/pt/sporttv1.php
09:00   ATP World Tour 250: Antwerp | https://v2.sportsonline.so/channels/pt/sporttv4.php
09:00   DP World Tour: Andalucia Masters - D2 | https://v2.sportsonline.so/channels/pt/sporttv3.php
12:00   Al Taawon x Al Ittihad | https://v2.sportsonline.so/channels/bra/br3.php
12:30   Lusitânia x Benfica | https://v2.sportsonline.so/channels/bra/br4.php
13:30   Hannover 96 x Magdeburg | https://v2.sportsonline.so/channels/pt/eleven1.php
14:00   F1: USA Practice 1 | https://v2.sportsonline.so/channels/bra/br3.php
14:00   ATP World Tour 250: Antwerp | https://v2.sportsonline.so/channels/pt/sporttv2.php
15:30   Borussia Dortmund x Werder Bremen | https://v2.sportsonline.so/channels/bra/br1.php
16:00   Osasuna x Granada | https://v2.sportsonline.so/channels/pt/eleven2.php
16:00   Rugby World Cup: Argentina x New Zealand | https://v2.sportsonline.so/channels/pt/sporttv3.php
16:45   Vilar de Perdizes x Porto | https://v2.sportsonline.so/channels/bra/br4.php
17:00   F1: USA Qualifying | https://v2.sportsonline.so/channels/pt/sporttv4.php
17:00   Hockey: Sporting x Benfica | https://v2.sportsonline.so/channels/pt/eleven3.php
18:00   F1: USA Qualifying | https://v2.sportsonline.so/channels/bra/br3.php
19:00   Sampaio Corrêa x Vitória | https://v2.sportsonline.so/channels/bra/br1.php
19:30   F1 Academy: USA Qualifying | https://v2.sportsonline.so/channels/pt/sporttv4.php
19:45   MotoGP: Australia Qualifying | https://v2.sportsonline.so/channels/bra/br4.php
21:30   Boca Juniors x Unión Santa Fe | https://v2.sportsonline.so/channels/pt/sporttv1.php
21:30   Mirassol x Guarani | https://v2.sportsonline.so/channels/bra/br1.php
21:30   Sport Recife x Chapecoense | https://v2.sportsonline.so/channels/bra/br2.php
22:30   Moto2/3: Australia Qualifying | https://v2.sportsonline.so/channels/bra/br4.php
00:00   WXV Rugby: Canada x Wales | https://v2.sportsonline.so/channels/pt/sporttv1.php
00:40   MotoGP: Australia Sprint Race | https://v2.sportsonline.so/channels/bra/br4.php
"""

# Divide as linhas em uma lista
linhas = lista_texto.strip().split('\n')

# Loop através das linhas e gere o formato desejado
for linha in linhas:
    partes = linha.split('|')
    horario_equipe = partes[0].strip()
    link = partes[1].strip()

    # Imprima o formato desejado
    print(f'<button style="width: 95%; margin: 10px; font-size: 20px; font-weight: bold;" class="waves-effect waves-light btn-large" onclick="openMovie(\'{horario_equipe}\', \'{link}\')">{horario_equipe}</button>')
