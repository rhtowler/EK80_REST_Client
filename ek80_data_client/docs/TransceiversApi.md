# ek80_data_client.TransceiversApi

All URIs are relative to *http://localhost:12346*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_installed_transceivers**](TransceiversApi.md#get_installed_transceivers) | **GET** /api/sounder/transceivers | Get information about all installed transceivers


# **get_installed_transceivers**
> list[EchoSounderTransducer] get_installed_transceivers()

Get information about all installed transceivers

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.TransceiversApi()

try:
    # Get information about all installed transceivers
    api_response = api_instance.get_installed_transceivers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransceiversApi->get_installed_transceivers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EchoSounderTransducer]**](EchoSounderTransducer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

