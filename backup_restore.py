import base64
import gzip
import requests

response = requests.get('https://hackattic.com/challenges/backup_restore/problem?access_token=9f9f52baaa6de505')
compressed_dump = response.json()
base64_data = compressed_dump['dump']
base64_bytes = base64_data.encode('utf-8')
dump_bytes = base64.b64decode(base64_bytes)
dump_data = gzip.decompress(dump_bytes).decode('utf-8')

print(dump_data)