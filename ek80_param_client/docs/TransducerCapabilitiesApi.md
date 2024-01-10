# ek80_param_client.TransducerCapabilitiesApi

All URIs are relative to *http://localhost:12345*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_adcp_transducer_capabilities**](TransducerCapabilitiesApi.md#get_adcp_transducer_capabilities) | **GET** /api/transducer-capabilities/adcp-transducers | Get capability information about installed adcp transducers
[**get_array_transducer_capabilities**](TransducerCapabilitiesApi.md#get_array_transducer_capabilities) | **GET** /api/transducer-capabilities/array-transducers | Get capability information about installed array transducers
[**get_single_split_transducer_capabilities**](TransducerCapabilitiesApi.md#get_single_split_transducer_capabilities) | **GET** /api/transducer-capabilities/single-split-transducers | Get capability information about installed single split transducers
[**get_single_transducer_capabilities**](TransducerCapabilitiesApi.md#get_single_transducer_capabilities) | **GET** /api/transducer-capabilities/single-transducers | Get capability information about installed single transducers
[**get_transducer_capabilities**](TransducerCapabilitiesApi.md#get_transducer_capabilities) | **GET** /api/transducer-capabilities | Get general/common information about all installed transducers
[**transducer_capabilities_get_transducer_capability**](TransducerCapabilitiesApi.md#transducer_capabilities_get_transducer_capability) | **GET** /api/transducer-capabilities/{channelid} | Get information about a specific installed transducer capabilities


# **get_adcp_transducer_capabilities**
> list[AdcpTransducerCapabilities] get_adcp_transducer_capabilities()

Get capability information about installed adcp transducers

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
    # Get capability information about installed adcp transducers
    api_response = api_instance.get_adcp_transducer_capabilities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransducerCapabilitiesApi->get_adcp_transducer_capabilities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AdcpTransducerCapabilities]**](AdcpTransducerCapabilities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_array_transducer_capabilities**
> list[ArrayTransducerCapabilities] get_array_transducer_capabilities()

Get capability information about installed array transducers

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
    # Get capability information about installed array transducers
    api_response = api_instance.get_array_transducer_capabilities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransducerCapabilitiesApi->get_array_transducer_capabilities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ArrayTransducerCapabilities]**](ArrayTransducerCapabilities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_split_transducer_capabilities**
> list[SingleSplitTransducerCapabilities] get_single_split_transducer_capabilities()

Get capability information about installed single split transducers

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
    # Get capability information about installed single split transducers
    api_response = api_instance.get_single_split_transducer_capabilities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransducerCapabilitiesApi->get_single_split_transducer_capabilities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SingleSplitTransducerCapabilities]**](SingleSplitTransducerCapabilities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_transducer_capabilities**
> list[SingleTransducerCapabilities] get_single_transducer_capabilities()

Get capability information about installed single transducers

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
    # Get capability information about installed single transducers
    api_response = api_instance.get_single_transducer_capabilities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransducerCapabilitiesApi->get_single_transducer_capabilities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SingleTransducerCapabilities]**](SingleTransducerCapabilities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transducer_capabilities**
> list[TransducerCapabilities] get_transducer_capabilities()

Get general/common information about all installed transducers

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
    # Get general/common information about all installed transducers
    api_response = api_instance.get_transducer_capabilities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransducerCapabilitiesApi->get_transducer_capabilities: %s\n" % e)
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

Get information about a specific installed transducer capabilities

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.TransducerCapabilitiesApi()
channelid = 'channelid_example' # str | The virtual channel id

try:
    # Get information about a specific installed transducer capabilities
    api_response = api_instance.transducer_capabilities_get_transducer_capability(channelid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransducerCapabilitiesApi->transducer_capabilities_get_transducer_capability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelid** | **str**| The virtual channel id | 

### Return type

[**TransducerCapabilities**](TransducerCapabilities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

