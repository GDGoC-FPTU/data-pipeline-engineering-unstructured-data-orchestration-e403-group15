try:
    from pydantic import BaseModel, Field
except ModuleNotFoundError:
    def Field(default, description=""):
        return default

    class BaseModel:
        def __init__(self, **data):
            for field_name, field_type in self.__annotations__.items():
                if field_name not in data:
                    raise ValueError(f"Missing required field: {field_name}")
                value = data[field_name]
                if not isinstance(value, field_type):
                    value = field_type(value)
                setattr(self, field_name, value)

        def model_dump(self):
            return {field_name: getattr(self, field_name) for field_name in self.__annotations__}

        def dict(self):
            return self.model_dump()


class UnifiedDocument(BaseModel):
    """Canonical schema shared by all processed sources."""

    document_id: str = Field(..., description="Unique identifier from the source system")
    source_type: str = Field(..., description="Origin type, such as PDF or Video")
    author: str = Field(..., description="Author, creator, or source owner")
    category: str = Field(..., description="Document category or topic")
    content: str = Field(..., description="Cleaned text content")
    timestamp: str = Field(..., description="Creation or publication timestamp")
