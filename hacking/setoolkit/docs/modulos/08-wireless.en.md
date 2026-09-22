# Wireless Access Point Attack Vector — menu 1 → 7

Creates a rogue AP to redirect test-network traffic to SET. Base:
`src/wireless/` (`wifiattack.py`, `stop_wifiattack.py`). Part of
[INDICE.en.md](INDICE.en.md).

## Options

```
1) Start → brings the rogue AP up
2) Stop  → takes the AP down
```

## How it works

1. AirBase-NG creates the AP (SSID `ACCESS_POINT_SSID`, channel `AP_CHANNEL=9`)
2. DHCP hands out IPs (`10.0.0.100-254` or `192.168.10.100-254`)
3. DNSSpoof resolves all DNS to the attacker box
4. Any web vector (e.g. the harvester) waits for victims on the SET server

## Requirements

Monitor-mode Wi-Fi card, root, and `airbase-ng`, `airmon-ng`, `dnsspoof`,
`dhcpd3` installed. Isolated, authorized test network only.
