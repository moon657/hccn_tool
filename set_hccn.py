#! /usr/bin/python
# -*- code: utf-8 -*-
# coding = utf-8

import sys
import os
import shutil
import subprocess

import cfg

class HCCN:
    def __init__(self):
        self.IPs = cfg.IPs
    
    def exec_cmd(self, cmd, err_flag, is_raise=True):
        print(cmd)
        subp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subp.wait()
        err = subp.stderr.read().decode("utf-8")
        if err:
            if is_raise:
                raise ValueError("%s, cmd: %s, err: %s" % (err_flag, cmd, err))
            else:
                print(err)
        out = subp.stdout.read().decode("utf-8")
        return out
    
    def get_mac(self, node):
        for i in range(8):
            cmd = "hccn_tool -i %d -mac -g" % i
            out = self.exec_cmd(cmd, "get_mac")
            mac = out.split("mac addr:")[-1].strip()
            print(mac)
            self.IPs[node][i]["mac"] = mac
    
    # step 1
    def set_ip_mask(self, node):
        for i in range(8):
            cmd = "hccn_tool -i %d -ip -s address %s netmask %s" % \
                (i, self.IPs[node][i]["ip"], self.IPs[node][i]["mask"])
            self.exec_cmd(cmd, "set_ip_mask")
    
    # step 2
    def set_ip_rule(self, node):
        for i in range(8):
            cmd = "hccn_tool -i %d -ip_rule -a dir from ip %s table %s" % \
                (i, self.IPs[node][i]["ip"], 102+i)
            self.exec_cmd(cmd, "set_ip_rule")
    
    # step 3
    def set_ip_route(self, node):
        for i in range(8):
            cmd = "hccn_tool -i %d -ip_route -a ip 0.0.0.0 ip_mask 0 via %s dev eth%d table %d" % \
                (i, self.IPs["common"]["gateway"], i, 102+i)
            self.exec_cmd(cmd, "set_ip_route")
            cmd = "hccn_tool -i %d -ip_route -a ip %s ip_mask 24 via %s dev eth%d table %d" % \
                (i, self.IPs["common"]["route_ip"], self.IPs[node][i]["ip"], i, 102+i)
            self.exec_cmd(cmd, "set_ip_route")
    
    # step 4
    def set_arp(self, node):
        for i in range(8):
            range_list = [0, 1, 2, 3] if i<=3 else [4, 5, 6, 7]
            for j in range_list:
                if i == j:
                    continue
                cmd = "hccn_tool -i %d -arp -a dev eth%d ip %s mac %s" % \
                    (i, i, self.IPs[node][j]["ip"], self.IPs[node][j]["mac"])
                self.exec_cmd(cmd, "set_arp")
    
    # step 5
    def set_leaf_arp(self, node):
        #all_nodes = list(self.IPs.keys()).remove("common")
        #res_nodes = all_nodes.remo
        opposite = "node-1"
        for i in range(8):
            cmd = "hccn_tool -i %d -arp -a dev eth%d ip %s mac %s" % \
                (i, i, self.IPs[opposite][i]["ip"], self.IPs[opposite][i]["mac"])
            self.exec_cmd(cmd, "set_leaf_arp")

    # step 6
    def set_mtu(self, node, mtu=8192):
        for i in range(8):
            cmd = "hccn_tool -i %d -mtu -s size %d" % (i, mtu)
            self.exec_cmd(cmd, "set_mtu")
    
    # 
    def clear_old_config(self, node):
        cmd = "cat /dev/null > /etc/hccn.conf"
        self.exec_cmd(cmd, "clear_old_config")
    
    #
    def del_old_ip_route(self, node):
        for i in range(8):
            cmd = "hccn_tool -i %d -ip_route -d ip 0.0.0.0 ip_mask 0 table %d" % \
                (i, 102+i)
            self.exec_cmd(cmd, "del_old_ip_route", is_raise=False)
            cmd = "hccn_tool -i %d -ip_route -d ip %s ip_mask 24 table %d" % (i, self.IPs["common"]["route_ip"], 102+i)
            self.exec_cmd(cmd, "del_old_ip_route", is_raise=False)
    
    #
    def set_config(self, node):
        print("==== set hccn config on %s ====" % node)

        print(">>>clear_old_config...")
        self.clear_old_config(node)
        print("done")

        print(">>>del_old_ip_route...")
        self.del_old_ip_route(node)
        print("done")

        print(">>>get_mac...")
        self.get_mac(node)
        print("done")

        print(">>>step1.set_ip_mask...")
        self.set_ip_mask(node)
        print("done")

        print(">>>step2.set_ip_rule...")
        self.set_ip_rule(node)
        print("done")

        print(">>>step3.set_ip_route...")
        self.set_ip_route(node)
        print("done")

        print(">>>step4.set_arp...")
        self.set_arp(node)
        print("done")

        print(">>>step5.set_leaf_arp...")
        self.set_leaf_arp(node)
        print("done")

        print(">>>step6.set_mtu...")
        self.set_mtu(node)
        print("done")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("run shell must be: python3 set_hccn.py node-x")
    # all_nodes = list(cfg.IPs.keys()).remove("common")
    if sys.argv[1] not in cfg.node_list:
        raise ValueError("%s not in %s" % (sys.argv[1]), str(cfg.node_list))
    hccn = HCCN()
    hccn.set_config(sys.argv[1])

