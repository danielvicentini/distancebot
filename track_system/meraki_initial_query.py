#!/usr/local/bin/python3.8
#
import meraki
from datetime import datetime
import time
import sys
import os
sys.path.append(os.path.abspath('..'))
import config_shared

from pprint import pprint

NET_ID = config_shared.MERAKI_NET_ID

DASHBOARD = meraki.DashboardAPI(
    api_key = config_shared.MERAKI_API_KEY, 
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
#   'lat': -29.6889,
#   'lng': -20.66139,
#   'mac': '88:15:44:cc:d9:d8',
#   'model': 'Z1',
#   'name': 'Z1',
#   'networkId': 'L_711509141124547009',
#   'serial': 'Q0HN-4PA5-AXRB',
#   'url': 'https://n264.meraki.com/Camera-appliance/n/TOJgRcie/manage/nodes/new_list/149624929966552',
#   'wan1Ip': '192.168.15.45'}]
 

    device_list = DASHBOARD.devices.getNetworkDevices(NET_ID)
    
    ap_list = []
    
    for device in device_list:
        if "MR33"  == device["model"] or "MR24" == device["model"] or "MR18" == device["model"]:
            print("LLLLLLLLLLLLLLLL")
            print(device["model"])
            ap_list.append(device)
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            pprint(device)
    print("-----------------------------------------------------")
    pprint(ap_list)
    return ap_list

def ClientList (device_list:list):
#[MA]: This function collects a user list from meraki's dashboard
#If the same user is connected with 2 devices, it will count as one user
#
# This is what it returns:
# [{'ap_name': 'Z1',
#   'ap_user_count': 2,
#   'clients_identity': ['lpavanel@cisco.com', 'maralves@cisco.com'],
#   'last_update': '14:13:55'}]

    device_clients_list = []
    wifi_count = []
    device_clients = {}
    now = datetime.now()
    #last_update = now.strftime("%H:%M:%S")
    last_update = time.time()

    for device in device_list:
        client_list = (DASHBOARD.clients.getDeviceClients(device["serial"]))
        #pprint(client_list)
        i = 0
        user_list = []
        for client in client_list:
            if ("user" in client and client["user"] not in device_clients.values()):
                i += 1
                user_list.append(client["user"])
                device_clients = {
                    "ap_name" : device["name"],
                    "ap_user_count" : i,
                    "clients_identity" : user_list,
                    "last_update": last_update
                    }
        wifi_count.append(device_clients)

    return wifi_count

def CurrentWifiUsers(): 
#[MA]: Callable function for external usage
    print("passei aqui")
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
    pprint (current_wifi_users)  

if(__name__ == "__main__"):
#[MA]: Just for testing:
    main ()