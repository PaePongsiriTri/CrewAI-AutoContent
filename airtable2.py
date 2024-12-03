import requests
import json


def get_record():
    url = "https://api.airtable.com/v0/appq3IScb2mngqDMD/tbldYUOI16uH10AuM"
    params = {}
    headers = { "Authorization" : "Bearer pathsN7joE7UizMxS.19cc28a7f900da8312e8c9c8331e8426d7b0654c6df8f5ae2ea48ac609492eac",}
    # Make a get request with the parameters.
    response = requests.get(url, params=params, headers=headers)

    if response.status_code==200:
        a =response.json()
        print(a)

def create_record():
    url =  "https://api.airtable.com/v0/appq3IScb2mngqDMD/tbldYUOI16uH10AuM"
    headers = { "Authorization" : "Bearer pathsN7joE7UizMxS.19cc28a7f900da8312e8c9c8331e8426d7b0654c6df8f5ae2ea48ac609492eac",
    "Content-Type":"application/json"}
    data = {
        "fields": {
            "Topic": "333 Post St",
            "Description": "Union Square"
        }
    }


    response = requests.post(url,headers=headers, json=data )
    print(response.content)

def create_multirecord(b):
    url = "https://api.airtable.com/v0/appq3IScb2mngqDMD/tbldYUOI16uH10AuM"
    headers = {
        "Authorization": "Bearer pathsN7joE7UizMxS.19cc28a7f900da8312e8c9c8331e8426d7b0654c6df8f5ae2ea48ac609492eac",
        "Content-Type": "application/json"
    }
    data = {
        "records": [{  # Wrap the fields in a records array
            "fields": {
                "Topic": "333 Post St",
                "Description": "Union Square"
            }
        }
        ,
            {
              "fields": {"Topic": "332 Post St",
                "Description": "Union Square"
              }
            }
        ]
    }
    response = requests.post(url,headers=headers, json=b )
    print(response.content)
# create_multirecord()


def convert_topics_to_records(data):
    # Initialize the result structure
    result = {"records": []}
    
    # Iterate through the topics and construct the new format
    for item in data["Topics"]:
        record = {
            "fields": {
                "Topic": item["topic"],
                "Description": item["description"],
                "keywords": item["keywords"]
            }
        }
        result["records"].append(record)
    
    return result

input_data = {"Topics":[{"topic":"Complimentary Report: Gartner® Names Zoho as a Visionary in 2023 Gartner® Magic Quadrant™ for Sales Force Automation Platforms","description":"Analysis on Zoho's standing in the industry as recognized by Gartner, exploring its innovative CRM solutions.","keywords":""},{"topic":"Creating a 360-Degree View of the Customer with Zoho CRM and Zoho Desk","description":"Utilize Zoho CRM and Zoho Desk to gain comprehensive insights into customer interactions and improve personalizations.","keywords":""},{"topic":"Maximizing the Value of Zoho CRM Implementations – Insights for CIOs and CTOs","description":"Strategic insights for C-level executives on optimizing the benefits of Zoho CRM implementations in businesses.","keywords":""},{"topic":"Selecting the Right CRM for Sales Success: Why Zoho CRM is a Top Choice for SMBs","description":"Discussing how Zoho CRM caters specifically to the needs of Small and Medium-sized Businesses and enhances sales processes.","keywords":""},{"topic":"Transform Your Business: Seamlessly Integrate Zoho CRM with ServiceNow for Ultimate Efficiency","description":"An exploration of integrating Zoho CRM with ServiceNow to improve operational workflows across departments.","keywords":""},{"topic":"Fostering Client Relationships: How Zoho CRM Turns Customers into Friends","description":"Techniques for leveraging Zoho CRM features to enhance client relationships and improve customer loyalty.","keywords":""},{"topic":"Zoho CRM vs. Salesforce: Which CRM Platform is Right for Your Business?","description":"A comparative analysis of Zoho CRM and Salesforce, detailing strengths, weaknesses, and suitable business types.","keywords":""},]}
# input_data = {"Topics":[{"topic":"Client Script for Subform Row Extraction in Zoho CRM","description":"A technical guide on using client scripts to manage data within Zoho CRM's subforms effectively.","keywords":""},{"topic":"Zoho Inventory Management: Streamlining Your Business’s Operations","description":"How best practices in Zoho Inventory can enhance your business’s supply chain and operational efficiency.","keywords":""},{"topic":"Boost Your Sales through Email Marketing with Zoho Campaigns","description":"Strategies for creating effective email campaigns using Zoho Campaigns and leveraging CRM data for better targeting.","keywords":""},{"topic":"Unlock Seamless Customer Communication with ControlHippo: WhatsApp-Zoho CRM Integration","description":"Best practices for integrating WhatsApp with Zoho CRM to streamline customer communications and support.","keywords":""},{"topic":"Enhancing Customer Experience through Omni-channel Communication with Zoho CRM","description":"Discussing the importance of multi-channel strategies in Zoho CRM to improve customer engagement.","keywords":""},{"topic":"Harnessing Rich Text Fields and Deluge Functions in Zoho CRM","description":"A guide to utilizing rich text fields and advanced Deluge functions to enhance data management in Zoho CRM.","keywords":""},{"topic":"The Importance of Subforms in Zoho CRM: A Guide for CRM Admins","description":"Utilizing subforms to structure data efficiently in Zoho CRM and improve user experience.","keywords":""},{"topic":"The Top 10 Reasons For CRM Failures and How Zoho Can Prevent Them","description":"Identifying common pitfalls of CRM implementations and how to effectively navigate them using Zoho.","keywords":""},{"topic":"Zoho Creator: A Quick Start Guide for Business Owners","description":"Essential tips and knowledge to begin using Zoho Creator for streamlining processes and building custom applications.","keywords":""},{"topic":"Maximizing Property Sales: A Guide to Using Zoho CRM for Real Estate","description":"Tailored strategies for real estate agents on how to utilize Zoho CRM to enhance property sales management.","keywords":""}]}


a = convert_topics_to_records(input_data)
create_multirecord(a)


# Print the content of the response
# print(response.content)