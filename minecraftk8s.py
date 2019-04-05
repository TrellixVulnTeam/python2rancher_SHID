import requests
import sys
import argparse
import json
import urllib3
def setNewWorkload(workloadName,projectID):
    url = "https://192.168.55.107/v3/project/"+projectID+"/workloads"
    rawPayload =  {
    "containers": [
        {
        "allowPrivilegeEscalation": 'false',
        "environment": {
        "EULA": 'TRUE',
        "SERVER_PORT": '8081'
        },
        "image": 'itzg/minecraft-server',
        "imagePullPolicy": 'Always',
        "initContainer": 'false',
        "name": workloadName,
        "ports": [
        {
        "containerPort": '8081',
        "dnsName": workloadName+'-nodeport',
        "kind": 'NodePort',
        "name": '8081tcp01',
        "protocol": 'TCP',
        "sourcePort": '0',
        "type": '/v3/project/schemas/containerPort'
        }
        ],
        "readOnly": 'false',
        "resources": {
        "type": '/v3/project/schemas/resourceRequirements'
        },
        "restartCount":'0',
        "runAsNonRoot": 'false',
        "stdin": 'true',
        "stdinOnce": 'false',
        "terminationMessagePath": '/dev/termination-log',
        "terminationMessagePolicy": 'File',
        "tty": 'true',
        "type": '/v3/project/schemas/container'
        }
    ],
    "dnsPolicy": 'ClusterFirst',
    "hostIPC": 'false',
    "hostNetwork": "false",
    "hostPID": "false",
    "labels": {
        "workload.user.cattle.io/workloadselector": 'statefulSet-default-'+workloadName
    },
    "name": workloadName,
    "namespaceId": 'default',
    "ownerReferences": [ ],
    "projectId": projectID,
    "publicEndpoints": [ ],
    "readinessGates": [ ],
    "restartPolicy": "Always",
    "scale": 1,
    "schedulerName": "default-scheduler",
    "selector": {
        "matchLabels": {
            "workload.user.cattle.io/workloadselector": "statefulSet-default-"+workloadName
        },
        "type": "/v3/project/schemas/labelSelector"
    },
    "state": "active",
    "statefulSetConfig": {
        "podManagementPolicy": "OrderedReady",
        "revisionHistoryLimit": '10',
        "serviceName": workloadName,
        "strategy": "RollingUpdate"
    },
    "statefulSetStatus": {
        "collisionCount": '0',
        "currentReplicas": '1',
        "observedGeneration": '1',
        "readyReplicas": '1',
        "replicas": '1',
        "type": "/v3/project/schemas/statefulSetStatus",
        "updatedReplicas": '1'
    },
    "sysctls": [ ],
    "terminationGracePeriodSeconds": '30',
    "transitioning": "no",
    "transitioningMessage": "",
    "volumes": [ ],
    "workloadAnnotations": {
        "field.cattle.io/creatorId": "user-k6jnq"
    },
    "workloadLabels": {
        "cattle.io/creator": "norman",
        "workload.user.cattle.io/workloadselector": "statefulSet-default-"+workloadName
    }
    }
    payload = json.dumps(rawPayload)
    ##payload = json.loads(dumpedPayload)
    ##print(payload)
    headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic dG9rZW4tbHFyZHg6NXE2emxmd21iNHF4YjZydm5nOThoazg3N2ZxZGJrNm01Nmt2ZjdwZGRnNGxtbWtjNGpnOHF3",
    'cache-control': "no-cache",
    'Postman-Token': "3925edcb-d2cb-4477-8303-5094ba36886b"
    }
    response = requests.request("POST", url, data=payload, headers=headers,verify=False)
def getWorkload(workloadName,projectID):
    url = "https://192.168.55.107/v3/project/"+projectID+"/workloads/statefulset:default:"+workloadName 
    payload = ""
    headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic dG9rZW4tbHFyZHg6NXE2emxmd21iNHF4YjZydm5nOThoazg3N2ZxZGJrNm01Nmt2ZjdwZGRnNGxtbWtjNGpnOHF3",
    'cache-control': "no-cache",
    'Postman-Token': "3925edcb-d2cb-4477-8303-5094ba36886b"
    }
    response = requests.request("GET", url, data=payload, headers=headers ,verify=False)
   # print(url)
   # print(response)
    return response.text