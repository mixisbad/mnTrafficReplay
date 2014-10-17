mnTrafficReplay
===============

Note: This hasn't been tested yet.
---

Currently parse_log.sh uses sed to grab the important parts of each request from the log file. $log_pattern is currently set to retrieve info from nginx access logs. You'll need to change it for other formats.

Run your log file through ```parse_log.sh``` then, use the command below to replay the traffic.

```
#!bash
python ReplayTraffic.py num_servers controller_ip server_link_speed client_link_speed < parsed_log_file.log
```
