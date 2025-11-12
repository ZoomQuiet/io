# debain 下轻量桌面
> [Opus: 如何安装并从 macOS 远程接入 Debain 的桌面](https://claude.ai/share/bc7de77d-f8b0-41cc-9049-872957371bc7)


## background
> 事儿是这么开始的..

有一系列项目哈, 可以使用某个学校的内部机房资源,
当然, 这种内部主机必须进行合理的安全隔离;

所以, 俺想上去部署, 调试, 就得走 VPN 了;

但是, 同时, 日常使用各种墙外死活也得科学上网..


## goal
> 问题来了..


- 国外资源, 走的是小火箭, 根据规则将相关请求从海外主机代理
- 校内资源, 走的是专线VPN, 也就是将当前主机拉到一个虚拟局域网
- 必须两种网络要求同时满足, 并不影响 VSCode 使用 SSH 远程工程能力, 直接打开远程主机目录进行调试..


## logging
> 最简单粗暴的方法...


既然网络配置复杂到不是一般人能搞定的, 那就不折腾:

- MBP 本身还是小火箭经典翻越
- 访问校内资源的开发行为, 迁移到另外一台 home server 即可..


所以, 问题的解决就变成了如何在另外一台 mini PC 上部署合适的桌面以及 VPN 来完成可以随时从 MBP 桌面进入本地内网另外一个开发桌面中?

现成的: `ASUS UN65U` 

```
$ neofetch
       _,met$$$$$gg.          zoomq@debian500
    ,g$$$$$$$$$$$$$$$P.       ---------------
  ,g$$P"     """Y$$.".        OS: Debian GNU/Linux 12 (bookworm) x86_64
 ,$$P'              `$$$.     Host: UN65U
',$$P       ,ggs.     `$$b:   Kernel: 6.1.0-28-amd64
`d$$'     ,$P"'   .    $$$    Uptime: 1 day, 15 hours, 3 mins
 $$P      d$'     ,    $$P    Packages: 1612 (dpkg)
 $$:      $$.   -    ,d$$'    Shell: bash 5.2.15
 $$;      Y$b._   _,d$P'      Terminal: /dev/pts/0
 Y$$.    `.`"Y$$$$P"'         CPU: Intel i3-7100U (4) @ 2.400GHz
 `$$b      "-.__              GPU: Intel HD Graphics 620
  `Y$$                        Memory: 1790MiB / 7812MiB
   `Y$$.
     `$$b.
       `Y$$b.
          `"Y$b._
              `"""
```

资源足够, 嘦:

- 安装桌面
- 安装 VNC 类似服务
- 安装 WireGuard 平替服务
- 安装 VSCode
- 配置好相关的一切...


### 桌面
> 当然是小巧的 Xfce

检验当前桌面环境:
```
# 查看当前显示管理器状态
systemctl status display-manager

# 查看已安装的桌面环境会话
ls /usr/share/xsessions/

# 检查当前运行的桌面环境
echo $XDG_CURRENT_DESKTOP

# 查看 X Server 是否运行
ps aux | grep -E 'X|Wayland'

# 检查已安装的桌面包
dpkg -l | grep -E 'desktop|xfce|gnome|kde|lxde|lxqt|mate|cinnamon'
```

> 技巧: 一定要先配置好加速的软件仓库镜像
> ..netselect-apt 是一个轻量工具，可自动测试 Debian 镜像源的速度，并生成最优的 sources.list 配置文件。

```
sudo apt update && sudo apt install netselect-apt -y

# 测试并生成最快源配置
sudo netselect-apt bookworm

# 替换系统源配置
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak  # 备份
sudo cp sources.list /etc/apt/sources.list  # 替换为最快源配置
sudo apt update  # 更新缓存生效
```

> ..apt-select 是另一个命令行工具，支持手动选择测试的镜像源区域（如仅国内源），并生成配置文件。

```
sudo apt install python3-pip -y
sudo pip3 install apt-select

sudo apt-select --country CN  # 仅测试中国的镜像源

# 按提示选择最快的源，自动生成 sources.list..
```



> 安装 Xfce 轻量级桌面管理系统(WM)

```
# 更新软件包列表
sudo apt update

# 升级已安装的包
sudo apt upgrade -y


## 用 tasksel 安装 XFCE
# 安装 tasksel 工具
sudo apt install tasksel -y

# 运行 tasksel 并选择 XFCE
sudo tasksel

# 或直接安装 XFCE（不进入交互界面）
sudo apt install task-xfce-desktop -y

## 用 apt 直接安装
# 最小化安装
sudo apt install xfce4 -y

# 完整安装（包含额外工具）
sudo apt install xfce4 xfce4-goodies -y
```


### VNC 为远程桌面服务
> 但是, 日常有各种粘贴问题..


```
# 安装 TightVNC
sudo apt install tightvncserver -y

# 设置 VNC 密码
vncpasswd

# 创建 VNC 启动配置
nano ~/.vnc/xstartup

# 添加以下内容：
#!/bin/bash
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
startxfce4 &

# 设置执行权限
chmod +x ~/.vnc/xstartup

# 启动 VNC 服务器
vncserver -geometry 1280x720 -depth 24
```

> 注意, 要根据本地显示器分辨率来启动合适的桌面大小

比如俺用的: 
```
$ vncserver -geometry 1920x1080 -depth 24

New 'X' desktop is debian500:1

Starting applications specified in /home/zoomq/.vnc/xstartup
Log file is /home/zoomq/.vnc/debian500:1.log
```

对应常用管理指令:
```
# 1. 查看命令
vncserver -list                      # 列出当前用户的会话
ps aux | grep -i vnc                 # 查看所有 VNC 进程
ls ~/.vnc/*.pid                      # 查看 PID 文件
lsof -i :5901                        # 查看端口占用

# 2. 启动命令
vncserver :1                         # 启动显示 :1
vncserver :1 -geometry 1920x1080    # 指定分辨率
vncserver :1 -depth 24              # 指定色深
vncserver :1 -localhost no          # 允许远程连接

# 3. 停止命令
vncserver -kill :1                   # 停止显示 :1
vncserver -kill :*                   # 停止所有（某些版本支持）
killall Xvnc                         # 终止所有 VNC 进程

# 4. 清理命令
vncserver -clean                     # 清理锁文件（某些版本）
rm -f ~/.vnc/*.pid                   # 手动清理 PID 文件
rm -f /tmp/.X1-lock                  # 清理 X 锁文件
rm -f /tmp/.X11-unix/X1              # 清理 Unix socket
```

> 记住，显示号 :1 对应端口 5901，:2 对应 5902，以此类推


>> 使用 SSH 隧道（最安全）：

```
# 在客户端创建 SSH 隧道
ssh -L 3389:localhost:3389 user@server_ip
```

然后用 VNC 客户端连接到 localhost:3389


### TODO:双向剪贴板共享

>> 配置 macOS 端 RealVNC Viewer
确保客户端启用剪贴板共享，否则无法接收 / 发送剪贴板内容：

- 打开 RealVNC Viewer，连接到 Debian 的 TightVNC 服务（IP:5901，如 192.168.1.100:5901）。
- 连接成功后，点击顶部菜单栏 Connection → Properties（属性）。
- 切换到 Options 标签，找到 Clipboard 选项，选择 Share clipboard with remote（与远程共享），并确认方向为 Bidirectional（双向）。
- 关闭窗口，无需重新连接（实时生效）。

>>> 测试双向剪贴板是否生效

- 本地 → 远程：在 macOS 复制一段文本（Ctrl+C 或 Cmd+C），在 Debian 桌面的文本编辑器（如 gedit、Mousepad）中粘贴（Ctrl+V）。
- 远程 → 本地：在 Debian 复制文本（Ctrl+C），在 macOS 文本工具（如备忘录、终端）中粘贴（Cmd+V）。


```
# 测试 CLIPBOARD 剪贴板（Ctrl+C 复制的内容）
echo "测试远程→本地" | xclip -selection clipboard  # 写入剪贴板
xclip -selection clipboard -o  # 读取剪贴板，若输出内容则正常

# 测试 PRIMARY 剪贴板（选中即复制的内容）
echo "测试选中复制" | xsel -p  # 写入 PRIMARY
xsel -p -o  # 读取，正常则输出内容
```



### WireGuard 平替
> ..Debian 12 上 WireGuard 的最佳替代就是 WireGuard 本身

```
sudo apt update && sudo apt install wireguard -y

# 生成密钥对
wg genkey | tee privatekey | wg pubkey > publickey

sudo nano /etc/wireguard/wg0.conf

```

> 配置模板:

```
[Interface]
PrivateKey = <你的私钥>
Address = 10.0.0.2/32
DNS = 1.1.1.1

[Peer]
PublicKey = <对端公钥>
Endpoint = <对端IP>:51820
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
```

启用:
```
sudo wg-quick up wg0

# ✅ 检查连接状态
sudo wg show

# 🧪 检验是否代理成功
curl ifconfig.me
```

>> wg-quick 脚本默认使用 resolvconf 来管理 DNS 设置

```
sudo apt update
sudo apt install resolvconf -y
sudo systemctl enable --now resolvconf

```

>>> TODO:WireGuard Web UI

#### wg-easy（Docker 版，5 分钟上桌）

准备 Docker:

```
curl -fsSL https://get.docker.com | sudo bash
sudo usermod -aG docker $USER && newgrp docker
```

一键拉起 wg-easy
```
docker run -d \
  --name=wg-easy \
  -e WG_HOST=`curl -s ifconfig.me` \
  -e PASSWORD=SupStrong@2025 \
  -v ~/.wg-easy:/etc/wireguard \
  -p 51820:51820/udp \
  -p 51821:51821/tcp \
  --cap-add=NET_ADMIN \
  --cap-add=SYS_MODULE \
  --sysctl net.ipv4.conf.all.src_valid_mark=1 \
  --sysctl net.ipv4.ip_forward=1 \
  --restart unless-stopped \
  ghcr.io/wg-easy/wg-easy:15
```

放行端口（如启用了 nftables/ufw）

> sudo ufw allow 51820/udp && sudo ufw allow 51821/tcp


- 浏览器访问 http://<服务器IP>:51821 → 输入密码即可进入。
- 点击「New Client」→ 生成二维码/配置文件 → 手机 WireGuard App 扫码导入。
- 客户端连接后刷新页面，能看到「Last seen」及实时流量，说明隧道已通 。



### VSCode
> 原先想用 Zed 来替代的, 结果无法安装..

M$ 的产品, 别的不说, 软件工程至少是过关的,
安装很流畅, 立即就能使用;

只是, 字体是个大问题, 要小心折腾一下:

```
# 查阅所有已安装字体
fc-list

# 查阅所有等宽字体
fc-list :monospace
```

一般而言对于编程友好的字体, 没有中文支持, 有中文支持的不一定有 Nerd 符号..

而所有都吻合期待的非常少,可以随时下载到并长期维护有保证的,
推荐: `更纱黑体 Mono SC Nerd ` （等宽简体中文版本，带 Nerd Font 图标补丁）

*[be5invis/Sarasa-Gothic](https://github.com/be5invis/Sarasa-Gothic)* 官方仓库

以及官方推荐的中国镜像:

- TUNA (CN): https://mirrors.tuna.tsinghua.edu.cn/github-release/be5invis/Sarasa-Gothic
- NJU (CN): https://mirror.nju.edu.cn/github-release/be5invis/Sarasa-Gothic


```
# 创建临时目录存放字体
mkdir -p ~/sarasa-nerd-font && cd ~/sarasa-nerd-font

# 下载最新版本的更纱黑体 Nerd Font 包（以当前最新版本为例，可替换为实际最新版）
# 版本号可在 https://github.com/be5invis/Sarasa-Gothic/releases 查看
wget https://github.com/be5invis/Sarasa-Gothic/releases/download/v0.41.5/sarasa-gothic-nerd-fonts-v0.41.5.zip

# 解压
unzip sarasa-gothic-nerd-fonts-v0.41.5.zip

# 查看包含的 Mono SC Nerd 字体（文件名通常包含 "SarasaMonoSC-Nerd"）
ls | grep "SarasaMonoSC-Nerd"

# 创建用户级字体目录（如果不存在）
mkdir -p ~/.local/share/fonts/sarasa-mono-sc-nerd

# 复制筛选出的字体文件到该目录
cp SarasaMonoSC-Nerd-*.ttf ~/.local/share/fonts/sarasa-mono-sc-nerd/

fc-cache -f -v ~/.local/share/fonts  # 用户级安装，更新用户字体缓存
# 系统级安装则运行：sudo fc-cache -f -v /usr/local/share/fonts


# 最后检验安装成果
$ fc-list | grep "Sarasa"
/usr/local/share/fonts/sarasa-mono-sc/SarasaMonoSC-LightItalic.ttf: 等距更纱黑体 SC,Sarasa Mono SC,Sarasa Mono SC Light,等距更纱黑体 SC Light:style=Light Italic,Italic
/usr/local/share/fonts/sarasa-mono-sc/SarasaMonoSC-Italic.ttf: 等距更纱黑体 SC,Sarasa Mono SC:style=Italic
/usr/local/share/fonts/sarasa-mono-sc/SarasaMonoSC-ExtraLightItalic.ttf: 等距更纱黑体 SC,Sarasa Mono SC,Sarasa Mono SC XLight,等距更纱黑体 SC XLight:style=ExtraLight Italic,Italic
/usr/local/share/fonts/sarasa-mono-sc/SarasaMonoSC-BoldItalic.ttf: 等距更纱黑体 SC,Sarasa Mono SC:style=Bold Italic
/usr/local/share/fonts/sarasa-mono-sc/SarasaMonoSC-Regular.ttf: 等距更纱黑体 SC,Sarasa Mono SC:style=Regular
/usr/local/share/fonts/sarasa-mono-sc/SarasaMonoSC-Light.ttf: 等距更纱黑体 SC,Sarasa Mono SC,Sarasa Mono SC Light,等距更纱黑体 SC Light:style=Light,Regular
/usr/local/share/fonts/sarasa-mono-sc/SarasaMonoSC-Bold.ttf: 等距更纱黑体 SC,Sarasa Mono SC:style=Bold
/usr/local/share/fonts/sarasa-mono-sc/SarasaMonoSC-ExtraLight.ttf: 等距更纱黑体 SC,Sarasa Mono SC,Sarasa Mono SC XLight,等距更纱黑体 SC XLight:style=ExtraLight,Regular
/usr/local/share/fonts/sarasa-mono-sc/SarasaMonoSC-SemiBoldItalic.ttf: 等距更纱黑体 SC,Sarasa Mono SC,Sarasa Mono SC SemiBold,等距更纱黑体 SC SemiBold:style=SemiBold Italic,Italic
/usr/local/share/fonts/sarasa-mono-sc/SarasaMonoSC-SemiBold.ttf: 等距更纱黑体 SC,Sarasa Mono SC,Sarasa Mono SC SemiBold,等距更纱黑体 SC SemiBold:style=SemiBold,Regular
```



### 小结


- 直接问 LLM 比一个个钻官方文档靠谱的多, 只是要注意, 具体指令还是得先对比一下官方文档, 毕竟有时差
- 字体是个大问题..所以, 解决 Linux 中的中文字体, 不如, 直接从 macOS 上远程进入 Linux 本地主机, 再继续 SSH 到校内主机, 进行双重远程..
- RustDesk 很时尚, 但是, 无论客户端还是本地服务, 都不是那么简单可以安装配置成功的, 使用传统 VNC 就好
    + 其它还有推荐的:
    + NoMachine 太丑
    + TeamViewer 收费
    + xrdp 只能 windows 
    + AnyDesk Linux 上安装不能


## refer.

- [Lightweight desktop environment for Debian 12](https://claude.ai/share/bc7de77d-f8b0-41cc-9049-872957371bc7)
- [Kimi: wireguard的替代](https://www.kimi.com/share/19a70a45-6a52-8b0b-8000-0000fd2454e0)
- [doubao:Debian 软件仓库镜像配置](https://www.doubao.com/thread/wb3ede00f98d337d4)



## tracing

- 251112 DAMA pub
- 251111 DAMA init.




```
nn 6020

          _~∽*`~_
      () /  ^ ◴  \ (/
        '_   v   _'
        | '--⌄--' )

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```
