#! /usr/bin/python
# -*- code: utf-8 -*-
# coding = utf-8

import sys
import os
import shutil
import subprocess
import datetime
import time
import getopt

import cfg

RUN_MODE = "server"
CLIENT = "node-1"
SERVER = "node-2"
SIZE = 4096
ROCE_TYPE = "read"
NUM = 1000

def usage_help():
    usage = """
            usage :  
                python roce_test_self.py  \
                    --run_mode [mode] \
                    --client [node] \
                    --server [node] \
                    -t <type> -s <size> -n <num>
            param :
                -h | --help  for help message
                     --run_mode  server or client
                     --client  client node name
                     --server  server node name
                -t | --type  <option> to set test type. type <option> could be "read send write"
                -s | --size  <size> to set test size of packet .  <size> could be [16-2^23]
                -n | --num   <num> to set test number of packet.  <num> could be [5-20000]
            """
    print(usage)

def parse_args():
    try:
        options, args = getopt.getopt(sys.argv[1:], "hm:t:s:n:", \
            ['help', 'run_mode=', 'client=', 'server=', 'type=', 'size=', 'num='])
        for opt, opt_val in options:
            if opt in ('-h', '--help'):
                usage_help()
                sys.exit()
            elif opt in ('--run_mode'):
                global RUN_MODE
                RUN_MODE = opt_val
            elif opt in ('--client'):
                global CLIENT
                CLIENT = opt_val
            elif opt in ('--server'):
                global SERVER
                SERVER = opt_val
            elif opt in ("-t", "--type"):
                global ROCE_TYPE
                ROCE_TYPE = opt_val
            elif opt in ("-s", "--size"):
                global SIZE
                SIZE = opt_val
            elif opt in ("-n", "--num"):
                global NUM
                NUM = opt_val
            else:
                usage_help()
                sys.exit()
    except getopt.GetoptError:
        usage_help()
        sys.exit()

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
    parse_args()
    if RUN_MODE == "server":
        run_server(roce_type=ROCE_TYPE, size=SIZE, num=NUM)
    elif RUN_MODE == "client":
        run_client(CLIENT, SERVER, roce_type=ROCE_TYPE, size=SIZE, num=NUM)
    else:
        usage_help()
        sys.exit()

