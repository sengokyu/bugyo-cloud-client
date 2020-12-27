USER_AGENT = 'Mozilla/5.0 ()'
CONTENT_ENCODING = 'utf-8'

# {0} : tenant_code
# {1} : user_code
URL_TEMPLATES = {
    'LoginPage': 'https://id.obc.co.jp/{0}',
    'CheckAuthenticationMethod': 'https://id.obc.co.jp/{0}/login/CheckAuthenticationMethod',
    'Authenticate': 'https://id.obc.jp/{0}/login/login/?Length=5',
    'PunchmarkPage':  'https://hromssp.obc.jp/{0}/{1}/timeclock/punchmark/',
    'TimeClock': 'https://hromssp.obc.jp/{0}/{1}/TimeClock/InsertReadDateTime/',
}
