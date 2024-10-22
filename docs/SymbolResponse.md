# SymbolResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_response** | **object** | The raw response from the langserver.  https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#workspace_symbol https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#document_symbol | [optional] 
**symbols** | [**List[Symbol]**](Symbol.md) |  | 

## Example

```python
from lsproxy.models.symbol_response import SymbolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SymbolResponse from a JSON string
symbol_response_instance = SymbolResponse.from_json(json)
# print the JSON string representation of the object
print(SymbolResponse.to_json())

# convert the object into a dict
symbol_response_dict = symbol_response_instance.to_dict()
# create an instance of SymbolResponse from a dict
symbol_response_from_dict = SymbolResponse.from_dict(symbol_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


