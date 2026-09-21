# GAMKERS-DDOS

Distributed Denial Of Service (DDoS) attacks are a subclass of denial of service (DoS) attacks. A DDoS attack involves multiple connected online devices, collectively known as a botnet, which are used to overwhelm a target website with fake traffic.


Note: THIS TOOL IS JUST ONLY FOR EDUCATIONAL PURPOSE..GIVING DDOS ATTACKs WITHOUT SITE OWNER'S PERMISSION IS ILLEGAL.. SO USE IT AT YOUR OWN RISK.. WE'LL BE NOT RESPONSIBLE FOR ANY TYPES OF MISISSUES!!!


How To Install GAMKERS-DDOS In Termux
The Tool Installation Process Is Very Easy.. Just Open Your Termux & Type This Provided Commands!!

$ apt update && apt upgrade

$ pkg install python

$ pkg install python2

$ pkg install git

$ pkg install figlet

$ git clone https://github.com/gamkers/GAMKERS-DDOS.git

$ cd GAMKERS-DDOS

$ chmod +x GAMKERS-DDOS.py

$ python2 GAMKERS-DDOS.py


To Run (Python 3)

$ cd GAMKERS-DDOS

$ python GAMKERS-DDOS.py 127.0.0.1 -p 80 -t 4 -d 10

Opcoes:
  host              IP ou hostname do alvo (obrigatorio)
  -p, --port        porta inicial do ciclo (default 80)
  -e, --end-port    porta final do ciclo (default 65535)
  -t, --threads     numero de threads (default 4; medido: 2-4 e o sweet spot)
  -d, --duration    duracao em segundos; 0 = infinito (default 0)
  -q, --quiet       esconde o reporter de taxa (pps)
  -s, --size        tamanho do payload em bytes (default 1490; use 64-128 pra mais pps)

Versao otimizada: sem print por pacote (~35x mais rapido), sem sleeps
teatrais, socket por thread, CLI via argparse. Limite real e a banda de
upload da sua conexao, nao o script.

Dica de pps: cada pacote de 1490 bytes custa ~11.9 kbit na rede. Com
~12 Mbps de upload o teto e ~1000 pps. Reduzindo o payload pra 64 bytes
(92 bytes no fio), a MESMA banda vira ~16k pps — 16x mais pacotes por
segundo pra saturar firewall/CPU do alvo. Ex.: -s 64.


Your Tool Install & Setup Done!!..Now Go To Google & Search`Website IP Finder`Now Open The 1st Wesite & Place Your Target Website Url e.g. www.biribaba.com..


After Getting The Website IP , Copy The IP & Come To The Termux.. Now Paste The Target Website IP On `Ip Target:` & Give The Port Number `8080`

Booom!! Your Ddos Attack Had Been Started...
