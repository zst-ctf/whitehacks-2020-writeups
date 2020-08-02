#!/usr/bin/env python3
import socket
import telnetlib

if __name__ == '__main__':
	# Connect to program
	s = socket.socket()
	s.connect(('chals.whitehacks.ctf.sg', 11001))
	t = telnetlib.Telnet()
	t.sock = s

	t.read_until(b'Just to be sure, can you say \'')
	word = t.read_until(b'\'')[:-1]
	print(word)
	
	t.write(word + b'\n')
	t.interact()