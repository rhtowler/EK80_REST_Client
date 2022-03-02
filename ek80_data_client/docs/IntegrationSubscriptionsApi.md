# ek80_data_client.IntegrationSubscriptionsApi

All URIs are relative to *http://localhost:12346*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_integration_subscription**](IntegrationSubscriptionsApi.md#create_integration_subscription) | **POST** /api/sounder/data-output/integration-subscriptions | Create an integration data subscription
[**delete_integration_subscription**](IntegrationSubscriptionsApi.md#delete_integration_subscription) | **DELETE** /api/sounder/data-output/integration-subscriptions/{subscriptionId} | Delete an integration data subscription
[**get_integration_subscription**](IntegrationSubscriptionsApi.md#get_integration_subscription) | **GET** /api/sounder/data-output/integration-subscriptions/{subscriptionId} | Get a particular integration data subscription specification
[**get_integration_subscriptions**](IntegrationSubscriptionsApi.md#get_integration_subscriptions) | **GET** /api/sounder/data-output/integration-subscriptions | Get all integration data subscriptions
[**update_integration_state**](IntegrationSubscriptionsApi.md#update_integration_state) | **PUT** /api/sounder/data-output/integration-subscriptions/{subscriptionId}/integration-state | Update the integration state (start/stop integration)
[**update_integration_subscription**](IntegrationSubscriptionsApi.md#update_integration_subscription) | **PUT** /api/sounder/data-output/integration-subscriptions/{subscriptionId} | Update an integration data subscription


# **create_integration_subscription**
> int create_integration_subscription(specification)

Create an integration data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.IntegrationSubscriptionsApi()
specification = ek80_data_client.IntegrationSubscriptionSpecification() # IntegrationSubscriptionSpecification | Specification of the data requested

try:
    # Create an integration data subscription
    api_response = api_instance.create_integration_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationSubscriptionsApi->create_integration_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**IntegrationSubscriptionSpecification**](IntegrationSubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_integration_subscription**
> delete_integration_subscription(subscription_id)

Delete an integration data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.IntegrationSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # Delete an integration data subscription
    api_instance.delete_integration_subscription(subscription_id)
except ApiException as e:
    print("Exception when calling IntegrationSubscriptionsApi->delete_integration_subscription: %s\n" % e)
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

# **get_integration_subscription**
> IntegrationSubscriptionSpecification get_integration_subscription(subscription_id)

Get a particular integration data subscription specification

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.IntegrationSubscriptionsApi()
subscription_id = 789 # int | The unique id of the subscription

try:
    # Get a particular integration data subscription specification
    api_response = api_instance.get_integration_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationSubscriptionsApi->get_integration_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| The unique id of the subscription | 

### Return type

[**IntegrationSubscriptionSpecification**](IntegrationSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration_subscriptions**
> list[IntegrationSubscriptionInfo] get_integration_subscriptions()

Get all integration data subscriptions

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.IntegrationSubscriptionsApi()

try:
    # Get all integration data subscriptions
    api_response = api_instance.get_integration_subscriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationSubscriptionsApi->get_integration_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[IntegrationSubscriptionInfo]**](IntegrationSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_integration_state**
> update_integration_state(subscription_id, state)

Update the integration state (start/stop integration)

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.IntegrationSubscriptionsApi()
subscription_id = 789 # int | Id of the subscription
state = 'state_example' # str | New integration state

try:
    # Update the integration state (start/stop integration)
    api_instance.update_integration_state(subscription_id, state)
except ApiException as e:
    print("Exception when calling IntegrationSubscriptionsApi->update_integration_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| Id of the subscription | 
 **state** | **str**| New integration state | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_integration_subscription**
> update_integration_subscription(subscription_id, settings)

Update an integration data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.IntegrationSubscriptionsApi()
subscription_id = 789 # int | Id of the subscription
settings = ek80_data_client.IntegrationSettings() # IntegrationSettings | New subscription settings

try:
    # Update an integration data subscription
    api_instance.update_integration_subscription(subscription_id, settings)
except ApiException as e:
    print("Exception when calling IntegrationSubscriptionsApi->update_integration_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| Id of the subscription | 
 **settings** | [**IntegrationSettings**](IntegrationSettings.md)| New subscription settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

