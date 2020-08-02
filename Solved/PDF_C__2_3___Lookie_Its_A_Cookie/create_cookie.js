'use strict';

const express = require('express');
const cookieSession = require('cookie-session')


// Constants
const PORT = 8080;
const HOST = '0.0.0.0';
const OUTPUT_DIR = "output";

// App
const app = express();

app.use(cookieSession({
  name: 'session',
  keys: ['🎌💩💩💩💩🎌']
}))

app.use(express.static('static'));

app.get('/', (req, res) => {
  req.session.admin = true
  res.end(req.session.admin + '.')
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
