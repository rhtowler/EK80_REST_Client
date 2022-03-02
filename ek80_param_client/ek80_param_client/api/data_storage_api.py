# coding: utf-8

"""
    REST API for the EK80 Echo Sounder

    This API is for internal Simrad/Kongsberg Maritime use only.  The API, and the documentation of it, is currently under construction and is subject to change without further notice  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ek80_param_client.api_client import ApiClient


class DataStorageApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def data_storage_get_basic_storage_settings(self, **kwargs):  # noqa: E501
        """Get MainStorageSettings struct with the most common storage settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_storage_get_basic_storage_settings(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MainStorageSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.data_storage_get_basic_storage_settings_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.data_storage_get_basic_storage_settings_with_http_info(**kwargs)  # noqa: E501
            return data

    def data_storage_get_basic_storage_settings_with_http_info(self, **kwargs):  # noqa: E501
        """Get MainStorageSettings struct with the most common storage settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_storage_get_basic_storage_settings_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MainStorageSettings
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
                    " to method data_storage_get_basic_storage_settings" % key
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
            '/api/sounder/data-storage', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MainStorageSettings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def data_storage_get_individual_channel_range(self, channel_name, **kwargs):  # noqa: E501
        """Get range settings for a specific channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_storage_get_individual_channel_range(channel_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str channel_name: The logical channel id (required)
        :return: IndividualRangeControl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.data_storage_get_individual_channel_range_with_http_info(channel_name, **kwargs)  # noqa: E501
        else:
            (data) = self.data_storage_get_individual_channel_range_with_http_info(channel_name, **kwargs)  # noqa: E501
            return data

    def data_storage_get_individual_channel_range_with_http_info(self, channel_name, **kwargs):  # noqa: E501
        """Get range settings for a specific channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_storage_get_individual_channel_range_with_http_info(channel_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str channel_name: The logical channel id (required)
        :return: IndividualRangeControl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_storage_get_individual_channel_range" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'channel_name' is set
        if ('channel_name' not in params or
                params['channel_name'] is None):
            raise ValueError("Missing the required parameter `channel_name` when calling `data_storage_get_individual_channel_range`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'channel_name' in params:
            path_params['channel_name'] = params['channel_name']  # noqa: E501

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
            '/api/sounder/data-storage/individual-channel-range/{channel_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IndividualRangeControl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def data_storage_get_record_raw_active(self, **kwargs):  # noqa: E501
        """Is recording raw files on or off  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_storage_get_record_raw_active(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.data_storage_get_record_raw_active_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.data_storage_get_record_raw_active_with_http_info(**kwargs)  # noqa: E501
            return data

    def data_storage_get_record_raw_active_with_http_info(self, **kwargs):  # noqa: E501
        """Is recording raw files on or off  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_storage_get_record_raw_active_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: bool
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
                    " to method data_storage_get_record_raw_active" % key
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
            '/api/sounder/data-storage/record-raw-active', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def data_storage_set_basic_storage_settings(self, storage_settings, **kwargs):  # noqa: E501
        """data_storage_set_basic_storage_settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_storage_set_basic_storage_settings(storage_settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MainStorageSettings storage_settings: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.data_storage_set_basic_storage_settings_with_http_info(storage_settings, **kwargs)  # noqa: E501
        else:
            (data) = self.data_storage_set_basic_storage_settings_with_http_info(storage_settings, **kwargs)  # noqa: E501
            return data

    def data_storage_set_basic_storage_settings_with_http_info(self, storage_settings, **kwargs):  # noqa: E501
        """data_storage_set_basic_storage_settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_storage_set_basic_storage_settings_with_http_info(storage_settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MainStorageSettings storage_settings: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['storage_settings']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_storage_set_basic_storage_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'storage_settings' is set
        if ('storage_settings' not in params or
                params['storage_settings'] is None):
            raise ValueError("Missing the required parameter `storage_settings` when calling `data_storage_set_basic_storage_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'storage_settings' in params:
            body_params = params['storage_settings']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/sounder/data-storage', 'PUT',
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

    def data_storage_set_individual_channel_range(self, channel_range, **kwargs):  # noqa: E501
        """Sets the range settings for a specific channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_storage_set_individual_channel_range(channel_range, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IndividualRangeControl channel_range: IndividualRangeControl struct with rabge settings for a channel (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.data_storage_set_individual_channel_range_with_http_info(channel_range, **kwargs)  # noqa: E501
        else:
            (data) = self.data_storage_set_individual_channel_range_with_http_info(channel_range, **kwargs)  # noqa: E501
            return data

    def data_storage_set_individual_channel_range_with_http_info(self, channel_range, **kwargs):  # noqa: E501
        """Sets the range settings for a specific channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_storage_set_individual_channel_range_with_http_info(channel_range, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IndividualRangeControl channel_range: IndividualRangeControl struct with rabge settings for a channel (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_range']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_storage_set_individual_channel_range" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'channel_range' is set
        if ('channel_range' not in params or
                params['channel_range'] is None):
            raise ValueError("Missing the required parameter `channel_range` when calling `data_storage_set_individual_channel_range`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'channel_range' in params:
            body_params = params['channel_range']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/sounder/data-storage/individual-channel-range', 'PUT',
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

    def data_storage_set_record_raw_active(self, record_raw_active, **kwargs):  # noqa: E501
        """Turns on or off raw data storage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_storage_set_record_raw_active(record_raw_active, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool record_raw_active: A bool value if raw data storage should be turned on or off (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.data_storage_set_record_raw_active_with_http_info(record_raw_active, **kwargs)  # noqa: E501
        else:
            (data) = self.data_storage_set_record_raw_active_with_http_info(record_raw_active, **kwargs)  # noqa: E501
            return data

    def data_storage_set_record_raw_active_with_http_info(self, record_raw_active, **kwargs):  # noqa: E501
        """Turns on or off raw data storage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_storage_set_record_raw_active_with_http_info(record_raw_active, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool record_raw_active: A bool value if raw data storage should be turned on or off (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['record_raw_active']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_storage_set_record_raw_active" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'record_raw_active' is set
        if ('record_raw_active' not in params or
                params['record_raw_active'] is None):
            raise ValueError("Missing the required parameter `record_raw_active` when calling `data_storage_set_record_raw_active`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'record_raw_active' in params:
            body_params = params['record_raw_active']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/sounder/data-storage/record-raw-active', 'PUT',
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
