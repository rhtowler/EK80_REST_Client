# ek80_param_client.AdvancedSequencingApi

All URIs are relative to *http://localhost:12345*

Method | HTTP request | Description
------------- | ------------- | -------------
[**advanced_sequencing_get_advanced_sequencing_settings**](AdvancedSequencingApi.md#advanced_sequencing_get_advanced_sequencing_settings) | **GET** /api/sounder/advanced-sequencing | Get Advanced Sequencing complete configuration
[**advanced_sequencing_get_sequences**](AdvancedSequencingApi.md#advanced_sequencing_get_sequences) | **GET** /api/sounder/advanced-sequencing/sequence-list | 
[**advanced_sequencing_set_advanced_sequencing_settings**](AdvancedSequencingApi.md#advanced_sequencing_set_advanced_sequencing_settings) | **PUT** /api/sounder/advanced-sequencing | Set Advanced Sequencing complete configuration


# **advanced_sequencing_get_advanced_sequencing_settings**
> AdvancedSequencingSettings advanced_sequencing_get_advanced_sequencing_settings()

Get Advanced Sequencing complete configuration

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.AdvancedSequencingApi()

try:
    # Get Advanced Sequencing complete configuration
    api_response = api_instance.advanced_sequencing_get_advanced_sequencing_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedSequencingApi->advanced_sequencing_get_advanced_sequencing_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdvancedSequencingSettings**](AdvancedSequencingSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **advanced_sequencing_get_sequences**
> list[str] advanced_sequencing_get_sequences()



### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.AdvancedSequencingApi()

try:
    api_response = api_instance.advanced_sequencing_get_sequences()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedSequencingApi->advanced_sequencing_get_sequences: %s\n" % e)
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

# **advanced_sequencing_set_advanced_sequencing_settings**
> advanced_sequencing_set_advanced_sequencing_settings(sequencing_setting)

Set Advanced Sequencing complete configuration

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.AdvancedSequencingApi()
sequencing_setting = ek80_param_client.AdvancedSequencingSettings() # AdvancedSequencingSettings | A struct giving a set of sequences. The struct contains:  A list of sequences (name, ensembles added)

try:
    # Set Advanced Sequencing complete configuration
    api_instance.advanced_sequencing_set_advanced_sequencing_settings(sequencing_setting)
except ApiException as e:
    print("Exception when calling AdvancedSequencingApi->advanced_sequencing_set_advanced_sequencing_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequencing_setting** | [**AdvancedSequencingSettings**](AdvancedSequencingSettings.md)| A struct giving a set of sequences. The struct contains:  A list of sequences (name, ensembles added) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

