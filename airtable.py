import os
from pyairtable import Api

api = Api('pathsN7joE7UizMxS.19cc28a7f900da8312e8c9c8331e8426d7b0654c6df8f5ae2ea48ac609492eac')
table = api.table('appq3IScb2mngqDMD', 'tbldYUOI16uH10AuM')
table.all()
print(table.all())
table.create({"Topic": "Bob","Description":"xxx"})