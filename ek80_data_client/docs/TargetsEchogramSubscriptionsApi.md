# ek80_data_client.TargetsEchogramSubscriptionsApi

All URIs are relative to *http://localhost:12346*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_targets_echogram_subscription**](TargetsEchogramSubscriptionsApi.md#create_targets_echogram_subscription) | **POST** /api/sounder/data-output/targets-echogram-subscriptions | Create a targets echogram data subscription
[**delete_targets_echogram_subscription**](TargetsEchogramSubscriptionsApi.md#delete_targets_echogram_subscription) | **DELETE** /api/sounder/data-output/targets-echogram-subscriptions/{subscriptionId} | Delete a targets echogram data subscription
[**get_targets_echogram_subscription**](TargetsEchogramSubscriptionsApi.md#get_targets_echogram_subscription) | **GET** /api/sounder/data-output/targets-echogram-subscriptions/{subscriptionId} | Get a particular targets echogram data subscription specification
[**get_targets_echogram_subscriptions**](TargetsEchogramSubscriptionsApi.md#get_targets_echogram_subscriptions) | **GET** /api/sounder/data-output/targets-echogram-subscriptions | Get all targets echogram data subscriptions
[**update_targets_echogram_subscription**](TargetsEchogramSubscriptionsApi.md#update_targets_echogram_subscription) | **PUT** /api/sounder/data-output/targets-echogram-subscriptions/{subscriptionId} | Update a targets echogram data subscription


# **create_targets_echogram_subscription**
> int create_targets_echogram_subscription(specification)

Create a targets echogram data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.TargetsEchogramSubscriptionsApi()
specification = ek80_data_client.TargetsEchogramSubscriptionSpecification() # TargetsEchogramSubscriptionSpecification | Specification of the data requested

try:
    # Create a targets echogram data subscription
    api_response = api_instance.create_targets_echogram_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsEchogramSubscriptionsApi->create_targets_echogram_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**TargetsEchogramSubscriptionSpecification**](TargetsEchogramSubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_targets_echogram_subscription**
> delete_targets_echogram_subscription(subscription_id)

Delete a targets echogram data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.TargetsEchogramSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # Delete a targets echogram data subscription
    api_instance.delete_targets_echogram_subscription(subscription_id)
except ApiException as e:
    print("Exception when calling TargetsEchogramSubscriptionsApi->delete_targets_echogram_subscription: %s\n" % e)
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

# **get_targets_echogram_subscription**
> TargetsEchogramSubscriptionSpecification get_targets_echogram_subscription(subscription_id)

Get a particular targets echogram data subscription specification

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.TargetsEchogramSubscriptionsApi()
subscription_id = 789 # int | The unique id of the subscription

try:
    # Get a particular targets echogram data subscription specification
    api_response = api_instance.get_targets_echogram_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsEchogramSubscriptionsApi->get_targets_echogram_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| The unique id of the subscription | 

### Return type

[**TargetsEchogramSubscriptionSpecification**](TargetsEchogramSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_targets_echogram_subscriptions**
> list[TargetsEchogramSubscriptionInfo] get_targets_echogram_subscriptions()

Get all targets echogram data subscriptions

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.TargetsEchogramSubscriptionsApi()

try:
    # Get all targets echogram data subscriptions
    api_response = api_instance.get_targets_echogram_subscriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsEchogramSubscriptionsApi->get_targets_echogram_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TargetsEchogramSubscriptionInfo]**](TargetsEchogramSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_targets_echogram_subscription**
> update_targets_echogram_subscription(subscription_id, settings)

Update a targets echogram data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.TargetsEchogramSubscriptionsApi()
subscription_id = 789 # int | Id of the subscription
settings = ek80_data_client.TargetsEchogramSettings() # TargetsEchogramSettings | New subscription settings

try:
    # Update a targets echogram data subscription
    api_instance.update_targets_echogram_subscription(subscription_id, settings)
except ApiException as e:
    print("Exception when calling TargetsEchogramSubscriptionsApi->update_targets_echogram_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| Id of the subscription | 
 **settings** | [**TargetsEchogramSettings**](TargetsEchogramSettings.md)| New subscription settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

