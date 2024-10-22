# DefinitionResponse

Response to a definition request.  The definition(s) of the symbol. Points to the start position of the symbol's identifier.  e.g. for the definition of `User` on line 5 of `src/main.py` with the code: ``` 0: class User: _________^ 1:     def __init__(self, name, age): 2:         self.name = name 3:         self.age = age 4: 5: user = User(\"John\", 30) __________^ ``` The definition(s) will be `[{\"path\": \"src/main.py\", \"line\": 0, \"character\": 6}]`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definitions** | [**List[FilePosition]**](FilePosition.md) |  | 
**raw_response** | **object** | The raw response from the langserver.  https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_definition | [optional] 
**source_code_context** | [**List[CodeContext]**](CodeContext.md) | The source code of symbol definitions. | [optional] 

## Example

```python
from lsproxy.models.definition_response import DefinitionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DefinitionResponse from a JSON string
definition_response_instance = DefinitionResponse.from_json(json)
# print the JSON string representation of the object
print(DefinitionResponse.to_json())

# convert the object into a dict
definition_response_dict = definition_response_instance.to_dict()
# create an instance of DefinitionResponse from a dict
definition_response_from_dict = DefinitionResponse.from_dict(definition_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


