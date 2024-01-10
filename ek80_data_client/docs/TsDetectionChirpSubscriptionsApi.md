# ek80_data_client.TsDetectionChirpSubscriptionsApi

All URIs are relative to *http://localhost:12346*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ts_detection_chirp_subscription**](TsDetectionChirpSubscriptionsApi.md#create_ts_detection_chirp_subscription) | **POST** /api/sounder/data-output/ts-detection-chirp-subscriptions | Create a ts detection chirp data subscription
[**delete_ts_detection_chirp_subscription**](TsDetectionChirpSubscriptionsApi.md#delete_ts_detection_chirp_subscription) | **DELETE** /api/sounder/data-output/ts-detection-chirp-subscriptions/{subscriptionId} | Delete a ts detection chirp data subscription
[**get_ts_detection_chirp_subscription**](TsDetectionChirpSubscriptionsApi.md#get_ts_detection_chirp_subscription) | **GET** /api/sounder/data-output/ts-detection-chirp-subscriptions/{subscriptionId} | Get a particular ts detection chirp subscription specification
[**get_ts_detection_chirp_subscriptions**](TsDetectionChirpSubscriptionsApi.md#get_ts_detection_chirp_subscriptions) | **GET** /api/sounder/data-output/ts-detection-chirp-subscriptions | Get all ts detection chirp subscriptions
[**update_ts_detection_chirp_subscription**](TsDetectionChirpSubscriptionsApi.md#update_ts_detection_chirp_subscription) | **PUT** /api/sounder/data-output/ts-detection-chirp-subscriptions/{subscriptionId} | Update a ts detection chirp data subscription


# **create_ts_detection_chirp_subscription**
> int create_ts_detection_chirp_subscription(specification)

Create a ts detection chirp data subscription

Subscription online help:   <a href=\"https://simrad.online/ek80/interface_en/subscr_type_ts_detection_chirp.html\" target=\"foo\">parameter description</a>.

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.TsDetectionChirpSubscriptionsApi()
specification = ek80_data_client.TsDetectionChirpSubscriptionSpecification() # TsDetectionChirpSubscriptionSpecification | Specification of the data requested

try:
    # Create a ts detection chirp data subscription
    api_response = api_instance.create_ts_detection_chirp_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TsDetectionChirpSubscriptionsApi->create_ts_detection_chirp_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**TsDetectionChirpSubscriptionSpecification**](TsDetectionChirpSubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ts_detection_chirp_subscription**
> delete_ts_detection_chirp_subscription(subscription_id)

Delete a ts detection chirp data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.TsDetectionChirpSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # Delete a ts detection chirp data subscription
    api_instance.delete_ts_detection_chirp_subscription(subscription_id)
except ApiException as e:
    print("Exception when calling TsDetectionChirpSubscriptionsApi->delete_ts_detection_chirp_subscription: %s\n" % e)
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

# **get_ts_detection_chirp_subscription**
> TsDetectionChirpSubscriptionSpecification get_ts_detection_chirp_subscription(subscription_id)

Get a particular ts detection chirp subscription specification

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.TsDetectionChirpSubscriptionsApi()
subscription_id = 789 # int | The unique id of the subscription

try:
    # Get a particular ts detection chirp subscription specification
    api_response = api_instance.get_ts_detection_chirp_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TsDetectionChirpSubscriptionsApi->get_ts_detection_chirp_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| The unique id of the subscription | 

### Return type

[**TsDetectionChirpSubscriptionSpecification**](TsDetectionChirpSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ts_detection_chirp_subscriptions**
> list[TsDetectionChirpSubscriptionInfo] get_ts_detection_chirp_subscriptions()

Get all ts detection chirp subscriptions

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.TsDetectionChirpSubscriptionsApi()

try:
    # Get all ts detection chirp subscriptions
    api_response = api_instance.get_ts_detection_chirp_subscriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TsDetectionChirpSubscriptionsApi->get_ts_detection_chirp_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TsDetectionChirpSubscriptionInfo]**](TsDetectionChirpSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ts_detection_chirp_subscription**
> update_ts_detection_chirp_subscription(subscription_id, settings)

Update a ts detection chirp data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.TsDetectionChirpSubscriptionsApi()
subscription_id = 789 # int | Id of the subscription
settings = ek80_data_client.TsDetectionChirpSettings() # TsDetectionChirpSettings | New subscription settings

try:
    # Update a ts detection chirp data subscription
    api_instance.update_ts_detection_chirp_subscription(subscription_id, settings)
except ApiException as e:
    print("Exception when calling TsDetectionChirpSubscriptionsApi->update_ts_detection_chirp_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| Id of the subscription | 
 **settings** | [**TsDetectionChirpSettings**](TsDetectionChirpSettings.md)| New subscription settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

