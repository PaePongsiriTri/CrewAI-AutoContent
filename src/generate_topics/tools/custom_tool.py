import os
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from typing import List
from pyairtable import Api



class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, you agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."

class TopicFormat(BaseModel):
    topic: str = Field(..., description="The main topic")
    description: str = Field(..., description="the description of topic")
    keywords: str = Field(...,description="list of keyword ")

class ListTopics(BaseModel):
    Topics: List[TopicFormat] = Field(..., description="A list of Topic and description")

    def _run(self, Topics) -> str:
        api = Api('pathsN7joE7UizMxS.19cc28a7f900da8312e8c9c8331e8426d7b0654c6df8f5ae2ea48ac609492eac')
        table = api.table('appq3IScb2mngqDMD', 'tbldYUOI16uH10AuM')
        # table.all()
        # print(table.all())
        table.create(Topics)
        return 'success'

# class InsertTopic(BaseModel):
#     api = Api('pathsN7joE7UizMxS.19cc28a7f900da8312e8c9c8331e8426d7b0654c6df8f5ae2ea48ac609492eac')
#     table = api.table('appq3IScb2mngqDMD', 'tbldYUOI16uH10AuM')
#     # table.all()
#     # print(table.all())
#     table.create({"Topic": "Bob","Description":"xxx"})

# api = Api('pathsN7joE7UizMxS.19cc28a7f900da8312e8c9c8331e8426d7b0654c6df8f5ae2ea48ac609492eac')
# table = api.table('appq3IScb2mngqDMD', 'tbldYUOI16uH10AuM')
# table.all()
# print(table.all())
# table.create({"Topic": "Bob","Description":"xxx"})