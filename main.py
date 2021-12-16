from pyaccesspoint import AccessPoint
import logging
import time

logging.basicConfig(level=logging.DEBUG)
ap = AccessPoint(wlan="wlan1", ip="192.168.50.1", ssid="WirelessPhantom", password="besecure6", inet="eth0")
ap.start()
time.sleep(50)
ap.stop()
