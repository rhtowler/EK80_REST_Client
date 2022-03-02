# ek80_data_client.CommunicationEndPointsApi

All URIs are relative to *http://localhost:12346*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_subscription_to_end_point**](CommunicationEndPointsApi.md#add_subscription_to_end_point) | **POST** /api/sounder/data-output/communication-end-points/{endPointId}/data-subscriptions | Add a subscription to the communication end point
[**create_communication_end_point**](CommunicationEndPointsApi.md#create_communication_end_point) | **POST** /api/sounder/data-output/communication-end-points | Create a new communication end point
[**delete_communication_end_point**](CommunicationEndPointsApi.md#delete_communication_end_point) | **DELETE** /api/sounder/data-output/communication-end-points/{endPointId} | Delete a communication end point
[**get_active_communication_end_points**](CommunicationEndPointsApi.md#get_active_communication_end_points) | **GET** /api/sounder/data-output/communication-end-points | Get information about the active communication end points
[**get_subscriptions_by_end_point**](CommunicationEndPointsApi.md#get_subscriptions_by_end_point) | **GET** /api/sounder/data-output/communication-end-points/{endPointId}/data-subscriptions | Get the active data subscriptions for the end point
[**remove_subscription_from_end_point**](CommunicationEndPointsApi.md#remove_subscription_from_end_point) | **DELETE** /api/sounder/data-output/communication-end-points/{endPointId}/data-subscriptions | Remove a subscription from the communication end point


# **add_subscription_to_end_point**
> add_subscription_to_end_point(end_point_id, subscription_output_args)

Add a subscription to the communication end point

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.CommunicationEndPointsApi()
end_point_id = 789 # int | Id of the communication end point
subscription_output_args = ek80_data_client.SubscriptionOutputArgs() # SubscriptionOutputArgs | Id of the subscription

try:
    # Add a subscription to the communication end point
    api_instance.add_subscription_to_end_point(end_point_id, subscription_output_args)
except ApiException as e:
    print("Exception when calling CommunicationEndPointsApi->add_subscription_to_end_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_point_id** | **int**| Id of the communication end point | 
 **subscription_output_args** | [**SubscriptionOutputArgs**](SubscriptionOutputArgs.md)| Id of the subscription | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_communication_end_point**
> int create_communication_end_point(settings)

Create a new communication end point

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.CommunicationEndPointsApi()
settings = ek80_data_client.CommunicationEndPointSettings() # CommunicationEndPointSettings | Settings for the new end point

try:
    # Create a new communication end point
    api_response = api_instance.create_communication_end_point(settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunicationEndPointsApi->create_communication_end_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings** | [**CommunicationEndPointSettings**](CommunicationEndPointSettings.md)| Settings for the new end point | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_communication_end_point**
> delete_communication_end_point(end_point_id)

Delete a communication end point

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.CommunicationEndPointsApi()
end_point_id = 789 # int | Id of the communication end point to delete

try:
    # Delete a communication end point
    api_instance.delete_communication_end_point(end_point_id)
except ApiException as e:
    print("Exception when calling CommunicationEndPointsApi->delete_communication_end_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_point_id** | **int**| Id of the communication end point to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = ek80_data_client.CommunicationEndPointsApi()

try:
    # Get information about the active communication end points
    api_response = api_instance.get_active_communication_end_points()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunicationEndPointsApi->get_active_communication_end_points: %s\n" % e)
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

# **get_subscriptions_by_end_point**
> list[SubscriptionSummary] get_subscriptions_by_end_point(end_point_id)

Get the active data subscriptions for the end point

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.CommunicationEndPointsApi()
end_point_id = 789 # int | Id of the communication end point

try:
    # Get the active data subscriptions for the end point
    api_response = api_instance.get_subscriptions_by_end_point(end_point_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunicationEndPointsApi->get_subscriptions_by_end_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_point_id** | **int**| Id of the communication end point | 

### Return type

[**list[SubscriptionSummary]**](SubscriptionSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_subscription_from_end_point**
> remove_subscription_from_end_point(end_point_id, subscription_id)

Remove a subscription from the communication end point

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.CommunicationEndPointsApi()
end_point_id = 789 # int | Id of the communication end point
subscription_id = 789 # int | Id of the subscription

try:
    # Remove a subscription from the communication end point
    api_instance.remove_subscription_from_end_point(end_point_id, subscription_id)
except ApiException as e:
    print("Exception when calling CommunicationEndPointsApi->remove_subscription_from_end_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_point_id** | **int**| Id of the communication end point | 
 **subscription_id** | **int**| Id of the subscription | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

