# ek80_param_client.PingInfoApi

All URIs are relative to *http://localhost:12345*

Method | HTTP request | Description
------------- | ------------- | -------------
[**executed_pings_get_executed_ping**](PingInfoApi.md#executed_pings_get_executed_ping) | **GET** /api/sounder/ping-info | Get information about all the executed channel pings
[**executed_pings_get_executed_ping_by_channel_id**](PingInfoApi.md#executed_pings_get_executed_ping_by_channel_id) | **GET** /api/sounder/ping-info/{channelid} | Get information about a specific executed channel ping


# **executed_pings_get_executed_ping**
> ExecutedPing executed_pings_get_executed_ping()

Get information about all the executed channel pings

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.PingInfoApi()

try:
    # Get information about all the executed channel pings
    api_response = api_instance.executed_pings_get_executed_ping()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingInfoApi->executed_pings_get_executed_ping: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ExecutedPing**](ExecutedPing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **executed_pings_get_executed_ping_by_channel_id**
> ChannelPingConfiguration executed_pings_get_executed_ping_by_channel_id(channelid)

Get information about a specific executed channel ping

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.PingInfoApi()
channelid = 'channelid_example' # str | The virtual channel id

try:
    # Get information about a specific executed channel ping
    api_response = api_instance.executed_pings_get_executed_ping_by_channel_id(channelid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingInfoApi->executed_pings_get_executed_ping_by_channel_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelid** | **str**| The virtual channel id | 

### Return type

[**ChannelPingConfiguration**](ChannelPingConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

