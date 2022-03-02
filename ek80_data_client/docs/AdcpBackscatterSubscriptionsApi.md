# ek80_data_client.AdcpBackscatterSubscriptionsApi

All URIs are relative to *http://localhost:12346*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_adcp_backscatter_subscription**](AdcpBackscatterSubscriptionsApi.md#create_adcp_backscatter_subscription) | **POST** /api/sounder/data-output/adcp-backscatter-subscriptions | Create an adcp data subscription
[**delete_adcp_backscatter_subscription**](AdcpBackscatterSubscriptionsApi.md#delete_adcp_backscatter_subscription) | **DELETE** /api/sounder/data-output/adcp-backscatter-subscriptions/{subscriptionId} | Delete an adcp detection data subscription
[**get_adcp_backscatter_subscriptions**](AdcpBackscatterSubscriptionsApi.md#get_adcp_backscatter_subscriptions) | **GET** /api/sounder/data-output/adcp-backscatter-subscriptions | Get all adcp data subscriptions
[**get_backscatter_adcp_subscription**](AdcpBackscatterSubscriptionsApi.md#get_backscatter_adcp_subscription) | **GET** /api/sounder/data-output/adcp-backscatter-subscriptions/{subscriptionId} | Get an adcp subscription specification
[**update_adcp_backscatter_subscription**](AdcpBackscatterSubscriptionsApi.md#update_adcp_backscatter_subscription) | **PUT** /api/sounder/data-output/adcp-backscatter-subscriptions/{subscriptionId} | Update an adcp subscription


# **create_adcp_backscatter_subscription**
> int create_adcp_backscatter_subscription(specification)

Create an adcp data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.AdcpBackscatterSubscriptionsApi()
specification = ek80_data_client.AdcpBackscatterSubscriptionSpecification() # AdcpBackscatterSubscriptionSpecification | Specification of the data requested

try:
    # Create an adcp data subscription
    api_response = api_instance.create_adcp_backscatter_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpBackscatterSubscriptionsApi->create_adcp_backscatter_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**AdcpBackscatterSubscriptionSpecification**](AdcpBackscatterSubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_adcp_backscatter_subscription**
> delete_adcp_backscatter_subscription(subscription_id)

Delete an adcp detection data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.AdcpBackscatterSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # Delete an adcp detection data subscription
    api_instance.delete_adcp_backscatter_subscription(subscription_id)
except ApiException as e:
    print("Exception when calling AdcpBackscatterSubscriptionsApi->delete_adcp_backscatter_subscription: %s\n" % e)
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

# **get_adcp_backscatter_subscriptions**
> list[AdcpBackscatterSubscriptionInfo] get_adcp_backscatter_subscriptions()

Get all adcp data subscriptions

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.AdcpBackscatterSubscriptionsApi()

try:
    # Get all adcp data subscriptions
    api_response = api_instance.get_adcp_backscatter_subscriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpBackscatterSubscriptionsApi->get_adcp_backscatter_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AdcpBackscatterSubscriptionInfo]**](AdcpBackscatterSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backscatter_adcp_subscription**
> AdcpBackscatterSubscriptionSpecification get_backscatter_adcp_subscription(subscription_id)

Get an adcp subscription specification

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.AdcpBackscatterSubscriptionsApi()
subscription_id = 789 # int | The unique id of the subscription

try:
    # Get an adcp subscription specification
    api_response = api_instance.get_backscatter_adcp_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpBackscatterSubscriptionsApi->get_backscatter_adcp_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| The unique id of the subscription | 

### Return type

[**AdcpBackscatterSubscriptionSpecification**](AdcpBackscatterSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_adcp_backscatter_subscription**
> update_adcp_backscatter_subscription(subscription_id, settings)

Update an adcp subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.AdcpBackscatterSubscriptionsApi()
subscription_id = 789 # int | Id of the subscription
settings = ek80_data_client.AdcpBackscatterSettings() # AdcpBackscatterSettings | New subscription settings

try:
    # Update an adcp subscription
    api_instance.update_adcp_backscatter_subscription(subscription_id, settings)
except ApiException as e:
    print("Exception when calling AdcpBackscatterSubscriptionsApi->update_adcp_backscatter_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| Id of the subscription | 
 **settings** | [**AdcpBackscatterSettings**](AdcpBackscatterSettings.md)| New subscription settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

