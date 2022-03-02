# ek80_param_client.InstalledTransceiversApi

All URIs are relative to *http://localhost:12345*

Method | HTTP request | Description
------------- | ------------- | -------------
[**echo_sounder_transducers_get_acoustic_source**](InstalledTransceiversApi.md#echo_sounder_transducers_get_acoustic_source) | **GET** /api/sounder/installed-transceivers/{acousticSource} | Get information about a specific installed transceiver
[**echo_sounder_transducers_get_acoustic_source_0**](InstalledTransceiversApi.md#echo_sounder_transducers_get_acoustic_source_0) | **GET** /api/sounder/installed-transceivers/{index} | Get information about a specific installed transceiver
[**echo_sounder_transducers_get_acoustic_sources**](InstalledTransceiversApi.md#echo_sounder_transducers_get_acoustic_sources) | **GET** /api/sounder/installed-transceivers | Get information about all installed transceivers


# **echo_sounder_transducers_get_acoustic_source**
> EchoSounderTransducer echo_sounder_transducers_get_acoustic_source(acoustic_source)

Get information about a specific installed transceiver

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.InstalledTransceiversApi()
acoustic_source = 'acoustic_source_example' # str | The virtual channel id

try:
    # Get information about a specific installed transceiver
    api_response = api_instance.echo_sounder_transducers_get_acoustic_source(acoustic_source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstalledTransceiversApi->echo_sounder_transducers_get_acoustic_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acoustic_source** | **str**| The virtual channel id | 

### Return type

[**EchoSounderTransducer**](EchoSounderTransducer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **echo_sounder_transducers_get_acoustic_source_0**
> EchoSounderTransducer echo_sounder_transducers_get_acoustic_source_0(index)

Get information about a specific installed transceiver

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.InstalledTransceiversApi()
index = 56 # int | The virtual channel id

try:
    # Get information about a specific installed transceiver
    api_response = api_instance.echo_sounder_transducers_get_acoustic_source_0(index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstalledTransceiversApi->echo_sounder_transducers_get_acoustic_source_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| The virtual channel id | 

### Return type

[**EchoSounderTransducer**](EchoSounderTransducer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **echo_sounder_transducers_get_acoustic_sources**
> list[EchoSounderTransducer] echo_sounder_transducers_get_acoustic_sources()

Get information about all installed transceivers

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.InstalledTransceiversApi()

try:
    # Get information about all installed transceivers
    api_response = api_instance.echo_sounder_transducers_get_acoustic_sources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstalledTransceiversApi->echo_sounder_transducers_get_acoustic_sources: %s\n" % e)
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

