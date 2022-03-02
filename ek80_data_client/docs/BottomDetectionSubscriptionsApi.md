# ek80_data_client.BottomDetectionSubscriptionsApi

All URIs are relative to *http://localhost:12346*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bottom_detection_subscription**](BottomDetectionSubscriptionsApi.md#create_bottom_detection_subscription) | **POST** /api/sounder/data-output/bottom-detection-subscriptions | Create a bottom detection data subscription
[**delete_bottom_detection_subscription**](BottomDetectionSubscriptionsApi.md#delete_bottom_detection_subscription) | **DELETE** /api/sounder/data-output/bottom-detection-subscriptions/{subscriptionId} | Delete a bottom detection data subscription
[**get_bottom_detection_subscription**](BottomDetectionSubscriptionsApi.md#get_bottom_detection_subscription) | **GET** /api/sounder/data-output/bottom-detection-subscriptions/{subscriptionId} | Get a bottom detection subscription specification
[**get_bottom_detection_subscriptions**](BottomDetectionSubscriptionsApi.md#get_bottom_detection_subscriptions) | **GET** /api/sounder/data-output/bottom-detection-subscriptions | Get all bottom detection data subscriptions
[**update_bottom_detection_subscription**](BottomDetectionSubscriptionsApi.md#update_bottom_detection_subscription) | **PUT** /api/sounder/data-output/bottom-detection-subscriptions/{subscriptionId} | Update an bottom detection subscription


# **create_bottom_detection_subscription**
> int create_bottom_detection_subscription(specification)

Create a bottom detection data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.BottomDetectionSubscriptionsApi()
specification = ek80_data_client.BottomDetectionSubscriptionSpecification() # BottomDetectionSubscriptionSpecification | Specification of the data requested

try:
    # Create a bottom detection data subscription
    api_response = api_instance.create_bottom_detection_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BottomDetectionSubscriptionsApi->create_bottom_detection_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**BottomDetectionSubscriptionSpecification**](BottomDetectionSubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bottom_detection_subscription**
> delete_bottom_detection_subscription(subscription_id)

Delete a bottom detection data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.BottomDetectionSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # Delete a bottom detection data subscription
    api_instance.delete_bottom_detection_subscription(subscription_id)
except ApiException as e:
    print("Exception when calling BottomDetectionSubscriptionsApi->delete_bottom_detection_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bottom_detection_subscription**
> BottomDetectionSubscriptionSpecification get_bottom_detection_subscription(subscription_id)

Get a bottom detection subscription specification

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.BottomDetectionSubscriptionsApi()
subscription_id = 789 # int | The unique id of the subscription

try:
    # Get a bottom detection subscription specification
    api_response = api_instance.get_bottom_detection_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BottomDetectionSubscriptionsApi->get_bottom_detection_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| The unique id of the subscription | 

### Return type

[**BottomDetectionSubscriptionSpecification**](BottomDetectionSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bottom_detection_subscriptions**
> list[BottomDetectionSubscriptionInfo] get_bottom_detection_subscriptions()

Get all bottom detection data subscriptions

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.BottomDetectionSubscriptionsApi()

try:
    # Get all bottom detection data subscriptions
    api_response = api_instance.get_bottom_detection_subscriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BottomDetectionSubscriptionsApi->get_bottom_detection_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BottomDetectionSubscriptionInfo]**](BottomDetectionSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bottom_detection_subscription**
> update_bottom_detection_subscription(subscription_id, settings)

Update an bottom detection subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.BottomDetectionSubscriptionsApi()
subscription_id = 789 # int | Id of the subscription
settings = ek80_data_client.BottomDetectionSettings() # BottomDetectionSettings | New subscription settings

try:
    # Update an bottom detection subscription
    api_instance.update_bottom_detection_subscription(subscription_id, settings)
except ApiException as e:
    print("Exception when calling BottomDetectionSubscriptionsApi->update_bottom_detection_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| Id of the subscription | 
 **settings** | [**BottomDetectionSettings**](BottomDetectionSettings.md)| New subscription settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

