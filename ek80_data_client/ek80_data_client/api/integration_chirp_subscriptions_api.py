# coding: utf-8

"""
    REST API for setting up data subscriptions on the EK80 Echo Sounder

    The API, and the documentation of it, is currently under construction and is subject to change without further notice  # How to start data output  1. Create a subscription  2. Create a communication end point  3. Add the subscription to the communication end point    A link example, [kongsberg.com](http://www.kongsberg.com).  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ek80_data_client.api_client import ApiClient


class IntegrationChirpSubscriptionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_integration_chirp_subscription(self, specification, **kwargs):  # noqa: E501
        """Create an integration chirp data subscription  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_integration_chirp_subscription(specification, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IntegrationChirpSubscriptionSpecification specification: Specification of the data requested (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_integration_chirp_subscription_with_http_info(specification, **kwargs)  # noqa: E501
        else:
            (data) = self.create_integration_chirp_subscription_with_http_info(specification, **kwargs)  # noqa: E501
            return data

    def create_integration_chirp_subscription_with_http_info(self, specification, **kwargs):  # noqa: E501
        """Create an integration chirp data subscription  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_integration_chirp_subscription_with_http_info(specification, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IntegrationChirpSubscriptionSpecification specification: Specification of the data requested (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['specification']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_integration_chirp_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'specification' is set
        if ('specification' not in params or
                params['specification'] is None):
            raise ValueError("Missing the required parameter `specification` when calling `create_integration_chirp_subscription`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'specification' in params:
            body_params = params['specification']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/sounder/data-output/integration-chirp-subscriptions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_integration_chirp_subscription(self, subscription_id, **kwargs):  # noqa: E501
        """Delete an integration data subscription  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_integration_chirp_subscription(subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int subscription_id:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_integration_chirp_subscription_with_http_info(subscription_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_integration_chirp_subscription_with_http_info(subscription_id, **kwargs)  # noqa: E501
            return data

    def delete_integration_chirp_subscription_with_http_info(self, subscription_id, **kwargs):  # noqa: E501
        """Delete an integration data subscription  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_integration_chirp_subscription_with_http_info(subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int subscription_id:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_integration_chirp_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params or
                params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `delete_integration_chirp_subscription`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in params:
            path_params['subscriptionId'] = params['subscription_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/sounder/data-output/integration-chirp-subscriptions/{subscriptionId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_integration_chirp_subscription(self, subscription_id, **kwargs):  # noqa: E501
        """Get a particular integration chrip data subscription specification  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_integration_chirp_subscription(subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int subscription_id: The unique id of the subscription (required)
        :return: IntegrationChirpSubscriptionSpecification
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_integration_chirp_subscription_with_http_info(subscription_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_integration_chirp_subscription_with_http_info(subscription_id, **kwargs)  # noqa: E501
            return data

    def get_integration_chirp_subscription_with_http_info(self, subscription_id, **kwargs):  # noqa: E501
        """Get a particular integration chrip data subscription specification  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_integration_chirp_subscription_with_http_info(subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int subscription_id: The unique id of the subscription (required)
        :return: IntegrationChirpSubscriptionSpecification
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_integration_chirp_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params or
                params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `get_integration_chirp_subscription`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in params:
            path_params['subscriptionId'] = params['subscription_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/sounder/data-output/integration-chirp-subscriptions/{subscriptionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntegrationChirpSubscriptionSpecification',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_integration_chirp_subscriptions(self, **kwargs):  # noqa: E501
        """Get all integration chirp data subscriptions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_integration_chirp_subscriptions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[IntegrationChirpSubscriptionInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_integration_chirp_subscriptions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_integration_chirp_subscriptions_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_integration_chirp_subscriptions_with_http_info(self, **kwargs):  # noqa: E501
        """Get all integration chirp data subscriptions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_integration_chirp_subscriptions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[IntegrationChirpSubscriptionInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_integration_chirp_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/sounder/data-output/integration-chirp-subscriptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[IntegrationChirpSubscriptionInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_integration_chirp_subscription(self, subscription_id, settings, **kwargs):  # noqa: E501
        """Update an integration chirp data subscription  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_integration_chirp_subscription(subscription_id, settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int subscription_id: Id of the subscription (required)
        :param IntegrationChirpSettings settings: New subscription settings (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_integration_chirp_subscription_with_http_info(subscription_id, settings, **kwargs)  # noqa: E501
        else:
            (data) = self.update_integration_chirp_subscription_with_http_info(subscription_id, settings, **kwargs)  # noqa: E501
            return data

    def update_integration_chirp_subscription_with_http_info(self, subscription_id, settings, **kwargs):  # noqa: E501
        """Update an integration chirp data subscription  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_integration_chirp_subscription_with_http_info(subscription_id, settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int subscription_id: Id of the subscription (required)
        :param IntegrationChirpSettings settings: New subscription settings (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_id', 'settings']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_integration_chirp_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params or
                params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `update_integration_chirp_subscription`")  # noqa: E501
        # verify the required parameter 'settings' is set
        if ('settings' not in params or
                params['settings'] is None):
            raise ValueError("Missing the required parameter `settings` when calling `update_integration_chirp_subscription`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in params:
            path_params['subscriptionId'] = params['subscription_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'settings' in params:
            body_params = params['settings']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/sounder/data-output/integration-chirp-subscriptions/{subscriptionId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_integration_state(self, subscription_id, state, **kwargs):  # noqa: E501
        """Update the integration state (start/stop integration)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_integration_state(subscription_id, state, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int subscription_id: Id of the subscription (required)
        :param str state: New integration state (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_integration_state_with_http_info(subscription_id, state, **kwargs)  # noqa: E501
        else:
            (data) = self.update_integration_state_with_http_info(subscription_id, state, **kwargs)  # noqa: E501
            return data

    def update_integration_state_with_http_info(self, subscription_id, state, **kwargs):  # noqa: E501
        """Update the integration state (start/stop integration)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_integration_state_with_http_info(subscription_id, state, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int subscription_id: Id of the subscription (required)
        :param str state: New integration state (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_id', 'state']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_integration_state" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params or
                params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `update_integration_state`")  # noqa: E501
        # verify the required parameter 'state' is set
        if ('state' not in params or
                params['state'] is None):
            raise ValueError("Missing the required parameter `state` when calling `update_integration_state`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in params:
            path_params['subscriptionId'] = params['subscription_id']  # noqa: E501

        query_params = []
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/sounder/data-output/integration-chirp-subscriptions/{subscriptionId}/integration-state', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)