from modules.get_signature import get_signature
import modules.config as config
import requests
import time

# GET ORDER DETAIL
def get_order_detail(access_token, shop_id, order_sn):
  path='/api/v2/order/get_order_detail'
  timestamp=int(time.time())
  signature=get_signature(path=path, timestamp=timestamp, access_token=access_token, shop_id=shop_id)
  params={
    'partner_id': config.partner_id,
    'timestamp': timestamp,
    'access_token': access_token,
    'shop_id': shop_id,
    'sign': signature,
    'order_sn_list': order_sn,
    'request_order_status_pending': 'false',
    'response_optional_fields': 'buyer_user_id,buyer_username,item_list'
  }
  database={}; response=requests.get(url='https://partner.shopeemobile.com' + path, params=params).json()
  for item in response['response']['order_list']:
    products=[]; buyer_user_id=item['buyer_user_id']; buyer_username=item['buyer_username']
    for product in item['item_list']:
      if product['model_sku'] == '': products.append(product['item_sku'])
      else: products.append(product['model_sku'])
      # # LOG PROGRESS
      # print(f"[{config.shops[shop_id]['username']}] [items list] [{len(products)}] - {products[-1]}")
    database[order_sn]={'buyer_user_id': buyer_user_id, 'buyer_username': buyer_username, 'products': products}
    if item['message_to_seller'] != '': database[order_sn]['message']=item['message_to_seller']
  return database
