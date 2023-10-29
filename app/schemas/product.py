from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=3, max_length=20)
    category: str = Field(min_length=3, max_length=15)
    description: str = Field(min_length=5, max_length=50)
    rating: float = Field(ge=0, le=5)
    cost: float = Field(ge=0)

    # example of the schema

    model_config = {
        "json_schema_extra": {
            "examples" : [
                {
                    "id": 1,
                    "name": "mouse",
                    "category": "tech",
                    "description": "Wireless mouse for PC",
                    "rating": 4.5,
                    "cost": 5
                }
            ]
        }
    }
