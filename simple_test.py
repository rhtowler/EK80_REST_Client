
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import datetime


client_config = swagger_client.Configuration()
client_config.host="http://localhost:12345"
api_client = swagger_client.ApiClient(configuration=client_config)


ownship = swagger_client.OwnshipApi(api_client)

x=ownship.ownship_get_navigation()
pprint(x)

x=ownship.ownship_get_motion()
pprint(x)

x=ownship.ownship_get_installed_transducers()
pprint(x)

it = swagger_client.InstalledTransceiversApi(api_client)

x=it.echo_sounder_transducers_get_acoustic_sources()
pprint(x)

