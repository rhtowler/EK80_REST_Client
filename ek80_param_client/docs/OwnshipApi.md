# ek80_param_client.OwnshipApi

All URIs are relative to *http://localhost:12345*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ownship_get_dimension**](OwnshipApi.md#ownship_get_dimension) | **GET** /api/ownship/dimension | Get ownship dimension settings
[**ownship_get_drop_keel_offset**](OwnshipApi.md#ownship_get_drop_keel_offset) | **GET** /api/ownship/manual-settings/drop-keel-offset | Get drop keel offset
[**ownship_get_installed_transducers**](OwnshipApi.md#ownship_get_installed_transducers) | **GET** /api/ownship/installation/transducers | Get a list of all installed transducers
[**ownship_get_manual_settings**](OwnshipApi.md#ownship_get_manual_settings) | **GET** /api/ownship/manual-settings | Get a list of all manual settings
[**ownship_get_manual_speed_setting**](OwnshipApi.md#ownship_get_manual_speed_setting) | **GET** /api/ownship/manual-settings/vessel-speed | Get manual speed settings
[**ownship_get_motion**](OwnshipApi.md#ownship_get_motion) | **GET** /api/ownship/motion | Get ownship motion settings
[**ownship_get_navigation**](OwnshipApi.md#ownship_get_navigation) | **GET** /api/ownship/navigation | Get ownship navigation settings
[**ownship_get_ownship**](OwnshipApi.md#ownship_get_ownship) | **GET** /api/ownship | Get ownship settings
[**ownship_get_water_level**](OwnshipApi.md#ownship_get_water_level) | **GET** /api/ownship/manual-settings/water-level | Get water level offset
[**ownship_set_drop_keel_offset**](OwnshipApi.md#ownship_set_drop_keel_offset) | **PUT** /api/ownship/manual-settings/drop-keel-offset | Set drop keel offset
[**ownship_set_manual_speed_setting**](OwnshipApi.md#ownship_set_manual_speed_setting) | **PUT** /api/ownship/manual-settings/vessel-speed | Set manual speed setting
[**ownship_set_transducer_installation**](OwnshipApi.md#ownship_set_transducer_installation) | **PUT** /api/ownship/installation/{transducerId} | Sets a new intallation for a given transducer
[**ownship_set_water_level**](OwnshipApi.md#ownship_set_water_level) | **PUT** /api/ownship/manual-settings/water-level | Set water level offset


# **ownship_get_dimension**
> Dimension ownship_get_dimension()

Get ownship dimension settings

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.OwnshipApi()

try:
    # Get ownship dimension settings
    api_response = api_instance.ownship_get_dimension()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnshipApi->ownship_get_dimension: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Dimension**](Dimension.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ownship_get_drop_keel_offset**
> ManualSetting ownship_get_drop_keel_offset()

Get drop keel offset

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.OwnshipApi()

try:
    # Get drop keel offset
    api_response = api_instance.ownship_get_drop_keel_offset()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnshipApi->ownship_get_drop_keel_offset: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ManualSetting**](ManualSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ownship_get_installed_transducers**
> dict(str, Installation) ownship_get_installed_transducers()

Get a list of all installed transducers

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.OwnshipApi()

try:
    # Get a list of all installed transducers
    api_response = api_instance.ownship_get_installed_transducers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnshipApi->ownship_get_installed_transducers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, Installation)**](Installation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ownship_get_manual_settings**
> dict(str, ManualSetting) ownship_get_manual_settings()

Get a list of all manual settings

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.OwnshipApi()

try:
    # Get a list of all manual settings
    api_response = api_instance.ownship_get_manual_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnshipApi->ownship_get_manual_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, ManualSetting)**](ManualSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ownship_get_manual_speed_setting**
> ManualSetting ownship_get_manual_speed_setting()

Get manual speed settings

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.OwnshipApi()

try:
    # Get manual speed settings
    api_response = api_instance.ownship_get_manual_speed_setting()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnshipApi->ownship_get_manual_speed_setting: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ManualSetting**](ManualSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ownship_get_motion**
> MotionData ownship_get_motion()

Get ownship motion settings

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.OwnshipApi()

try:
    # Get ownship motion settings
    api_response = api_instance.ownship_get_motion()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnshipApi->ownship_get_motion: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MotionData**](MotionData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ownship_get_navigation**
> NavigationData ownship_get_navigation()

Get ownship navigation settings

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.OwnshipApi()

try:
    # Get ownship navigation settings
    api_response = api_instance.ownship_get_navigation()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnshipApi->ownship_get_navigation: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NavigationData**](NavigationData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ownship_get_ownship**
> Ownship ownship_get_ownship()

Get ownship settings

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.OwnshipApi()

try:
    # Get ownship settings
    api_response = api_instance.ownship_get_ownship()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnshipApi->ownship_get_ownship: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Ownship**](Ownship.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ownship_get_water_level**
> ManualSetting ownship_get_water_level()

Get water level offset

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.OwnshipApi()

try:
    # Get water level offset
    api_response = api_instance.ownship_get_water_level()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnshipApi->ownship_get_water_level: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ManualSetting**](ManualSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ownship_set_drop_keel_offset**
> ownship_set_drop_keel_offset(dropkeel_settings)

Set drop keel offset

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.OwnshipApi()
dropkeel_settings = ek80_param_client.ManualSetting() # ManualSetting | The new offset value and IsManual flag. New value only takes effect if IsManual is true

try:
    # Set drop keel offset
    api_instance.ownship_set_drop_keel_offset(dropkeel_settings)
except ApiException as e:
    print("Exception when calling OwnshipApi->ownship_set_drop_keel_offset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dropkeel_settings** | [**ManualSetting**](ManualSetting.md)| The new offset value and IsManual flag. New value only takes effect if IsManual is true | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ownship_set_manual_speed_setting**
> ownship_set_manual_speed_setting(speed_settings)

Set manual speed setting

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.OwnshipApi()
speed_settings = ek80_param_client.ManualSetting() # ManualSetting | The new vessel speed value and IsManual flag. New value only takes effect if IsManual is true

try:
    # Set manual speed setting
    api_instance.ownship_set_manual_speed_setting(speed_settings)
except ApiException as e:
    print("Exception when calling OwnshipApi->ownship_set_manual_speed_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **speed_settings** | [**ManualSetting**](ManualSetting.md)| The new vessel speed value and IsManual flag. New value only takes effect if IsManual is true | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ownship_set_transducer_installation**
> ownship_set_transducer_installation(transducer_id, installation)

Sets a new intallation for a given transducer

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.OwnshipApi()
transducer_id = 'transducer_id_example' # str | Custom Name of the transducer to be updated
installation = ek80_param_client.Installation() # Installation | The new installation struct for the specified transducer

try:
    # Sets a new intallation for a given transducer
    api_instance.ownship_set_transducer_installation(transducer_id, installation)
except ApiException as e:
    print("Exception when calling OwnshipApi->ownship_set_transducer_installation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transducer_id** | **str**| Custom Name of the transducer to be updated | 
 **installation** | [**Installation**](Installation.md)| The new installation struct for the specified transducer | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ownship_set_water_level**
> ownship_set_water_level(water_level_settings)

Set water level offset

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.OwnshipApi()
water_level_settings = ek80_param_client.ManualSetting() # ManualSetting | The new water level offset value and IsManual flag. New value only takes effect if IsManual is true

try:
    # Set water level offset
    api_instance.ownship_set_water_level(water_level_settings)
except ApiException as e:
    print("Exception when calling OwnshipApi->ownship_set_water_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **water_level_settings** | [**ManualSetting**](ManualSetting.md)| The new water level offset value and IsManual flag. New value only takes effect if IsManual is true | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

