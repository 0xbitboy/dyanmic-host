# dyanmic-host
A solution for sync host file between lot of machine which are using DHCP

编写这个项目的初衷是为了管理开发环境的一些虚拟机，为了可以更好的融合到办公网中，虚拟集群用的是桥接网络，也就是跟办公网使用的是DHCP的，这就导致有时候IP会变，需要去把集群中的host文件修改过来，这就很麻烦，所以想通过一个agent主动上报到云端，然后开发机可以同步在线的host文件下来。比如使用[SwitchHosts](https://github.com/oldj/SwitchHosts) 来管理host文件

# 主要功能
1. 上报机器的hostname和ip到云端
2. 云端可以管理机器上报来的信息（管理后台开发中）
3. 集群分组，在线host文件生成 （/public/v1/host/{gropId}/hostfile)

# agent

- linux 和 mac 可以使用 linux下的agent，由shell编写。
- windows的agent由python编写，可以使用pyinstaller生成一个独立的可执行文件，不用依赖python环境
- 建议将agent加入定时任务定时上报

Linux:
```
agent.sh --eth eth0 --server host.liaojiacan.me --agent-key 50o9k7pI run
```
Windows
```
agent_cli.exe --eth en0 --server host.liaojiacan.me --agent-key HwhcZoxa run
```

使用参数解释如下
```
参数选项有：
--eth  指定网络接口（网卡）
--hostname 自定义hostname ，不指定将采用机器的hostname
--server 指定服务端地址
--scheme 指定协议（http或者https）
--agent-key 服务端生成用于安装的key （管理后台可获取）

命令选项有：
run 上报信息
sync 同步host文件到本地

```

# server

- 在线host文件:/public/v1/host/{gropId}/hostfile
- demo:[http://host.liaojiacan.me/public/v1/hosts/1@RMl0Au9D/hostfile](http://host.liaojiacan.me/public/v1/hosts/1@RMl0Au9D/hostfile)

# plan
- agent install script
- 管理后台




