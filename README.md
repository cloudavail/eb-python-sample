# Objective

To create a basic Elastic Beanstalk stack in CloudFormation that:

1. Utilizes a codebase for running a basic webserver.
2. Utilizes the same codebase for running a job on a regular schedule.

# Validate Stack
`aws cloudformation validate-template --template-body file://infra/eb-python-sample.yaml`

# Create a eb-python-sample Stack
`aws cloudformation create-stack --stack-name eb-python-sample --template-body file://infra/eb-python-sample.yaml`

# Update a eb-python-sample Stack
`aws cloudformation update-stack --stack-name eb-python-sample --template-body file://infra/eb-python-sample.yaml`

# Delete a eb-python-sample Stack
`aws cloudformation delete-stack --stack-name eb-python-sample`
