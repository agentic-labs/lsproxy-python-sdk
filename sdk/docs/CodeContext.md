# CodeContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | [**FileRange**](FileRange.md) |  | 
**source_code** | **str** |  | 

## Example

```python
from lsproxy.models.code_context import CodeContext

# TODO update the JSON string below
json = "{}"
# create an instance of CodeContext from a JSON string
code_context_instance = CodeContext.from_json(json)
# print the JSON string representation of the object
print(CodeContext.to_json())

# convert the object into a dict
code_context_dict = code_context_instance.to_dict()
# create an instance of CodeContext from a dict
code_context_from_dict = CodeContext.from_dict(code_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


