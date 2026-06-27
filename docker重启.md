jiangzixi@Macintosh server-main % ssh server
Connection closed by 49.52.27.92 port 22
jiangzixi@Macintosh server-main % ssh server
The authenticity of host '49.52.27.92 (49.52.27.92)' can't be established.
ED25519 key fingerprint is: SHA256:kIHVnP7cWCgZyWiI/TvlW0TYMZmQb3x0jIpVcOaED9E
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '49.52.27.92' (ED25519) to the list of known hosts.
lx@49.52.27.92's password: 
Last login: Fri Jun  5 14:43:35 2026 from 172.25.89.111
(base) [lx@localhost ~]$ sudo docker ps
[sudo] password for lx: 
Sorry, try again.
[sudo] password for lx: 
CONTAINER ID   IMAGE                                         COMMAND                  CREATED         STATUS        PORTS                                                                                          NAMES
834dfece3583   ufoym/deepo                                   "/bin/bash"              5 weeks ago     Up 5 weeks    6006/tcp, 0.0.0.0:2024-2048->2024-2048/tcp, :::2024-2048->2024-2048/tcp, 8888/tcp              chenzeyuan
594ade582cf1   qdrant/qdrant:latest                          "./entrypoint.sh"        6 weeks ago     Up 6 weeks    0.0.0.0:16333->6333/tcp, [::]:16333->6333/tcp, 0.0.0.0:16334->6334/tcp, [::]:16334->6334/tcp   qdrant_yujing
1009b3bb900b   ufoym/deepo                                   "/bin/bash"              2 months ago    Up 2 months   6006/tcp, 0.0.0.0:1500-1509->1500-1509/tcp, :::1500-1509->1500-1509/tcp, 8888/tcp              hepingli
dcea22b50d54   ufoym/deepo                                   "/bin/bash"              4 months ago    Up 4 months   6006/tcp, 0.0.0.0:1015-1020->1015-1020/tcp, :::1015-1020->1015-1020/tcp, 8888/tcp              zhangjiaming
f9c2e3cf5a54   ufoym/deepo                                   "/bin/bash"              4 months ago    Up 4 months   6006/tcp, 0.0.0.0:3020-3025->3020-3025/tcp, :::3020-3025->3020-3025/tcp, 8888/tcp              yujing
b22705345150   ufoym/deepo                                   "/bin/bash"              4 months ago    Up 4 months   6006/tcp, 0.0.0.0:259-264->259-264/tcp, :::259-264->259-264/tcp, 8888/tcp                      ckxx2
2bbd19b745be   ufoym/deepo                                   "/bin/bash"              4 months ago    Up 3 months   6006/tcp, 0.0.0.0:1000-1005->1000-1005/tcp, :::1000-1005->1000-1005/tcp, 8888/tcp              yzx1
2a70574f7e0b   ufoym/deepo                                   "/bin/bash"              4 months ago    Up 4 months   6006/tcp, 8888/tcp, 0.0.0.0:25565-25575->25565-25575/tcp, :::25565-25575->25565-25575/tcp      hqduan2
eae201ae704a   yzx:v2                                        "/bin/bash"              5 months ago    Up 2 months   1001-1005/tcp, 6006/tcp, 8888/tcp, 0.0.0.0:2000->1000/tcp, [::]:2000->1000/tcp                 yzx
2aad2ee4ddf0   ufoym/deepo                                   "/bin/bash"              6 months ago    Up 3 months   6006/tcp, 0.0.0.0:3330-3335->3330-3335/tcp, :::3330-3335->3330-3335/tcp, 8888/tcp              gnociew
8c3f27c649ef   ufoym/deepo                                   "/bin/bash"              6 months ago    Up 3 months   6006/tcp, 0.0.0.0:1300-1305->1300-1305/tcp, :::1300-1305->1300-1305/tcp, 8888/tcp              caiqinnan
fe4aeba3a8c8   pytorch/pytorch:2.8.0-cuda12.8-cudnn9-devel   "/opt/nvidia/nvidia_…"   7 months ago    Up 3 months   0.0.0.0:1120-1125->1120-1125/tcp, :::1120-1125->1120-1125/tcp                                  yjx3
eb25744edda0   ufoym/deepo                                   "/bin/bash"              7 months ago    Up 3 months   6006/tcp, 0.0.0.0:1225-1230->1225-1230/tcp, :::1225-1230->1225-1230/tcp, 8888/tcp              yjx2
ffe64e26945f   ollama/ollama                                 "/bin/ollama serve"      8 months ago    Up 4 months   0.0.0.0:11434->11434/tcp, :::11434->11434/tcp                                                  crj_llm
12a12499232a   ufoym/deepo                                   "/bin/bash"              8 months ago    Up 4 months   6006/tcp, 0.0.0.0:716-721->716-721/tcp, :::716-721->716-721/tcp, 8888/tcp                      ckxx
1642039dc33d   ufoym/deepo                                   "/bin/bash"              11 months ago   Up 3 months   6006/tcp, 0.0.0.0:1032->1032/tcp, :::1032->1032/tcp, 8888/tcp                                  ybzhao_32g
717698d9b939   ufoym/deepo                                   "/bin/bash"              12 months ago   Up 4 months   6006/tcp, 8888/tcp, 0.0.0.0:10096-10097->10096-10097/tcp, :::10096-10097->10096-10097/tcp      scx
c18ac6a5ecc3   ufoym/deepo                                   "/bin/bash"              14 months ago   Up 3 months   6006/tcp, 0.0.0.0:525-530->525-530/tcp, :::525-530->525-530/tcp, 8888/tcp                      yujianxiang
(base) [lx@localhost ~]$ sudo docker restart ckxx2
ckxx2
(base) [lx@localhost ~]$ sudo docker ps | grep ckxx2
b22705345150   ufoym/deepo                                   "/bin/bash"              4 months ago    Up 2 minutes   6006/tcp, 0.0.0.0:259-264->259-264/tcp, :::259-264->259-264/tcp, 8888/tcp                      ckxx2
(base) [lx@localhost ~]$ sudo docker exec -it ckxx2 /bin/bash
(base) root@b22705345150:/# service ssh status
 * sshd is not running
(base) root@b22705345150:/# service ssh start
 * Starting OpenBSD Secure Shell server sshd                                         [ OK ] 
(base) root@b22705345150:/# service ssh status
 * sshd is running
(base) root@b22705345150:/# 