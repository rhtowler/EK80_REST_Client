# ek80_data_client.AdcpBottomDetectorSubscriptionsApi

All URIs are relative to *http://localhost:12346*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_adcp_bottom_detector_subscription**](AdcpBottomDetectorSubscriptionsApi.md#create_adcp_bottom_detector_subscription) | **POST** /api/sounder/data-output/adcp-bottom-detector-subscriptions | Create an adcp data subscription
[**delete_adcp_bottom_detector_subscription**](AdcpBottomDetectorSubscriptionsApi.md#delete_adcp_bottom_detector_subscription) | **DELETE** /api/sounder/data-output/adcp-bottom-detector-subscriptions/{subscriptionId} | Delete an adcp detection data subscription
[**get_adcp_bottom_detector_subscriptions**](AdcpBottomDetectorSubscriptionsApi.md#get_adcp_bottom_detector_subscriptions) | **GET** /api/sounder/data-output/adcp-bottom-detector-subscriptions | Get all adcp data subscriptions
[**get_bottom_detector_adcp_subscription**](AdcpBottomDetectorSubscriptionsApi.md#get_bottom_detector_adcp_subscription) | **GET** /api/sounder/data-output/adcp-bottom-detector-subscriptions/{subscriptionId} | Get an adcp subscription specification
[**update_adcp_bottom_detector_subscription**](AdcpBottomDetectorSubscriptionsApi.md#update_adcp_bottom_detector_subscription) | **PUT** /api/sounder/data-output/adcp-bottom-detector-subscriptions/{subscriptionId} | Update an adcp subscription


# **create_adcp_bottom_detector_subscription**
> int create_adcp_bottom_detector_subscription(specification)

Create an adcp data subscription

Subscription online help:   <a href=\"https://simrad.online/ek80/interface_en/subscr_type_adcp_bottom_detector.html\" target=\"foo\">parameter description</a>.

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.AdcpBottomDetectorSubscriptionsApi()
specification = ek80_data_client.AdcpBottomDetectorSubscriptionSpecification() # AdcpBottomDetectorSubscriptionSpecification | Specification of the data requested

try:
    # Create an adcp data subscription
    api_response = api_instance.create_adcp_bottom_detector_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpBottomDetectorSubscriptionsApi->create_adcp_bottom_detector_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**AdcpBottomDetectorSubscriptionSpecification**](AdcpBottomDetectorSubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_adcp_bottom_detector_subscription**
> delete_adcp_bottom_detector_subscription(subscription_id)

Delete an adcp detection data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.AdcpBottomDetectorSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # Delete an adcp detection data subscription
    api_instance.delete_adcp_bottom_detector_subscription(subscription_id)
except ApiException as e:
    print("Exception when calling AdcpBottomDetectorSubscriptionsApi->delete_adcp_bottom_detector_subscription: %s\n" % e)
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

# **get_adcp_bottom_detector_subscriptions**
> list[AdcpBottomDetectorSubscriptionInfo] get_adcp_bottom_detector_subscriptions()

Get all adcp data subscriptions

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.AdcpBottomDetectorSubscriptionsApi()

try:
    # Get all adcp data subscriptions
    api_response = api_instance.get_adcp_bottom_detector_subscriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpBottomDetectorSubscriptionsApi->get_adcp_bottom_detector_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AdcpBottomDetectorSubscriptionInfo]**](AdcpBottomDetectorSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bottom_detector_adcp_subscription**
> AdcpBottomDetectorSubscriptionSpecification get_bottom_detector_adcp_subscription(subscription_id)

Get an adcp subscription specification

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.AdcpBottomDetectorSubscriptionsApi()
subscription_id = 789 # int | The unique id of the subscription

try:
    # Get an adcp subscription specification
    api_response = api_instance.get_bottom_detector_adcp_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpBottomDetectorSubscriptionsApi->get_bottom_detector_adcp_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| The unique id of the subscription | 

### Return type

[**AdcpBottomDetectorSubscriptionSpecification**](AdcpBottomDetectorSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_adcp_bottom_detector_subscription**
> update_adcp_bottom_detector_subscription(subscription_id, settings)

Update an adcp subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.AdcpBottomDetectorSubscriptionsApi()
subscription_id = 789 # int | Id of the subscription
settings = ek80_data_client.AdcpBottomDetectorSettings() # AdcpBottomDetectorSettings | New subscription settings

try:
    # Update an adcp subscription
    api_instance.update_adcp_bottom_detector_subscription(subscription_id, settings)
except ApiException as e:
    print("Exception when calling AdcpBottomDetectorSubscriptionsApi->update_adcp_bottom_detector_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| Id of the subscription | 
 **settings** | [**AdcpBottomDetectorSettings**](AdcpBottomDetectorSettings.md)| New subscription settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

