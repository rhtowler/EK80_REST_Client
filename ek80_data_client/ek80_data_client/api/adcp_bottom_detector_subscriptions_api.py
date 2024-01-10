# coding: utf-8

"""
    REST API for setting up data subscriptions on the EK80 Echo Sounder

    The API, and the documentation of it, is still under construction. Feel free to experiment with it, but Kongsberg is only able to provide very limited support at the moment.  # How to start data output  1. Create a subscription  2. Create a communication end point  3. Add the subscription to the communication end point      # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ek80_data_client.api_client import ApiClient


class AdcpBottomDetectorSubscriptionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_adcp_bottom_detector_subscription(self, specification, **kwargs):  # noqa: E501
        """Create an adcp data subscription  # noqa: E501

        Subscription online help:   <a href=\"https://simrad.online/ek80/interface_en/subscr_type_adcp_bottom_detector.html\" target=\"foo\">parameter description</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_adcp_bottom_detector_subscription(specification, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AdcpBottomDetectorSubscriptionSpecification specification: Specification of the data requested (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_adcp_bottom_detector_subscription_with_http_info(specification, **kwargs)  # noqa: E501
        else:
            (data) = self.create_adcp_bottom_detector_subscription_with_http_info(specification, **kwargs)  # noqa: E501
            return data

    def create_adcp_bottom_detector_subscription_with_http_info(self, specification, **kwargs):  # noqa: E501
        """Create an adcp data subscription  # noqa: E501

        Subscription online help:   <a href=\"https://simrad.online/ek80/interface_en/subscr_type_adcp_bottom_detector.html\" target=\"foo\">parameter description</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_adcp_bottom_detector_subscription_with_http_info(specification, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AdcpBottomDetectorSubscriptionSpecification specification: Specification of the data requested (required)
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
                    " to method create_adcp_bottom_detector_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'specification' is set
        if ('specification' not in params or
                params['specification'] is None):
            raise ValueError("Missing the required parameter `specification` when calling `create_adcp_bottom_detector_subscription`")  # noqa: E501

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
            '/api/sounder/data-output/adcp-bottom-detector-subscriptions', 'POST',
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

    def delete_adcp_bottom_detector_subscription(self, subscription_id, **kwargs):  # noqa: E501
        """Delete an adcp detection data subscription  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_adcp_bottom_detector_subscription(subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int subscription_id:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_adcp_bottom_detector_subscription_with_http_info(subscription_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_adcp_bottom_detector_subscription_with_http_info(subscription_id, **kwargs)  # noqa: E501
            return data

    def delete_adcp_bottom_detector_subscription_with_http_info(self, subscription_id, **kwargs):  # noqa: E501
        """Delete an adcp detection data subscription  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_adcp_bottom_detector_subscription_with_http_info(subscription_id, async_req=True)
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
                    " to method delete_adcp_bottom_detector_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params or
                params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `delete_adcp_bottom_detector_subscription`")  # noqa: E501

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
            '/api/sounder/data-output/adcp-bottom-detector-subscriptions/{subscriptionId}', 'DELETE',
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

    def get_adcp_bottom_detector_subscriptions(self, **kwargs):  # noqa: E501
        """Get all adcp data subscriptions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_adcp_bottom_detector_subscriptions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[AdcpBottomDetectorSubscriptionInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_adcp_bottom_detector_subscriptions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_adcp_bottom_detector_subscriptions_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_adcp_bottom_detector_subscriptions_with_http_info(self, **kwargs):  # noqa: E501
        """Get all adcp data subscriptions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_adcp_bottom_detector_subscriptions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[AdcpBottomDetectorSubscriptionInfo]
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
                    " to method get_adcp_bottom_detector_subscriptions" % key
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
            '/api/sounder/data-output/adcp-bottom-detector-subscriptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[AdcpBottomDetectorSubscriptionInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_bottom_detector_adcp_subscription(self, subscription_id, **kwargs):  # noqa: E501
        """Get an adcp subscription specification  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bottom_detector_adcp_subscription(subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int subscription_id: The unique id of the subscription (required)
        :return: AdcpBottomDetectorSubscriptionSpecification
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bottom_detector_adcp_subscription_with_http_info(subscription_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_bottom_detector_adcp_subscription_with_http_info(subscription_id, **kwargs)  # noqa: E501
            return data

    def get_bottom_detector_adcp_subscription_with_http_info(self, subscription_id, **kwargs):  # noqa: E501
        """Get an adcp subscription specification  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bottom_detector_adcp_subscription_with_http_info(subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int subscription_id: The unique id of the subscription (required)
        :return: AdcpBottomDetectorSubscriptionSpecification
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
                    " to method get_bottom_detector_adcp_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params or
                params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `get_bottom_detector_adcp_subscription`")  # noqa: E501

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
            '/api/sounder/data-output/adcp-bottom-detector-subscriptions/{subscriptionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AdcpBottomDetectorSubscriptionSpecification',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_adcp_bottom_detector_subscription(self, subscription_id, settings, **kwargs):  # noqa: E501
        """Update an adcp subscription  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_adcp_bottom_detector_subscription(subscription_id, settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int subscription_id: Id of the subscription (required)
        :param AdcpBottomDetectorSettings settings: New subscription settings (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_adcp_bottom_detector_subscription_with_http_info(subscription_id, settings, **kwargs)  # noqa: E501
        else:
            (data) = self.update_adcp_bottom_detector_subscription_with_http_info(subscription_id, settings, **kwargs)  # noqa: E501
            return data

    def update_adcp_bottom_detector_subscription_with_http_info(self, subscription_id, settings, **kwargs):  # noqa: E501
        """Update an adcp subscription  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_adcp_bottom_detector_subscription_with_http_info(subscription_id, settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int subscription_id: Id of the subscription (required)
        :param AdcpBottomDetectorSettings settings: New subscription settings (required)
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
                    " to method update_adcp_bottom_detector_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params or
                params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `update_adcp_bottom_detector_subscription`")  # noqa: E501
        # verify the required parameter 'settings' is set
        if ('settings' not in params or
                params['settings'] is None):
            raise ValueError("Missing the required parameter `settings` when calling `update_adcp_bottom_detector_subscription`")  # noqa: E501

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
            '/api/sounder/data-output/adcp-bottom-detector-subscriptions/{subscriptionId}', 'PUT',
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
