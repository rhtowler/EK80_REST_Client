# ek80_param_client.ProcessingApi

All URIs are relative to *http://localhost:12345*

Method | HTTP request | Description
------------- | ------------- | -------------
[**processing_get_adcp_processing_setting**](ProcessingApi.md#processing_get_adcp_processing_setting) | **GET** /api/sounder/processing/{channel_name}/adcp | Get all adcp processing parameters for specific channel
[**processing_get_adcp_processing_settings**](ProcessingApi.md#processing_get_adcp_processing_settings) | **GET** /api/sounder/processing/adcp | 
[**processing_get_bottom_detection_active**](ProcessingApi.md#processing_get_bottom_detection_active) | **GET** /api/sounder/processing/{channel_name}/bottom-detection/bottom-detection-active | Check if bottom detection is on and off
[**processing_set_bottom_detection_active**](ProcessingApi.md#processing_set_bottom_detection_active) | **PUT** /api/sounder/processing/{channel_name}/bottom-detection/bottom-detection-active | Turn on and off bottom detection
[**processing_set_bottom_detection_backstep**](ProcessingApi.md#processing_set_bottom_detection_backstep) | **PUT** /api/sounder/processing/{channel_name}/bottom-detection/bottom-backstep | Set the bottom backstep value for bottom detection
[**processing_set_bottom_detection_maximum_depth**](ProcessingApi.md#processing_set_bottom_detection_maximum_depth) | **PUT** /api/sounder/processing/{channel_name}/bottom-detection/maximum-depth | Set range from where bottom detector should stop searching for bottom
[**processing_set_bottom_detection_minimum_depth**](ProcessingApi.md#processing_set_bottom_detection_minimum_depth) | **PUT** /api/sounder/processing/{channel_name}/bottom-detection/minimum-depth | Set range from where bottom detector should start searching for bottom
[**processing_set_correlation_limit_percentage**](ProcessingApi.md#processing_set_correlation_limit_percentage) | **PUT** /api/sounder/processing/{channel_name}/adcp/correlation-limit-percentage | Set correlation percentage limit
[**processing_set_error_velocity_limit**](ProcessingApi.md#processing_set_error_velocity_limit) | **PUT** /api/sounder/processing/{channel_name}/adcp/error-velocity-limit | Set error velocity limit
[**processing_set_error_velocity_limit_0**](ProcessingApi.md#processing_set_error_velocity_limit_0) | **PUT** /api/sounder/processing/{channel_name}/adcp/is-error-velocity-limit-active | Activate or deactivate error velocity limit
[**processing_set_is_correlation_limit_percentage_active**](ProcessingApi.md#processing_set_is_correlation_limit_percentage_active) | **PUT** /api/sounder/processing/{channel_name}/adcp/is-correlation-limit-percentage-active | Activate or deactivate correlation percentage limit
[**processing_set_is_min_quality_average_data_factor_active**](ProcessingApi.md#processing_set_is_min_quality_average_data_factor_active) | **PUT** /api/sounder/processing/{channel_name}/adcp/is-min-quality-average-data-factor-active | Activate or deactivate minimum quality average data factor
[**processing_set_min_quality_average_data_percentage**](ProcessingApi.md#processing_set_min_quality_average_data_percentage) | **PUT** /api/sounder/processing/{channel_name}/adcp/min-quality-average-data-percentage | Set minimum quality average data factor
[**processing_set_svd_b_high_limit**](ProcessingApi.md#processing_set_svd_b_high_limit) | **PUT** /api/sounder/processing/{channel_name}/adcp/sv-dB-high-limit | Set maximum limit for Sv
[**processing_set_svd_b_high_limit_active**](ProcessingApi.md#processing_set_svd_b_high_limit_active) | **PUT** /api/sounder/processing/{channel_name}/adcp/is-sv-dB-high-limit-active | Activate or deactivate test on maximum limit for Sv
[**processing_set_svd_b_low_limit**](ProcessingApi.md#processing_set_svd_b_low_limit) | **PUT** /api/sounder/processing/{channel_name}/adcp/sv-dB-low-limit | Set minimum limit for Sv
[**processing_set_svd_b_low_limit_active**](ProcessingApi.md#processing_set_svd_b_low_limit_active) | **PUT** /api/sounder/processing/{channel_name}/adcp/is-sv-dB-low-limit-active | Activate or deactivate test on minimum limit for Sv
[**processing_set_use_epoch_time**](ProcessingApi.md#processing_set_use_epoch_time) | **PUT** /api/sounder/processing/{channel_name}/adcp/use-epoch-time | Switch between PC time or epoch time from transceiver


# **processing_get_adcp_processing_setting**
> ProcessingAdcp processing_get_adcp_processing_setting(channel_name)

Get all adcp processing parameters for specific channel

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.ProcessingApi()
channel_name = 'channel_name_example' # str | The virtual channel id

try:
    # Get all adcp processing parameters for specific channel
    api_response = api_instance.processing_get_adcp_processing_setting(channel_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessingApi->processing_get_adcp_processing_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**| The virtual channel id | 

### Return type

[**ProcessingAdcp**](ProcessingAdcp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processing_get_adcp_processing_settings**
> ProcessingAdcp processing_get_adcp_processing_settings()



### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.ProcessingApi()

try:
    api_response = api_instance.processing_get_adcp_processing_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessingApi->processing_get_adcp_processing_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProcessingAdcp**](ProcessingAdcp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processing_get_bottom_detection_active**
> bool processing_get_bottom_detection_active(channel_name)

Check if bottom detection is on and off

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.ProcessingApi()
channel_name = 'channel_name_example' # str | 

try:
    # Check if bottom detection is on and off
    api_response = api_instance.processing_get_bottom_detection_active(channel_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessingApi->processing_get_bottom_detection_active: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processing_set_bottom_detection_active**
> processing_set_bottom_detection_active(channel_name, active)

Turn on and off bottom detection

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.ProcessingApi()
channel_name = 'channel_name_example' # str | The virtual channel id
active = true # bool | Activate or deactivate bottom detection(true/false)

try:
    # Turn on and off bottom detection
    api_instance.processing_set_bottom_detection_active(channel_name, active)
except ApiException as e:
    print("Exception when calling ProcessingApi->processing_set_bottom_detection_active: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**| The virtual channel id | 
 **active** | **bool**| Activate or deactivate bottom detection(true/false) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processing_set_bottom_detection_backstep**
> processing_set_bottom_detection_backstep(channel_name, backstep)

Set the bottom backstep value for bottom detection

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.ProcessingApi()
channel_name = 'channel_name_example' # str | The virtual channel id
backstep = 1.2 # float | Bottom backstep value [dB]

try:
    # Set the bottom backstep value for bottom detection
    api_instance.processing_set_bottom_detection_backstep(channel_name, backstep)
except ApiException as e:
    print("Exception when calling ProcessingApi->processing_set_bottom_detection_backstep: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**| The virtual channel id | 
 **backstep** | **float**| Bottom backstep value [dB] | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processing_set_bottom_detection_maximum_depth**
> processing_set_bottom_detection_maximum_depth(channel_name, limit)

Set range from where bottom detector should stop searching for bottom

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.ProcessingApi()
channel_name = 'channel_name_example' # str | The virtual channel id
limit = 1.2 # float | Upper bottom detection limit [m]

try:
    # Set range from where bottom detector should stop searching for bottom
    api_instance.processing_set_bottom_detection_maximum_depth(channel_name, limit)
except ApiException as e:
    print("Exception when calling ProcessingApi->processing_set_bottom_detection_maximum_depth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**| The virtual channel id | 
 **limit** | **float**| Upper bottom detection limit [m] | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processing_set_bottom_detection_minimum_depth**
> processing_set_bottom_detection_minimum_depth(channel_name, limit)

Set range from where bottom detector should start searching for bottom

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.ProcessingApi()
channel_name = 'channel_name_example' # str | The virtual channel id
limit = 1.2 # float | Upper bottom detection limit [m]

try:
    # Set range from where bottom detector should start searching for bottom
    api_instance.processing_set_bottom_detection_minimum_depth(channel_name, limit)
except ApiException as e:
    print("Exception when calling ProcessingApi->processing_set_bottom_detection_minimum_depth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**| The virtual channel id | 
 **limit** | **float**| Upper bottom detection limit [m] | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processing_set_correlation_limit_percentage**
> processing_set_correlation_limit_percentage(channel_name, limit)

Set correlation percentage limit

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.ProcessingApi()
channel_name = 'channel_name_example' # str | The virtual channel id
limit = 1.2 # float | The new correlation percentage limit

try:
    # Set correlation percentage limit
    api_instance.processing_set_correlation_limit_percentage(channel_name, limit)
except ApiException as e:
    print("Exception when calling ProcessingApi->processing_set_correlation_limit_percentage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**| The virtual channel id | 
 **limit** | **float**| The new correlation percentage limit | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processing_set_error_velocity_limit**
> processing_set_error_velocity_limit(channel_name, limit)

Set error velocity limit

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.ProcessingApi()
channel_name = 'channel_name_example' # str | The virtual channel id
limit = 1.2 # float | The new error velocity limit

try:
    # Set error velocity limit
    api_instance.processing_set_error_velocity_limit(channel_name, limit)
except ApiException as e:
    print("Exception when calling ProcessingApi->processing_set_error_velocity_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**| The virtual channel id | 
 **limit** | **float**| The new error velocity limit | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processing_set_error_velocity_limit_0**
> processing_set_error_velocity_limit_0(channel_name, active)

Activate or deactivate error velocity limit

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.ProcessingApi()
channel_name = 'channel_name_example' # str | The virtual channel id
active = true # bool | Activate or deactivate (true/false)

try:
    # Activate or deactivate error velocity limit
    api_instance.processing_set_error_velocity_limit_0(channel_name, active)
except ApiException as e:
    print("Exception when calling ProcessingApi->processing_set_error_velocity_limit_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**| The virtual channel id | 
 **active** | **bool**| Activate or deactivate (true/false) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processing_set_is_correlation_limit_percentage_active**
> processing_set_is_correlation_limit_percentage_active(channel_name, active)

Activate or deactivate correlation percentage limit

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.ProcessingApi()
channel_name = 'channel_name_example' # str | The virtual channel id
active = true # bool | Activate or deactivate (true/false)

try:
    # Activate or deactivate correlation percentage limit
    api_instance.processing_set_is_correlation_limit_percentage_active(channel_name, active)
except ApiException as e:
    print("Exception when calling ProcessingApi->processing_set_is_correlation_limit_percentage_active: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**| The virtual channel id | 
 **active** | **bool**| Activate or deactivate (true/false) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processing_set_is_min_quality_average_data_factor_active**
> processing_set_is_min_quality_average_data_factor_active(channel_name, active)

Activate or deactivate minimum quality average data factor

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.ProcessingApi()
channel_name = 'channel_name_example' # str | The virtual channel id
active = true # bool | Activate or deactivate (true/false)

try:
    # Activate or deactivate minimum quality average data factor
    api_instance.processing_set_is_min_quality_average_data_factor_active(channel_name, active)
except ApiException as e:
    print("Exception when calling ProcessingApi->processing_set_is_min_quality_average_data_factor_active: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**| The virtual channel id | 
 **active** | **bool**| Activate or deactivate (true/false) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processing_set_min_quality_average_data_percentage**
> processing_set_min_quality_average_data_percentage(channel_name, limit)

Set minimum quality average data factor

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.ProcessingApi()
channel_name = 'channel_name_example' # str | The virtual channel id
limit = 1.2 # float | The new minimum quality average data factor

try:
    # Set minimum quality average data factor
    api_instance.processing_set_min_quality_average_data_percentage(channel_name, limit)
except ApiException as e:
    print("Exception when calling ProcessingApi->processing_set_min_quality_average_data_percentage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**| The virtual channel id | 
 **limit** | **float**| The new minimum quality average data factor | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processing_set_svd_b_high_limit**
> processing_set_svd_b_high_limit(channel_name, limit)

Set maximum limit for Sv

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.ProcessingApi()
channel_name = 'channel_name_example' # str | The virtual channel id
limit = 56 # int | The new maximum limit for Sv in dB

try:
    # Set maximum limit for Sv
    api_instance.processing_set_svd_b_high_limit(channel_name, limit)
except ApiException as e:
    print("Exception when calling ProcessingApi->processing_set_svd_b_high_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**| The virtual channel id | 
 **limit** | **int**| The new maximum limit for Sv in dB | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processing_set_svd_b_high_limit_active**
> processing_set_svd_b_high_limit_active(channel_name, active)

Activate or deactivate test on maximum limit for Sv

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.ProcessingApi()
channel_name = 'channel_name_example' # str | The virtual channel id
active = true # bool | Activate or deactivate (true/false)

try:
    # Activate or deactivate test on maximum limit for Sv
    api_instance.processing_set_svd_b_high_limit_active(channel_name, active)
except ApiException as e:
    print("Exception when calling ProcessingApi->processing_set_svd_b_high_limit_active: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**| The virtual channel id | 
 **active** | **bool**| Activate or deactivate (true/false) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processing_set_svd_b_low_limit**
> processing_set_svd_b_low_limit(channel_name, limit)

Set minimum limit for Sv

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.ProcessingApi()
channel_name = 'channel_name_example' # str | The virtual channel id
limit = 56 # int | The new minimum limit for Sv in dB

try:
    # Set minimum limit for Sv
    api_instance.processing_set_svd_b_low_limit(channel_name, limit)
except ApiException as e:
    print("Exception when calling ProcessingApi->processing_set_svd_b_low_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**| The virtual channel id | 
 **limit** | **int**| The new minimum limit for Sv in dB | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processing_set_svd_b_low_limit_active**
> processing_set_svd_b_low_limit_active(channel_name, active)

Activate or deactivate test on minimum limit for Sv

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.ProcessingApi()
channel_name = 'channel_name_example' # str | The virtual channel id
active = true # bool | Activate or deactivate (true/false)

try:
    # Activate or deactivate test on minimum limit for Sv
    api_instance.processing_set_svd_b_low_limit_active(channel_name, active)
except ApiException as e:
    print("Exception when calling ProcessingApi->processing_set_svd_b_low_limit_active: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**| The virtual channel id | 
 **active** | **bool**| Activate or deactivate (true/false) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processing_set_use_epoch_time**
> processing_set_use_epoch_time(channel_name, active)

Switch between PC time or epoch time from transceiver

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.ProcessingApi()
channel_name = 'channel_name_example' # str | The virtual channel id
active = true # bool | Activate or deactivate epoch time(true/false)

try:
    # Switch between PC time or epoch time from transceiver
    api_instance.processing_set_use_epoch_time(channel_name, active)
except ApiException as e:
    print("Exception when calling ProcessingApi->processing_set_use_epoch_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**| The virtual channel id | 
 **active** | **bool**| Activate or deactivate epoch time(true/false) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

