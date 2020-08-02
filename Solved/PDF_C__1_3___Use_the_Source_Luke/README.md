# PDF-C (1/3): Use the Source Luke!
Web

## Challenge 

DESCRIPTION
I made my own OCR service for PDFs! There's more to this service than meets the eye though: can you find and query the hidden functionality in my code and retrieve the first flag?

Thankfully, you managed to recover the source code of the application before it went private on GitHub. The source code of the application can be found in website.zip. (you do not have to look up GitHub to solve any challenges in this series)

PLEASE DO NOT UPLOAD ANY SENSITIVE DATA ON THE SERVER, IT WILL BE COMPROMISED!

Visit the challenge at http://chals.whitehacks.ctf.sg:13003/


ATTACHED FILES
website.zip

## Solution

From server.js

	app.options('/admin', (req, res) => {
	  let body = req.body
	  if (body && body.admin && body.admin === 'WhiteHacksAdmin') {
	    let flag = fs.readFileSync('flag1.txt').toString('utf8')
	    flag = `<h1>${flag}</h1>`
	    flag += '<br/> but you are still not a real admin :>'
	    res.send(flag)
	  } else {
	    res.send('<h1 style="color:red;">swiper no swiping!</h1>')
	  }
	})

We have an OPTIONS request and then the parameter of admin.

	$ curl http://chals.whitehacks.ctf.sg:13003/admin -X OPTIONS --data admin=WhiteHacksAdmin
	<h1>WH2020{r3Ad_th3_s0urc3}</h1><br/> but you are still not a real admin :>

## Flag

	WH2020{r3Ad_th3_s0urc3}
