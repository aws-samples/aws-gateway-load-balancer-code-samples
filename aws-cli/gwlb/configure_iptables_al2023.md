* Following example shows how to configure iptables on an Amazon Linux 2023 (AL2023) instance acting as a target behind an AWS Gateway Load Balancer (GWLB).

* iptables configuration creates a hairpin setup. The hairpin setup allows traffic coming from GWLB on the Amazon Linux 2023 appliance to be sent back to GWLB.

* This is the AL2023 counterpart of `configure_iptables_al2.md`. Unlike Amazon Linux 2, on AL2023 iptables is not preinstalled (install `iptables` and `iptables-services`), the package manager is `dnf`, and the primary interface is usually `ens5`.

* iptables configuration is for **sample purpose only. It allows all the traffic! Use it for GWLB POC only**

```bash
# instance IP, primary interface, region and VPC id:
export iface=$(ip route show default | awk '{print $5; exit}')
export instance_ip=$(ip -4 addr show $iface | awk '/inet /{print $2}' | cut -d/ -f1)
TOKEN=$(curl -sX PUT http://169.254.169.254/latest/api/token -H "X-aws-ec2-metadata-token-ttl-seconds: 300")
export instance_region=$(curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/placement/region)
export instance_vpcid=$(curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/network/interfaces/macs/$(curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/mac)/vpc-id)

# Enable IP Forwarding and persist across reboot:
echo "net.ipv4.ip_forward = 1" | sudo tee /etc/sysctl.d/99-gwlb.conf
sudo sysctl -p /etc/sysctl.d/99-gwlb.conf

# Install iptables and iptables-services (NOT preinstalled on AL2023):
sudo dnf install iptables iptables-services -y;

# Start and configure iptables:
sudo systemctl enable iptables;
sudo systemctl start iptables;

# Configuration below allows all traffic:
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
  sudo iptables -t nat -A PREROUTING -p udp -s $gwlb_ip -d $instance_ip -i $iface -j DNAT --to-destination $gwlb_ip:6081
  sudo iptables -t nat -A POSTROUTING -p udp --dport 6081 -s $gwlb_ip -d $gwlb_ip -o $iface -j MASQUERADE
done

# Save iptables:
sudo service iptables save;
```
