# ek80_data_client.TargetsIntegrationSubscriptionsApi

All URIs are relative to *http://localhost:12346*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_targets_integration_subscription**](TargetsIntegrationSubscriptionsApi.md#create_targets_integration_subscription) | **POST** /api/sounder/data-output/targets-integration-subscriptions | Create a targets integration data subscription
[**delete_targets_integration_subscription**](TargetsIntegrationSubscriptionsApi.md#delete_targets_integration_subscription) | **DELETE** /api/sounder/data-output/targets-integration-subscriptions/{subscriptionId} | Delete a targets integration data subscription
[**get_targets_integration_subscription**](TargetsIntegrationSubscriptionsApi.md#get_targets_integration_subscription) | **GET** /api/sounder/data-output/targets-integration-subscriptions/{subscriptionId} | Get a particular targets integration data subscription specification
[**get_targets_integration_subscriptions**](TargetsIntegrationSubscriptionsApi.md#get_targets_integration_subscriptions) | **GET** /api/sounder/data-output/targets-integration-subscriptions | Get all targets integration data subscriptions
[**update_targets_integration_subscription**](TargetsIntegrationSubscriptionsApi.md#update_targets_integration_subscription) | **PUT** /api/sounder/data-output/targets-integration-subscriptions/{subscriptionId} | Update a targets integration data subscription


# **create_targets_integration_subscription**
> int create_targets_integration_subscription(specification)

Create a targets integration data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.TargetsIntegrationSubscriptionsApi()
specification = ek80_data_client.TargetsIntegrationSubscriptionSpecification() # TargetsIntegrationSubscriptionSpecification | Specification of the data requested

try:
    # Create a targets integration data subscription
    api_response = api_instance.create_targets_integration_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsIntegrationSubscriptionsApi->create_targets_integration_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**TargetsIntegrationSubscriptionSpecification**](TargetsIntegrationSubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_targets_integration_subscription**
> delete_targets_integration_subscription(subscription_id)

Delete a targets integration data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.TargetsIntegrationSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # Delete a targets integration data subscription
    api_instance.delete_targets_integration_subscription(subscription_id)
except ApiException as e:
    print("Exception when calling TargetsIntegrationSubscriptionsApi->delete_targets_integration_subscription: %s\n" % e)
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

# **get_targets_integration_subscription**
> TargetsIntegrationSubscriptionSpecification get_targets_integration_subscription(subscription_id)

Get a particular targets integration data subscription specification

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.TargetsIntegrationSubscriptionsApi()
subscription_id = 789 # int | The unique id of the subscription

try:
    # Get a particular targets integration data subscription specification
    api_response = api_instance.get_targets_integration_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsIntegrationSubscriptionsApi->get_targets_integration_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| The unique id of the subscription | 

### Return type

[**TargetsIntegrationSubscriptionSpecification**](TargetsIntegrationSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_targets_integration_subscriptions**
> list[TargetsIntegrationSubscriptionInfo] get_targets_integration_subscriptions()

Get all targets integration data subscriptions

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.TargetsIntegrationSubscriptionsApi()

try:
    # Get all targets integration data subscriptions
    api_response = api_instance.get_targets_integration_subscriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsIntegrationSubscriptionsApi->get_targets_integration_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TargetsIntegrationSubscriptionInfo]**](TargetsIntegrationSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_targets_integration_subscription**
> update_targets_integration_subscription(subscription_id, settings)

Update a targets integration data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.TargetsIntegrationSubscriptionsApi()
subscription_id = 789 # int | Id of the subscription
settings = ek80_data_client.TargetsIntegrationSettings() # TargetsIntegrationSettings | New subscription settings

try:
    # Update a targets integration data subscription
    api_instance.update_targets_integration_subscription(subscription_id, settings)
except ApiException as e:
    print("Exception when calling TargetsIntegrationSubscriptionsApi->update_targets_integration_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| Id of the subscription | 
 **settings** | [**TargetsIntegrationSettings**](TargetsIntegrationSettings.md)| New subscription settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

