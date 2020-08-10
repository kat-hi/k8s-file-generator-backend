import subprocess
import json


def kubectl(command):
    data = subprocess.check_output(
        "kubectl {0} -o json".format(command), shell=True)
    return json.loads(data)


def _get_ingress_hosts_in_all_namespaces():
    json_data = kubectl("get ingress --all-namespaces")
    host_list = [item['spec']['rules'][0]['host'] for item in json_data['items']]
    print(host_list)
    return host_list


def is_hostname_already_used(hostname):
    current_hosts = _get_ingress_hosts_in_all_namespaces()
    if hostname in current_hosts:
        return False
    else:
        return True
