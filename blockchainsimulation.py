import hashlib
import time
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()
    def mine_block(self, difficulty=2):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
    def __str__(self):
        return (f"Block {self.index}:\n"
                f"  Timestamp      : {self.timestamp}\n"
                f"  Data           : {self.data}\n"
                f"  Previous Hash  : {self.previous_hash}\n"
                f"  Hash           : {self.hash}\n"
                f"  Nonce          : {self.nonce}\n")
genesis_block = Block(0, "Genesis Block", "0")
genesis_block.mine_block()
block1 = Block(1, "Block 1 Data", genesis_block.hash)
block1.mine_block()
block2 = Block(2, "Block 2 Data", block1.hash)
block2.mine_block()
blockchain = [genesis_block, block1, block2]

print("Original Blockchain:")
for block in blockchain:
    print(block)

# Challenge Part: Tamper with Block 1
print("\n Tampering with Block 1...")
block1.data = "Tampered Data"
block1.hash = block1.calculate_hash()

# Display blocks after tampering
print("Blockchain After Tampering:")
for block in blockchain:
    print(block)

# Verify validity of the chain
def is_chain_valid(chain):
    for i in range(1, len(chain)):
        current = chain[i]
        previous = chain[i - 1]
        if current.hash != current.calculate_hash():
            return False, f"Block {i}'s hash is invalid"
        if current.previous_hash != previous.hash:
            return False, f"Block {i}'s previous hash does not match Block {i-1}'s hash"
    return True, "Blockchain is valid"

is_valid, message = is_chain_valid(blockchain)
print(f"Chain Validity Check: {message}")
