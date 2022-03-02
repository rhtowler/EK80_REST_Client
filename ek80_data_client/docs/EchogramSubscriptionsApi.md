# ek80_data_client.EchogramSubscriptionsApi

All URIs are relative to *http://localhost:12346*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_echogram_subscription**](EchogramSubscriptionsApi.md#create_echogram_subscription) | **POST** /api/sounder/data-output/echogram-subscriptions | Create an echogram data subscription
[**delete_echogram_subscription**](EchogramSubscriptionsApi.md#delete_echogram_subscription) | **DELETE** /api/sounder/data-output/echogram-subscriptions/{subscriptionId} | Delete a echogram data subscription
[**get_echogram_subscription**](EchogramSubscriptionsApi.md#get_echogram_subscription) | **GET** /api/sounder/data-output/echogram-subscriptions/{subscriptionId} | Get a particular echogram data subscription specification
[**get_echogram_subscriptions**](EchogramSubscriptionsApi.md#get_echogram_subscriptions) | **GET** /api/sounder/data-output/echogram-subscriptions | Get all echogram data subscriptions
[**update_echogram_subscription**](EchogramSubscriptionsApi.md#update_echogram_subscription) | **PUT** /api/sounder/data-output/echogram-subscriptions/{subscriptionId} | Update an echogram data subscription


# **create_echogram_subscription**
> int create_echogram_subscription(specification)

Create an echogram data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.EchogramSubscriptionsApi()
specification = ek80_data_client.EchogramSubscriptionSpecification() # EchogramSubscriptionSpecification | Specification of the data requested

try:
    # Create an echogram data subscription
    api_response = api_instance.create_echogram_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EchogramSubscriptionsApi->create_echogram_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**EchogramSubscriptionSpecification**](EchogramSubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_echogram_subscription**
> delete_echogram_subscription(subscription_id)

Delete a echogram data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.EchogramSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # Delete a echogram data subscription
    api_instance.delete_echogram_subscription(subscription_id)
except ApiException as e:
    print("Exception when calling EchogramSubscriptionsApi->delete_echogram_subscription: %s\n" % e)
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

# **get_echogram_subscription**
> EchogramSubscriptionSpecification get_echogram_subscription(subscription_id)

Get a particular echogram data subscription specification

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.EchogramSubscriptionsApi()
subscription_id = 789 # int | The unique id of the subscription

try:
    # Get a particular echogram data subscription specification
    api_response = api_instance.get_echogram_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EchogramSubscriptionsApi->get_echogram_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| The unique id of the subscription | 

### Return type

[**EchogramSubscriptionSpecification**](EchogramSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_echogram_subscriptions**
> list[EchogramSubscriptionInfo] get_echogram_subscriptions()

Get all echogram data subscriptions

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.EchogramSubscriptionsApi()

try:
    # Get all echogram data subscriptions
    api_response = api_instance.get_echogram_subscriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EchogramSubscriptionsApi->get_echogram_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EchogramSubscriptionInfo]**](EchogramSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_echogram_subscription**
> update_echogram_subscription(subscription_id, settings)

Update an echogram data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.EchogramSubscriptionsApi()
subscription_id = 789 # int | Id of the subscription
settings = ek80_data_client.EchogramSettings() # EchogramSettings | New subscription settings

try:
    # Update an echogram data subscription
    api_instance.update_echogram_subscription(subscription_id, settings)
except ApiException as e:
    print("Exception when calling EchogramSubscriptionsApi->update_echogram_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| Id of the subscription | 
 **settings** | [**EchogramSettings**](EchogramSettings.md)| New subscription settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

