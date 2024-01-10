# ek80_data_client.AdcpVelocitySubscriptionsApi

All URIs are relative to *http://localhost:12346*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_adcp_velocity_subscription**](AdcpVelocitySubscriptionsApi.md#create_adcp_velocity_subscription) | **POST** /api/sounder/data-output/adcp-velocity-subscriptions | Create an adcp data subscription
[**delete_adcp_velocity_subscription**](AdcpVelocitySubscriptionsApi.md#delete_adcp_velocity_subscription) | **DELETE** /api/sounder/data-output/adcp-velocity-subscriptions/{subscriptionId} | Delete an adcp detection data subscription
[**get_adcp_velocity_subscriptions**](AdcpVelocitySubscriptionsApi.md#get_adcp_velocity_subscriptions) | **GET** /api/sounder/data-output/adcp-velocity-subscriptions | Get all adcp data subscriptions
[**get_velocity_adcp_subscription**](AdcpVelocitySubscriptionsApi.md#get_velocity_adcp_subscription) | **GET** /api/sounder/data-output/adcp-velocity-subscriptions/{subscriptionId} | Get an adcp subscription specification
[**update_adcp_velocity_subscription**](AdcpVelocitySubscriptionsApi.md#update_adcp_velocity_subscription) | **PUT** /api/sounder/data-output/adcp-velocity-subscriptions/{subscriptionId} | Update an adcp subscription


# **create_adcp_velocity_subscription**
> int create_adcp_velocity_subscription(specification)

Create an adcp data subscription

Subscription online help:   <a href=\"https://simrad.online/ek80/interface_en/subscr_type_adcp_velocity.html\" target=\"foo\">parameter description</a>.

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.AdcpVelocitySubscriptionsApi()
specification = ek80_data_client.AdcpVelocitySubscriptionSpecification() # AdcpVelocitySubscriptionSpecification | Specification of the data requested

try:
    # Create an adcp data subscription
    api_response = api_instance.create_adcp_velocity_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpVelocitySubscriptionsApi->create_adcp_velocity_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**AdcpVelocitySubscriptionSpecification**](AdcpVelocitySubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_adcp_velocity_subscription**
> delete_adcp_velocity_subscription(subscription_id)

Delete an adcp detection data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.AdcpVelocitySubscriptionsApi()
subscription_id = 789 # int | 

try:
    # Delete an adcp detection data subscription
    api_instance.delete_adcp_velocity_subscription(subscription_id)
except ApiException as e:
    print("Exception when calling AdcpVelocitySubscriptionsApi->delete_adcp_velocity_subscription: %s\n" % e)
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

# **get_adcp_velocity_subscriptions**
> list[AdcpVelocitySubscriptionInfo] get_adcp_velocity_subscriptions()

Get all adcp data subscriptions

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.AdcpVelocitySubscriptionsApi()

try:
    # Get all adcp data subscriptions
    api_response = api_instance.get_adcp_velocity_subscriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpVelocitySubscriptionsApi->get_adcp_velocity_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AdcpVelocitySubscriptionInfo]**](AdcpVelocitySubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_velocity_adcp_subscription**
> AdcpVelocitySubscriptionSpecification get_velocity_adcp_subscription(subscription_id)

Get an adcp subscription specification

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.AdcpVelocitySubscriptionsApi()
subscription_id = 789 # int | The unique id of the subscription

try:
    # Get an adcp subscription specification
    api_response = api_instance.get_velocity_adcp_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpVelocitySubscriptionsApi->get_velocity_adcp_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| The unique id of the subscription | 

### Return type

[**AdcpVelocitySubscriptionSpecification**](AdcpVelocitySubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_adcp_velocity_subscription**
> update_adcp_velocity_subscription(subscription_id, settings)

Update an adcp subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.AdcpVelocitySubscriptionsApi()
subscription_id = 789 # int | Id of the subscription
settings = ek80_data_client.AdcpVelocitySettings() # AdcpVelocitySettings | New subscription settings

try:
    # Update an adcp subscription
    api_instance.update_adcp_velocity_subscription(subscription_id, settings)
except ApiException as e:
    print("Exception when calling AdcpVelocitySubscriptionsApi->update_adcp_velocity_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| Id of the subscription | 
 **settings** | [**AdcpVelocitySettings**](AdcpVelocitySettings.md)| New subscription settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

