import base64
import re

def universal_decoder(data):
    count = 0
    while True:
        # Look for Base64 patterns or common wrappers
        match = re.search(r"(['\"])([A-Za-z0-9+/=]{10,})\1", data)
        if not match:
            break
            
        encoded_str = match.group(2)
        try:
            decoded_bytes = base64.b64decode(encoded_str)
            data = decoded_bytes.decode('utf-8', errors='ignore')
            count += 1
            print(f"[+] Layer {count} decoded...")
        except:
            break
            
    return data

# Replace this with the string or file content you want to decode
encoded_input = input("Paste the encoded string or script content: ")
result = universal_decoder(encoded_input)

print("\n--- DECODED OUTPUT ---")
print(result)
