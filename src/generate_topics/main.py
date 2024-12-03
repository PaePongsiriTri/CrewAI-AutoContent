#!/usr/bin/env python
import sys
import warnings

from generate_topics.crew import GenerateTopics,ContentWriter

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
from crewai import Flow
from crewai.flow.flow import listen, start

import requests

def convert_topics_to_records(data):
    # Initialize the result structure
    result = {"records": []}
    
    # Iterate through the topics and construct the new format
    for item in data["Topics"]:
        record = {
            "fields": {
                "Topic": item["topic"],
                "Description": item["description"]
                # "keywords": item["keywords"]
            }
        }
        result["records"].append(record)
    
    return result

def create_record_airtable(data):
    url =  "https://api.airtable.com/v0/appq3IScb2mngqDMD/tbldYUOI16uH10AuM"
    headers = { "Authorization" : "Bearer pathsN7joE7UizMxS.19cc28a7f900da8312e8c9c8331e8426d7b0654c6df8f5ae2ea48ac609492eac",
    "Content-Type":"application/json"}
    # data = {
    #     "fields": {
    #         "Topic": "333 Post St",
    #         "Description": "Union Square"
    #     }
    # }
    response = requests.post(url,headers=headers, json=convert_topics_to_records(data))
    # print(response.json())
    return response.json()


class SalesPipeline(Flow):
    @start()
    def fetch_leads(self):
        # Pull our leads from the database
        leads = [
            {
                "topic": "ZohoCRM",
                "number_of_topics": 100,
            },
        ]
        return leads

    @listen(fetch_leads)
    def generate_topics(self, leads):
        ListofTopics = GenerateTopics().crew().kickoff_for_each(leads)
        self.state["ListofTopics"] = ListofTopics
        # ListofTopics = {"Topics":[{"topic":"Engineering Leadership in Tech","description":"Explore the journey of João Moura as an Engineering Manager at Clearbit, focusing on his leadership style, coaching methods for engineering teams, and contributions in tech innovation.","keywords":"Engineering, Leadership"},{"topic":"Open Source Contributions and Software Development","description":"A look into João Moura’s engagement with the open-source community through his GitHub projects, significant contributions, and the impact of open-source software on modern engineering practices.","keywords":"Open Source, Software Development"},]}
        return ListofTopics

    
    @listen(generate_topics)
    def store_topic(self, ListofTopics):
        # print(ListofTopics)
        # print(ListofTopics)
        scored_leads = [lead.to_dict() for lead in ListofTopics]
        # print(scored_leads)
        response = create_record_airtable(scored_leads[0])
        # Here we would store the scores in the database
        # print(response)
        return response

    # @listen(generate_topics)
    # def write_content(self, ListofTopics):
    #     scored_leads = [lead.to_dict() for lead in ListofTopics]
    #     content = ContentWriter().crew().kickoff_for_each(scored_leads[0]['Topics'])
    #     return content

    # @listen(write_content)
    # def store_content(self, contents):
    #     print('store content----------------------------------------------')
    #     print(contents)
    #     content_list = [content.to_dict() for content in contents]
    #     print(content_list)
        # return content

def run():
    
    flow = SalesPipeline()
    flow.kickoff()
    
