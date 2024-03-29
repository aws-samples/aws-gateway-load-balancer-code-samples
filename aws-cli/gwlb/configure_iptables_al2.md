* Following example shows how to configure iptables on Amazon Linux 2 instance acting as a target behind an AWS Gateway Load Balancer (GWLB). 

* iptables configuration creates a hairpin setup. The hairpin setup allows traffic coming from GWLB on Amazon Linux 2 appliance to be sent back to GWLB.

* iptables configuration is for **sample purpose only. It allows all the traffic! Use it for GWLB POC only** 

```bash
# instance IP:
# Replace <x.x.x.x> with appropriate instance IP
export instance_ip=<x.x.x.x>

# Retrieve GWLB IP:
# Replace <y.y.y.y> with appropriate GWLB IP. It should be from the same AZ as the instance.
export gwlb_ip=<y.y.y.y>

# Enable IP Forwarding and persist across reboot
# Enabling using sysctl -w net.ipv4.ip_forward=1, won't persist across reboot.
sudo echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.d/00-defaults.conf
sudo sysctl -p /etc/sysctl.d/00-defaults.conf

# Install iptables-services:
sudo yum install iptables-services -y;

# Start and configure iptables:
sudo systemctl enable iptables;
sudo systemctl start iptables;

# Configuration below allows allows all traffic:
# Set the default policies for each of the built-in chains to ACCEPT:
sudo iptables -P INPUT ACCEPT;
sudo iptables -P FORWARD ACCEPT;
sudo iptables -P OUTPUT ACCEPT;

# Flush the nat and mangle tables, flush all chains (-F), and delete all non-default chains (-X):
sudo iptables -t nat -F;
sudo iptables -t mangle -F;
sudo iptables -F;
sudo iptables -X;

# Configure nat table to hairpin traffic back to GWLB:
for gwlb_ip in $(aws ec2 describe-network-interfaces --filters Name=vpc-id,Values=$instance_vpcid --region $instance_region | jq ' .NetworkInterfaces[] | select(.InterfaceType=="gateway_load_balancer") |.PrivateIpAddress' -r)
  do
  sudo iptables -t nat -A PREROUTING -p udp -s $gwlb_ip -d $instance_ip -i eth0 -j DNAT --to-destination $gwlb_ip:6081
  sudo iptables -t nat -A POSTROUTING -p udp --dport 6081 -s $gwlb_ip -d $gwlb_ip -o eth0 -j MASQUERADE
done

# Save iptables:
sudo service iptables save;
```
