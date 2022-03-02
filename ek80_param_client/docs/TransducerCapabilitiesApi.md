# ek80_param_client.TransducerCapabilitiesApi

All URIs are relative to *http://localhost:12345*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transducer_capabilities_get**](TransducerCapabilitiesApi.md#transducer_capabilities_get) | **GET** /api/transducer-capabilities | 
[**transducer_capabilities_get_transducer_capability**](TransducerCapabilitiesApi.md#transducer_capabilities_get_transducer_capability) | **GET** /api/transducer-capabilities/{channelid} | 


# **transducer_capabilities_get**
> list[TransducerCapabilities] transducer_capabilities_get()



### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.TransducerCapabilitiesApi()

try:
    api_response = api_instance.transducer_capabilities_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransducerCapabilitiesApi->transducer_capabilities_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TransducerCapabilities]**](TransducerCapabilities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transducer_capabilities_get_transducer_capability**
> TransducerCapabilities transducer_capabilities_get_transducer_capability(channelid)



### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.TransducerCapabilitiesApi()
channelid = 'channelid_example' # str | 

try:
    api_response = api_instance.transducer_capabilities_get_transducer_capability(channelid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransducerCapabilitiesApi->transducer_capabilities_get_transducer_capability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelid** | **str**|  | 

### Return type

[**TransducerCapabilities**](TransducerCapabilities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

