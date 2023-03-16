import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part 1 - Building the Blockchain

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')  #Genesis Block
        
    
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1, #Block position
                 'timestamp': str(datetime.datetime().now()), #Time where the block was created
                 'proof' : proof, #proof 
                 'previous_hash': previous_hash #previous block hash
                 }
        self.chain.append(block)
        return block