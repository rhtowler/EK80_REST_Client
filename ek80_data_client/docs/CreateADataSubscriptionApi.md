# ek80_data_client.CreateADataSubscriptionApi

All URIs are relative to *http://localhost:12346*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_adcp_backscatter_subscription**](CreateADataSubscriptionApi.md#create_adcp_backscatter_subscription) | **POST** /api/sounder/data-output/adcp-backscatter-subscriptions | Create an adcp data subscription
[**create_adcp_beam_data_subscription**](CreateADataSubscriptionApi.md#create_adcp_beam_data_subscription) | **POST** /api/sounder/data-output/adcp-beam-data-subscriptions | Create an adcp data subscription
[**create_adcp_bottom_detector_subscription**](CreateADataSubscriptionApi.md#create_adcp_bottom_detector_subscription) | **POST** /api/sounder/data-output/adcp-bottom-detector-subscriptions | Create an adcp data subscription
[**create_adcp_output_subscription**](CreateADataSubscriptionApi.md#create_adcp_output_subscription) | **POST** /api/sounder/data-output/adcp-output-subscriptions | Create an adcp data subscription
[**create_adcp_quality_factor_subscription**](CreateADataSubscriptionApi.md#create_adcp_quality_factor_subscription) | **POST** /api/sounder/data-output/adcp-quality-factor-subscriptions | Create an adcp data subscription
[**create_adcp_velocity_subscription**](CreateADataSubscriptionApi.md#create_adcp_velocity_subscription) | **POST** /api/sounder/data-output/adcp-velocity-subscriptions | Create an adcp data subscription
[**create_bottom_detection_subscription**](CreateADataSubscriptionApi.md#create_bottom_detection_subscription) | **POST** /api/sounder/data-output/bottom-detection-subscriptions | Create a bottom detection data subscription
[**create_echogram_subscription**](CreateADataSubscriptionApi.md#create_echogram_subscription) | **POST** /api/sounder/data-output/echogram-subscriptions | Create an echogram data subscription
[**create_integration_chirp_subscription**](CreateADataSubscriptionApi.md#create_integration_chirp_subscription) | **POST** /api/sounder/data-output/integration-chirp-subscriptions | Create an integration chirp data subscription
[**create_integration_subscription**](CreateADataSubscriptionApi.md#create_integration_subscription) | **POST** /api/sounder/data-output/integration-subscriptions | Create an integration data subscription
[**create_noise_spectrum_subscription**](CreateADataSubscriptionApi.md#create_noise_spectrum_subscription) | **POST** /api/sounder/data-output/noise-spectrum-subscriptions | Create a noise spectrum data subscription
[**create_sample_data_subscription**](CreateADataSubscriptionApi.md#create_sample_data_subscription) | **POST** /api/sounder/data-output/sample-data-subscriptions | Create a processed sample-data subscription
[**create_system_state_subscription**](CreateADataSubscriptionApi.md#create_system_state_subscription) | **POST** /api/sounder/data-output/system-state-subscriptions | Create a system state data subscription
[**create_targets_echogram_subscription**](CreateADataSubscriptionApi.md#create_targets_echogram_subscription) | **POST** /api/sounder/data-output/targets-echogram-subscriptions | Create a targets echogram data subscription
[**create_targets_integration_subscription**](CreateADataSubscriptionApi.md#create_targets_integration_subscription) | **POST** /api/sounder/data-output/targets-integration-subscriptions | Create a targets integration data subscription
[**create_ts_detection_chirp_subscription**](CreateADataSubscriptionApi.md#create_ts_detection_chirp_subscription) | **POST** /api/sounder/data-output/ts-detection-chirp-subscriptions | Create a ts detection chirp data subscription
[**create_ts_detection_subscription**](CreateADataSubscriptionApi.md#create_ts_detection_subscription) | **POST** /api/sounder/data-output/ts-detection-subscriptions | Create a ts detection data subscription


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
api_instance = ek80_data_client.CreateADataSubscriptionApi()
specification = ek80_data_client.AdcpBackscatterSubscriptionSpecification() # AdcpBackscatterSubscriptionSpecification | Specification of the data requested

try:
    # Create an adcp data subscription
    api_response = api_instance.create_adcp_backscatter_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->create_adcp_backscatter_subscription: %s\n" % e)
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

# **create_adcp_beam_data_subscription**
> int create_adcp_beam_data_subscription(specification)

Create an adcp data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.CreateADataSubscriptionApi()
specification = ek80_data_client.AdcpBeamDataSubscriptionSpecification() # AdcpBeamDataSubscriptionSpecification | Specification of the data requested

try:
    # Create an adcp data subscription
    api_response = api_instance.create_adcp_beam_data_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->create_adcp_beam_data_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**AdcpBeamDataSubscriptionSpecification**](AdcpBeamDataSubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_adcp_bottom_detector_subscription**
> int create_adcp_bottom_detector_subscription(specification)

Create an adcp data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.CreateADataSubscriptionApi()
specification = ek80_data_client.AdcpBottomDetectorSubscriptionSpecification() # AdcpBottomDetectorSubscriptionSpecification | Specification of the data requested

try:
    # Create an adcp data subscription
    api_response = api_instance.create_adcp_bottom_detector_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->create_adcp_bottom_detector_subscription: %s\n" % e)
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

# **create_adcp_output_subscription**
> int create_adcp_output_subscription(specification)

Create an adcp data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.CreateADataSubscriptionApi()
specification = ek80_data_client.AdcpOutputSubscriptionSpecification() # AdcpOutputSubscriptionSpecification | Specification of the data requested

try:
    # Create an adcp data subscription
    api_response = api_instance.create_adcp_output_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->create_adcp_output_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**AdcpOutputSubscriptionSpecification**](AdcpOutputSubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_adcp_quality_factor_subscription**
> int create_adcp_quality_factor_subscription(specification)

Create an adcp data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.CreateADataSubscriptionApi()
specification = ek80_data_client.AdcpQualityFactorSubscriptionSpecification() # AdcpQualityFactorSubscriptionSpecification | Specification of the data requested

try:
    # Create an adcp data subscription
    api_response = api_instance.create_adcp_quality_factor_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->create_adcp_quality_factor_subscription: %s\n" % e)
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

# **create_adcp_velocity_subscription**
> int create_adcp_velocity_subscription(specification)

Create an adcp data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.CreateADataSubscriptionApi()
specification = ek80_data_client.AdcpVelocitySubscriptionSpecification() # AdcpVelocitySubscriptionSpecification | Specification of the data requested

try:
    # Create an adcp data subscription
    api_response = api_instance.create_adcp_velocity_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->create_adcp_velocity_subscription: %s\n" % e)
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

# **create_bottom_detection_subscription**
> int create_bottom_detection_subscription(specification)

Create a bottom detection data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.CreateADataSubscriptionApi()
specification = ek80_data_client.BottomDetectionSubscriptionSpecification() # BottomDetectionSubscriptionSpecification | Specification of the data requested

try:
    # Create a bottom detection data subscription
    api_response = api_instance.create_bottom_detection_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->create_bottom_detection_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**BottomDetectionSubscriptionSpecification**](BottomDetectionSubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = ek80_data_client.CreateADataSubscriptionApi()
specification = ek80_data_client.EchogramSubscriptionSpecification() # EchogramSubscriptionSpecification | Specification of the data requested

try:
    # Create an echogram data subscription
    api_response = api_instance.create_echogram_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->create_echogram_subscription: %s\n" % e)
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

# **create_integration_chirp_subscription**
> int create_integration_chirp_subscription(specification)

Create an integration chirp data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.CreateADataSubscriptionApi()
specification = ek80_data_client.IntegrationChirpSubscriptionSpecification() # IntegrationChirpSubscriptionSpecification | Specification of the data requested

try:
    # Create an integration chirp data subscription
    api_response = api_instance.create_integration_chirp_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->create_integration_chirp_subscription: %s\n" % e)
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

# **create_integration_subscription**
> int create_integration_subscription(specification)

Create an integration data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.CreateADataSubscriptionApi()
specification = ek80_data_client.IntegrationSubscriptionSpecification() # IntegrationSubscriptionSpecification | Specification of the data requested

try:
    # Create an integration data subscription
    api_response = api_instance.create_integration_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->create_integration_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**IntegrationSubscriptionSpecification**](IntegrationSubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_noise_spectrum_subscription**
> int create_noise_spectrum_subscription(specification)

Create a noise spectrum data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.CreateADataSubscriptionApi()
specification = ek80_data_client.NoiseSpectrumSubscriptionSpecification() # NoiseSpectrumSubscriptionSpecification | Specification of the data requested

try:
    # Create a noise spectrum data subscription
    api_response = api_instance.create_noise_spectrum_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->create_noise_spectrum_subscription: %s\n" % e)
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

# **create_sample_data_subscription**
> int create_sample_data_subscription(specification)

Create a processed sample-data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.CreateADataSubscriptionApi()
specification = ek80_data_client.SampleDataSubscriptionSpecification() # SampleDataSubscriptionSpecification | Specification of the data requested

try:
    # Create a processed sample-data subscription
    api_response = api_instance.create_sample_data_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->create_sample_data_subscription: %s\n" % e)
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

# **create_system_state_subscription**
> int create_system_state_subscription(specification)

Create a system state data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.CreateADataSubscriptionApi()
specification = ek80_data_client.SystemStateSubscriptionSpecification() # SystemStateSubscriptionSpecification | Specification of the data requested

try:
    # Create a system state data subscription
    api_response = api_instance.create_system_state_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->create_system_state_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**SystemStateSubscriptionSpecification**](SystemStateSubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_targets_echogram_subscription**
> int create_targets_echogram_subscription(specification)

Create a targets echogram data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.CreateADataSubscriptionApi()
specification = ek80_data_client.TargetsEchogramSubscriptionSpecification() # TargetsEchogramSubscriptionSpecification | Specification of the data requested

try:
    # Create a targets echogram data subscription
    api_response = api_instance.create_targets_echogram_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->create_targets_echogram_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**TargetsEchogramSubscriptionSpecification**](TargetsEchogramSubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_targets_integration_subscription**
> int create_targets_integration_subscription(specification)

Create a targets integration data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.CreateADataSubscriptionApi()
specification = ek80_data_client.TargetsIntegrationSubscriptionSpecification() # TargetsIntegrationSubscriptionSpecification | Specification of the data requested

try:
    # Create a targets integration data subscription
    api_response = api_instance.create_targets_integration_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->create_targets_integration_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**TargetsIntegrationSubscriptionSpecification**](TargetsIntegrationSubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ts_detection_chirp_subscription**
> int create_ts_detection_chirp_subscription(specification)

Create a ts detection chirp data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.CreateADataSubscriptionApi()
specification = ek80_data_client.TsDetectionChirpSubscriptionSpecification() # TsDetectionChirpSubscriptionSpecification | Specification of the data requested

try:
    # Create a ts detection chirp data subscription
    api_response = api_instance.create_ts_detection_chirp_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->create_ts_detection_chirp_subscription: %s\n" % e)
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

# **create_ts_detection_subscription**
> int create_ts_detection_subscription(specification)

Create a ts detection data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.CreateADataSubscriptionApi()
specification = ek80_data_client.TsDetectionSubscriptionSpecification() # TsDetectionSubscriptionSpecification | Specification of the data requested

try:
    # Create a ts detection data subscription
    api_response = api_instance.create_ts_detection_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->create_ts_detection_subscription: %s\n" % e)
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

