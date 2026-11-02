from modules.webchat.get_email_by_chat import get_email_by_chat
from modules.webchat.after_sales import after_sales
from modules.order.update_ship_pending import update_ship_pending
from modules.order.get_product_detail import get_product_detail
from modules.send_email import send_email

# SHIP PENDING
def ship_pending(headers, content):
  for order_sn in list(content):
    shop_id=content[order_sn]['shop_id']
    products=content[order_sn]['products']
    buyer_user_id=content[order_sn]['buyer_user_id']
    buyer_username=content[order_sn]['buyer_username']
    email=get_email_by_chat(headers=headers, buyer_user_id=content[order_sn]['buyer_user_id'])
    if email != '':
      # (1) PRODUCT DETAIL
      products=get_product_detail(shop_id=shop_id, products=products)
      # (2) SEND EMAIL
      send_email(shop_id=shop_id, email=email, invoice=order_sn, products=products)
      # (3) UPDATE SHIP PENDING
      del content[order_sn]; update_ship_pending(content=content)
      # (4) AFTER SALES
      after_sales(
        headers=dict(headers),
        shop_id=int(shop_id),
        buyer_user_id=int(buyer_user_id),
        buyer_username=str(buyer_username),
        email=str(email)
      )