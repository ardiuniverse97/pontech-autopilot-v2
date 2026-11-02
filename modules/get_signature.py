import modules.config as config
import hashlib
import hmac

# SET SIGNATURE
def set_signature(base_string):
    return hmac.new(config.partner_key.encode("utf-8"), base_string.encode("utf-8"), hashlib.sha256).hexdigest()

# GET SIGNATURE
def get_signature(path, timestamp, access_token=None, shop_id=None):
    base_string=f"{config.partner_id}{path}{timestamp}"
    if access_token != None: base_string += f"{access_token}{shop_id}"
    return set_signature(base_string=base_string)