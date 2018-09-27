import pexpect

ping = pexpect.spawn('ping 172.17.1.1 -c 5')
result = ping.expect([pexpect.EOF, pexpect.TIMEOUT])
print(ping.before)
