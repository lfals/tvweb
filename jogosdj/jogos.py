# Sua lista de texto
lista_texto = """
02:00   Moto2: GP of Indonesia | https://sportsonline.so/channels/bra/br4.php
03:30   MotoGP: GP of Indonesia | https://sportsonline.so/channels/bra/br4.php
05:30   ATP World Tour 1000: Shangai - Final | https://sportsonline.so/channels/pt/sporttv3.php
07:00   WSL: Challenger Series - Saquarema Pro | https://sportsonline.so/channels/pt/sporttv5.php
07:30   Basketball: Real Madrid x Murcia | https://sportsonline.so/channels/pt/eleven1.php 
10:00	Georgia x Cyprus | https://sportsonline.so/channels/pt/sporttv1.php
10:00	Arsenal W x Aston Villa W | https://sportsonline.so/channels/bra/br2.php
10:30   NFL: Raves @ Titans | https://sportsonline.so/channels/pt/eleven2.php 
10:30   Sail GP: Cadiz, Spain - D2 | https://sportsonline.so/channels/pt/sporttv2.php
11:00   Cruzeiro U20 x Grêmio U20 | https://sportsonline.so/channels/bra/br1.php
11:00	Roma W x Inter Milano W | https://sportsonline.so/channels/bra/br4.php
11:00   Rugby World Cup: England x Fiji | https://sportsonline.so/channels/pt/sporttv3.php
13:00	Switzerland x Belarus | https://sportsonline.so/channels/bra/br2.php
13:00	Czech Republic x Faroe Islands | https://sportsonline.so/channels/bra/br1.php
13:00   Padel: WPT Open 1000: Amsterdam - Final | https://sportsonline.so/channels/pt/eleven1.php 
13:30   Leganés x Amorebieta | https://sportsonline.so/channels/pt/eleven2.php
15:30   NASCAR Cup Series: South Point 400 - Las Vegas Motor | https://sportsonline.so/channels/pt/sporttv4.php
15:45	Norway x Spain | https://sportsonline.so/channels/bra/br2.php
15:45	Turkey x Latvia | https://sportsonline.so/channels/bra/br4.php
15:45	Wales x Croatia | https://sportsonline.so/channels/bra/br1.php
15:45	Ponte Preta x Atlético Goianiense | https://sportsonline.so/channels/bra/br3.php
16:00   Rugby World Cup: France x South Africa | https://sportsonline.so/channels/pt/sporttv3.php
17:25   NFL: Lions @ Buccaneers | https://sportsonline.so/channels/pt/eleven2.php
18:00	Vitória x Guarani | https://sportsonline.so/channels/bra/br3.php
18:30	Londrina x Avaí | https://sportsonline.so/channels/bra/br4.php
23:00   ATP World Tour 500: Tokyo | https://sportsonline.so/channels/pt/sporttv2.php
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
