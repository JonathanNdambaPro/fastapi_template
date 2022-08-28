from fastapi import APIRouter
from pydantic import BaseModel, Field
import typing as t


router = APIRouter(
    prefix="/gcs",
    tags=["gcs"]
)

class BodyUploadGcs(BaseModel):
    buckect: str = Field(default=None, title="Define the name of project we want to extract")
    prefixe: str = Field(default=None, title="Define the date of project when we want to extract")
    suffixe: str = Field(default=None, title="Define the date of project when we want to extract")


@router.post("/upload/unzip",
          summary="Unzip and upload bhp data",
          description="Unzip and upload bhp data in the bucket "
                      "sknow-gcs-landing-eu-dv/Econnect/bhp/type_bhp/date/json/name_of_file",
          tags=["bhp"]
          )
def post_upload_unzip_file(event_request: BodyUploadGcs) -> t.Dict:
    """
    unzip and upload file from sknow-gcs-landing-eu-dv/Econnect/bhp/type_bhp/date/zip/name_of_file to sknow-gcs-landing-eu-dv/Econnect/bhp/type_bhp/date/json/name_of_file""

    - **type_bhp**: name of project in bhp we want to extract
    - **date**: date of when the extract have been executed. format YYYY-MM-DD
    """
    return {"code": "done"}