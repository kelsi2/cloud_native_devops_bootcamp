# Week 2: Scripting Like a Developer

The code found in this repository is to learn how to script like a developer.

## WIP

Code is a Work in Progress (WIP) and readme will be updated when ready

## PowerShell Code

PowerShell code is for creating a Resource Group in Azure

### How to Use the PowerShell Code

`New-ResourceGroup` function is found under the `PowerShell` directory and can be used as a reusable function. A user has the ability to pass in parameters at runtime to ensure they can re-use the script at any point for any environment.

## Python Code

Python code is for creating an S3 bucket in AWS

### How to Use the Python Code

`s3bucket.py` script is designed to be re-used at any point for any environment. No hard-coded values.

## Examples

```powershell
function New-ResourceGroup {
  [cmdletbinding(SupportsShouldProcess)]

  param(
    [parameter(Mandatory)]
    [string]$rgName,

    [parameter(Mandatory)]
    [string]$location
  )

  $params = @{
    'Name'     = $rgName
    'Location' = $location
  }

  if ($pscmdlet.ShouldProcess('location')) {
    New-AzResourceGroup @params
  }
}

New-ResourceGroup -rgName 'cloudskills' -location 'eastus2'
```

```python
import sys
import boto3

try:
    def main():
        create_s3bucket(bucket_name, region=None)

except Exception as e:
    print(e)


def create_s3bucket(bucket_name, region=None):
    region = sys.argv[2]
    if region is None:
        s3_bucket = boto3.client(
            's3',
        )
        bucket = s3_bucket.create_bucket(
            Bucket=bucket_name,
            ACL='private',
        )
    else:
        s3_bucket = boto3.client(
            's3',
            region_name=region
        )
        location = {'LocationConstraint': region}
        bucket = s3_bucket.create_bucket(
            Bucket=bucket_name,
            ACL='private',
            CreateBucketConfiguration=location
        )

    print(bucket)


bucket_name = sys.argv[1]

if __name__ == '__main__':
    main()

python s3bucket.py 'cloudskills3bucket'
```

## Testing

Both PowerShell and Python code have unit tests available to ensure desired outcomes, including values and types, are accurate.
Tests can be found in the `PowerShell` and `Python` directories.

## Contributors

1. Kelsi Proulx
