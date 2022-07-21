from pipedrive import Pipedrive

pipedrive = Pipedrive('') #Enter API key of account 

DF_name_list = ['Street Number 2', 'Unit Number 2','Street Name 2','Street Type 2','City 2','Province 2','Country 2','Postal Code 2','Employer 2', 'Occupation 2','Address type 2',
'Street Number 3', 'Unit Number 3','Street Name 3','Street Type 3','City 3','Province 3','Country 3','Postal Code 3','Employer 3', 'Occupation 3','Address type 3']
Field_Type_list = []
for x in range(len(DF_name_list)):
    pipedrive.personFields({'name':DF_name_list[x],'field_type':'text','add_visible_flag':True},method='POST')
