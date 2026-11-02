import modules.config as config
import requests

# SEND EMAIL
def send_email(shop_id, email, invoice, products):
  requests.post(
    url=config.email_sender_url, 
    json={
      'shop_username': config.shops[shop_id]['username'],
      'shop': config.shops[shop_id]['shop'],
      'email': email,
      'invoice': invoice,
      'products': products,
      'affiliate': config.shops[shop_id]['affiliate']
    }
  )
  # # LOG PROGRESS
  # print(f"[{config.shops[shop_id]['username']}] [send email] [0] - berhasil kirim ke {email}")
