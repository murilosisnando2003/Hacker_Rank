from adal import AuthenticationContext
from dynamics365crm.client import Client


DYNAMIC_RESOURCE = 'https://edge.crm2.dynamics.com/'

auth_context = AuthenticationContext('https://login.microsoftonline.com/76b77ddd-7462-4810-b24e-bc1668ab6f19')
token = auth_context.acquire_token_with_username_password('https://edge.crm2.dynamics.com/',
                                                          'D365AppUser@edge-br.com',
                                                          'Murilao23',
                                                          '87dafbc3-e1eb-418f-abbb-3d526d1508d4')
                                                          #'e84e50cb-b9df-4311-b672-b47951e6a2c7')
client = Client(DYNAMIC_RESOURCE)
client.set_token(token["accessToken"])