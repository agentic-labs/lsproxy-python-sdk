# lsproxy.SymbolApi

All URIs are relative to *http://localhost:4444/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**definitions_in_file**](SymbolApi.md#definitions_in_file) | **GET** /symbol/definitions-in-file | Get symbols in a specific file
[**find_definition**](SymbolApi.md#find_definition) | **POST** /symbol/find-definition | Get the definition of a symbol at a specific position in a file
[**find_references**](SymbolApi.md#find_references) | **POST** /symbol/find-references | Find all references to a symbol


# **definitions_in_file**
> SymbolResponse definitions_in_file(file_path, include_raw_response=include_raw_response)

Get symbols in a specific file

Get symbols in a specific file  Returns a list of symbols (functions, classes, variables, etc.) defined in the specified file.  The returned positions point to the start of the symbol's identifier.  e.g. for `User` on line 0 of `src/main.py`: ``` 0: class User: _________^ 1:     def __init__(self, name, age): 2:         self.name = name 3:         self.age = age ```

### Example


```python
import lsproxy
from lsproxy.models.symbol_response import SymbolResponse
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
    api_instance = lsproxy.SymbolApi(api_client)
    file_path = 'file_path_example' # str | The path to the file to get the symbols for, relative to the root of the workspace.
    include_raw_response = True # bool | Whether to include the raw response from the langserver in the response. Defaults to false. (optional)

    try:
        # Get symbols in a specific file
        api_response = api_instance.definitions_in_file(file_path, include_raw_response=include_raw_response)
        print("The response of SymbolApi->definitions_in_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SymbolApi->definitions_in_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path** | **str**| The path to the file to get the symbols for, relative to the root of the workspace. | 
 **include_raw_response** | **bool**| Whether to include the raw response from the langserver in the response. Defaults to false. | [optional] 

### Return type

[**SymbolResponse**](SymbolResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Symbols retrieved successfully |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_definition**
> DefinitionResponse find_definition(get_definition_request)

Get the definition of a symbol at a specific position in a file

Get the definition of a symbol at a specific position in a file  Returns the location of the definition for the symbol at the given position.  The input position should point inside the symbol's identifier, e.g.  The returned position points to the identifier of the symbol, and the file_path from workspace root  e.g. for the definition of `User` on line 5 of `src/main.py` with the code: ``` 0: class User: output___^ 1:     def __init__(self, name, age): 2:         self.name = name 3:         self.age = age 4: 5: user = User(\"John\", 30) input_____^^^^ ```

### Example


```python
import lsproxy
from lsproxy.models.definition_response import DefinitionResponse
from lsproxy.models.get_definition_request import GetDefinitionRequest
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
    api_instance = lsproxy.SymbolApi(api_client)
    get_definition_request = lsproxy.GetDefinitionRequest() # GetDefinitionRequest | 

    try:
        # Get the definition of a symbol at a specific position in a file
        api_response = api_instance.find_definition(get_definition_request)
        print("The response of SymbolApi->find_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SymbolApi->find_definition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_definition_request** | [**GetDefinitionRequest**](GetDefinitionRequest.md)|  | 

### Return type

[**DefinitionResponse**](DefinitionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Definition retrieved successfully |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_references**
> ReferencesResponse find_references(get_references_request)

Find all references to a symbol

Find all references to a symbol  The input position should point to the identifier of the symbol you want to get the references for.  Returns a list of locations where the symbol at the given position is referenced.  The returned positions point to the start of the reference identifier.  e.g. for `User` on line 0 of `src/main.py`: ``` 0: class User: input____^^^^ 1:     def __init__(self, name, age): 2:         self.name = name 3:         self.age = age 4: 5: user = User(\"John\", 30) output____^ ```

### Example


```python
import lsproxy
from lsproxy.models.get_references_request import GetReferencesRequest
from lsproxy.models.references_response import ReferencesResponse
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
    api_instance = lsproxy.SymbolApi(api_client)
    get_references_request = lsproxy.GetReferencesRequest() # GetReferencesRequest | 

    try:
        # Find all references to a symbol
        api_response = api_instance.find_references(get_references_request)
        print("The response of SymbolApi->find_references:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SymbolApi->find_references: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_references_request** | [**GetReferencesRequest**](GetReferencesRequest.md)|  | 

### Return type

[**ReferencesResponse**](ReferencesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | References retrieved successfully |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

