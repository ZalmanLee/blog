Title:centos7安装supervisor
Date:2017-08-25 12:52
Tags:linux,centos
Slug:centos7_install_supervisor

Centos7安装supervisor
####################

supervisor已经安装过很多遍了，写在这里做个备忘。

安装pip

    sudo yum -y install epel-release
    sudo yum -y install python-pip

安装supervisor

    sudo pip install supervisor

配置supervisord

    sudo mkdir -p /etc/supervisord/conf.d
    sudo echo_supervisord_conf > /etc/supervisord.conf
    sudo echo "files = /etc/supervisord/conf.d/*.ini" >> /etc/supervisord.conf

新建supervisord.service在/usr/lib/systemd/system下

    [Unit]
    Description=supervisord - Supervisor process control system for UNIX
    Documentation=http://supervisord.org
    After=network.target

    [Service]
    Type=forking
    ExecStart=/bin/supervisord -c /etc/supervisord.conf
    ExecReload=/bin/supervisorctl $OPTIONS reload
    ExecStop=/bin/supervisorctl $OPTIONS shutdown
    User=root
    KillMode=process
    Restart=on-failure
    RestartSec=60s

    [Install]
    WantedBy=multi-user.target

启动supervisord

    sudo systemctl start supervisord.service

设置开机启动

    sudo systemctl enable supervisord.service
