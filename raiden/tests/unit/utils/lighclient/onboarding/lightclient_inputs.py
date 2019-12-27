from eth_utils import encode_hex, decode_hex
from raiden.utils.signer import LocalSigner

private_key = decode_hex('0x55a7041a7daac35f1b3c9052fbd8bc1298625a05cb7dec68f91eee0d6a8062ee')
display_name_to_sign = "@0x7003c65bd39c5b3de3b5b3c0423e4c36ff1dab71:raidentransport.exchangeunion.com"
password_to_sign = "raidentransport.exchangeunion.com"
seed_retry = "seed"

signer = LocalSigner(private_key)

print(f'signed_seed_retry: {encode_hex(signer.sign(seed_retry.encode()))}')
print(f'signed_display_name: {encode_hex(signer.sign(display_name_to_sign.encode()))}')
print(f'signed_password: {encode_hex(signer.sign(password_to_sign.encode()))}')




