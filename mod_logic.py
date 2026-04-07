import json
import os

path = 'source_folder/assets/data/profile/wallet.json'

if os.path.exists(path):
    with open(path, 'r') as f:
        data = json.load(f)
    
    # ID 1 is usually coins, ID 2 is usually keys
    # We set them to 2 billion (stay under 2.1b to avoid crashing)
    for currency in data.get('currencies', {}):
        data['currencies'][currency]['value'] = 2000000000

    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
