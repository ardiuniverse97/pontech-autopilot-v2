import modules.config as config
import requests

# UPDATE SHIP PENDING
def update_ship_pending(content):
  requests.patch(
    url=config.ship_pending_url,
    headers={'Content-Type': 'application/json', 'X-Edit-Key': config.ship_pending_key},
    json=content
  ) 