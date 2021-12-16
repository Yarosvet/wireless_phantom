from pyaccesspoint import AccessPoint
import logging
from flask import Flask, render_template

HOST = "192.168.50.1"
app = Flask(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)
    ap = AccessPoint(wlan="wlan1", ip=HOST, ssid="WirelessPhantom", password="besecure6", inet="eth0")
    ap.start()
    app.run(HOST, 8080)
    ap.stop()


@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    main()
