from modules.get_signature import get_signature
import modules.config as config
import requests
import time

# GET ORDER LIST
def get_order_list(access_token, shop_id):
  path='/api/v2/order/get_order_list'
  timestamp=int(time.time())
  signature=get_signature(path=path, timestamp=timestamp, access_token=access_token, shop_id=shop_id)
  params={
    'partner_id': config.partner_id,
    'timestamp': timestamp,
    'access_token': access_token,
    'shop_id': shop_id,
    'sign': signature,
    'order_status': 'READY_TO_SHIP',
    'time_range_field': 'create_time',
    'time_from': timestamp-86400,
    'time_to': timestamp,
    'page_size': 100
  }
  database=[]; response=requests.get(url='https://partner.shopeemobile.com' + path, params=params).json()
  for item in response['response']['order_list']:
    order_sn=item['order_sn']; database.append(order_sn)
    # # LOG PROGRESS
    # print(f"[{config.shops[shop_id]['username']}] [order list] [{len(database)}] - {order_sn}")
  return database
