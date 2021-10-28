## Pre-requirements: 

* vlocity commands installed - find instructions [here](https://github.com/vlocityinc/vlocity_build)

## Installing from pypi and running locally

1. Setting up your excel file

Refer to the attached excel file in the repo. There are 3 columns - ComponentType, ComponentName, ComponentId (keep them as it is) and sheetName as 'CTSheet' (you can change it but then chnage the main command with the updated sheet name in Sec. 2)

2. In your cmd/terminal - 

```cmd
pip3 install vbt_yaml==0.0.5
python3 -m vbt_yaml -x /path/ComponentsTracker.xlsx -s CTSheet -y vlocity.yaml
```

You will see a yaml file created in the directory.

3. Vbt commands

To retrieve the components from your Salesforce org - you need a file called 'login.properties' as shown below

```yaml
sf.username = <org_username>
sf.password = <org_password><security_token>
sf.loginUrl = https://test.salesforce.com
vlocity.namespace = vlocity_cmt
```

To find your security token follow this [link](https://www.mcafee.com/blogs/enterprise/cloud-security/what-is-salesforce-security-token-and-how-do-i-find-it/)

After that you need to run the following command

```cmd
vlocity -propertyfile login.properties -job vlocity.yaml packExport
```

If the command runs without any issues, you will see a folder created 'example_vlocity_build' in your project directory which will have the components. 

## Installing from github repo
