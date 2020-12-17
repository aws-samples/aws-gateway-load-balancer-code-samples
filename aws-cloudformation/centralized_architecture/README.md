### AWS Gateway Load Balancer In Centralized Architecture

## Welcome

* This section contains sample AWS Cloudformation templates that demonstrates how to create centralized inspection architecture using AWS Gateway Load Balancer (GWLB) AWS Gateway Load Balancer Endpoints (GWLBe), virtual appliances and AWS Transit Gateway (TGW) from templates that are written in YAML.

* For more details, refer to blog: **[Centralized inspection architecture with AWS Gateway Load Balancer and AWS Transit Gateway](https://aws.amazon.com/blogs/networking-and-content-delivery/centralized-inspection-architecture-with-aws-gateway-load-balancer-and-aws-transit-gateway/)**

![](images/gwlb_centralized_architecture.jpg)

* **Launch CloudFormation templates in following order:**
  1. Appliance VPC Template
  2. Spoke1 VPC Template
  3. Spoke2 VPC Template
  4. Transit Gateway Template. Transit Gateway Template is dependent on Appliance VPC, Spoke1 VPC and Spoke2 VPC templates. Template will fail if launched before successfuly deployments of above 3 templates.

### **Appliance VPC:**
* [GWLB Appliance VPC Sample](CentralizedArchitectureApplianceVpc2Az.yaml)

### **Spoke VPCs:**
* We use the same spoke VPC template for both Spoke1 VPC and Spoke2 VPC. When deploying the template for Spoke2 VPC, make sure you have changed the default values so that Spoke2 VPC has different VPC and related subnet network addresses.

* [GWLB Spoke1 VPC Sample](CentralizedArchitectureSpokeVpc2Az.yaml)
* [GWLB Spoke2 VPC Sample](CentralizedArchitectureSpokeVpc2Az.yaml)

### **Transit Gateway:**
* [GWLB Transit Gateway Sample](CentralizedArchitectureTgw.yaml)

### Enable Transit Gateway Appliance Mode:

To ensure flow symmetry, Transit Gateway appliance mode should be enabled on the Appliance VPC’s attachment. Once Transit Gateway template has been successfully deployed, fetch the Appliance VPC Attachment ID from stack's Outputs tab and enable applince mode using AWS CLI as shown below. Replace the parameter values inside '< >' with appropriate values.

```bash
aws ec2 modify-transit-gateway-vpc-attachment \
    --transit-gateway-attachment-id <tgw-attach-0253EXAMPLE>
    --options ApplianceModeSupport=enable
```