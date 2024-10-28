# VecInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier_position** | [**FilePosition**](FilePosition.md) | The start position of the symbol&#39;s identifier. | 
**kind** | **str** | The kind of the symbol (e.g., function, class). | 
**name** | **str** | The name of the symbol. | 

## Example

```python
from lsproxy.models.vec_inner import VecInner

# TODO update the JSON string below
json = "{}"
# create an instance of VecInner from a JSON string
vec_inner_instance = VecInner.from_json(json)
# print the JSON string representation of the object
print(VecInner.to_json())

# convert the object into a dict
vec_inner_dict = vec_inner_instance.to_dict()
# create an instance of VecInner from a dict
vec_inner_from_dict = VecInner.from_dict(vec_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


