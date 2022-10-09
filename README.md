## Python bot
Echo-bot.

Converting BYN to RUB on real-time market stocks.

### Install
```bash
git clone https://github.com/nudimannui4e/pythonBynRubBot.git
cd pythonBynRubBot/
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requironments.txt
```

### Loop start with SystemD
```
/lib/systemd/system/pythonBynRubBot.service
```
```bash
[Unit]
Description=BYN to RUB bot
After=network.target

[Service]
ExecStart=/root/pythonBynRubBot/venv/bin/python main.py
ExecReload=/root/pythonBynRubBot/venv/bin/python main.py
WorkingDirectory=<PATH-TO-FOLDER>/pythonBynRubBot/
KillMode=process
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
systemctl start pythonBynRubBot.service
systemctl enable pythonBynRubBot.service
```
