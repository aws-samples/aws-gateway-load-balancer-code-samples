## AWS GWLB + VPC Routing Enhancement + ALB Validation:

### Welcome

* This section walks you through steps to validate ingress traffic inspection with ALB - using VPC routing enhancemnts and GWLB endpoint.

### Testing:

1. Using Session Manager, connect to Appliance 1 running in Inspection VPC:

![](images/connect_appliance_1_a.jpg)
*Figure 1: Select appliance 1 and click on Connect*

![](images/connect_appliance_1_b.jpg)
*Figure 2: Select Session Manager and click on Connect*

![](images/connect_appliance_1_c.jpg)
*Figure 3: Appliance 1*

2. Using Session Manager, connection to Server 1 and Server 2 running in Ingress VPC:

![](images/ingress/ingress_connect_server_1_a.jpg)
*Figure 7: Select server 1 and click on Connect*

![](images/ingress/ingress_connect_server_1_b.jpg)
*Figure 8: Select Session Manager and click on Connect*

![](images/ingress/ingress_connect_server_1_c.jpg)
*Figure 9: Server 1*

![](images/ingress_connect_server_2_a.jpg)
*Figure 10: Select server 2 and click on Connect*

![](images/ingress/ingress_connect_server_2_b.jpg)
*Figure 11: Select Session Manager and click on Connect*

![](images/ingress/ingress_connect_server_2_c.jpg)
*Figure 12: Server 2*

3. Verify the IP address for the servers:

![](images/ingress/ingress_server_1_ip.jpg)
*Figure 13: Server 1 IP address*

![](images/ingress/ingress_server_2_ip.jpg)
*Figure 14: Server 2 IP address*

4. Capture GENEVE traffic using tcpdump. 

   The following tcpdump command filters traffic based inside packet source and destination IP and protocol.
   
   * 0x0a011544 = 10.1.21.68, server 1's IP address
   * 0x0a011696 = 10.1.22.150, server 2's IP address
   * 0x0a010b10 = 10.1.11.16, ALB's AZ1 private IP address

```bash
sudo tcpdump -ni eth0 "(ether[94:4]=0x0a010b10 and ether[98:4]=0x0a011544) or (ether[94:4]=0x0a010b10 and ether[98:4]=0x0a011696) or (ether[94:4]=0x0a011544 and ether[98:4]=0x0a010b10) or (ether[94:4]=0x0a011696 and ether[98:4]=0x0a010b10) and (ether[91:1]=0x06)"
```

![](images/ingress/ingress_tcpdump_appliance_1.jpg)
*Figure 15: Capture GENEVE traffic on appliance 1*

5. Access ALB's FQDN:

![](images/ingress/ingress_access_alb_fqdn_server1.jpg)
*Figure 17: Access ALB*

4. Verify traffic being processed by respective appliances

   * While veryifying traffic on inspection appliance, you notice 2 packets. This is because inspection appliance is set up in an [hairpin mode](../../aws-cli/gwlb/configure_iptables_al2.md). In this mode, it sends all the traffic that it receives from GWLB back to GWLB on same interface.

![](images/ingress/ingress_tcpdump_appliance_1_verify_1.jpg)
*Figure 18: Verifying Traffic on Appliance 1*
