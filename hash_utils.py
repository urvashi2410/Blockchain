from hashlib import sha256
from json import dumps

def hash_string_256(string):
    return sha256(string).hexdigest()


def hash_block(block):
    '''Generates a hash for the given block'''
    hashable_block = block.__dict__.copy()
    return sha256(dumps(block, sort_keys=True).encode()).hexdigest()