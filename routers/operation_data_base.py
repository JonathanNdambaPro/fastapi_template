from fastapi import APIRouter, Query
import typing as t
import random
import string

router = APIRouter(
    prefix="/database",
    tags=["database"]
)

@router.get("/database/trasaction",
         summary="get information from database",
         description="Unzip and upload bhp data in the bucket "
                     "sknow-gcs-landing-eu-dv/Econnect/bhp/type_bhp/date/json/name_of_file",
         response_description="response to signal the operaton have been successfully achieved"
         )
def get_transaction(type_bhp: str = Query(min_length=4, max_length=10, title="Project from bhp string",
                                                description="Define the name of project in bhp we want to extract",
                                                regex=r"[A-Za-z]+",
                                                alias="transaction id"),
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


def get_keys_auth():
    letters = string.ascii_lowercase
    key = "".join(random.choice(letters) for i in range(10)) 
    return {"key": key}




