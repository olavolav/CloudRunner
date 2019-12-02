# CloudRunner

CloudRunner is a prototype of a CLI application to run a series of tasks on the AWS EC2 cloud.

The use case it was built for is to run hyperparameter scans for machine learning models, on as many EC2
instances as you like in parallel.

Please note that EC2 is a paid service, so if you are not in
[the AWS free tier](https://aws.amazon.com/en/free/) then using CloudRunner will incur costs.


## Setup

First you need to install the dependencies of CloudRunner:
```
pip3 install -r requirements.txt
```
