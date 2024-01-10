# ek80_data_client.NoiseSpectrumSubscriptionsApi

All URIs are relative to *http://localhost:12346*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_noise_spectrum_subscription**](NoiseSpectrumSubscriptionsApi.md#create_noise_spectrum_subscription) | **POST** /api/sounder/data-output/noise-spectrum-subscriptions | Create a noise spectrum data subscription
[**delete_noise_spectrum_subscription**](NoiseSpectrumSubscriptionsApi.md#delete_noise_spectrum_subscription) | **DELETE** /api/sounder/data-output/noise-spectrum-subscriptions/{subscriptionId} | Delete a noise spectrum data subscription
[**get_noise_spectrum_subscription**](NoiseSpectrumSubscriptionsApi.md#get_noise_spectrum_subscription) | **GET** /api/sounder/data-output/noise-spectrum-subscriptions/{subscriptionId} | Get a particular noise spectrum data subscription specification
[**get_noise_spectrum_subscriptions**](NoiseSpectrumSubscriptionsApi.md#get_noise_spectrum_subscriptions) | **GET** /api/sounder/data-output/noise-spectrum-subscriptions | Get all noise spectrum data subscriptions
[**update_noise_spectrum_subscription**](NoiseSpectrumSubscriptionsApi.md#update_noise_spectrum_subscription) | **PUT** /api/sounder/data-output/noise-spectrum-subscriptions/{subscriptionId} | Update a noise spectrum data subscription


# **create_noise_spectrum_subscription**
> int create_noise_spectrum_subscription(specification)

Create a noise spectrum data subscription

Subscription online help:   <a href=\"https://simrad.online/ek80/interface_en/subscr_type_noise_spectrum.html\" target=\"foo\">parameter description</a>.

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.NoiseSpectrumSubscriptionsApi()
specification = ek80_data_client.NoiseSpectrumSubscriptionSpecification() # NoiseSpectrumSubscriptionSpecification | Specification of the data requested

try:
    # Create a noise spectrum data subscription
    api_response = api_instance.create_noise_spectrum_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoiseSpectrumSubscriptionsApi->create_noise_spectrum_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**NoiseSpectrumSubscriptionSpecification**](NoiseSpectrumSubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_noise_spectrum_subscription**
> delete_noise_spectrum_subscription(subscription_id)

Delete a noise spectrum data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.NoiseSpectrumSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # Delete a noise spectrum data subscription
    api_instance.delete_noise_spectrum_subscription(subscription_id)
except ApiException as e:
    print("Exception when calling NoiseSpectrumSubscriptionsApi->delete_noise_spectrum_subscription: %s\n" % e)
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

# **get_noise_spectrum_subscription**
> NoiseSpectrumSubscriptionSpecification get_noise_spectrum_subscription(subscription_id)

Get a particular noise spectrum data subscription specification

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.NoiseSpectrumSubscriptionsApi()
subscription_id = 789 # int | The unique id of the subscription

try:
    # Get a particular noise spectrum data subscription specification
    api_response = api_instance.get_noise_spectrum_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoiseSpectrumSubscriptionsApi->get_noise_spectrum_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| The unique id of the subscription | 

### Return type

[**NoiseSpectrumSubscriptionSpecification**](NoiseSpectrumSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_noise_spectrum_subscriptions**
> list[NoiseSpectrumSubscriptionInfo] get_noise_spectrum_subscriptions()

Get all noise spectrum data subscriptions

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.NoiseSpectrumSubscriptionsApi()

try:
    # Get all noise spectrum data subscriptions
    api_response = api_instance.get_noise_spectrum_subscriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoiseSpectrumSubscriptionsApi->get_noise_spectrum_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NoiseSpectrumSubscriptionInfo]**](NoiseSpectrumSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_noise_spectrum_subscription**
> update_noise_spectrum_subscription(subscription_id, settings)

Update a noise spectrum data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.NoiseSpectrumSubscriptionsApi()
subscription_id = 789 # int | Id of the subscription
settings = ek80_data_client.NoiseSpectrumSettings() # NoiseSpectrumSettings | New subscription settings

try:
    # Update a noise spectrum data subscription
    api_instance.update_noise_spectrum_subscription(subscription_id, settings)
except ApiException as e:
    print("Exception when calling NoiseSpectrumSubscriptionsApi->update_noise_spectrum_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| Id of the subscription | 
 **settings** | [**NoiseSpectrumSettings**](NoiseSpectrumSettings.md)| New subscription settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

