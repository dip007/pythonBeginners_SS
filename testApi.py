#import urllib.request
#import json
#citi_api = 'A1fH7aU7sW8bM4pM8kQ1vG5dD8wK2nA2tW6fN3rD3pS3eE0bH3'
#url = 'https://sandbox.apihub.citi.com/gcb/api/authCode/oauth2/authorize?response_type=code&scope=pay_with_points%20accounts_details_transactions%20customers_profiles%20payees%20personal_domestic_transfers%20internal_domestic_transfers%20external_domestic_transfers%20bill_payments%20Drawees%20Card_Payments%20Auto_Debit%20cards%20onboarding%20reference_data%20reset_atm_pin%20statements_and_advices%20meta_data&countryCode=au&businessCode=gcb&locale=en_US&state=dfe4945b-9b06-4dfb-36d7-a2816951d532&redirect_uri=https%3A%2F%2Fsandbox.developerhub.citi.com%2Fapi-authorize&client_id=3906dd6d-534b-4d20-81d7-0e78848013a3'
#json_obj = urllib.request.urlopen(url)
#data = json.load(json_obj)
#print(data)
import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
   print(html)
