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

class SalesPipeline(Flow):
    @start()
    def fetch_leads(self):
        # Pull our leads from the database
        leads = [
            {
                "topic": "ZohoCRM",
                "number_of_topics": 2,
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
    def write_content(self, ListofTopics):
        scored_leads = [lead.to_dict() for lead in ListofTopics]
        print(scored_leads[0]['Topics'])
        content = ContentWriter().crew().kickoff_for_each(scored_leads[0]['Topics'])
        # print(content)
        return content
    # @listen(score_leads)
    # def store_leads_score(self, scores):
    #     # Here we would store the scores in the database
    #     return scores

    # @listen(score_leads)
    # def filter_leads(self, scores):
    #     return [score for score in scores if score['lead_score'].score > 70]

    # @listen(filter_leads)
    # def write_email(self, leads):
    #     scored_leads = [lead.to_dict() for lead in leads]
    #     emails = email_writing_crew().crew().kickoff_for_each(scored_leads)
    #     return emails

    # @listen(write_email)
    # def send_email(self, emails):

def run():
    
    flow = SalesPipeline()
    flow.kickoff()
    
