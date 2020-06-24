#!/usr/local/bin/python3.7
#
import wifi_sensor_settings
import meraki
from datetime import datetime

from pprint import pprint


NET_ID = wifi_sensor_settings.MERAKI_NET_ID

DASHBOARD = meraki.DashboardAPI(
    api_key = wifi_sensor_settings.MERAKI_API_KEY, 
    base_url = "https://api.meraki.com/api/v0/",
    print_console = False,
    output_log = False
    )

def ApList ():
#[MA]: This function collects a device list from meraki's dashboard
#and it filters for MRs and Z1s --> not considering MX wireless
#
# Here is the return expected:
#  [{'address': 'xxxx',
#   'firmware': 'wired-14-53',
#   'floorPlanId': None,
#   'lat': -22.68889,
#   'lng': -45.66139,
#   'mac': '88:15:44:cc:d9:d8',
#   'model': 'Z1',
#   'name': 'Z1',
#   'networkId': 'L_711568741124547009',
#   'serial': 'Q0HN-4PA5-AXRB',
#   'url': 'https://n264.meraki.com/Camera-appliance/n/TOJgRcie/manage/nodes/new_list/149624929966552',
#   'wan1Ip': '192.168.15.45'}]
 

    device_list = DASHBOARD.devices.getNetworkDevices(NET_ID)
    
    ap_list = []
    
    for device in device_list:
        if "Z1" or "Z3" or  "MR" in devices["model"]:
            ap_list.append(device)

    return ap_list

def ClientList (device_list:list):
#[MA]: This function collects a user list from meraki's dashboard
#If the same user is connected with 2 devices, it will count as one user
#
# This is what it returns:
#  [{'ap_name': 'Z1',
#   'ap_user_count': 1,
#   'clients_identity': 'maralves@cisco.com',
#   'last_update': '12:52:43'}]

    user_list = []
    wifi_count = []
    device_clients = {}
    now = datetime.now()
    last_update = now.strftime("%H:%M:%S")

    for device in device_list:
        client_list = (DASHBOARD.clients.getDeviceClients(device["serial"]))
        i = 0
        for client in client_list:
            if "user" in client and client["user"] not in device_clients:
                i += 1
                device_clients = {
                    "ap_name" : device["name"],
                    "ap_user_count" : i,
                    "clients_identity" : client["user"],
                    "last_update": last_update
                    }
        wifi_count.append(device_clients)

    return wifi_count

def CurrentWifiUsers(): 
#[MA]: Callable function for external usage
    current_wifi_users = ClientList(ApList())
    return current_wifi_users

def CurrentAllUsers():
#[MA]: Callable function for external usage
    device_list = DASHBOARD.devices.getNetworkDevices(NET_ID)
    current_all_users = ClientList(device_list)
    return current_all_users

def main ():
#[MA]: Just for testing:
    current_wifi_users = ClientList(ApList())
    print ("Wifi: " + str(current_wifi_users))  

if(__name__ == "__main__"):
#[MA]: Just for testing:
    main ()