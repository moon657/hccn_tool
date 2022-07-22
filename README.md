# 该脚本用于快速配置、测试多台训练服务器NPU交换机组网

## 使用方法
### 1.修改配置文件
修改根目录下的cfg.py文件, 按实际情况填写：\
    node_list：每台服务器的命名；\
    IPs["common"]: 根据实际情况填写当前的服务器所在IP网段、掩码、网关、网关mac；\
    IPS["node-x"]: 根据实际情况填写每台设备8个NPU使用的IP及MASK；\


### 2.配置网络
使用root用户在当前目录下执行 python set_hccn.py NODE , NODE需按实际情况修改为cfg.py文件中配置的节点名称。\
例如，在第2台服务器上配置组网：
```
python set_hccn.py node-2
```

### 3.单机测试带宽
测试命令如下：
```
python roce_test_self.py  -m [node] -t <type> -s <size>  <num>
    -h | --help  for help message 
    -m | --machine  swtich node 
    -t | --type  <option> to set test type. type <option> could be "read send write"
    -s | --size  <size> to set test size of packet .  <size> could be [16-2^23]
    -n | --num   <num> to set test number of packet.  <num> could be [5-20000]
```
例如，在第3台服务器上测试read带宽1000次：
```
python roce_test_self.py -m node-3 -t read -s 8192 -n 1000
```

### 4.双机测试带宽
测试命令如下：
```
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
```
假设使用node-1为client， node-2为server。需要先在node-2上执行：
```
python roce_test_self.py  \
        --run_mode server \
        --client node-1 \
        --server node-2 \
        -t read -s 8192 -n 1000
```
然后在node-1上执行：
```
python roce_test_self.py  \
        --run_mode client \
        --client node-1 \
        --server node-2 \
        -t read -s 8192 -n 1000
```
