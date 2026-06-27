# docker容器配置方法

## 创建容器

```
sudo docker run --gpus all -itd --privileged --name=[姓名]  -p [xxx]-[xxx]:[xxx]-[xxx] [--mount type=bind,source=/data/shared_planing,target=/root/shared_planing](optional)  ufoym/deepo /bin/bash

e.g.
sudo docker run --gpus all -itd --privileged --name=yujianxiang  -p 1000-1005:1000-1005 ufoym/deepo /bin/bash
sudo docker run --gpus all -itd --privileged --name=yujianxiang  -p 1000-1005:1000-1005 --mount type=bind,source=/data/shared_planing,target=/root/shared_planing  ufoym/deepo /bin/bash
```

注释：
1. name 这里输入容器名（比如姓名，自定义）
2. -p 端口号这里冒号前后一致，类似于1230-1235：1230-1235，120-125：120-125 都可以
3. **在旧版上，新增了--mount参数，用于共享文件夹，这是一个可选项，source表示host服务器上的地址，target表示创建容器后的共享文件夹地址。如果没有额外需求可以按默认命令来。**

## 查看创建的容器

```
sudo docker ps
```

可以查看创建完，是否有有刚刚创建好容器的name以及id

## 进入容器

```
sudo docker exec -it 容器名称（or容器id） /bin/bash 
```

## 配置网络

```
apt update
apt install openssh-server
```

## 更新密码

```
passwd
输入 123456
```

## 配置网络，目的是为了可以直接连上容器

`
apt-get install vim
`

## 修改配置文件

```
vim /etc/ssh/sshd_config
```

## vim文件下的配置

```
 Port 1400
 PermitRootLogin yes
```

注释：
1. 这里Port 端口号 和你容器id一致比如1230,120，第一位
2. PermitRootLogin 这里注释取消

## 重启ssh

```
/etc/init.d/ssh restart
```

成功会输出ok

## 然后就可以直接用49.52.20.55的主机ip，加刚刚设定的端口号，用户名root，刚刚设置好的密码，直接连接上服务器。


## 一些可选项
### tmux工具（可用可不用）

```
apt-get install tmux
```

### anacoda3 现在已经在共享文件夹中，没有共享文件夹的可以按以下步骤下载miniconda3

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
/bin/bash Miniconda3-latest-Linux-x86_64.sh   
```

### 环境变量的配置

```
vim /usr/local/bin/torch-activate
 #export PATH=/usr/local/bin:$PATH
```

## 退出容器

```
exit
```
