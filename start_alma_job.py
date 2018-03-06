#!/home/alma/anaconda3/bin/python

api_key = '<YOUR API KEY HERE>'
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import sys

def start_alma_jobs(job_id):
    ## the parameter 'job_id') is the Alma job number of the job. 
    ## first we need to get the job object from Alma. 
    url = 'https://api-eu.hosted.exlibrisgroup.com/almaws/v1/conf/jobs/{job_id}'.replace('{job_id}',quote_plus(job_id))
    queryParams = '?' + urlencode({ quote_plus('apikey') : api_key  })
    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()
    #print(response_body)
    ## With the job object stored in the respons_body variable, we send the command to start the job, passing the job_id and job object.
    url = 'https://api-eu.hosted.exlibrisgroup.com/almaws/v1/conf/jobs/{job_id}'.replace('{job_id}',quote_plus(job_id))
    queryParams = '?' + urlencode({ quote_plus('op') : 'run' ,quote_plus('apikey') : api_key  })
    values  = response_body
    headers = {  'Content-Type':'application/xml'  }
    request = Request(url + queryParams
    , data=values
    , headers=headers)
    request.get_method = lambda: 'POST'
    response_body = urlopen(request).read()
    return(response_body)

if len(sys.argv) == 2:

    job_id = sys.argv[1]
    print('starting job: ',job_id)
    start_alma_jobs(job_id)
else:
    print('\nPlease specify a job_id as a command line argument')
    print('\tex: python start_alma_job.py S26054811740001121\n')


