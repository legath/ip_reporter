import psutil, socket
import requests as requests

wlan = "wlan0"  # "wlan0"
tun = "tun0"  # "tun0"
base_api = "http://back.event-horizon.systems/api"
api = base_api + "/integration/module/healthcheck"

module_id = "31f4133e-933d-38d9-931b-d1bb46d4fa4e"
def get_wlan_mac():
    nics = psutil.net_if_addrs()
    if wlan in nics:
        nic = nics[wlan]
        for i in nic:
            if i.family == psutil.AF_LINK:
                return i.address


def get_tun_ip():
    nics = psutil.net_if_addrs()
    if tun in nics:
        nic = nics[tun]
        for i in nic:
            if i.family == socket.AF_INET:
                return i.address


def get_wlan_ip():
    nics = psutil.net_if_addrs()
    if tun in nics:
        nic = nics[wlan]
        for i in nic:
            if i.family == socket.AF_INET:
                return i.address


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mac = get_wlan_mac()
    ip = get_tun_ip()
    wlan_ip = get_wlan_ip()
    headers = {'Content-type': 'application/json', "accept": "application/json"}
    jsondat = {"id": module_id, "mac": mac, "tun":ip, "wlan":wlan_ip}
    response = requests.post(api, json=jsondat, headers=headers)
    print(jsondat)
    print(response)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
