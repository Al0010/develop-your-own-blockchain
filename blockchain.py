from block import Block

blockchain  = []

genesis_block = Block("Chancellow on the brink.......", ["Satoshi sent 1 BTC to CerryHash",
                                                        "Satoshi sent 10 BTC to MikyMouse",
                                                        "Satoshi sent 100 BTC to Harry Plotter"])

second_block = Block(genesis_block.block_hash, ["CerrHash sent 0.50 BTC to Frank Sinatra"])
third_block = Block(second_block.block_hash, ["MikyMouse sent 1.50 BTC to Donald Trump"])

print("Block Hash: Genesis Block")
print(genesis_block.block_hash)

print("Block Hash: Second Block")
print(second_block.block_hash)

print("Block Hash: Third Block")
print(third_block.block_hash)
