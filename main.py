from fastapi import FastAPI, Query
from pydantic import BaseModel, Field, ValidationError, validator
import typing as t
import logging
import re
import error_api

app = FastAPI()
logger = logging.getLogger("FastAPI bhp")

logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
logging.basicConfig(level=logging.NOTSET)


class BodyUploadUnzipFiles(BaseModel):
    type_file: str = Field(default=None, title="Define the name of project we want to extract")
    date: str = Field(default=None, title="Define the date of project when we want to extract")

    @validator('type_file')
    def greater_than_four_character(cls, value):
        if len(value) < 4:
            raise error_api.GreaterThanFourNumber('must be greater than 4 characters')
        return value

    @validator('type_file')
    def is_in_lowercase(cls, value):
        if not value.islower():
            raise error_api.LowerCaseError(value)
        return value

    @validator('date')
    def date_matching(cls, value):
        pattern = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
        if not pattern.match(value):
            raise error_api.DateMatchingError("must follow the format YYYY-MM-DD")
        return value


@app.get("/bhp/upload/unzip",
         summary="Unzip and upload bhp data",
         description="Unzip and upload bhp data in the bucket "
                     "sknow-gcs-landing-eu-dv/Econnect/bhp/type_bhp/date/json/name_of_file",
         tags=["bhp"]
         )
def get_upload_unzip_file(type_bhp: str = Query(min_length=4, max_length=10, title="Project from bhp string",
                                                description="Define the name of project in bhp we want to extract",
                                                regex=r"[A-Za-z]+"),
                          date: str = Query(min_length=10, title="Date of extration",
                                            description="Define the date of when the extract have been executed. "
                                                        "format YYYY-MM-DD",
                                            regex=r"[0-9]{4}-[0-9]{2}-[0-9]{2}")) -> t.Dict:
    """
    unzip and upload file from sknow-gcs-landing-eu-dv/Econnect/bhp/type_bhp/date/zip/name_of_file to sknow-gcs-landing-eu-dv/Econnect/bhp/type_bhp/date/json/name_of_file""

    - **type_bhp**: name of project in bhp we want to extract
    - **date**: date of when the extract have been executed. format YYYY-MM-DD
    """
    return {"code": "done"}


@app.post("/bhp/upload/unzip",
          summary="Unzip and upload bhp data",
          description="Unzip and upload bhp data in the bucket "
                      "sknow-gcs-landing-eu-dv/Econnect/bhp/type_bhp/date/json/name_of_file",
          tags=["bhp"]
          )
def post_upload_unzip_file(event_request: BodyUploadUnzipFiles) -> t.Dict:
    """
    unzip and upload file from sknow-gcs-landing-eu-dv/Econnect/bhp/type_bhp/date/zip/name_of_file to sknow-gcs-landing-eu-dv/Econnect/bhp/type_bhp/date/json/name_of_file""

    - **type_bhp**: name of project in bhp we want to extract
    - **date**: date of when the extract have been executed. format YYYY-MM-DD
    """
    return {"code": "done"}
