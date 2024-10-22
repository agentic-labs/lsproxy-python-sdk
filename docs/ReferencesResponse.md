# ReferencesResponse

Response to a references request.  Points to the start position of the symbol's identifier.  e.g. for the references of `User` on line 0 character 6 of `src/main.py` with the code: ``` 0: class User: 1:     def __init__(self, name, age): 2:         self.name = name 3:         self.age = age 4: 5: user = User(\"John\", 30) _________^ 6: 7: print(user.name) ``` The references will be `[{\"path\": \"src/main.py\", \"line\": 5, \"character\": 7}]`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**List[CodeContext]**](CodeContext.md) | The source code around the references. | [optional] 
**raw_response** | **object** | The raw response from the langserver.  https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_references | [optional] 
**references** | [**List[FilePosition]**](FilePosition.md) |  | 

## Example

```python
from lsproxy.models.references_response import ReferencesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencesResponse from a JSON string
references_response_instance = ReferencesResponse.from_json(json)
# print the JSON string representation of the object
print(ReferencesResponse.to_json())

# convert the object into a dict
references_response_dict = references_response_instance.to_dict()
# create an instance of ReferencesResponse from a dict
references_response_from_dict = ReferencesResponse.from_dict(references_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


