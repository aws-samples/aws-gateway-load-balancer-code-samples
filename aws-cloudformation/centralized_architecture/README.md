### AWS Gateway Load Balancer In Centralized Architecture

## Welcome

* This section contains sample AWS Cloudformation templates that demonstrates how to create centralized inspection architecture using AWS Gateway Load Balancer (GWLB) AWS Gateway Load Balancer Endpoints (GWLBe), virtual appliances and AWS Transit Gateway (TGW) from templates that are written in YAML.

![](images/gwlb_centralized_architecture.jpg)

* **Launch CloudFormation templates in following order:**
  1. Appliance VPC Template
  2. Spoke1 VPC Template
  3. Spoke2 VPC Template
  4. TGW Template. TGW Template is dependent on Appliance VPC, Spoke1 VPC and Spoke2 VPC templates. Template will fail if launch before successfuly deployments of above 3 templates.

### **Appliance VPC:**
* [GWLB Appliance VPC Sample](CentralizedArchitectureApplianceVpc2Az.yaml)

### **Spoke1 VPC:**
* [GWLB Spoke1 VPC Sample](CentralizedArchitectureSpoke1Vpc2Az.yaml)

### **Spoke2 VPC:**
* [GWLB Spoke2 VPC Sample](CentralizedArchitectureSpoke2Vpc2Az.yaml)

### **TGW:**
* [GWLB TGW Sample](CentralizedArchitectureTgw.yaml)