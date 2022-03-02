# ek80_param_client.DataOutputApi

All URIs are relative to *http://localhost:12345*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_output_get_all_outputs**](DataOutputApi.md#data_output_get_all_outputs) | **GET** /api/data-output | 
[**data_output_get_processed_data_storage**](DataOutputApi.md#data_output_get_processed_data_storage) | **GET** /api/data-output/processed-data | Get Processed data storage enabled flag
[**data_output_set_processed_data_storage**](DataOutputApi.md#data_output_set_processed_data_storage) | **PUT** /api/data-output/processed-data | Turn on or off storage of processed data


# **data_output_get_all_outputs**
> list[DataOutput] data_output_get_all_outputs()



### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.DataOutputApi()

try:
    api_response = api_instance.data_output_get_all_outputs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataOutputApi->data_output_get_all_outputs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DataOutput]**](DataOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_output_get_processed_data_storage**
> bool data_output_get_processed_data_storage()

Get Processed data storage enabled flag

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.DataOutputApi()

try:
    # Get Processed data storage enabled flag
    api_response = api_instance.data_output_get_processed_data_storage()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataOutputApi->data_output_get_processed_data_storage: %s\n" % e)
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

# **data_output_set_processed_data_storage**
> data_output_set_processed_data_storage(enabled)

Turn on or off storage of processed data

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.DataOutputApi()
enabled = true # bool | The Processed data storage enabled flag (On/Off)

try:
    # Turn on or off storage of processed data
    api_instance.data_output_set_processed_data_storage(enabled)
except ApiException as e:
    print("Exception when calling DataOutputApi->data_output_set_processed_data_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enabled** | **bool**| The Processed data storage enabled flag (On/Off) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

