import base64
data = "aGkgbmFtYSBzYXlhIHdpbmR1"
# Decode the base64 encoded string
decode_data = base64.b64decode(data)
# Decode the bytes to string
print(decode_data)