"""
Dictionaries:

d1={
    key:value,
    key:value
}

IPs:
Devices_names:
Policies:
Status:

Example 1
d1={
    ip:'172.0.0.1',
    d_name:'PC#1',
    policy:'Avoid .2, .3.5'
    status:True
}

"""

#First Dictionary
net_config = {
    "0001": {
        "ip": "192.168.0.2",
        "device": "Switch",
        "policy": "Deny All",
        "status": True,
        "list": [1, 4, 6, 0, 8]
    },
    "0002": {
        "ip": "192.168.0.1",
        "device": "Firewall",
        "policy": "Avoid .2 .3 .4",
        "status": False
    },
    "0003": {
        "ip": "192.168.0.4",
        "device": "Router",
        "policy": "Round Robin",
        "status": True
    },
    "0004": {
        "ip": "192.168.0.3",
        "device": "Server",
        "policy": "Guest Network Only",
        "status": True
    },
    "0005": {
        "ip": "192.168.0.5",
        "device": "AccessPoint",
        "policy": "Allow all",
        "status": True
    }
}

#Making a list inside a list
a = [1,2,3, [6.9, 1]]


#Way one to print a single index for the list inside 0001
print (net_config.get("0001").get("list")[2])

#Second Way Matrioska method
ContentOf0001 = net_config.get("0001")
List0001 = ContentOf0001.get("list")
NumFromList0001 = List0001[2]
print (NumFromList0001)

#Adding a item to the dictionary
net_config["0006"] = {
    "ip": "192.168.0.6",
    "device": "Printer",
    "policy": "Allow all",
    "status": True
}

#Final Printing of the modified dictionary
print(net_config)  

