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


class CommunicationEndPointsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_subscription_to_end_point(self, end_point_id, subscription_output_args, **kwargs):  # noqa: E501
        """Add a subscription to the communication end point  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_subscription_to_end_point(end_point_id, subscription_output_args, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int end_point_id: Id of the communication end point (required)
        :param SubscriptionOutputArgs subscription_output_args: Id of the subscription (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_subscription_to_end_point_with_http_info(end_point_id, subscription_output_args, **kwargs)  # noqa: E501
        else:
            (data) = self.add_subscription_to_end_point_with_http_info(end_point_id, subscription_output_args, **kwargs)  # noqa: E501
            return data

    def add_subscription_to_end_point_with_http_info(self, end_point_id, subscription_output_args, **kwargs):  # noqa: E501
        """Add a subscription to the communication end point  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_subscription_to_end_point_with_http_info(end_point_id, subscription_output_args, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int end_point_id: Id of the communication end point (required)
        :param SubscriptionOutputArgs subscription_output_args: Id of the subscription (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['end_point_id', 'subscription_output_args']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_subscription_to_end_point" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'end_point_id' is set
        if ('end_point_id' not in params or
                params['end_point_id'] is None):
            raise ValueError("Missing the required parameter `end_point_id` when calling `add_subscription_to_end_point`")  # noqa: E501
        # verify the required parameter 'subscription_output_args' is set
        if ('subscription_output_args' not in params or
                params['subscription_output_args'] is None):
            raise ValueError("Missing the required parameter `subscription_output_args` when calling `add_subscription_to_end_point`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'end_point_id' in params:
            path_params['endPointId'] = params['end_point_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'subscription_output_args' in params:
            body_params = params['subscription_output_args']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/sounder/data-output/communication-end-points/{endPointId}/data-subscriptions', 'POST',
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

    def create_communication_end_point(self, settings, **kwargs):  # noqa: E501
        """Create a new communication end point  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_communication_end_point(settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CommunicationEndPointSettings settings: Settings for the new end point (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_communication_end_point_with_http_info(settings, **kwargs)  # noqa: E501
        else:
            (data) = self.create_communication_end_point_with_http_info(settings, **kwargs)  # noqa: E501
            return data

    def create_communication_end_point_with_http_info(self, settings, **kwargs):  # noqa: E501
        """Create a new communication end point  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_communication_end_point_with_http_info(settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CommunicationEndPointSettings settings: Settings for the new end point (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['settings']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_communication_end_point" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'settings' is set
        if ('settings' not in params or
                params['settings'] is None):
            raise ValueError("Missing the required parameter `settings` when calling `create_communication_end_point`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/api/sounder/data-output/communication-end-points', 'POST',
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

    def delete_communication_end_point(self, end_point_id, **kwargs):  # noqa: E501
        """Delete a communication end point  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_communication_end_point(end_point_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int end_point_id: Id of the communication end point to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_communication_end_point_with_http_info(end_point_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_communication_end_point_with_http_info(end_point_id, **kwargs)  # noqa: E501
            return data

    def delete_communication_end_point_with_http_info(self, end_point_id, **kwargs):  # noqa: E501
        """Delete a communication end point  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_communication_end_point_with_http_info(end_point_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int end_point_id: Id of the communication end point to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['end_point_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_communication_end_point" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'end_point_id' is set
        if ('end_point_id' not in params or
                params['end_point_id'] is None):
            raise ValueError("Missing the required parameter `end_point_id` when calling `delete_communication_end_point`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'end_point_id' in params:
            path_params['endPointId'] = params['end_point_id']  # noqa: E501

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
            '/api/sounder/data-output/communication-end-points/{endPointId}', 'DELETE',
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

    def get_active_communication_end_points(self, **kwargs):  # noqa: E501
        """Get information about the active communication end points  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_active_communication_end_points(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[CommunicationEndPointInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_active_communication_end_points_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_active_communication_end_points_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_active_communication_end_points_with_http_info(self, **kwargs):  # noqa: E501
        """Get information about the active communication end points  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_active_communication_end_points_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[CommunicationEndPointInfo]
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
                    " to method get_active_communication_end_points" % key
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
            '/api/sounder/data-output/communication-end-points', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CommunicationEndPointInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_subscriptions_by_end_point(self, end_point_id, **kwargs):  # noqa: E501
        """Get the active data subscriptions for the end point  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_subscriptions_by_end_point(end_point_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int end_point_id: Id of the communication end point (required)
        :return: list[SubscriptionSummary]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_subscriptions_by_end_point_with_http_info(end_point_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_subscriptions_by_end_point_with_http_info(end_point_id, **kwargs)  # noqa: E501
            return data

    def get_subscriptions_by_end_point_with_http_info(self, end_point_id, **kwargs):  # noqa: E501
        """Get the active data subscriptions for the end point  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_subscriptions_by_end_point_with_http_info(end_point_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int end_point_id: Id of the communication end point (required)
        :return: list[SubscriptionSummary]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['end_point_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subscriptions_by_end_point" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'end_point_id' is set
        if ('end_point_id' not in params or
                params['end_point_id'] is None):
            raise ValueError("Missing the required parameter `end_point_id` when calling `get_subscriptions_by_end_point`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'end_point_id' in params:
            path_params['endPointId'] = params['end_point_id']  # noqa: E501

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
            '/api/sounder/data-output/communication-end-points/{endPointId}/data-subscriptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SubscriptionSummary]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_subscription_from_end_point(self, end_point_id, subscription_id, **kwargs):  # noqa: E501
        """Remove a subscription from the communication end point  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_subscription_from_end_point(end_point_id, subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int end_point_id: Id of the communication end point (required)
        :param int subscription_id: Id of the subscription (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_subscription_from_end_point_with_http_info(end_point_id, subscription_id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_subscription_from_end_point_with_http_info(end_point_id, subscription_id, **kwargs)  # noqa: E501
            return data

    def remove_subscription_from_end_point_with_http_info(self, end_point_id, subscription_id, **kwargs):  # noqa: E501
        """Remove a subscription from the communication end point  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_subscription_from_end_point_with_http_info(end_point_id, subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int end_point_id: Id of the communication end point (required)
        :param int subscription_id: Id of the subscription (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['end_point_id', 'subscription_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_subscription_from_end_point" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'end_point_id' is set
        if ('end_point_id' not in params or
                params['end_point_id'] is None):
            raise ValueError("Missing the required parameter `end_point_id` when calling `remove_subscription_from_end_point`")  # noqa: E501
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params or
                params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `remove_subscription_from_end_point`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'end_point_id' in params:
            path_params['endPointId'] = params['end_point_id']  # noqa: E501

        query_params = []
        if 'subscription_id' in params:
            query_params.append(('subscriptionId', params['subscription_id']))  # noqa: E501

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
            '/api/sounder/data-output/communication-end-points/{endPointId}/data-subscriptions', 'DELETE',
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
