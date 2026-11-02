from modules.webchat.handle_conversation import handle_conversation
from modules.webchat.contact_buyer import contact_buyer
from modules.webchat.get_payload import get_payload
from modules.webchat.get_params import get_params
import modules.config as config
import requests

# AFTER SALES
def after_sales(headers, shop_id, buyer_user_id, buyer_username, email):
  if email == '': content=f'Halo Kak! 😊 Bantu info email untuk pengiriman produk digital kakak yaa. Terimakasih! 🙏'
  elif email != '': content="Halo Kak! 😊 Terimakasih sudah belanja di toko kami. Pesanan sudah dikirimkan ya. Jika belum menerima, tolong bantu cek di folder spam/sampah kak. Terimakasih! 🙏"
  conversation_id=contact_buyer(headers=headers, shop_id=shop_id, buyer_user_id=buyer_user_id)
  requests.post(
    url='https://seller.shopee.co.id/webchat/api/v1.2/messages',
    headers=headers,
    params=get_params(headers=headers),
    json=get_payload(shop_id=shop_id, buyer_user_id=buyer_user_id, content=content)
  )
  handle_conversation(headers=headers, shop_id=shop_id, conversation_id=conversation_id, status='closed')
  # LOG PROGRESS
  print(f"[{config.shops[str(shop_id)]['username']}] [chat buyer] [0] - berhasil chat ke {buyer_username}")