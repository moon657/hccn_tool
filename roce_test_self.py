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

node = "node-1"
size = 4096
roce_type = "read"
num = 1000

def usage_help():
    usage = '\nusage :  python roce_test_self.py  -m [node] -t <type> -s <size> -n <num>\n'\
            '    -h | --help  for help message \n'\
            '    -m | --machine  swtich node \n'\
            '    -t | --type  <option> to set test type. type <option> could be "read send write"\n'\
            '    -s | --size  <size> to set test size of packet .  <size> could be [16-2^23]\n'\
            '    -n | --num   <num> to set test number of packet.  <num> could be [5-20000]\n'\

    print (usage)
def getopt_test():
    try:
        options,args=getopt.getopt(sys.argv[1:], "hm:t:s:n:",['help','machine=','type=','size=','num='])
        for opt,opt_val in options:
            if opt in ('-h','--help'):
                usage_help()
                sys.exit()
            elif opt in ('-m','--machine'):
                print opt_val
                global node
                node= opt_val
            elif opt in ('-t','--type'):
                print opt_val
                global roce_type
                roce_type=opt_val
            elif opt in ('-s','--size'):
                print opt_val
                global size
                size = int(opt_val)

            elif opt in ('-n','--num'):
                print opt_val
                global num
                num=int(opt_val)
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

def test_onece(node, ind_send, ind_recv, roce_type="read", size=1048576, num=1000):
    cmd_send = "hccn_tool -i %d -roce_test ib_%s_bw -s %d -n %d -tcp address %s" % \
        (ind_send, roce_type, size, num, cfg.IPs[node][ind_recv]["ip"])
    cmd_recv = "hccn_tool -i %d -roce_test ib_%s_bw -s %d -n %d -tcp" % \
        (ind_recv, roce_type, size, num)
    print(cmd_recv)
    print(cmd_send)
    subp_recv = subprocess.Popen(cmd_recv, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(4)
    subp_send = subprocess.Popen(cmd_send, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subp_send.wait()
    subp_recv.wait()
    out_recv = subp_recv.stdout.read().decode("utf-8").strip()
    out_send = subp_send.stdout.read().decode("utf-8").strip()
    print(out_send)
    return out_send, out_recv

def test_all_eth(node, size, roce_type, num):
    reset_roce()
    dt_str = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    if not os.path.exists("./output"):
        os.makedirs("./output")
    f = open("./output/%s_%s.txt" % (node, dt_str), "w")
    for i in range(8):
        reset_roce()
        for j in range(8):
            if i == j:
                continue
            out_send, out_recv = test_onece(node, i, j, roce_type=roce_type, size=size, num=num)
            f.write(out_send)
    f.close()

if __name__ == "__main__":
    getopt_test()
    test_all_eth(node, size, roce_type, num)







    
    
    
