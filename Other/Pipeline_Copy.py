from pipedrive import Pipedrive
pipedrive = Pipedrive('') #Api key of the account requiring the new pipelines


Stage_names_AD = ['Leads - Application Started','App Received - Doc','Educated Sit Down','Mortgage Prep',
                'Submitted to Lender','Pre-Approvals','Active Approval','Broker Complete - Lawyer/Compliance',
                'Funded']

Stage_names_PF = ['30 Days Post Funding','4 Years until Maturity','3 Years until Maturity','2 Years until Maturity',
                '1 Year until Maturity','180 Days until Maturity','90 Days until Maturity', '30 Days until Maturity']

#Create the first pipeline Active Deals
pipedrive.pipelines({ 
        'name': 'Active Deals',
        'active': 1,
        'order_nr':0 
}, method= 'POST')

#Fill Active Deals with stages
for name in Stage_names_AD:
    pipedrive.stages({
        'name': name,
        'pipeline_id': 2
    }, method= 'POST')

#Create the second pipeline Post Funding
pipedrive.pipelines({
        'name': 'Post Funding',
        'active': 1,
        'order_nr':1 
}, method= 'POST')

#Fill Post Funding with stages
for name in Stage_names_PF:
    pipedrive.stages({
        'name': name,
        'pipeline_id': 3
    }, method= 'POST')


