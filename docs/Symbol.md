# Symbol


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The kind of the symbol (e.g., function, class). | 
**name** | **str** | The name of the symbol. | 
**start_position** | [**FilePosition**](FilePosition.md) |  | 

## Example

```python
from lsproxy.models.symbol import Symbol

# TODO update the JSON string below
json = "{}"
# create an instance of Symbol from a JSON string
symbol_instance = Symbol.from_json(json)
# print the JSON string representation of the object
print(Symbol.to_json())

# convert the object into a dict
symbol_dict = symbol_instance.to_dict()
# create an instance of Symbol from a dict
symbol_from_dict = Symbol.from_dict(symbol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


