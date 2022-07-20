# 该脚本用于快速配置、测试2*Atlas 800 9010训练服务器NPU组网

## 使用方法
### 1.修改配置文件
    修改根目录下的cfg.py文件, 把每台服务器NPU的IP/MASK/MAC按实际情况填写

### 2.配置网络
使用root用户在当前目录下执行：
```
python set_hccn.py node-name
```
node-name需按实际情况修改为cfg.py文件中配置的节点名称

### 3.单机测试带宽
使用root用户在当前目录下执行：
```
python roce_test_self.py -h 
```
查看使用方法
### 4.双机测试带宽
假设使用node-1做client， node-2做server
1）先在node-2上使用root用户在当前目录下执行：
```
python roce_test.py server node-1 node-2 size roce_type num
```
2）然后在node-1上使用root用户在当前目录下执行：
```
python roce_test.py client node-1 node-2 size roce_type num
```
第一个参数是client/server，表示当前设备运行客户端/服务端，必选；
第二个参数是客户端节点名称，需要与cfg.py中保持一致，必选；
第三个参数是服务端节点名称，需要与cfg.py中保持一致，必选；
第四个参数是发包大小，默认为4096，可选；
第五个参数是测试类型，默认为read，可选send/read/write；
第六个参数是发包次数，默认为1000，可选5~20000；
