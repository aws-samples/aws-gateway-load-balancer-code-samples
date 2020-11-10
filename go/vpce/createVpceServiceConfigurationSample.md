* Following example show how to create VPC Endpoint Service using Gateway Load Balancer ARN using AWS SDK for Go.

```go
// Creates VPC Endpoint Service:
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

	gwlbArn := os.Args[1]

	createVpceService, serviceErr := ec2Client.CreateVpcEndpointServiceConfiguration(&ec2.CreateVpcEndpointServiceConfigurationInput{
		AcceptanceRequired: aws.Bool(false),
		GatewayLoadBalancerArns: []*string{
			aws.String(gwlbArn),
		},
		TagSpecifications: []*ec2.TagSpecification{
			{
				ResourceType: aws.String("vpc-endpoint-service"),
				Tags: []*ec2.Tag{
					{
						Key: aws.String("Name"),
						Value: aws.String("gwlb1-service1"),
					},
				},
			},
		},		
	})

	if serviceErr != nil{
		fmt.Println("Could not create vpce service", serviceErr)
		return
	}

	fmt.Println("Create vpce service:", createVpceService)

}
```