# ek80_data_client.OperationApi

All URIs are relative to *http://localhost:12346*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_auto_range**](OperationApi.md#get_auto_range) | **GET** /api/sounder/operation/auto-display-range | Get ping auto display range
[**get_ext_sync**](OperationApi.md#get_ext_sync) | **GET** /api/sounder/operation/external-sync | Get external sync settings
[**get_ext_sync_delay**](OperationApi.md#get_ext_sync_delay) | **GET** /api/sounder/operation/external-sync/delay | Get synchronization delay
[**get_ext_sync_mode**](OperationApi.md#get_ext_sync_mode) | **GET** /api/sounder/operation/external-sync/sync-mode | Get synchronization mode
[**get_operation_mode**](OperationApi.md#get_operation_mode) | **GET** /api/sounder/operation/operation-mode | Get operation mode
[**get_operational_state**](OperationApi.md#get_operational_state) | **GET** /api/sounder/operation | Get operation state of the application
[**get_ping_interval**](OperationApi.md#get_ping_interval) | **GET** /api/sounder/operation/ping-interval | Get ping interval
[**get_ping_mode**](OperationApi.md#get_ping_mode) | **GET** /api/sounder/operation/ping-mode | Get ping mode
[**get_play_state**](OperationApi.md#get_play_state) | **GET** /api/sounder/operation/play-state | Get play state
[**get_range**](OperationApi.md#get_range) | **GET** /api/sounder/operation/display-range | Get ping display range
[**put_auto_range**](OperationApi.md#put_auto_range) | **PUT** /api/sounder/operation/auto-display-range | Set ping auto display range
[**put_ext_sync**](OperationApi.md#put_ext_sync) | **PUT** /api/sounder/operation/external-sync | Set external sync settings
[**put_ext_sync_delay**](OperationApi.md#put_ext_sync_delay) | **PUT** /api/sounder/operation/external-sync/delay | Set synchronization delay
[**put_ext_sync_mode**](OperationApi.md#put_ext_sync_mode) | **PUT** /api/sounder/operation/external-sync/sync-mode | Set synchronization mode
[**put_operation_mode**](OperationApi.md#put_operation_mode) | **PUT** /api/sounder/operation/operation-mode | Set operation mode
[**put_ping_interval**](OperationApi.md#put_ping_interval) | **PUT** /api/sounder/operation/ping-interval | Set ping interval
[**put_ping_mode**](OperationApi.md#put_ping_mode) | **PUT** /api/sounder/operation/ping-mode | Set ping mode
[**put_play_state**](OperationApi.md#put_play_state) | **PUT** /api/sounder/operation/play-state | Set play state
[**put_range**](OperationApi.md#put_range) | **PUT** /api/sounder/operation/display-range | Set ping display range


# **get_auto_range**
> bool get_auto_range()

Get ping auto display range

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.OperationApi()

try:
    # Get ping auto display range
    api_response = api_instance.get_auto_range()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationApi->get_auto_range: %s\n" % e)
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

# **get_ext_sync**
> ExternalSync get_ext_sync()

Get external sync settings

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.OperationApi()

try:
    # Get external sync settings
    api_response = api_instance.get_ext_sync()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationApi->get_ext_sync: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ExternalSync**](ExternalSync.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ext_sync_delay**
> int get_ext_sync_delay()

Get synchronization delay

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.OperationApi()

try:
    # Get synchronization delay
    api_response = api_instance.get_ext_sync_delay()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationApi->get_ext_sync_delay: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ext_sync_mode**
> str get_ext_sync_mode()

Get synchronization mode

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.OperationApi()

try:
    # Get synchronization mode
    api_response = api_instance.get_ext_sync_mode()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationApi->get_ext_sync_mode: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operation_mode**
> str get_operation_mode()

Get operation mode

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.OperationApi()

try:
    # Get operation mode
    api_response = api_instance.get_operation_mode()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationApi->get_operation_mode: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operational_state**
> OperationalState get_operational_state()

Get operation state of the application

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.OperationApi()

try:
    # Get operation state of the application
    api_response = api_instance.get_operational_state()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationApi->get_operational_state: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OperationalState**](OperationalState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ping_interval**
> int get_ping_interval()

Get ping interval

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.OperationApi()

try:
    # Get ping interval
    api_response = api_instance.get_ping_interval()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationApi->get_ping_interval: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ping_mode**
> str get_ping_mode()

Get ping mode

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.OperationApi()

try:
    # Get ping mode
    api_response = api_instance.get_ping_mode()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationApi->get_ping_mode: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_play_state**
> str get_play_state()

Get play state

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.OperationApi()

try:
    # Get play state
    api_response = api_instance.get_play_state()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationApi->get_play_state: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_range**
> float get_range()

Get ping display range

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.OperationApi()

try:
    # Get ping display range
    api_response = api_instance.get_range()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationApi->get_range: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**float**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_auto_range**
> put_auto_range(auto_display_range)

Set ping auto display range

This operation will set display range to Auto

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.OperationApi()
auto_display_range = true # bool | The new auto display range

try:
    # Set ping auto display range
    api_instance.put_auto_range(auto_display_range)
except ApiException as e:
    print("Exception when calling OperationApi->put_auto_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_display_range** | **bool**| The new auto display range | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_ext_sync**
> put_ext_sync(es)

Set external sync settings

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.OperationApi()
es = ek80_data_client.ExternalSync() # ExternalSync | 

try:
    # Set external sync settings
    api_instance.put_ext_sync(es)
except ApiException as e:
    print("Exception when calling OperationApi->put_ext_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **es** | [**ExternalSync**](ExternalSync.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_ext_sync_delay**
> put_ext_sync_delay(delay)

Set synchronization delay

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.OperationApi()
delay = 56 # int | 

try:
    # Set synchronization delay
    api_instance.put_ext_sync_delay(delay)
except ApiException as e:
    print("Exception when calling OperationApi->put_ext_sync_delay: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delay** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_ext_sync_mode**
> put_ext_sync_mode(sync_mode)

Set synchronization mode

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.OperationApi()
sync_mode = 'sync_mode_example' # str | 

try:
    # Set synchronization mode
    api_instance.put_ext_sync_mode(sync_mode)
except ApiException as e:
    print("Exception when calling OperationApi->put_ext_sync_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_mode** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_operation_mode**
> put_operation_mode(operation_mode)

Set operation mode

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.OperationApi()
operation_mode = 'operation_mode_example' # str | The new operation mode

try:
    # Set operation mode
    api_instance.put_operation_mode(operation_mode)
except ApiException as e:
    print("Exception when calling OperationApi->put_operation_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_mode** | **str**| The new operation mode | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_ping_interval**
> put_ping_interval(ping_interval)

Set ping interval

'ping-mode' must be set to 'interval' for this to take effect

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.OperationApi()
ping_interval = 56 # int | The new ping interval (ms) [20 - 2000000000]

try:
    # Set ping interval
    api_instance.put_ping_interval(ping_interval)
except ApiException as e:
    print("Exception when calling OperationApi->put_ping_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ping_interval** | **int**| The new ping interval (ms) [20 - 2000000000] | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_ping_mode**
> put_ping_mode(ping_mode)

Set ping mode

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.OperationApi()
ping_mode = 'ping_mode_example' # str | The new ping mode

try:
    # Set ping mode
    api_instance.put_ping_mode(ping_mode)
except ApiException as e:
    print("Exception when calling OperationApi->put_ping_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ping_mode** | **str**| The new ping mode | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_play_state**
> put_play_state(play_state)

Set play state

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.OperationApi()
play_state = 'play_state_example' # str | The new play state

try:
    # Set play state
    api_instance.put_play_state(play_state)
except ApiException as e:
    print("Exception when calling OperationApi->put_play_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **play_state** | **str**| The new play state | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_range**
> put_range(display_range)

Set ping display range

This operation will only take effect when the Display Range setting in the EK80 UI is not set to 'Auto'

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.OperationApi()
display_range = 1.2 # float | The new display range (m) [1 - 12500]

try:
    # Set ping display range
    api_instance.put_range(display_range)
except ApiException as e:
    print("Exception when calling OperationApi->put_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_range** | **float**| The new display range (m) [1 - 12500] | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

