from validation import validator
from database.db import find_forms_by_fields


class Form:
    def __init__(self, fields_with_content: dict["str", "str"]) -> None:
        self.name: str = "Unknown"
        self.fields_with_content: dict = fields_with_content 
        self.fields_with_types: dict = {} 

    def get_types(self) -> dict:
        if not self.fields_with_types:
            self.fields_with_types: dict = {}
            for field in self.fields_with_content:
                field_content = self.fields_with_content[field]
                self.fields_with_types[field] = validator(field_content)
        return self.fields_with_types
    
    def find_name(self) -> str:
        if not self.fields_with_types:
            self.get_types()
        fields = self.fields_with_content.keys()
        forms_that_fit: list = find_forms_by_fields(*fields)
        if len(forms_that_fit) == 1:
            the_form = forms_that_fit[0]
            self.name = the_form["form_name"]
        return self.name
        
        
