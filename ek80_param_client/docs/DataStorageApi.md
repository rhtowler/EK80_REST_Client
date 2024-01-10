# ek80_param_client.DataStorageApi

All URIs are relative to *http://localhost:12345*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_storage_ek80_get_individual_channel_range**](DataStorageApi.md#data_storage_ek80_get_individual_channel_range) | **GET** /api/sounder/data-storage/individual-channel-range/{channel_name} | Get range settings for a specific channel
[**data_storage_ek80_set_individual_channel_range**](DataStorageApi.md#data_storage_ek80_set_individual_channel_range) | **PUT** /api/sounder/data-storage/individual-channel-range | Sets the range settings for a specific channel
[**data_storage_get_basic_storage_settings**](DataStorageApi.md#data_storage_get_basic_storage_settings) | **GET** /api/sounder/data-storage | Get MainStorageSettings struct with the most common storage settings
[**data_storage_get_record_raw_active**](DataStorageApi.md#data_storage_get_record_raw_active) | **GET** /api/sounder/data-storage/record-raw-active | Is recording raw files on or off
[**data_storage_set_basic_storage_settings**](DataStorageApi.md#data_storage_set_basic_storage_settings) | **PUT** /api/sounder/data-storage | 
[**data_storage_set_record_raw_active**](DataStorageApi.md#data_storage_set_record_raw_active) | **PUT** /api/sounder/data-storage/record-raw-active | Turns on or off raw data storage
[**data_storage_set_sample_data_format**](DataStorageApi.md#data_storage_set_sample_data_format) | **PUT** /api/sounder/data-storage/sample-data-format-wbt-cw | Sets storage sample data format for WBTs running CW


# **data_storage_ek80_get_individual_channel_range**
> IndividualRangeControl data_storage_ek80_get_individual_channel_range(channel_name)

Get range settings for a specific channel

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.DataStorageApi()
channel_name = 'channel_name_example' # str | The logical channel id

try:
    # Get range settings for a specific channel
    api_response = api_instance.data_storage_ek80_get_individual_channel_range(channel_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStorageApi->data_storage_ek80_get_individual_channel_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**| The logical channel id | 

### Return type

[**IndividualRangeControl**](IndividualRangeControl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_storage_ek80_set_individual_channel_range**
> data_storage_ek80_set_individual_channel_range(channel_range)

Sets the range settings for a specific channel

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.DataStorageApi()
channel_range = ek80_param_client.IndividualRangeControl() # IndividualRangeControl | IndividualRangeControl struct with rabge settings for a channel

try:
    # Sets the range settings for a specific channel
    api_instance.data_storage_ek80_set_individual_channel_range(channel_range)
except ApiException as e:
    print("Exception when calling DataStorageApi->data_storage_ek80_set_individual_channel_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_range** | [**IndividualRangeControl**](IndividualRangeControl.md)| IndividualRangeControl struct with rabge settings for a channel | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_storage_get_basic_storage_settings**
> MainStorageSettings data_storage_get_basic_storage_settings()

Get MainStorageSettings struct with the most common storage settings

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.DataStorageApi()

try:
    # Get MainStorageSettings struct with the most common storage settings
    api_response = api_instance.data_storage_get_basic_storage_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStorageApi->data_storage_get_basic_storage_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MainStorageSettings**](MainStorageSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_storage_get_record_raw_active**
> bool data_storage_get_record_raw_active()

Is recording raw files on or off

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.DataStorageApi()

try:
    # Is recording raw files on or off
    api_response = api_instance.data_storage_get_record_raw_active()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStorageApi->data_storage_get_record_raw_active: %s\n" % e)
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

# **data_storage_set_basic_storage_settings**
> data_storage_set_basic_storage_settings(storage_settings)



### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.DataStorageApi()
storage_settings = ek80_param_client.MainStorageSettings() # MainStorageSettings | 

try:
    api_instance.data_storage_set_basic_storage_settings(storage_settings)
except ApiException as e:
    print("Exception when calling DataStorageApi->data_storage_set_basic_storage_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_settings** | [**MainStorageSettings**](MainStorageSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_storage_set_record_raw_active**
> data_storage_set_record_raw_active(record_raw_active)

Turns on or off raw data storage

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.DataStorageApi()
record_raw_active = true # bool | A bool value if raw data storage should be turned on or off

try:
    # Turns on or off raw data storage
    api_instance.data_storage_set_record_raw_active(record_raw_active)
except ApiException as e:
    print("Exception when calling DataStorageApi->data_storage_set_record_raw_active: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_raw_active** | **bool**| A bool value if raw data storage should be turned on or off | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_storage_set_sample_data_format**
> data_storage_set_sample_data_format(storage_sample_data_format)

Sets storage sample data format for WBTs running CW

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.DataStorageApi()
storage_sample_data_format = 'storage_sample_data_format_example' # str | A enumerated value identifiying the storage sample data format. Storage sample formats available: 0=Complex, 1=Power Angle, 2=Power Angle Decimated

try:
    # Sets storage sample data format for WBTs running CW
    api_instance.data_storage_set_sample_data_format(storage_sample_data_format)
except ApiException as e:
    print("Exception when calling DataStorageApi->data_storage_set_sample_data_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_sample_data_format** | **str**| A enumerated value identifiying the storage sample data format. Storage sample formats available: 0&#x3D;Complex, 1&#x3D;Power Angle, 2&#x3D;Power Angle Decimated | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

