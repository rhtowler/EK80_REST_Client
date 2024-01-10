# ek80_param_client.InstalledTransceiversApi

All URIs are relative to *http://localhost:12345*

Method | HTTP request | Description
------------- | ------------- | -------------
[**echo_sounder_transducers_get_acoustic_source_by_channel_id**](InstalledTransceiversApi.md#echo_sounder_transducers_get_acoustic_source_by_channel_id) | **GET** /api/sounder/installed-transceivers/{channelid} | Get information about a specific installed transceiver
[**echo_sounder_transducers_get_acoustic_source_by_channel_index**](InstalledTransceiversApi.md#echo_sounder_transducers_get_acoustic_source_by_channel_index) | **GET** /api/sounder/installed-transceivers/{channellistindex} | Get information about a specific installed transceiver
[**echo_sounder_transducers_get_acoustic_sources**](InstalledTransceiversApi.md#echo_sounder_transducers_get_acoustic_sources) | **GET** /api/sounder/installed-transceivers | Get information about all installed transceivers


# **echo_sounder_transducers_get_acoustic_source_by_channel_id**
> EchoSounderTransducer echo_sounder_transducers_get_acoustic_source_by_channel_id(channelid)

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
channelid = 'channelid_example' # str | The virtual channel id

try:
    # Get information about a specific installed transceiver
    api_response = api_instance.echo_sounder_transducers_get_acoustic_source_by_channel_id(channelid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstalledTransceiversApi->echo_sounder_transducers_get_acoustic_source_by_channel_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelid** | **str**| The virtual channel id | 

### Return type

[**EchoSounderTransducer**](EchoSounderTransducer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **echo_sounder_transducers_get_acoustic_source_by_channel_index**
> EchoSounderTransducer echo_sounder_transducers_get_acoustic_source_by_channel_index(channellistindex)

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
channellistindex = 56 # int | The channel list index

try:
    # Get information about a specific installed transceiver
    api_response = api_instance.echo_sounder_transducers_get_acoustic_source_by_channel_index(channellistindex)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstalledTransceiversApi->echo_sounder_transducers_get_acoustic_source_by_channel_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channellistindex** | **int**| The channel list index | 

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

