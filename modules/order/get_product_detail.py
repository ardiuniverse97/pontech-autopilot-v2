import modules.config as config
import gspread

# GET PRODUCT DETAIL
def get_product_detail(shop_id, products):
  google_api=gspread.service_account_from_dict(config.service_account_key)
  workbook=google_api.open_by_url(config.spreadsheet_url)
  worksheet=workbook.worksheet(config.shops[shop_id]['username'])
  database=[]
  for item in worksheet.get_all_values():
    if str(item[1]) in products: name=str(item[4]); variant=str(item[5]); gdrive=str(item[6])
    database.append([name, variant, gdrive])
  return database
