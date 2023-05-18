# Rasberry Pi Bitcoin Ticker
Display the current Bitcoin price on a Raspberry Pi Zero with Micro dot pHAT

## Requirements
1. Raspberry Pi Zero W or Wifi dongle
2. Micro dot pHAT

## Installation instructions

1. Install the Micro dot pHAT on the pi
```
curl -sS https://get.pimoroni.com/microdotphat | bash
```
2. clone this repo into the pi home dir
```
cd ~
git clone https://github.com/robertclarkson/RaspberryPiBitcoinTicker.git

```
3.
```
sudo pip install requests
cd RaspberryPiBitcoinTicker
chmod 777 bitcoin-ticker.py
./bitcoin-ticker.py
```
4. setup crontab (root)
```
sudo crontab -e

@reboot sleep 60 && /home/pi/RaspberryPiBitcoinTicker/bitcoin-ticker.py >> /home/pi/RaspberryPiBitcoinTicker/bitcoin-scroll.log 2>&1
```
