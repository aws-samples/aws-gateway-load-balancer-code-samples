* Following example show how to create Gateway Load Balancer Endpoint using VPC Endpoint Service Name using AWS SDK for Go.

```go
// Creates VPC Endpoint
package main

import (
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/ec2"

	"fmt"
	"os"
)

func main() {
	sess, sessErr := session.NewSessionWithOptions(session.Options{
		// Force enable Shared Config support
		SharedConfigState: session.SharedConfigEnable,
	})

	if sessErr != nil{
		fmt.Println("Could not create session", sessErr)
		return
	}

	ec2Client := ec2.New(sess)

	serviceName := os.Args[1]
	vpcId := os.Args[2]
	subnet1Id := os.Args[3]

	createVpce, vpceErr := ec2Client.CreateVpcEndpoint(&ec2.CreateVpcEndpointInput{
		VpcEndpointType: aws.String("GatewayLoadBalancer"),
		ServiceName: aws.String(serviceName),
		VpcId: aws.String(vpcId),
		SubnetIds: []*string{
			aws.String(subnet1Id),
		},
		TagSpecifications: []*ec2.TagSpecification{
			{
				ResourceType: aws.String("vpc-endpoint"),
				Tags: []*ec2.Tag{
					{
						Key: aws.String("Name"),
						Value: aws.String("gwlbe1"),
					},
				},
			},
		},		
	})

	if vpceErr != nil{
		fmt.Println("Could not create vpce", vpceErr)
		return
	}

	fmt.Println("Create vpce service:", createVpce)

}
```