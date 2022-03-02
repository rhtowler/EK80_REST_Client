# ek80_param_client.SystemApi

All URIs are relative to *http://localhost:12345*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_get**](SystemApi.md#system_get) | **GET** /api/system | Get current state of the application
[**system_get_active_user_settings**](SystemApi.md#system_get_active_user_settings) | **GET** /api/system/active-user-settings | Get current user setting
[**system_get_application_details**](SystemApi.md#system_get_application_details) | **GET** /api/system/application-details | Get details about the application
[**system_get_ext_sync**](SystemApi.md#system_get_ext_sync) | **GET** /api/system/external-sync | Get current external sync settings
[**system_get_ext_sync_delay**](SystemApi.md#system_get_ext_sync_delay) | **GET** /api/system/external-sync/delay | Get current synchronization delay
[**system_get_ext_sync_mode**](SystemApi.md#system_get_ext_sync_mode) | **GET** /api/system/external-sync/mode | Get current synchronization mode
[**system_get_operation_mode**](SystemApi.md#system_get_operation_mode) | **GET** /api/system/operation-mode | Get current operation mode
[**system_get_operational_state**](SystemApi.md#system_get_operational_state) | **GET** /api/system/operational-state | Get current state of the application
[**system_get_ping_interval**](SystemApi.md#system_get_ping_interval) | **GET** /api/system/ping-interval | Get current ping interval (when ping-mode is set to interval)
[**system_get_ping_mode**](SystemApi.md#system_get_ping_mode) | **GET** /api/system/ping-mode | Get current ping mode
[**system_get_play_state**](SystemApi.md#system_get_play_state) | **GET** /api/system/play-state | Get current play state
[**system_put_active_user_settings**](SystemApi.md#system_put_active_user_settings) | **PUT** /api/system/active-user-settings | Set current user setting
[**system_put_ext_sync**](SystemApi.md#system_put_ext_sync) | **PUT** /api/system/external-sync | Set current external sync settings
[**system_put_ext_sync_delay**](SystemApi.md#system_put_ext_sync_delay) | **PUT** /api/system/external-sync/delay | Set current synchronization delay
[**system_put_ext_sync_mode**](SystemApi.md#system_put_ext_sync_mode) | **PUT** /api/system/external-sync/mode | Set current synchronization mode
[**system_put_operation_mode**](SystemApi.md#system_put_operation_mode) | **PUT** /api/system/operation-mode | Set current operation mode
[**system_put_ping_interval**](SystemApi.md#system_put_ping_interval) | **PUT** /api/system/ping-interval | Set current ping interval
[**system_put_ping_mode**](SystemApi.md#system_put_ping_mode) | **PUT** /api/system/ping-mode | Set current ping mode
[**system_put_play_state**](SystemApi.md#system_put_play_state) | **PUT** /api/system/play-state | Set current play state


# **system_get**
> OperationalState system_get()

Get current state of the application

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SystemApi()

try:
    # Get current state of the application
    api_response = api_instance.system_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_get: %s\n" % e)
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

# **system_get_active_user_settings**
> str system_get_active_user_settings()

Get current user setting

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SystemApi()

try:
    # Get current user setting
    api_response = api_instance.system_get_active_user_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_get_active_user_settings: %s\n" % e)
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

# **system_get_application_details**
> ApplicationDetails system_get_application_details()

Get details about the application

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SystemApi()

try:
    # Get details about the application
    api_response = api_instance.system_get_application_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_get_application_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApplicationDetails**](ApplicationDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_get_ext_sync**
> ExternalSync system_get_ext_sync()

Get current external sync settings

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SystemApi()

try:
    # Get current external sync settings
    api_response = api_instance.system_get_ext_sync()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_get_ext_sync: %s\n" % e)
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

# **system_get_ext_sync_delay**
> int system_get_ext_sync_delay()

Get current synchronization delay

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SystemApi()

try:
    # Get current synchronization delay
    api_response = api_instance.system_get_ext_sync_delay()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_get_ext_sync_delay: %s\n" % e)
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

# **system_get_ext_sync_mode**
> str system_get_ext_sync_mode()

Get current synchronization mode

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SystemApi()

try:
    # Get current synchronization mode
    api_response = api_instance.system_get_ext_sync_mode()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_get_ext_sync_mode: %s\n" % e)
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

# **system_get_operation_mode**
> str system_get_operation_mode()

Get current operation mode

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SystemApi()

try:
    # Get current operation mode
    api_response = api_instance.system_get_operation_mode()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_get_operation_mode: %s\n" % e)
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

# **system_get_operational_state**
> OperationalState system_get_operational_state()

Get current state of the application

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SystemApi()

try:
    # Get current state of the application
    api_response = api_instance.system_get_operational_state()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_get_operational_state: %s\n" % e)
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

# **system_get_ping_interval**
> int system_get_ping_interval()

Get current ping interval (when ping-mode is set to interval)

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SystemApi()

try:
    # Get current ping interval (when ping-mode is set to interval)
    api_response = api_instance.system_get_ping_interval()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_get_ping_interval: %s\n" % e)
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

# **system_get_ping_mode**
> str system_get_ping_mode()

Get current ping mode

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SystemApi()

try:
    # Get current ping mode
    api_response = api_instance.system_get_ping_mode()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_get_ping_mode: %s\n" % e)
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

# **system_get_play_state**
> str system_get_play_state()

Get current play state

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SystemApi()

try:
    # Get current play state
    api_response = api_instance.system_get_play_state()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_get_play_state: %s\n" % e)
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

# **system_put_active_user_settings**
> system_put_active_user_settings(user_settings)

Set current user setting

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SystemApi()
user_settings = 'user_settings_example' # str | 

try:
    # Set current user setting
    api_instance.system_put_active_user_settings(user_settings)
except ApiException as e:
    print("Exception when calling SystemApi->system_put_active_user_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_settings** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_put_ext_sync**
> system_put_ext_sync(es)

Set current external sync settings

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SystemApi()
es = ek80_param_client.ExternalSync() # ExternalSync | 

try:
    # Set current external sync settings
    api_instance.system_put_ext_sync(es)
except ApiException as e:
    print("Exception when calling SystemApi->system_put_ext_sync: %s\n" % e)
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

# **system_put_ext_sync_delay**
> system_put_ext_sync_delay(delay)

Set current synchronization delay

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SystemApi()
delay = 56 # int | 

try:
    # Set current synchronization delay
    api_instance.system_put_ext_sync_delay(delay)
except ApiException as e:
    print("Exception when calling SystemApi->system_put_ext_sync_delay: %s\n" % e)
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

# **system_put_ext_sync_mode**
> system_put_ext_sync_mode(mode)

Set current synchronization mode

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SystemApi()
mode = 'mode_example' # str | 

try:
    # Set current synchronization mode
    api_instance.system_put_ext_sync_mode(mode)
except ApiException as e:
    print("Exception when calling SystemApi->system_put_ext_sync_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mode** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_put_operation_mode**
> system_put_operation_mode(mode)

Set current operation mode

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SystemApi()
mode = 'mode_example' # str | The new operation mode

try:
    # Set current operation mode
    api_instance.system_put_operation_mode(mode)
except ApiException as e:
    print("Exception when calling SystemApi->system_put_operation_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mode** | **str**| The new operation mode | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_put_ping_interval**
> system_put_ping_interval(interval)

Set current ping interval

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SystemApi()
interval = 56 # int | 

try:
    # Set current ping interval
    api_instance.system_put_ping_interval(interval)
except ApiException as e:
    print("Exception when calling SystemApi->system_put_ping_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interval** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_put_ping_mode**
> system_put_ping_mode(mode)

Set current ping mode

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SystemApi()
mode = 'mode_example' # str | The new ping mode

try:
    # Set current ping mode
    api_instance.system_put_ping_mode(mode)
except ApiException as e:
    print("Exception when calling SystemApi->system_put_ping_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mode** | **str**| The new ping mode | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_put_play_state**
> system_put_play_state(state)

Set current play state

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SystemApi()
state = 'state_example' # str | The new play state

try:
    # Set current play state
    api_instance.system_put_play_state(state)
except ApiException as e:
    print("Exception when calling SystemApi->system_put_play_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| The new play state | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

