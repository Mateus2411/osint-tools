# Wireless Access Point Attack Vector — menu 1 → 7

Cria um AP falso para redirecionar o tráfego da rede de teste ao SET. Base:
`src/wireless/` (`wifiattack.py`, `stop_wifiattack.py`). Parte de
[INDICE.md](INDICE.md).

## Opções

```
1) Start → sobe o AP falso
2) Stop  → derruba o AP
```

## Como funciona

1. AirBase-NG cria o AP (SSID `ACCESS_POINT_SSID`, canal `AP_CHANNEL=9`)
2. DHCP distribui IPs (`10.0.0.100-254` ou `192.168.10.100-254`)
3. DNSSpoof resolve todo DNS para a máquina atacante
4. Qualquer vetor web (ex.: harvester) aguarda as vítimas no servidor do SET

## Requisitos

Placa Wi-Fi com modo monitor, root, e `airbase-ng`, `airmon-ng`, `dnsspoof`,
`dhcpd3` instalados. Só em rede de teste isolada e autorizada.
