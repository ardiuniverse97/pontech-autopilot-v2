from modules.get_signature import get_signature
import modules.config as config
import requests
import time

# SHIP ORDER
def ship_order(access_token, shop_id, order_sn):
  path='/api/v2/logistics/ship_order'
  timestamp=int(time.time())
  signature=get_signature(path=path, timestamp=timestamp, access_token=access_token, shop_id=shop_id)
  params={
    'partner_id': config.partner_id,
    'timestamp': timestamp,
    'access_token': access_token,
    'shop_id': shop_id,
    'sign': signature,
  }
  requests.post(
    url='https://partner.shopeemobile.com' + path,
    headers={'Content-Type': 'application/json'},
    params=params,
    json={'order_sn': order_sn, config.shops[shop_id]['ship']: {}}
  )
  # LOG PROGRESS
  print(f"[{config.shops[shop_id]['username']}] [ship order] [0] - berhasil ubah status dikirim")