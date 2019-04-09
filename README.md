# Rasberry Pi Bitcoin Ticker
Display the current Bitcoin price on a Raspberry Pi Zero with Scroll pHAT

## Requirements
1. Raspberry Pi Zero
2. Scroll pHAT
3. WIFI dongle

## Installation instructions

1. Install the Scroll pHAT on the pi
```
curl -sS https://get.pimoroni.com/scrollphat | bash
```
2. clone this repo into the pi home dir
```
cd ~
git clone git@github.com:robertclarkson/RasberryPiBitcoinTicker.git

```
3.
```
sudo pip install requests
cd RaspberryPiBitcoinTicker
chmod 774 bitcoin.py
./bitcoin.py
```
