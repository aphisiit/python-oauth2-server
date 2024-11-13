def read_file(filename):
  fh = open(filename, "r")
  try:
      return fh.read()
  finally:
      fh.close()

from authlib.jose import jwt
header = {'alg': 'RS256'}
payload = {'iss': 'Authlib', 'sub': '123'}
private_key = read_file('private.pem')
s = jwt.encode(header, payload, private_key)
public_key = read_file('public.pem')
claims = jwt.decode(s, public_key)
print(claims)
print(claims.header)
print(s)