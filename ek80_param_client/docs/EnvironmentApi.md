# ek80_param_client.EnvironmentApi

All URIs are relative to *http://localhost:12345*

Method | HTTP request | Description
------------- | ------------- | -------------
[**environment_get_transducer_face_data**](EnvironmentApi.md#environment_get_transducer_face_data) | **GET** /api/environment/TransducerFace | Get environmental data for the transducer face
[**environment_get_water_column_data**](EnvironmentApi.md#environment_get_water_column_data) | **GET** /api/environment/WaterColumn | Get environmental data for the water column
[**environment_set_transducer_face_data**](EnvironmentApi.md#environment_set_transducer_face_data) | **POST** /api/environment/TransducerFace | Set environmental data for the transducer face
[**environment_set_water_column_data**](EnvironmentApi.md#environment_set_water_column_data) | **PUT** /api/environment/WaterColumn | set environmental data for the water column


# **environment_get_transducer_face_data**
> EnvironmentTransducerData environment_get_transducer_face_data()

Get environmental data for the transducer face

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.EnvironmentApi()

try:
    # Get environmental data for the transducer face
    api_response = api_instance.environment_get_transducer_face_data()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->environment_get_transducer_face_data: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EnvironmentTransducerData**](EnvironmentTransducerData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **environment_get_water_column_data**
> WaterColumnData environment_get_water_column_data()

Get environmental data for the water column

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.EnvironmentApi()

try:
    # Get environmental data for the water column
    api_response = api_instance.environment_get_water_column_data()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->environment_get_water_column_data: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WaterColumnData**](WaterColumnData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **environment_set_transducer_face_data**
> environment_set_transducer_face_data(transducer_face)

Set environmental data for the transducer face

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.EnvironmentApi()
transducer_face = ek80_param_client.EnvironmentTransducerData() # EnvironmentTransducerData | EnvironmentTransducerData struct

try:
    # Set environmental data for the transducer face
    api_instance.environment_set_transducer_face_data(transducer_face)
except ApiException as e:
    print("Exception when calling EnvironmentApi->environment_set_transducer_face_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transducer_face** | [**EnvironmentTransducerData**](EnvironmentTransducerData.md)| EnvironmentTransducerData struct | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **environment_set_water_column_data**
> environment_set_water_column_data(water_column)

set environmental data for the water column

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.EnvironmentApi()
water_column = ek80_param_client.WaterColumnData() # WaterColumnData | WaterColumnData struct

try:
    # set environmental data for the water column
    api_instance.environment_set_water_column_data(water_column)
except ApiException as e:
    print("Exception when calling EnvironmentApi->environment_set_water_column_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **water_column** | [**WaterColumnData**](WaterColumnData.md)| WaterColumnData struct | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

