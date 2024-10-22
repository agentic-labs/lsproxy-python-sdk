# lsproxy.WorkspaceApi

All URIs are relative to *http://localhost:4444/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_files**](WorkspaceApi.md#list_files) | **GET** /workspace/list-files | Get a list of all files in the workspace


# **list_files**
> List[str] list_files()

Get a list of all files in the workspace

Get a list of all files in the workspace  Returns an array of file paths for all files in the current workspace.  This is a convenience endpoint that does not use the underlying Language Servers directly, but it does apply the same filtering.

### Example


```python
import lsproxy
from lsproxy.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4444/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = lsproxy.Configuration(
    host = "http://localhost:4444/v1"
)


# Enter a context with an instance of the API client
with lsproxy.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lsproxy.WorkspaceApi(api_client)

    try:
        # Get a list of all files in the workspace
        api_response = api_instance.list_files()
        print("The response of WorkspaceApi->list_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->list_files: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace files retrieved successfully |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

