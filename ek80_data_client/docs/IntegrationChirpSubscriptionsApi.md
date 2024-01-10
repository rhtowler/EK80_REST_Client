# ek80_data_client.IntegrationChirpSubscriptionsApi

All URIs are relative to *http://localhost:12346*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_integration_chirp_subscription**](IntegrationChirpSubscriptionsApi.md#create_integration_chirp_subscription) | **POST** /api/sounder/data-output/integration-chirp-subscriptions | Create an integration chirp data subscription
[**delete_integration_chirp_subscription**](IntegrationChirpSubscriptionsApi.md#delete_integration_chirp_subscription) | **DELETE** /api/sounder/data-output/integration-chirp-subscriptions/{subscriptionId} | Delete an integration data subscription
[**get_integration_chirp_subscription**](IntegrationChirpSubscriptionsApi.md#get_integration_chirp_subscription) | **GET** /api/sounder/data-output/integration-chirp-subscriptions/{subscriptionId} | Get a particular integration chrip data subscription specification
[**get_integration_chirp_subscriptions**](IntegrationChirpSubscriptionsApi.md#get_integration_chirp_subscriptions) | **GET** /api/sounder/data-output/integration-chirp-subscriptions | Get all integration chirp data subscriptions
[**update_integration_chirp_subscription**](IntegrationChirpSubscriptionsApi.md#update_integration_chirp_subscription) | **PUT** /api/sounder/data-output/integration-chirp-subscriptions/{subscriptionId} | Update an integration chirp data subscription
[**update_integration_state**](IntegrationChirpSubscriptionsApi.md#update_integration_state) | **PUT** /api/sounder/data-output/integration-chirp-subscriptions/{subscriptionId}/integration-state | Update the integration state (start/stop integration)


# **create_integration_chirp_subscription**
> int create_integration_chirp_subscription(specification)

Create an integration chirp data subscription

Subscription online help:   <a href=\"https://simrad.online/ek80/interface_en/subscr_type_integration_chirp.html\" target=\"foo\">parameter description</a>.

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.IntegrationChirpSubscriptionsApi()
specification = ek80_data_client.IntegrationChirpSubscriptionSpecification() # IntegrationChirpSubscriptionSpecification | Specification of the data requested

try:
    # Create an integration chirp data subscription
    api_response = api_instance.create_integration_chirp_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationChirpSubscriptionsApi->create_integration_chirp_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**IntegrationChirpSubscriptionSpecification**](IntegrationChirpSubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_integration_chirp_subscription**
> delete_integration_chirp_subscription(subscription_id)

Delete an integration data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.IntegrationChirpSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # Delete an integration data subscription
    api_instance.delete_integration_chirp_subscription(subscription_id)
except ApiException as e:
    print("Exception when calling IntegrationChirpSubscriptionsApi->delete_integration_chirp_subscription: %s\n" % e)
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

# **get_integration_chirp_subscription**
> IntegrationChirpSubscriptionSpecification get_integration_chirp_subscription(subscription_id)

Get a particular integration chrip data subscription specification

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.IntegrationChirpSubscriptionsApi()
subscription_id = 789 # int | The unique id of the subscription

try:
    # Get a particular integration chrip data subscription specification
    api_response = api_instance.get_integration_chirp_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationChirpSubscriptionsApi->get_integration_chirp_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| The unique id of the subscription | 

### Return type

[**IntegrationChirpSubscriptionSpecification**](IntegrationChirpSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration_chirp_subscriptions**
> list[IntegrationChirpSubscriptionInfo] get_integration_chirp_subscriptions()

Get all integration chirp data subscriptions

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.IntegrationChirpSubscriptionsApi()

try:
    # Get all integration chirp data subscriptions
    api_response = api_instance.get_integration_chirp_subscriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationChirpSubscriptionsApi->get_integration_chirp_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[IntegrationChirpSubscriptionInfo]**](IntegrationChirpSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_integration_chirp_subscription**
> update_integration_chirp_subscription(subscription_id, settings)

Update an integration chirp data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.IntegrationChirpSubscriptionsApi()
subscription_id = 789 # int | Id of the subscription
settings = ek80_data_client.IntegrationChirpSettings() # IntegrationChirpSettings | New subscription settings

try:
    # Update an integration chirp data subscription
    api_instance.update_integration_chirp_subscription(subscription_id, settings)
except ApiException as e:
    print("Exception when calling IntegrationChirpSubscriptionsApi->update_integration_chirp_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| Id of the subscription | 
 **settings** | [**IntegrationChirpSettings**](IntegrationChirpSettings.md)| New subscription settings | 

### Return type

void (empty response body)

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
api_instance = ek80_data_client.IntegrationChirpSubscriptionsApi()
subscription_id = 789 # int | Id of the subscription
state = 'state_example' # str | New integration state

try:
    # Update the integration state (start/stop integration)
    api_instance.update_integration_state(subscription_id, state)
except ApiException as e:
    print("Exception when calling IntegrationChirpSubscriptionsApi->update_integration_state: %s\n" % e)
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

