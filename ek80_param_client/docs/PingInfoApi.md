# ek80_param_client.PingInfoApi

All URIs are relative to *http://localhost:12345*

Method | HTTP request | Description
------------- | ------------- | -------------
[**executed_pings_get_executed_ping**](PingInfoApi.md#executed_pings_get_executed_ping) | **GET** /api/sounder/ping-info | 


# **executed_pings_get_executed_ping**
> ExecutedPing executed_pings_get_executed_ping()



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

