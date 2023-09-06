import boto3
import time
import sys
import csv
import pandas as pd  
import datetime

ec2 = boto3.resource('ec2', region_name='us-east-1')
client = boto3.client('ec2', region_name='us-east-1')
waiter = client.get_waiter('snapshot_completed')
waiter.config.delay =60
waiter.config.max_attempts = 180
volume_waiter = client.get_waiter('volume_available')

def read_csv(csv_file):
    with open(csv_file, mode = 'r') as infile:
        reader = csv.reader(infile)
        next(reader)
        instance_info = {rows[0]:rows[1] for rows in reader}
        return instance_info

def write_csv(created_snapshot):
    df = pd.DataFrame(created_snapshot)
    df.to_csv('snapshot_created_{0}.csv'.format(str(datetime.datetime.now().date())))

def create_snapshot(instance_info):
    created_snapshot = dict()
    for name, instace_id in instance_info.items():
        instance = ec2.Instance(instace_id)
        volumnes = instance.volumes.all()
        successful_snapshots = dict()
        for volume in volumnes:
            try:
                response = client.create_snapshot(Description= 'Instance id {}'.format(instance) + 'volume id is {}'.format(volume.id), VolumeId= volume.id,DryRun= False)
                snapshot_id = response['SnapshotId']
                waiter.wait(SnapshotIds=[snapshot_id,])
                client.create_tags(Resources=[snapshot_id,],Tags=[{'Key': 'Name', 'Value': name}])
                status_code = response['ResponseMetadata']['HTTPStatusCode']
                if status_code == 200:
                    successful_snapshots[volume.id] = snapshot_id
                    created_snapshot.update({name : instace_id})
            except Exception as e:
                print (e)
    return created_snapshot
if __name__ == '__main__':
    file_name = 'instance.csv'
    instance_info = read_csv(file_name)
    created_snapshot = create_snapshot(instance_info)
    write_csv(created_snapshot)

