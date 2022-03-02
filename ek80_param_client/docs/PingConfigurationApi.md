# ek80_param_client.PingConfigurationApi

All URIs are relative to *http://localhost:12345*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping_configuration_get_channel_pulse_settings**](PingConfigurationApi.md#ping_configuration_get_channel_pulse_settings) | **GET** /api/sounder/ping-configuration/{channelid}/pulse-settings | Get pulse settings for a given channel
[**ping_configuration_get_channel_transmit_power**](PingConfigurationApi.md#ping_configuration_get_channel_transmit_power) | **GET** /api/sounder/ping-configuration/{channelid}/transmit-power | Get transmit power for a given channel
[**ping_configuration_get_channels**](PingConfigurationApi.md#ping_configuration_get_channels) | **GET** /api/sounder/ping-configuration/channel-list | 
[**ping_configuration_get_ping_configuration**](PingConfigurationApi.md#ping_configuration_get_ping_configuration) | **GET** /api/sounder/ping-configuration/adcp | Get adcp ping configuration
[**ping_configuration_get_transceiver_sequencing**](PingConfigurationApi.md#ping_configuration_get_transceiver_sequencing) | **GET** /api/sounder/ping-configuration/sequencing | 
[**ping_configuration_set_channel_pulse_settings**](PingConfigurationApi.md#ping_configuration_set_channel_pulse_settings) | **PUT** /api/sounder/ping-configuration/{channelid}/pulse-settings | Set pulse settings for a given channel
[**ping_configuration_set_channel_transmit_power**](PingConfigurationApi.md#ping_configuration_set_channel_transmit_power) | **PUT** /api/sounder/ping-configuration/{channelid}/transmit-power | Set transmit power for a given channel
[**ping_configuration_set_ping_configuration**](PingConfigurationApi.md#ping_configuration_set_ping_configuration) | **PUT** /api/sounder/ping-configuration/adcp | Set adcp ping configuration
[**ping_configuration_set_transceiver_sequencing**](PingConfigurationApi.md#ping_configuration_set_transceiver_sequencing) | **PUT** /api/sounder/ping-configuration/sequencing | 


# **ping_configuration_get_channel_pulse_settings**
> PulseSettings ping_configuration_get_channel_pulse_settings(channelid)

Get pulse settings for a given channel

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.PingConfigurationApi()
channelid = 'channelid_example' # str | The virtual channel id

try:
    # Get pulse settings for a given channel
    api_response = api_instance.ping_configuration_get_channel_pulse_settings(channelid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingConfigurationApi->ping_configuration_get_channel_pulse_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelid** | **str**| The virtual channel id | 

### Return type

[**PulseSettings**](PulseSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_configuration_get_channel_transmit_power**
> float ping_configuration_get_channel_transmit_power(channelid)

Get transmit power for a given channel

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.PingConfigurationApi()
channelid = 'channelid_example' # str | The virtual channel id

try:
    # Get transmit power for a given channel
    api_response = api_instance.ping_configuration_get_channel_transmit_power(channelid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingConfigurationApi->ping_configuration_get_channel_transmit_power: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelid** | **str**| The virtual channel id | 

### Return type

**float**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_configuration_get_channels**
> list[str] ping_configuration_get_channels()



### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.PingConfigurationApi()

try:
    api_response = api_instance.ping_configuration_get_channels()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingConfigurationApi->ping_configuration_get_channels: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_configuration_get_ping_configuration**
> AdcpConfigurationEc150 ping_configuration_get_ping_configuration()

Get adcp ping configuration

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.PingConfigurationApi()

try:
    # Get adcp ping configuration
    api_response = api_instance.ping_configuration_get_ping_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingConfigurationApi->ping_configuration_get_ping_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdcpConfigurationEc150**](AdcpConfigurationEc150.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_configuration_get_transceiver_sequencing**
> bool ping_configuration_get_transceiver_sequencing()



### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.PingConfigurationApi()

try:
    api_response = api_instance.ping_configuration_get_transceiver_sequencing()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingConfigurationApi->ping_configuration_get_transceiver_sequencing: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_configuration_set_channel_pulse_settings**
> ping_configuration_set_channel_pulse_settings(channelid, pulse_settings)

Set pulse settings for a given channel

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.PingConfigurationApi()
channelid = 'channelid_example' # str | The virtual channel id
pulse_settings = ek80_param_client.PulseSettings() # PulseSettings | A struct giving a set of pulse setting. The struct contains: pulse-type (string)[CW, LFM, LFMD], pulse-duration (double, [s], depending on frequency and pulse-type), start-frequency ([Hz]), end-frequency ( [Hz]),  channel-mode(Active, Passive, test), Ramping (Fast/Slow), filter-type (string) .

try:
    # Set pulse settings for a given channel
    api_instance.ping_configuration_set_channel_pulse_settings(channelid, pulse_settings)
except ApiException as e:
    print("Exception when calling PingConfigurationApi->ping_configuration_set_channel_pulse_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelid** | **str**| The virtual channel id | 
 **pulse_settings** | [**PulseSettings**](PulseSettings.md)| A struct giving a set of pulse setting. The struct contains: pulse-type (string)[CW, LFM, LFMD], pulse-duration (double, [s], depending on frequency and pulse-type), start-frequency ([Hz]), end-frequency ( [Hz]),  channel-mode(Active, Passive, test), Ramping (Fast/Slow), filter-type (string) . | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_configuration_set_channel_transmit_power**
> ping_configuration_set_channel_transmit_power(channelid, transmit_power)

Set transmit power for a given channel

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.PingConfigurationApi()
channelid = 'channelid_example' # str | The virtual channel id
transmit_power = 1.2 # float | The new transmit power in [W]

try:
    # Set transmit power for a given channel
    api_instance.ping_configuration_set_channel_transmit_power(channelid, transmit_power)
except ApiException as e:
    print("Exception when calling PingConfigurationApi->ping_configuration_set_channel_transmit_power: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelid** | **str**| The virtual channel id | 
 **transmit_power** | **float**| The new transmit power in [W] | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_configuration_set_ping_configuration**
> ping_configuration_set_ping_configuration(adcp_config)

Set adcp ping configuration

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.PingConfigurationApi()
adcp_config = ek80_param_client.AdcpConfigurationEc150() # AdcpConfigurationEc150 | 

try:
    # Set adcp ping configuration
    api_instance.ping_configuration_set_ping_configuration(adcp_config)
except ApiException as e:
    print("Exception when calling PingConfigurationApi->ping_configuration_set_ping_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adcp_config** | [**AdcpConfigurationEc150**](AdcpConfigurationEc150.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_configuration_set_transceiver_sequencing**
> ping_configuration_set_transceiver_sequencing(sequencing)



### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.PingConfigurationApi()
sequencing = true # bool | 

try:
    api_instance.ping_configuration_set_transceiver_sequencing(sequencing)
except ApiException as e:
    print("Exception when calling PingConfigurationApi->ping_configuration_set_transceiver_sequencing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequencing** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

