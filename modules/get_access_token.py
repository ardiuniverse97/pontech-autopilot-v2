import modules.config as config
import requests

# GET ACCESS TOKEN
def get_access_token(shop_id):
  return requests.get(config.access_token_url).json()['content'][shop_id]['access_token']