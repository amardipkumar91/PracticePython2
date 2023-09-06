import boto3
import time
import sys
ec2 = boto3.resource('ec2', region_name='us-east-1')
client = boto3.client('ec2', region_name='us-east-1')
waiter = client.get_waiter('snapshot_completed')
waiter.config.delay =60
waiter.config.max_attempts = 180
volume_waiter = client.get_waiter('volume_available')
Instance_ID = str(sys.argv[1])
instance = ec2.Instance(Instance_ID)
volumes = instance.volumes.all()

#Instance Volume Info like size and device name
encrypted_vol, unecrypted_vol = 0, 0
volumes_info = dict()
for volume in volumes:
    volumes_info[volume.id] = [volume.size, volume.attachments[0]['Device'], volume.encrypted]
    if volume.encrypted:
        encrypted_vol = encrypted_vol + 1
    elif not volume.encrypted:
        unecrypted_vol = unecrypted_vol + 1
    else:
        pass

if len(volumes_info) == unecrypted_vol:
    print '*'*100
    print 'All {} volumes of Instance {} are unencrypted, so we are encrypting them'.format(unecrypted_vol, Instance_ID)
    print '*'*100
else:
    print '*'*100
    print "Total {} volumes are attached to Instance {}, {} are encrypted and {} are unencrypted.\nSO PLEASE CHECK IT AT YOUR END".format(len(volumes_info), Instance_ID, encrypted_vol, unecrypted_vol)
    print '*'*100
    exit()

print '*'*100
print 'VOLUME INFO FOR INSTANCE {}'.format(Instance_ID)
print volumes_info
print '*'*100

successful_snapshots = dict()
for volume in volumes:
    try:
        response = client.create_snapshot(Description= 'Instance id {}'.format(instance) + 'volume id is {}'.format(volume.id), VolumeId= volume.id, DryRun= False)
        snapshot_id = response['SnapshotId']
        waiter.wait(SnapshotIds=[snapshot_id,])
        status_code = response['ResponseMetadata']['HTTPStatusCode']
        if status_code == 200:
            successful_snapshots[volume.id] = snapshot_id
    except Exception as e:
        exception_message = "There was error in creating snapshot " + volume.id + " with volume id "+volume.id+" and error is: \n" + str(e)
        print exception_message
print '*'*100
print 'SUCCESFUL SNAPSHOTS FOR INSTANCE {}'.format(Instance_ID)
print successful_snapshots
print '*'*100

#Create Encrypted Snapshots
successful_encrypted_snapshots = dict()
for snapshot in successful_snapshots:
    try:
       response = client.copy_snapshot(Description='Snapshot copied from {}'.format(successful_snapshots[snapshot]), DestinationRegion='us-east-1', SourceRegion='us-east-1', SourceSnapshotId=successful_snapshots[snapshot], Encrypted=True)
       snapshot_encrypted_id = response['SnapshotId']
       waiter.wait(SnapshotIds=[snapshot_encrypted_id,])
       status_code = response['ResponseMetadata']['HTTPStatusCode']
       if status_code == 200:
            successful_encrypted_snapshots[successful_snapshots[snapshot]] = snapshot_encrypted_id
    except Exception as e:
        exception_message = "There was error in creating encrypted snapshot " + successful_snapshots[snapshot]  + str(e)
        print exception_message
print '*'*100
print 'SUCCESFUL ENCRYPTED SNAPSHOTS FOR INSTANCE {}'.format(Instance_ID)
print successful_encrypted_snapshots
print '*'*100

#Create Volume from sanpshot
successful_encrypted_volumes = dict()
for snapshot in successful_encrypted_snapshots:
    try:
        response = client.create_volume(AvailabilityZone='us-east-1a', SnapshotId=successful_encrypted_snapshots[snapshot], VolumeType='gp2', Encrypted=True)
        volume_encrypted_id = response['VolumeId']
        volume_waiter.wait(VolumeIds=[volume_encrypted_id,])
        status_code = response['ResponseMetadata']['HTTPStatusCode']
        if status_code == 200:
            successful_encrypted_volumes[successful_encrypted_snapshots[snapshot]] = [volume_encrypted_id, response['Size'], response['SnapshotId']]
    except Exception as e:
        exception_message = "There was error in creating encrypted volume " +successful_encrypted_snapshots[snapshot]  + str(e)
        print exception_message

print '*'*100
print 'SUCCESFUL ENCRYPTED VOLUME FOR INSTANCE {}'.format(Instance_ID)
print successful_encrypted_volumes
print '*'*100


#Detach All ebs volume from an instance
successfully_detached_volumes = dict()
for volume in volumes_info:
    try:
        response = client.detach_volume(Device=volumes_info[volume][1], Force=False, InstanceId=Instance_ID, VolumeId=volume)
        volume_waiter.wait(VolumeIds=[volume,])
        status_code = response['ResponseMetadata']['HTTPStatusCode']
        if status_code == 200:
            successfully_detached_volumes[volume] = [Instance_ID, volumes_info[volume][1]]
    except Exception as e:
        exception_message = "There was error in detaching volume " + volume + "from instacne " + Instance_ID + str(e)
        print exception_message

print '*'*100
print 'SUCESSFULY DETACHTED VOLUMES OF INSTANCE {}'.format(Instance_ID)
print successfully_detached_volumes
print '*'*100

#Attach a volume from ec2 instance
volume_in_use_waiter = client.get_waiter('volume_in_use')
successful_attached_volumes = dict()
for volume in volumes_info:
    for newvolume in successful_encrypted_volumes:
        if volumes_info[volume][0] == successful_encrypted_volumes[newvolume][1]:
            try:
                response = response = client.attach_volume(Device=volumes_info[volume][1], InstanceId=Instance_ID, VolumeId=successful_encrypted_volumes[newvolume][0])
                volume_in_use_waiter.wait(VolumeIds=[successful_encrypted_volumes[newvolume][0],])
                status_code = response['ResponseMetadata']['HTTPStatusCode']
                if status_code == 200:
                    successful_attached_volumes[successful_encrypted_volumes[newvolume][0]] = [response['Device'], response['InstanceId'], response['State']]
            except Exception as e:
                exception_message = "There was error in attaching volume " + successful_encrypted_volumes[newvolume][0] + "to instacne " + Instance_ID + str(e)
                print exception_message
print '*'*100
print 'SUCESSFULY ATTACHTED VOLUMES OF INSTANCE {}'.format(Instance_ID)
print successful_attached_volumes
print '*'*100
