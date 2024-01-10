# ek80_data_client.SampleDataSubscriptionsApi

All URIs are relative to *http://localhost:12346*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sample_data_subscription**](SampleDataSubscriptionsApi.md#create_sample_data_subscription) | **POST** /api/sounder/data-output/sample-data-subscriptions | Create a processed sample-data subscription
[**delete_sample_data_subscription**](SampleDataSubscriptionsApi.md#delete_sample_data_subscription) | **DELETE** /api/sounder/data-output/sample-data-subscriptions/{subscriptionId} | Delete a processed sample-data subscription
[**get_sample_data_subscription**](SampleDataSubscriptionsApi.md#get_sample_data_subscription) | **GET** /api/sounder/data-output/sample-data-subscriptions/{subscriptionId} | Get a particular processed sample-data subscription specification
[**get_sample_data_subscriptions**](SampleDataSubscriptionsApi.md#get_sample_data_subscriptions) | **GET** /api/sounder/data-output/sample-data-subscriptions | Get all processed sample-data subscriptions
[**update_sample_data_subscription**](SampleDataSubscriptionsApi.md#update_sample_data_subscription) | **PUT** /api/sounder/data-output/sample-data-subscriptions/{subscriptionId} | Update a processed sample-data subscription


# **create_sample_data_subscription**
> int create_sample_data_subscription(specification)

Create a processed sample-data subscription

Subscription online help:   <a href=\"https://simrad.online/ek80/interface_en/subscr_type_sample_data.html\" target=\"foo\">parameter description</a>.

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.SampleDataSubscriptionsApi()
specification = ek80_data_client.SampleDataSubscriptionSpecification() # SampleDataSubscriptionSpecification | Specification of the data requested

try:
    # Create a processed sample-data subscription
    api_response = api_instance.create_sample_data_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleDataSubscriptionsApi->create_sample_data_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**SampleDataSubscriptionSpecification**](SampleDataSubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sample_data_subscription**
> delete_sample_data_subscription(subscription_id)

Delete a processed sample-data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.SampleDataSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # Delete a processed sample-data subscription
    api_instance.delete_sample_data_subscription(subscription_id)
except ApiException as e:
    print("Exception when calling SampleDataSubscriptionsApi->delete_sample_data_subscription: %s\n" % e)
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

# **get_sample_data_subscription**
> SampleDataSubscriptionSpecification get_sample_data_subscription(subscription_id)

Get a particular processed sample-data subscription specification

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.SampleDataSubscriptionsApi()
subscription_id = 789 # int | The unique id of the subscription

try:
    # Get a particular processed sample-data subscription specification
    api_response = api_instance.get_sample_data_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleDataSubscriptionsApi->get_sample_data_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| The unique id of the subscription | 

### Return type

[**SampleDataSubscriptionSpecification**](SampleDataSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sample_data_subscriptions**
> list[SampleDataSubscriptionInfo] get_sample_data_subscriptions()

Get all processed sample-data subscriptions

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.SampleDataSubscriptionsApi()

try:
    # Get all processed sample-data subscriptions
    api_response = api_instance.get_sample_data_subscriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleDataSubscriptionsApi->get_sample_data_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SampleDataSubscriptionInfo]**](SampleDataSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sample_data_subscription**
> update_sample_data_subscription(subscription_id, settings)

Update a processed sample-data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.SampleDataSubscriptionsApi()
subscription_id = 789 # int | Id of the subscription
settings = ek80_data_client.SampleDataSettings() # SampleDataSettings | New subscription settings

try:
    # Update a processed sample-data subscription
    api_instance.update_sample_data_subscription(subscription_id, settings)
except ApiException as e:
    print("Exception when calling SampleDataSubscriptionsApi->update_sample_data_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| Id of the subscription | 
 **settings** | [**SampleDataSettings**](SampleDataSettings.md)| New subscription settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

