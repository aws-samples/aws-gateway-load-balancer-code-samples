### AWS Gateway Load Balancer In Distributed Architecture

## Welcome

* For more details, refer to [Scaling network traffic inspection using AWS Gateway Load Balancer Blog](https://aws-blogs-prod.amazon.com/networking-and-content-delivery/scaling-network-traffic-inspection-using-AWS-Gateway-Load-Balancer/)

* This section contains sample AWS Cloudformation templates that demonstrates how to create distributed architecture using AWS Gateway Load Balancer and Gateway Load Balancer Endpoints from templates that are written in YAML.

![](images/distributed_architecture.jpg)

### **Appliance VPC:**
* [GWLB Appliance VPC](DistributedArchitectureApplianceVpc2Az.md)

### **Spoke VPC:**
* [GWLB Spoke VPC](DistributedArchitectureSpokeVpc2Az.md)