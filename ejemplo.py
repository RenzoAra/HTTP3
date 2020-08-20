import http3
r = http3.get('http://www.ucp.edu.ar')

"""r
r.status_code
r.protocol
r.headers['content-type']
r.text"""

print(r.protocol)
