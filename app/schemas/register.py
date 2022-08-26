from pydantic import BaseModel, ValidationError, validator


class RegisterSchema(BaseModel):
    number: str
    created_by: str

    @validator("number")
    def lengthvalidation(cls, v):
        if len(v) > 14:
            raise ValueError(
                "The maximum length of the number is 14 characters"
            )
        return v.strip()
