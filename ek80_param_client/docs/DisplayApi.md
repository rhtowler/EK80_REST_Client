# ek80_param_client.DisplayApi

All URIs are relative to *http://localhost:12345*

Method | HTTP request | Description
------------- | ------------- | -------------
[**display_get**](DisplayApi.md#display_get) | **GET** /api/display | 
[**display_get_display_palette**](DisplayApi.md#display_get_display_palette) | **GET** /api/display/display-palette | 
[**display_get_display_settings**](DisplayApi.md#display_get_display_settings) | **GET** /api/display/settings | 
[**display_get_echo_colours**](DisplayApi.md#display_get_echo_colours) | **GET** /api/display/echo-colours | 
[**display_get_full_screen**](DisplayApi.md#display_get_full_screen) | **GET** /api/display/full-screen | 
[**display_get_screen_brightness**](DisplayApi.md#display_get_screen_brightness) | **GET** /api/display/screen-brightness | 
[**display_put_display_palette**](DisplayApi.md#display_put_display_palette) | **PUT** /api/display/display-palette | 
[**display_put_display_settings**](DisplayApi.md#display_put_display_settings) | **PUT** /api/display/settings | 
[**display_put_echo_colours**](DisplayApi.md#display_put_echo_colours) | **PUT** /api/display/echo-colours | 
[**display_put_full_screen**](DisplayApi.md#display_put_full_screen) | **PUT** /api/display/full-screen | 
[**display_put_screen_brightness**](DisplayApi.md#display_put_screen_brightness) | **PUT** /api/display/screen-brightness | 


# **display_get**
> DisplaySettings display_get()



### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.DisplayApi()

try:
    api_response = api_instance.display_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayApi->display_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DisplaySettings**](DisplaySettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_get_display_palette**
> str display_get_display_palette()



### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.DisplayApi()

try:
    api_response = api_instance.display_get_display_palette()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayApi->display_get_display_palette: %s\n" % e)
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

# **display_get_display_settings**
> DisplaySettings display_get_display_settings()



### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.DisplayApi()

try:
    api_response = api_instance.display_get_display_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayApi->display_get_display_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DisplaySettings**](DisplaySettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_get_echo_colours**
> str display_get_echo_colours()



### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.DisplayApi()

try:
    api_response = api_instance.display_get_echo_colours()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayApi->display_get_echo_colours: %s\n" % e)
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

# **display_get_full_screen**
> bool display_get_full_screen()



### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.DisplayApi()

try:
    api_response = api_instance.display_get_full_screen()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayApi->display_get_full_screen: %s\n" % e)
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

# **display_get_screen_brightness**
> int display_get_screen_brightness()



### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.DisplayApi()

try:
    api_response = api_instance.display_get_screen_brightness()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayApi->display_get_screen_brightness: %s\n" % e)
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

# **display_put_display_palette**
> display_put_display_palette(palette)



### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.DisplayApi()
palette = 'palette_example' # str | 

try:
    api_instance.display_put_display_palette(palette)
except ApiException as e:
    print("Exception when calling DisplayApi->display_put_display_palette: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **palette** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_put_display_settings**
> display_put_display_settings(settings)



### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.DisplayApi()
settings = ek80_param_client.DisplaySettings() # DisplaySettings | 

try:
    api_instance.display_put_display_settings(settings)
except ApiException as e:
    print("Exception when calling DisplayApi->display_put_display_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings** | [**DisplaySettings**](DisplaySettings.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_put_echo_colours**
> display_put_echo_colours(colours)



### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.DisplayApi()
colours = 'colours_example' # str | 

try:
    api_instance.display_put_echo_colours(colours)
except ApiException as e:
    print("Exception when calling DisplayApi->display_put_echo_colours: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **colours** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_put_full_screen**
> display_put_full_screen(fullscreen)



### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.DisplayApi()
fullscreen = true # bool | 

try:
    api_instance.display_put_full_screen(fullscreen)
except ApiException as e:
    print("Exception when calling DisplayApi->display_put_full_screen: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fullscreen** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **display_put_screen_brightness**
> display_put_screen_brightness(brightness)



### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.DisplayApi()
brightness = 789 # int | 

try:
    api_instance.display_put_screen_brightness(brightness)
except ApiException as e:
    print("Exception when calling DisplayApi->display_put_screen_brightness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brightness** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

