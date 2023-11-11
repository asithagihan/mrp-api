import boto3


def create_billing_group():
    client = boto3.client("iot")
    response = client.create_billing_group(
        billingGroupName="string",
        billingGroupProperties={"billingGroupDescription": "string"},
        tags=[
            {"Key": "string", "Value": "string"},
        ],
    )


def create_policy():
    client = boto3.client("iot")
    response = client.create_policy(
        policyName="string",
        policyDocument="string",
        tags=[
            {"Key": "string", "Value": "string"},
        ],
    )


def create_device():
    client = boto3.client("iot")
    response = client.create_thing(
        thingName="string",
        thingTypeName="string",
        attributePayload={"attributes": {"string": "string"}, "merge": True | False},
        billingGroupName="string",
    )
