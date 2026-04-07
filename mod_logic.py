import json
import os

# Path where Apktool will unpack the files
target_file = 'decompiled/assets/data/inventory/wallet.json'

if os.path.exists(target_file):
    with open(target_file, 'r') as f:
        data = json.load(f)

    # Set keys and coins to the 32-bit integer limit
    for item in data.get('currencies', {}):
        data['currencies'][item]['value'] = 2147483647

    with open(target_file, 'w') as f:
        json.dump(data, f, indent=4)
    print("Successfully maxed out coins and keys!")