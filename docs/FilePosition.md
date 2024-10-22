# FilePosition

Specific position within a file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | 
**position** | [**Position**](Position.md) |  | 

## Example

```python
from lsproxy.models.file_position import FilePosition

# TODO update the JSON string below
json = "{}"
# create an instance of FilePosition from a JSON string
file_position_instance = FilePosition.from_json(json)
# print the JSON string representation of the object
print(FilePosition.to_json())

# convert the object into a dict
file_position_dict = file_position_instance.to_dict()
# create an instance of FilePosition from a dict
file_position_from_dict = FilePosition.from_dict(file_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


