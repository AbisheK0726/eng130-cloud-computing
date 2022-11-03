# Setup Connection to S3

![S3](images/AWS-S3.png)

## Install Python3 and PIP

```bash
sudo apt-get install python3
sudo apt-get install python3-pip
alias python=python3
python --version
```

## Install AWS CLI

```bash
sudo pip install awscli
```

## Configure AWS CLI

**_NOTE_**: DO NOT SHARE YOUR AWS CREDENTIALS WITH ANYONE

```bash
aws configure
Enter AWS Access Key ID: `AWSACCESSENG130EXAMPLE`
Enter AWS Secret Access Key: `spArTGloBAl/ENG130DO/EXAMPLEKEY`
Enter Default region name: `eu-west-1`
Enter Default output format: `json`
```

## Test AWS CLI

You should see a list of buckets

```bash
aws s3 ls
```

## S3 Commands

### Create a Bucket

```bash
aws s3 mb s3://bucket-name
```

### Upload a file to S3

```bash
aws s3 cp <path/to/file> s3://bucket-name
```

### Download a file from S3

```bash
aws s3 cp s3://bucket-name/file-name.txt new-file-name.txt
```

### Delete a file from S3

```bash
aws s3 rm s3://bucket-name/file-name.txt
```

### Delete a bucket

```bash
aws s3 rb s3://bucket-name
```