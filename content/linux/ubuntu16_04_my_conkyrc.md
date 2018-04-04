Title:分享我的conkyrc
Date:2017-08-26 14:5
Tags:linux,ubuntu
Slug:ubuntu_my_conkyrc

分享我的conkyrc
#############


最近折腾了一下家里的电脑。装了ubuntu16.04，配置了conky。分享下自己的conkyrc。主要抄的[MyConky](http://martinsosic.com/linux/2015/07/06/my-conky.html)这篇。

```shell preset=mypreset lineno=True
use_xft yes
font Microsoft YaHei:size=8
xftfont Microsoft YaHei:size=8
override_utf8_locale yes
update_interval 1.0
own_window yes
own_window_type normal
own_window_transparent yes
own_window_hints undecorated,below,sticky,skip_taskbar,skip_pager
double_buffer yes
minimum_size 206 5
maximum_width 400
draw_shades yes
draw_outline no
draw_borders no
draw_graph_borders no
default_color ffffff
default_shade_color 000000
default_outline_color 000000
alignment top_right
gap_x 5
gap_y 30
cpu_avg_samples 2
uppercase no # set to yes if you want all text to be in uppercase

TEXT
${font Microsoft YaHei:style=Bold:pixelsize=30}${alignc}${time %H:%M:%S}
${font Microsoft YaHei:pixelsize=18}${alignc}${time %G年%b%d日 星期%a}${font Microsoft YaHei:pixelsize=12}
${color #ffd700}${hr 1}$color
${color #98c2c7}主机名:${color #db7093} $alignr$nodename
${color #98c2c7}内核: ${color #db7093}$alignr$kernel
${color #98c2c7}已运行时间: ${color #db7093}$alignr$uptime

${color #FFFFFF}GPU信息${hr 2}
${color #98c2c7}显存使用: ${color #db7093}${alignr}${exec nvidia-smi --query-gpu=memory.used --format=csv,noheader} / ${exec nvidia-smi --query-gpu=memory.total --format=csv,noheader}
${color #98c2c7}GPU风扇: ${color #db7093}${alignr}${exec nvidia-smi --query-gpu=fan.speed --format=csv,noheader}
${color #98c2c7}GPU温度: ${color #db7093}${alignr}${exec nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits} °C
${color #98c2c7}GPU使用率: ${color #db7093}${alignr}${exec nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits}%

${color #FFFFFF}CPU信息${hr 2}
${color #98c2c7}CPU温度: ${color #db7093}${alignr}${execi 1 sensors | grep 'temp1' | cut -c16-23}
${color #98c2c7}CPU使用率: ${color #db7093} $alignr$cpu%
${color #78af78}${cpubar cpu1 8,34}    ${cpubar cpu2 8,34}    ${cpubar cpu3 8,34}    ${cpubar cpu4 8,34}
${color #78af78}${cpubar cpu5 8,34}    ${cpubar cpu6 8,34}    ${cpubar cpu7 8,34}    ${cpubar cpu8 8,34}
${color #98c2c7}进程总数:$alignr${color }$processes ($running_processes 个运行中)
${color #98c2c7}CPU 最高占用:$alignr PID CPU%
${color #ddaa00} ${top name 1}$alignr ${top pid 1}${top cpu 1}
${color lightgrey} ${top name 2}$alignr ${top pid 2}${top cpu 2}
${color lightgrey} ${top name 3} $alignr${top pid 3}${top cpu 3}
${color lightgrey} ${top name 4} $alignr${top pid 4}${top cpu 4}
${color lightgrey} ${top name 5} $alignr${top pid 5}${top cpu 5}
${color #98c2c7}总内存:${color #4169e1}$alignr ${color}$mem ${color #98c2c7}已用/总${color}$memmax${color #4169e1}${color #db7093}$memperc%
${color #78af78}${membar}
${color #98c2c7}SWAP:${color} $alignr ${color}$swap${color #98c2c7}已用/总${color}$swapmax${color #4169e1}${color #db7093}$swapperc%
${color #78af78}${fs_bar 4 /dev/sda1}
${color #98c2c7}内存最高占用:$alignr PID MEM%
${color #ddaa00}${top_mem name 1}$alignr${top_mem pid 1}${top_mem mem 1}
${color}${top_mem name 2}$alignr${top_mem pid 2}${top_mem mem 2}
${color}${top_mem name 3}$alignr${top_mem pid 3}${top_mem mem 3}
${color}${top_mem name 4}$alignr${top_mem pid 4}${top_mem mem 4}
${color}${top_mem name 5}$alignr${top_mem pid 5}${top_mem mem 5}

${color #FFFFFF}NET信息${hr 2}
${color #98c2c7}网络 $alignr ${color #98c2c7}IP地址: ${color DDAA00}${addr enp3s0}${color}
${voffset 1}${color #98c2c7}eth0(上行):${color #db7093} ${upspeed enp3s0}s ${alignr}${color #98c2c7}总发送: ${color #db7093}${totalup enp3s0}
${upspeedgraph enp3s0 20,160 dcff82 ffffff}
${voffset 1}${color #98c2c7}eth0(下行):${color #ddaa00} ${downspeed enp3s0}/s ${alignr}${color #98c2c7}总接收:${color #ddaa00}${totaldown enp3s0}
${downspeedgraph enp3s0 20,160 dcff82 ffffff}

${color #FFFFFF}DISK信息${hr 2}
${color #98c2c7}根分区: ${color}${alignr}${fs_free /} 可用/总 ${fs_size /}
${color #78af78}${fs_bar 4 /}
${color #98c2c7}Data分区: ${color}${alignr}${fs_free /data} 可用/总 ${fs_size /data}
${color #78af78}${fs_bar 4 /data}
${color #ffd700}${hr 1}$color
```


效果是这样的～

![avatar](/static/img/ubuntu_desktop.png)
