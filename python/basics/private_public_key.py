"""Setup
# python -m pip install --upgrade pip
# pip install -r requirements.txt
"""

from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend


key = rsa.generate_private_key(
    backend=crypto_default_backend(),
    public_exponent=65537,
    key_size=2048
)

private_key = key.private_bytes(
    crypto_serialization.Encoding.PEM,
    crypto_serialization.PrivateFormat.PKCS8,
    crypto_serialization.NoEncryption()
)

print("PRIVATE KEY", "\n", private_key, "\n")

with open('privat.key', 'w') as f:
    f.write(str(private_key))
  

public_key = key.public_key().public_bytes(
    crypto_serialization.Encoding.OpenSSH,
    crypto_serialization.PublicFormat.OpenSSH
)

print("PUBLIC KEY", "\n", public_key, "\n")

with open('public.key', 'w') as f:
    f.write(str(public_key))