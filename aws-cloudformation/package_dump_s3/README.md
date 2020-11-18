## GWLB package dump
A cloudformation template that will help you test, inspect and troubleshoot your GWLB traffic. 
This can help you if you want to build your own appliance/GWLB target or if you want to inspect the GWLB and GENEVE integration closer.

### Features
This cloudformation creates an S3 bucket for package dumps and an EC2 instance and registers it as a target in your provided GWLB target group.
The EC2 will run two traffic analyze scripts. One script captures all traffic as a .pcap and the other script will only capture GENEVE packages. It will upload the package dumps every minute to the S3 bucket at: `<yourbucket>/pcap` and `<yourbucket>/simple-geneve`.
The simple-geneve dump can be opened and inspected in your browser or favorite text editor while you can analyze the pcap-file using eg Wireshark or tcpdump.
