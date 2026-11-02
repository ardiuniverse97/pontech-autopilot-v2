from modules.webchat.get_email_by_chat import get_email_by_chat
from modules.webchat.get_headers import get_headers
from modules.webchat.after_sales import after_sales
from modules.order.update_ship_pending import update_ship_pending
from modules.order.get_product_detail import get_product_detail
from modules.order.get_order_detail import get_order_detail
from modules.order.get_order_list import get_order_list
from modules.order.ship_pending import ship_pending
from modules.order.ship_order import ship_order
from modules.get_access_token import get_access_token
from modules.send_email import send_email
from modules.get_email import get_email
import modules.config as config
import requests
import time

# RUNNING (Pontech Autopilot v2)
if __name__ == '__main__':
  # (1) SET HEADERS & SHIP PENDING
  headers=get_headers(); content=requests.get(config.ship_pending_url).json()['content']; ship_pending(headers=headers, content=content)
  # (2) AUTOMATE NEW ORDERS
  for shop_id in config.shops:
    access_token=get_access_token(shop_id=shop_id)
    for order_sn in get_order_list(access_token=access_token, shop_id=shop_id):
      # (2.1) ORDER DETAIL
      order_detail=get_order_detail(access_token=access_token, shop_id=shop_id, order_sn=order_sn)
      # (2.2) GET EMAIL
      if 'message' in order_detail[order_sn]:
        email=get_email(text=order_detail[order_sn]['message'])
        if email == '': email=get_email_by_chat(headers=headers, buyer_user_id=order_detail[order_sn]['buyer_user_id'])
      else:
        email=get_email_by_chat(headers=headers, buyer_user_id=order_detail[order_sn]['buyer_user_id'])
      # (2.3) SEND EMAIL
      if email != '':
        products=get_product_detail(shop_id=shop_id, products=order_detail[order_sn]['products'])
        send_email(shop_id=shop_id, email=email, invoice=order_sn, products=products)
      else:
        content[order_sn]={
          'buyer_user_id': order_detail[order_sn]['buyer_user_id'],
          'buyer_username': order_detail[order_sn]['buyer_username'],
          'products': order_detail[order_sn]['products'],
          'shop_id': shop_id,
          'shop': config.shops[shop_id]['shop'],
          'timestamp': int(time.time())
        }
        update_ship_pending(content=content)
      # (2.4) SHIP ORDER
      ship_order(access_token=access_token, shop_id=shop_id, order_sn=order_sn)
      # (2.5) AFTER SALES
      after_sales(
        headers=dict(headers),
        shop_id=int(shop_id),
        buyer_user_id=int(order_detail[order_sn]['buyer_user_id']),
        buyer_username=str(order_detail[order_sn]['buyer_username']),
        email=str(email)
      )