# FAQ: 常见问题解答

## Q1: 如何解决中文乱码问题？

**A:**  如果在使用 Vim 查看文档时遇到中文乱码问题，请按照以下步骤操作：

1. 打开 `/etc/vim/` 目录下的 `vimrc` 文件。
2. 添加以下三行代码：

   ```vim
   set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
   set termencoding=utf-8
   set encoding=utf-8

## Q2: 服务器联网问题。

**A:**  服务器联网，有两步，一个是可否访问局域网以外的网络，比如百度，一个是外网比如谷歌。后者请直接联系虞健翔，不会一直开着。

1. 测试可否连接
```
curl www.baidu.com
```
`
(base) [lixiang@node1 ~]$ <html><head><title>Web authentication Redirect</title><meta http-equiv="Cache-control" content="no-cache"><meta http-equiv="Pragma" content="no-cache"><meta http-equiv="Expires" content="-1"><meta http-equiv="refresh" content="1; url=https://login.ecnu.edu.cn/index_1.html?vlan_id1=0&vlan_id2=0&mac=40:06:d5:a2:f0:02&user_ip=49.52.20.55"></head></html>
`

以上的返回信息是错误信息，证明没有连接成功。返回信息重新定位到ecnu.edu.cn的网站。

如果返回很多信息，带点中文之类的，说明连接成功。

<img width="817" alt="image" src="https://github.com/user-attachments/assets/4772aafd-da00-496b-b10e-e47d17516848" />

2. 连接局域网以外的网络，在host主机上/home/lixiang下（三卡服务器是/home/lx)，运行
   ```
   python login.py login
   ```
   会返回学号和密码，输入之后，返回login sucess，再测试一下curl命令。

## Q3: 容器连不上但是22端口可以。

**A:** 可能是由于服务器重启导致容器关闭，首先执行`docker ps`，如果正常输出容器列表，但是没有你的容器，请执行：

```
docker start <你的容器名>
docker exec -it <你的容器名> /bin/bash
service ssh start
```

然后再尝试进行链接。

## Q4：使用Ray跑代码的时候`ray start`不起作用

**A:** 可能是由于同一服务器上还有其他docker在使用ray，可以在`ray start`后加上参数`--port xxxx`来避免冲突。**请勿直接进行`ray stop`，这会误杀他人程序！**
