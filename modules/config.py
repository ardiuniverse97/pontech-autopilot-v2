import json
import os

# (1) SHOP AUTHORIZATION
partner_id=os.environ["PARTNER_ID"]
partner_key=os.environ["PARTNER_KEY"]
request_id=os.environ["REQUEST_ID"]
_uid=os.environ["_UID"]
# (2) EXTERNAL APPS
auth_headers_url=os.environ["AUTH_HEADERS_URL"]
access_token_url=os.environ["ACCESS_TOKEN_URL"]
ship_pending_url=os.environ["SHIP_PENDING_URL"]
ship_pending_key=os.environ["SHIP_PENDING_KEY"]
email_sender_url=os.environ["EMAIL_SENDER_URL"]
# (3) SHOP DATASET
shops=json.loads(os.environ["SHOPS"])
# (4) GOOGLE DATASET
spreadsheet_url=os.environ["SPREADSHEET_URL"]
api_gemini_key=os.environ["API_GEMINI_KEY"]
service_account_key=json.loads(os.environ["SERVICE_ACCOUNT_KEY"])
