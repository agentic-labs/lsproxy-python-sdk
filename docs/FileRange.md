# FileRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | [**Position**](Position.md) |  | 
**path** | **str** | The path to the file. | 
**start** | [**Position**](Position.md) |  | 

## Example

```python
from lsproxy.models.file_range import FileRange

# TODO update the JSON string below
json = "{}"
# create an instance of FileRange from a JSON string
file_range_instance = FileRange.from_json(json)
# print the JSON string representation of the object
print(FileRange.to_json())

# convert the object into a dict
file_range_dict = file_range_instance.to_dict()
# create an instance of FileRange from a dict
file_range_from_dict = FileRange.from_dict(file_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


