# ek80_data_client.TsDetectionSubscriptionsApi

All URIs are relative to *http://localhost:12346*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ts_detection_subscription**](TsDetectionSubscriptionsApi.md#create_ts_detection_subscription) | **POST** /api/sounder/data-output/ts-detection-subscriptions | Create a ts detection data subscription
[**delete_ts_detection_subscription**](TsDetectionSubscriptionsApi.md#delete_ts_detection_subscription) | **DELETE** /api/sounder/data-output/ts-detection-subscriptions/{subscriptionId} | Delete a ts detection data subscription
[**get_ts_detection_subscription**](TsDetectionSubscriptionsApi.md#get_ts_detection_subscription) | **GET** /api/sounder/data-output/ts-detection-subscriptions/{subscriptionId} | Get a particular ts detection subscription specification
[**get_ts_detection_subscriptions**](TsDetectionSubscriptionsApi.md#get_ts_detection_subscriptions) | **GET** /api/sounder/data-output/ts-detection-subscriptions | Get all ts detection subscriptions
[**update_ts_detection_subscription**](TsDetectionSubscriptionsApi.md#update_ts_detection_subscription) | **PUT** /api/sounder/data-output/ts-detection-subscriptions/{subscriptionId} | Update a ts detection data subscription


# **create_ts_detection_subscription**
> int create_ts_detection_subscription(specification)

Create a ts detection data subscription

Subscription online help:   <a href=\"https://simrad.online/ek80/interface_en/subscr_type_ts_detection.html\" target=\"foo\">parameter description</a>.

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.TsDetectionSubscriptionsApi()
specification = ek80_data_client.TsDetectionSubscriptionSpecification() # TsDetectionSubscriptionSpecification | Specification of the data requested

try:
    # Create a ts detection data subscription
    api_response = api_instance.create_ts_detection_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TsDetectionSubscriptionsApi->create_ts_detection_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**TsDetectionSubscriptionSpecification**](TsDetectionSubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ts_detection_subscription**
> delete_ts_detection_subscription(subscription_id)

Delete a ts detection data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.TsDetectionSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # Delete a ts detection data subscription
    api_instance.delete_ts_detection_subscription(subscription_id)
except ApiException as e:
    print("Exception when calling TsDetectionSubscriptionsApi->delete_ts_detection_subscription: %s\n" % e)
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

# **get_ts_detection_subscription**
> TsDetectionSubscriptionSpecification get_ts_detection_subscription(subscription_id)

Get a particular ts detection subscription specification

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.TsDetectionSubscriptionsApi()
subscription_id = 789 # int | The unique id of the subscription

try:
    # Get a particular ts detection subscription specification
    api_response = api_instance.get_ts_detection_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TsDetectionSubscriptionsApi->get_ts_detection_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| The unique id of the subscription | 

### Return type

[**TsDetectionSubscriptionSpecification**](TsDetectionSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ts_detection_subscriptions**
> list[TsDetectionSubscriptionInfo] get_ts_detection_subscriptions()

Get all ts detection subscriptions

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.TsDetectionSubscriptionsApi()

try:
    # Get all ts detection subscriptions
    api_response = api_instance.get_ts_detection_subscriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TsDetectionSubscriptionsApi->get_ts_detection_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TsDetectionSubscriptionInfo]**](TsDetectionSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ts_detection_subscription**
> update_ts_detection_subscription(subscription_id, settings)

Update a ts detection data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.TsDetectionSubscriptionsApi()
subscription_id = 789 # int | Id of the subscription
settings = ek80_data_client.TsDetectionSettings() # TsDetectionSettings | New subscription settings

try:
    # Update a ts detection data subscription
    api_instance.update_ts_detection_subscription(subscription_id, settings)
except ApiException as e:
    print("Exception when calling TsDetectionSubscriptionsApi->update_ts_detection_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| Id of the subscription | 
 **settings** | [**TsDetectionSettings**](TsDetectionSettings.md)| New subscription settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

