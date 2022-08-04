# Blockchain Getting Started

## Setup
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Lesson 1 - basics
learn cryptography basics
```bash
cd python/basics
python decode_encode.py
python learn_hashlib.py
python private_public_key.py
python decode_encode_2.py
```

## Lesson2 - create blockchain
learn blockchain basics
```bash
cd python/blockchain
python step1_create_chain
python step2_hashed
python step3_nonce
python step4_mining
```

## Lesson3 - create wallet
learn the wallet mechanism 
```bash
cd python/wallet
python step1_generate_keys.py
python step2_blockchain_address.py
python step3_transaction.py
python step4/wallet.py

```

## Lesson4 - blockchain server
learn the blockchain server API 
```bash
# create blockchain and wallet server
cd python/blockchain_server

cd step1
#terminal 1
python blockchain_server.py -p 5001

#terminal 2
python wallet_server.py


# create transaction api
cd step2
#terminal 1
python blockchain_server.py -p 5001

#terminal 2
python wallet_server.py

```


## Lesson5 - blockchain network
```bash
# create blockchain network
cd python/blockchain_network
python blockchain_server.py -p 5000
python blockchain_server.py -p 5001
python uitls.py # check your host_ip address and replace





```