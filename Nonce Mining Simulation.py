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
        value = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        print(f"⛏️  Mining Block {self.index} with difficulty {difficulty}...")
        target = '0' * difficulty
        start_time = time.time()

        attempts = 0
        while not self.hash.startswith(target):
            self.nonce += 1
            attempts += 1
            self.hash = self.calculate_hash()

        end_time = time.time()
        print(f"\n Block {self.index} mined!")
        print(f"  Nonce attempts : {attempts}")
        print(f" Time taken      : {end_time - start_time:.4f} seconds")
        print(f" Final Hash     : {self.hash}")
        print(f" Final Nonce    : {self.nonce}\n")

# Set the difficulty level (e.g., 4 means hash must start with "0000")
difficulty = 4

# Simulate mining a block
block = Block(0, "Nonce Mining Simulation", "0")
block.mine_block(difficulty)
