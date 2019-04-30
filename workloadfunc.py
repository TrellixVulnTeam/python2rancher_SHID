### Rancher Create workload from json workload template ###
#Module to manage https requests
import requests
import sys
import json
#Module to manage HTTPS python config
import urllib3
#Custom librarie to manage Minecraft workloads on a given k8s cluster managed by Rancher
import python2rancher as rancher
import os
import re
urllib3.disable_warnings()

def create(workloadName):
    #Get Rancher API cred from system variable enviroments
    headers = {
        'Content-Type': "application/json",
        'Authorization': os.environ.get('RancherAuth'),
        'cache-control': "no-cache",
        'Postman-Token': os.environ.get('RancherToken')
    }
    RancherObj =  {
        'rancherEndpoint':os.environ.get('RancherEndpoint'),
        'rancherClusterID':os.environ.get('RancherClusterID'),
        'rancherProjectID':os.environ.get('RancherProjectID'),
        'workloadTemplate':workloadName,
        'headers': headers
    }
    #Set HTTP Header for Rancher API Calls
    isStorageClass = rancher.getStorageClass(RancherObj)
    workloads = rancher.getAllWorkloadName(RancherObj)
    #Get A list of actual workload matching the template workload requested using a regex filter
    regex = re.compile(RancherObj['workloadTemplate'])
    filteredList = list(filter(regex.match, workloads))
    
    if not filteredList:
        firstOccurence = 0
    else:
        filteredList.sort(reverse=True)
        if  isStorageClass == 404:
            print('Storage Class storageclass'+workloadName+' not found , creating ... ')
            rancher.setNewStorageClass(RancherObj)
        firstOccurence =int(re.findall(r'\d', str(filteredList[0]))[0])
    workload = workloadName+str(firstOccurence+1)
    rancher.setNewPVC(RancherObj,workload)
    newWorkload = rancher.setNewWorkload(RancherObj,workload)
    print(workloadName+str(firstOccurence+1))
    #newWorkload = rancher.getWorkload(RancherObj,workload)
    return workloadName+str(firstOccurence+1)#+"created, the service is available on "+(str(json.loads(newWorkload.content)))

                
def remove(workloadName):
    #Get Rancher API cred from system variable enviroments
    headers = {
        'Content-Type': "application/json",
        'Authorization': os.environ.get('RancherAuth'),
        'cache-control': "no-cache",
        'Postman-Token': os.environ.get('RancherToken')
    }
    RancherObj =  {
        'rancherEndpoint':os.environ.get('RancherEndpoint'),
        'rancherClusterID':os.environ.get('RancherClusterID'),
        'rancherProjectID':os.environ.get('RancherProjectID'),
        'workloadTemplate':workloadName,
        'headers': headers
    }
       #Set HTTP Header for Rancher API Calls
    return rancher.removeWorkload(RancherObj,workloadName)

def get(workloadName):
      #Get Rancher API cred from system variable enviroments
    headers = {
        'Content-Type': "application/json",
        'Authorization': os.environ.get('RancherAuth'),
        'cache-control': "no-cache",
        'Postman-Token': os.environ.get('RancherToken')
    }
    RancherObj =  {
        'rancherEndpoint':os.environ.get('RancherEndpoint'),
        'rancherClusterID':os.environ.get('RancherClusterID'),
        'rancherProjectID':os.environ.get('RancherProjectID'),
        'workloadTemplate':workloadName,
        'headers': headers
    }
       #Set HTTP Header for Rancher API Calls
    return rancher.getWorkload(RancherObj,workloadName)