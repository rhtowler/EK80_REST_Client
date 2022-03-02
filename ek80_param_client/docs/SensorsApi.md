# ek80_param_client.SensorsApi

All URIs are relative to *http://localhost:12345*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sensors_add_or_update_sensor**](SensorsApi.md#sensors_add_or_update_sensor) | **POST** /api/sensors/installed-sensors | Adds a new sensor.
[**sensors_delete_sensor**](SensorsApi.md#sensors_delete_sensor) | **DELETE** /api/sensors/installed-sensors/{customName} | Deletes a sensor.
[**sensors_get_available_sensors**](SensorsApi.md#sensors_get_available_sensors) | **GET** /api/sensors/available-sensors | Get list of all sensor types that can be installed.
[**sensors_get_installed_sensors**](SensorsApi.md#sensors_get_installed_sensors) | **GET** /api/sensors | Get list of all installed sensors
[**sensors_get_installed_sensors_full**](SensorsApi.md#sensors_get_installed_sensors_full) | **GET** /api/sensors/installed-sensors | Get list of all sensors that are installed.


# **sensors_add_or_update_sensor**
> sensors_add_or_update_sensor(sensor_def)

Adds a new sensor.

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SensorsApi()
sensor_def = ek80_param_client.ConfiguredSensorDefinition() # ConfiguredSensorDefinition | A ConfiguredSensorDefinition that the defines the sensor to add.

try:
    # Adds a new sensor.
    api_instance.sensors_add_or_update_sensor(sensor_def)
except ApiException as e:
    print("Exception when calling SensorsApi->sensors_add_or_update_sensor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_def** | [**ConfiguredSensorDefinition**](ConfiguredSensorDefinition.md)| A ConfiguredSensorDefinition that the defines the sensor to add. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensors_delete_sensor**
> sensors_delete_sensor(custom_name)

Deletes a sensor.

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SensorsApi()
custom_name = 'custom_name_example' # str | Custom name of the sensor to delete.

try:
    # Deletes a sensor.
    api_instance.sensors_delete_sensor(custom_name)
except ApiException as e:
    print("Exception when calling SensorsApi->sensors_delete_sensor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_name** | **str**| Custom name of the sensor to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensors_get_available_sensors**
> list[AvailableSensor] sensors_get_available_sensors()

Get list of all sensor types that can be installed.

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SensorsApi()

try:
    # Get list of all sensor types that can be installed.
    api_response = api_instance.sensors_get_available_sensors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensors_get_available_sensors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AvailableSensor]**](AvailableSensor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensors_get_installed_sensors**
> list[str] sensors_get_installed_sensors()

Get list of all installed sensors

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SensorsApi()

try:
    # Get list of all installed sensors
    api_response = api_instance.sensors_get_installed_sensors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensors_get_installed_sensors: %s\n" % e)
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

# **sensors_get_installed_sensors_full**
> list[ConfiguredSensorDefinition] sensors_get_installed_sensors_full()

Get list of all sensors that are installed.

### Example
```python
from __future__ import print_function
import time
import ek80_param_client
from ek80_param_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_param_client.SensorsApi()

try:
    # Get list of all sensors that are installed.
    api_response = api_instance.sensors_get_installed_sensors_full()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensors_get_installed_sensors_full: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ConfiguredSensorDefinition]**](ConfiguredSensorDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

