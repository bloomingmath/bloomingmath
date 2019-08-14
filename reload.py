import requests
my_domain = 'bloomingmath.pythonanywhere.com'
username = 'bloomingmath'
token = '7e55a68985256b299fced98a8b2dd6a318078265'

response = requests.post(
  'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain}/reload/'.format(
      username=username, domain=my_domain
  ),
  headers={'Authorization': 'Token {token}'.format(token=token)}
)

if response.status_code == 200:
  print('All OK: app reloaded.')
else:
  print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
