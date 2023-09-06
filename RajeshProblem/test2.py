import json
import time

def main():
    merge_replicas_json('replicas.json', 'iam_replicas.json')

def merge_replicas_json(replicas_file1, replicas_file2):
    """merge two replicas files"""

    rf2 = open(replicas_file2, )
    rf2_data = json.load(rf2)
    rf2_deployment = [i['deploymentName'] for i in rf2_data]

    rf1 = open(replicas_file1, )
    rf1_data = json.load(rf1)
    rf1_deployment = [i['deploymentName'] for i in rf1_data]

    final_result = []
    if rf1_data == rf2_data:
        print("no changes")
    else:
        change_status = False
        for data in rf2_data:
            if data['deploymentName'] in rf1_deployment:
                for k in rf1_data:
                    if data['deploymentName'] == k['deploymentName']:
                        k['resources'] = data['resources']
                        change_status = True
        if change_status:
            json_object = json.dumps(rf1_data, indent=4)
            with open(replicas_file1, "w") as outfile:
                outfile.write(json_object)

if __name__ == "__main__":
    main()