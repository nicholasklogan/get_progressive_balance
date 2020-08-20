import requests


def get_progressive_balance():
    sess = requests.Session()

    accesstoken = sess.post(
        'https://api.progressive.com/onlineaccount/v1/accesstoken',
        json={
            'userName': '',  # ENTER USERNAME HERE,
            'password': ''  # ENTER PASSWORD HERE
        },
        headers={
            'X-PGRClient': 'Online Servicing Web Portal',
            'X-PGRSiteServerId': '51c394a35a004a46940b597fe139e6af',
            'api_key': ''  # ENTER API KEY FOUND IT VIA CHROME INSPECT
        }
    ).json()['accessToken']
    handshake = sess.post(
        'https://api.progressive.com/policypro/v1/handshake',
        headers={
            'api_key': '',  # ENTER API KEY FOUND IT VIA CHROME INSPECT
            'Authorization': 'Bearer {}'.format(accesstoken)},
        json={
            "customerId": '',  # ENTER ID FOUND IT VIA CHROME INSPECT
            "accessType": "PPRO",
            "accessMode": "Internet",
            "brandingExperience": "",
            "s2Slot": "https://policyservicing.apps.progressive.com/app",
            "enableDebugPanel": False,
            "debugPanelAdapterVersion": "",
            "debugPanelClientVersion": ""
        }).json()
    return sess.get(
        'https://policyservicing.progressive.com/api/v1/account?billingFlag=true',
        headers={
            "X-PRGPProApiKey": "",  # ENTER API KEY FOUND IT VIA CHROME INSPECT
            "X-PRGDestinationHost": "https://[production-gatewayHost]/policypro/",
            "x-prgaccountsessionid": handshake['accountSessionId'],
            "x-prgsessiondatalocation": handshake['sessionDataLocation'],
            "x-prgaccesstoken": accesstoken
        }).json()


def format_results(result):
    return ' & '.join(
        [
            f"you owe ${bill['paymentAmount']} for {policy['vehicles'][0]['modelYear']} {policy['vehicles'][0]['make']} {policy['vehicles'][0]['model']}"
            for bill, policy in (
                (b, [p for p in result['policies'] if p['number'] == b['policyNumber']][0])
            for b in result['billingInfo'])])
