# ek80_data_client.AdcpQualityFactorSubscriptionsApi

All URIs are relative to *http://localhost:12346*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_adcp_quality_factor_subscription**](AdcpQualityFactorSubscriptionsApi.md#create_adcp_quality_factor_subscription) | **POST** /api/sounder/data-output/adcp-quality-factor-subscriptions | Create an adcp data subscription
[**delete_adcp_quality_factor_subscription**](AdcpQualityFactorSubscriptionsApi.md#delete_adcp_quality_factor_subscription) | **DELETE** /api/sounder/data-output/adcp-quality-factor-subscriptions/{subscriptionId} | Delete an adcp detection data subscription
[**get_adcp_quality_factor_subscriptions**](AdcpQualityFactorSubscriptionsApi.md#get_adcp_quality_factor_subscriptions) | **GET** /api/sounder/data-output/adcp-quality-factor-subscriptions | Get all adcp data subscriptions
[**get_quality_factor_adcp_subscription**](AdcpQualityFactorSubscriptionsApi.md#get_quality_factor_adcp_subscription) | **GET** /api/sounder/data-output/adcp-quality-factor-subscriptions/{subscriptionId} | Get an adcp subscription specification
[**update_adcp_quality_factor_subscription**](AdcpQualityFactorSubscriptionsApi.md#update_adcp_quality_factor_subscription) | **PUT** /api/sounder/data-output/adcp-quality-factor-subscriptions/{subscriptionId} | Update an adcp subscription


# **create_adcp_quality_factor_subscription**
> int create_adcp_quality_factor_subscription(specification)

Create an adcp data subscription

Subscription online help:   <a href=\"https://simrad.online/ek80/interface_en/subscr_type_adcp_quality_factor.html\" target=\"foo\">parameter description</a>.

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.AdcpQualityFactorSubscriptionsApi()
specification = ek80_data_client.AdcpQualityFactorSubscriptionSpecification() # AdcpQualityFactorSubscriptionSpecification | Specification of the data requested

try:
    # Create an adcp data subscription
    api_response = api_instance.create_adcp_quality_factor_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpQualityFactorSubscriptionsApi->create_adcp_quality_factor_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**AdcpQualityFactorSubscriptionSpecification**](AdcpQualityFactorSubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_adcp_quality_factor_subscription**
> delete_adcp_quality_factor_subscription(subscription_id)

Delete an adcp detection data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.AdcpQualityFactorSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # Delete an adcp detection data subscription
    api_instance.delete_adcp_quality_factor_subscription(subscription_id)
except ApiException as e:
    print("Exception when calling AdcpQualityFactorSubscriptionsApi->delete_adcp_quality_factor_subscription: %s\n" % e)
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

# **get_adcp_quality_factor_subscriptions**
> list[AdcpQualityFactorSubscriptionInfo] get_adcp_quality_factor_subscriptions()

Get all adcp data subscriptions

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.AdcpQualityFactorSubscriptionsApi()

try:
    # Get all adcp data subscriptions
    api_response = api_instance.get_adcp_quality_factor_subscriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpQualityFactorSubscriptionsApi->get_adcp_quality_factor_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AdcpQualityFactorSubscriptionInfo]**](AdcpQualityFactorSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quality_factor_adcp_subscription**
> AdcpQualityFactorSubscriptionSpecification get_quality_factor_adcp_subscription(subscription_id)

Get an adcp subscription specification

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.AdcpQualityFactorSubscriptionsApi()
subscription_id = 789 # int | The unique id of the subscription

try:
    # Get an adcp subscription specification
    api_response = api_instance.get_quality_factor_adcp_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpQualityFactorSubscriptionsApi->get_quality_factor_adcp_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| The unique id of the subscription | 

### Return type

[**AdcpQualityFactorSubscriptionSpecification**](AdcpQualityFactorSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_adcp_quality_factor_subscription**
> update_adcp_quality_factor_subscription(subscription_id, settings)

Update an adcp subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.AdcpQualityFactorSubscriptionsApi()
subscription_id = 789 # int | Id of the subscription
settings = ek80_data_client.AdcpQualitySettings() # AdcpQualitySettings | New subscription settings

try:
    # Update an adcp subscription
    api_instance.update_adcp_quality_factor_subscription(subscription_id, settings)
except ApiException as e:
    print("Exception when calling AdcpQualityFactorSubscriptionsApi->update_adcp_quality_factor_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| Id of the subscription | 
 **settings** | [**AdcpQualitySettings**](AdcpQualitySettings.md)| New subscription settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

