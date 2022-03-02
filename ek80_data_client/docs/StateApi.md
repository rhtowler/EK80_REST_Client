# ek80_data_client.StateApi

All URIs are relative to *http://localhost:12346*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_communication_end_points**](StateApi.md#get_active_communication_end_points) | **GET** /api/sounder/data-output/state/communication-end-points | Get information about the active communication end points
[**get_available_data_sources**](StateApi.md#get_available_data_sources) | **GET** /api/sounder/data-output/state/data-sources | Get information about data sources currently available to be used in data subscription requests
[**get_data_output_state**](StateApi.md#get_data_output_state) | **GET** /api/sounder/data-output/state | Get information about the data output of the system
[**get_subscription_summaries**](StateApi.md#get_subscription_summaries) | **GET** /api/sounder/data-output/state/subscription-summary | Get information about active data subscriptions


# **get_active_communication_end_points**
> list[CommunicationEndPointInfo] get_active_communication_end_points()

Get information about the active communication end points

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.StateApi()

try:
    # Get information about the active communication end points
    api_response = api_instance.get_active_communication_end_points()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateApi->get_active_communication_end_points: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CommunicationEndPointInfo]**](CommunicationEndPointInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_data_sources**
> list[str] get_available_data_sources()

Get information about data sources currently available to be used in data subscription requests

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.StateApi()

try:
    # Get information about data sources currently available to be used in data subscription requests
    api_response = api_instance.get_available_data_sources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateApi->get_available_data_sources: %s\n" % e)
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

# **get_data_output_state**
> DataOutputState get_data_output_state()

Get information about the data output of the system

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.StateApi()

try:
    # Get information about the data output of the system
    api_response = api_instance.get_data_output_state()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateApi->get_data_output_state: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DataOutputState**](DataOutputState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_summaries**
> list[SubscriptionSummary] get_subscription_summaries()

Get information about active data subscriptions

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.StateApi()

try:
    # Get information about active data subscriptions
    api_response = api_instance.get_subscription_summaries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateApi->get_subscription_summaries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SubscriptionSummary]**](SubscriptionSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

