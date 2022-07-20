#! /usr/bin/python
# -*- code: utf-8 -*-
# coding = utf-8

node_list = ["node-1", "node-2", "node-3", "node-4", "node-5", "node-5"]

IPs = {
    "common":{
        "route_ip": "10.163.226.0",
        "route_mask": "255.255.255.0",
        "gateway": "10.163.226.1",
    },
    "node-1":[
        {
            "ip": "10.163.226.2",
            "mask": "255.255.255.0",
            "mac": "c8:c4:65:b7:fc:3f"
        },
        {
            "ip": "10.163.226.3",
            "mask": "255.255.255.0",
            "mac": "c8:c4:65:b7:fc:40"
        },
        {
            "ip": "10.163.226.4",
            "mask": "255.255.255.0",
            "mac": "c8:c4:65:b7:fc:41"
        },
        {
            "ip": "10.163.226.5",
            "mask": "255.255.255.0",
            "mac": "c8:c4:65:b7:fc:42"
        },
        {
            "ip": "10.163.226.6",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:dc"
        },
        {
            "ip": "10.163.226.7",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:dd"
        },
        {
            "ip": "10.163.226.8",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:de"
        },
        {
            "ip": "10.163.226.9",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:df"
        },
    ],
    "node-2":[
        {
            "ip": "10.163.226.10",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:9c"
        },
        {
            "ip": "10.163.226.11",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:9d"
        },
        {
            "ip": "10.163.226.12",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:9e"
        },
        {
            "ip": "10.163.226.13",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:9f"
        },
        {
            "ip": "10.163.226.14",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:a0"
        },
        {
            "ip": "10.163.226.15",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:a1"
        },
        {
            "ip": "10.163.226.16",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:a2"
        },
        {
            "ip": "10.163.226.17",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:a3"
        },
    ],
    "node-3":[
        {
            "ip": "10.163.226.18",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:9c"
        },
        {
            "ip": "10.163.226.19",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:9d"
        },
        {
            "ip": "10.163.226.20",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:9e"
        },
        {
            "ip": "10.163.226.21",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:9f"
        },
        {
            "ip": "10.163.226.22",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:a0"
        },
        {
            "ip": "10.163.226.23",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:a1"
        },
        {
            "ip": "10.163.226.24",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:a2"
        },
        {
            "ip": "10.163.226.25",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:a3"
        },
    ],
    "node-4":[
        {
            "ip": "10.163.226.26",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:9c"
        },
        {
            "ip": "10.163.226.27",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:9d"
        },
        {
            "ip": "10.163.226.28",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:9e"
        },
        {
            "ip": "10.163.226.29",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:9f"
        },
        {
            "ip": "10.163.226.30",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:a0"
        },
        {
            "ip": "10.163.226.31",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:a1"
        },
        {
            "ip": "10.163.226.32",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:a2"
        },
        {
            "ip": "10.163.226.33",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:a3"
        },
    ],
    "node-5":[
        {
            "ip": "10.163.226.34",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:9c"
        },
        {
            "ip": "10.163.226.35",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:9d"
        },
        {
            "ip": "10.163.226.36",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:9e"
        },
        {
            "ip": "10.163.226.37",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:9f"
        },
        {
            "ip": "10.163.226.38",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:a0"
        },
        {
            "ip": "10.163.226.39",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:a1"
        },
        {
            "ip": "10.163.226.40",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:a2"
        },
        {
            "ip": "10.163.226.41",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:a3"
        },
    ],
    "node-6":[
        {
            "ip": "10.163.226.42",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:9c"
        },
        {
            "ip": "10.163.226.43",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:9d"
        },
        {
            "ip": "10.163.226.44",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:9e"
        },
        {
            "ip": "10.163.226.45",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:9f"
        },
        {
            "ip": "10.163.226.46",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:a0"
        },
        {
            "ip": "10.163.226.47",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:a1"
        },
        {
            "ip": "10.163.226.48",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:a2"
        },
        {
            "ip": "10.163.226.49",
            "mask": "255.255.255.0",
            "mac": "80:e1:bf:a2:fa:a3"
        },
    ],
}


