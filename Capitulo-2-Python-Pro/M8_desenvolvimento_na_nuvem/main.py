from __future__ import print_function

from troposphere import ec2
from troposphere import Tags, ImportValue
from troposphere import Template

t = Template() #objeto do nosso modelo

ec2_learncf_1a = ec2.Instance("ec2LearnCf1a")
ec2_learncf_1a.ImageId = "ami-e487179d"                
ec2_learncf_1a.InstanceType = "t2.micro"

ec2_learncf_1a.SubnetId = ImportValue("learncf-subnet-netLearnCf1a")
ec2_learncf_1a.Tags = Tags(
        Name="learncf",
        Comment="Learning CloudFormation and Troposphere")

t.add_resource(ec2_learncf_1a)

with open('learncf-ec2.yaml', 'w') as f:
    f.write(t.to_yaml())