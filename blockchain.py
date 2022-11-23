import hashlib

class Block:
  def __init__(self,data,prevhash,n):
    self.data = data
    self.prevhash = prevhash
    self.n = n 

  def get_hash(self):
    nonce = 0
    if self.prevhash == None:
      self.nonce = 0
      self.hash = hashlib.sha256(self.data.encode()).hexdigest()
      return 0
    
    pad = '0' * self.n 
    while True:
      hash = self.prevhash + str(self.data) + str(nonce)
      hash = hashlib.sha256(hash.encode()).hexdigest()
      if hash.startswith(pad):
        self.nonce = nonce
        self.hash = hash
        break 
      nonce += 1
    return 0

def block_chain_printer(block_chain):
  for block in block_chain:
    print(f'nonce : {block.nonce}')
    print(f'data : {block.data}')
    print(f'prevhash : {block.prevhash}')
    print(f'hash : {block.hash}')
    print()

GenesisBlock = Block('Genesis Block',None,4)
GenesisBlock.get_hash()
block_chain = [GenesisBlock]

for i in range(10):
  prior_block = block_chain[-1]
  NextBlock = Block(i + 1,prior_block.hash,4)
  NextBlock.get_hash()
  block_chain.append(NextBlock)

block_chain_printer(block_chain)

