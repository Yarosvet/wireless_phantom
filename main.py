import subprocess
import os


def main():
    configfile = os.path.join(os.path.abspath(__file__)[:-len(os.path.split(os.path.abspath(__file__))[-1])],
                              "hostapd.conf")
    subprocess.call(args=["hostapd", "-B", configfile])


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        subprocess.call(args=["killall", "hostapd"])
        raise exc
