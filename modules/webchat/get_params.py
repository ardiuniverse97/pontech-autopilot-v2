from modules.webchat.spc_cds_chat import spc_cds_chat
import modules.config as config

# GET PARAMS
def get_params(headers):
  return {
    "_uid": config._uid,
    "_v": "9.1.17",
    "SPC_CDS_CHAT": spc_cds_chat(headers=headers),
    "x-shop-region": "ID",
    "_api_source": "sc"
  }