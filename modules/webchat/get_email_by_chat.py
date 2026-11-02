from modules.webchat.spc_cds_chat import spc_cds_chat
from modules.get_email import get_email
import modules.config as config
import requests

# GET INBOX
def get_inbox(headers, buyer_user_id):
  params={
    "_uid": config._uid,
    "_v": "9.1.17",
    "SPC_CDS_CHAT": spc_cds_chat(headers=headers),
    "x-shop-region": "GLOBAL",
    "_api_source": "webchat"
  }
  payload={
    "direction": "older",
    "biz_id": 2,
    "on_message_received": True,
    "last_message_region": "ID",
    "last_received_message_id": "",
    "next_timestamp_nano": "",
    "shops": [{"region": "id"}]
  }
  databse=[]; url='https://seller.shopee.co.id/webchat/api/v1.2/subaccount/serving_mode/conversations'
  response=requests.post(url, params=params, headers=headers, json=payload).json()
  for item in response['conversations']:
    if item['to_id'] == buyer_user_id: databse.append({'id': item['id'], 'shop_id': item['shop_id']}); break
  return databse

# GET CONVERSATIONS
def get_conversations(headers, conversation_id, shop_id):
  params={
    "shop_id": shop_id,
    "offset": 0,
    "limit": 100,
    "direction": "older",
    "biz_id": 2,
    "on_message_received": 'true',
    "_uid": config._uid,
    "_v": "9.1.17",
    "SPC_CDS_CHAT": spc_cds_chat(headers=headers),
    "x-shop-region": "ID",
    "_api_source": "webchat"
  }
  database=[]; url=f"https://seller.shopee.co.id/webchat/api/v1.2/conversations/{conversation_id}/messages"
  response=requests.get(url=url, params=params, headers=headers).json()
  for item in response:
    if 'text' in item['content'] and '@' in str(item['content']['text']): database.append(item['content']['text']); break
  return database

# GET EMAIL BY CHAT
def get_email_by_chat(headers, buyer_user_id):
  database=[]
  for item in get_inbox(headers=headers, buyer_user_id=buyer_user_id):
    for message in get_conversations(headers=headers, conversation_id=item['id'], shop_id=item['shop_id']):
      database.append(message)
  if len(database) != 0: return get_email(text=database[0])
  else: return ''