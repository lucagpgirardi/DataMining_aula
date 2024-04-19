import hashlib
import time
import random
import json
from time import sleep

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def to_dict(self):
        return self.__dict__

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, proof):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof = proof
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        transactions_str = "".join(str(tx.__dict__) for tx in self.transactions)
        block_str = str(self.index) + self.previous_hash + str(self.timestamp) + transactions_str + str(self.proof)
        return hashlib.sha256(block_str.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.mining_difficulty = 2
        self.mining_reward = 100

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), [Transaction("sender", "receiver", 0)], 0)

    def get_latest_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, miner_address):
        new_block = Block(len(self.chain), self.get_latest_block().hash, int(time.time()), list(self.pending_transactions), 0)
        new_block.proof = self.proof_of_work(new_block)
        self.chain.append(new_block)
        self.pending_transactions = [Transaction(None, miner_address, self.mining_reward)]

    def create_transaction(self, sender, receiver, amount):
        self.pending_transactions.append(Transaction(sender, receiver, amount))

    def get_balance(self, address):
        balance = 0
        for block in self.chain:
            for tx in block.transactions:
                if tx.sender == address:
                    balance -= tx.amount
                if tx.receiver == address:
                    balance += tx.amount
        return balance

    def proof_of_work(self, block):
        while block.hash[:self.mining_difficulty] != '0' * self.mining_difficulty:
            block.proof += 1
            block.hash = block.calculate_hash()
        return block.proof

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

if __name__ == "__main__":
    # Create a new Blockchain
    blockchain = Blockchain()

    # Create new transactions
    for i in range(50):
        sender = "User" + str(random.randint(1, 10))
        receiver = "User" + str(random.randint(1, 10))
        amount = random.randint(1, 100)
        blockchain.create_transaction(sender, receiver, amount)

    # Mine the transactions and print each block's info
    for i in range(50):
        print("Starting the miner...")
        blockchain.mine_pending_transactions("Miner1")
        print("Balance of Miner1 is", blockchain.get_balance("Miner1"))
        print("Block #{} has been added to the blockchain!".format(blockchain.get_latest_block().index))
        print("Hash: {}\\n".format(blockchain.get_latest_block().hash))
        print("Block Information: {}\\n".format(json.dumps(blockchain.get_latest_block().__dict__, default=lambda o: o.to_dict(), indent=4)))
        print("Blockchain valid: {}\\n".format(blockchain.is_chain_valid()))
        sleep(1)