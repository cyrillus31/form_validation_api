from validation import validator



class Form:
    def __init__(self, **kwargs) -> None:
        self.name: str = "Unknown"
        self.fields_with_content: dict = kwargs 

    def get_types(self) -> dict:
        if not self.fields_with_types:
            self.fields_with_types: dict = {}
            for field in self.fields_with_content:
                field_content = self.fields_with_content[field]
                self.fields_with_types[field] = validator(field_content)
        return self.fields_with_types
    
    def find_match(self) -> str | None:
        ...
