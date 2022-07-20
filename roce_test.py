#! /usr/bin/python
# -*- code: utf-8 -*-
# coding = utf-8

import sys
import os
import shutil
import subprocess
import datetime
import time

import cfg

def exec_cmd(cmd, err_flag, is_raise=True):
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

def reset_roce():
    for i in range(8):
        cmd = "hccn_tool -i %d -roce_test reset" % i
        exec_cmd(cmd, "reset_roce", is_raise=False)

def run_server(roce_type="read", size=4096, num=1000):
    reset_roce()
    for i in range(8):
        reset_roce()
        for j in range(8):
            cmd = "hccn_tool -i %d -roce_test ib_%s_bw -s %d -n %d -tcp" % \
                (j, roce_type, size, num)
            out = exec_cmd(cmd, "", is_raise=False)
            print (out)

def run_client(client_node, server_node, roce_type="read", size=4096, num=1000):
    dt_str = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    if not os.path.exists("./output"):
        os.makedirs("./output")
    f = open("./output/%s_to_%s_%s.txt" % (client_node, server_node, dt_str), "w")
    for i in range(8):
        reset_roce()
        for j in range(8):
            cmd = "hccn_tool -i %d -roce_test ib_%s_bw -s %d -n %d -tcp address %s" % \
                (i, roce_type, size, num, cfg.IPs[server_node][j]["ip"])
            out = exec_cmd(cmd, "%s-eth%d-->%s-eth%d"%(client_node, i, server_node, j), is_raise=False)
            print(out)
            time.sleep(5)
            f.write(out)
    f.close()

if __name__ == "__main__":
    #
    if len(sys.argv) < 5:
        raise ValueError("run shell must be: python3 roce_test_crouple.py server/client client_node server_node size roce_type num")
    #
    client_node = str(sys.argv[2])
    server_node = str(sys.argv[3])
    size = 4096
    roce_type = "read"
    num = 1000
    if len(sys.argv) >= 5:
        size = int(sys.argv[4])
    if len(sys.argv) >= 6:
        roce_type=int(sys.argv[5])
    if len(sys.argv) >= 7:
        num=int(sys.argv[6])
    #
    if sys.argv[1] == "server":
        run_server(roce_type=roce_type, size=size, num=num)
    elif sys.argv[1] == "client":
        run_client(client_node, server_node, roce_type=roce_type, size=size, num=num)

