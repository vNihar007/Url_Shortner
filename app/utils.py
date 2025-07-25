# TODO: Implement utility functions here
# Consider functions for:
# - Generating short codes
# - Validating URLs
# - Any other helper functions you need


import string , random , re 
import qrcode 
import os 


def generate_code(length=6):
    return "".join(random.choices(string.ascii_letters+string.digits , k = length))

def is_valid_url(url):
    # for basic validation 
    pattern = re.compile(r'https?://')
    return bool(pattern.match(url))

def generate_qr_code(data,code):
    folder = "static/qr_codes"

    if not os.path.exists(folder):
        os.makedirs(folder)

    filepath = os.path.join(folder,f"{code}.png")
    img = qrcode.make(data)
    img.save(filepath)
