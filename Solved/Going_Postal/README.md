# Going Postal
Web

## Challenge 

DESCRIPTION
A new delivery service is in town, but the site doesn't seem to be fully complete. Maybe there's a secret administrative interface that we can access somehow?

Visit the challenge at http://chals.whitehacks.ctf.sg:13001/

Author: waituck


## Solution

Find admin text

	$ curl -s http://chals.whitehacks.ctf.sg:13001/ | grep admin
	<li><a href="/admin_s3kr1t_backd0Or" class="nav-link">Admin</a></li>

Then find the flag

	$ curl http://chals.whitehacks.ctf.sg:13001/admin_s3kr1t_backd0Or
	GET method not supported

	$ curl http://chals.whitehacks.ctf.sg:13001/admin_s3kr1t_backd0Or -X POST
	WH2020{POST4l_s3rv1ces}
