* Following example show how to create Gateway Load Balancer using AWS SDK for Go.

```go
// Create Gateway Load Balancer
package main

import (
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/elbv2"

    "fmt"
    "os"
)

func main() {
	sess, err := session.NewSessionWithOptions(session.Options{
		// Force enable Shared Config support
		SharedConfigState: session.SharedConfigEnable,
	})

	elbv2Client := elbv2.New(sess)

	gwlbName := os.Args[1]
	subnet1Id := os.Args[2]

	// Specify the details of the GWLB that you want to create.
	createGwlb, err := elbv2Client.CreateLoadBalancer(&elbv2.CreateLoadBalancerInput{
		Name: aws.String(gwlbName),
		Subnets: []*string{
			aws.String(subnet1Id),
		},
		Tags: []*elbv2.Tag{
			{
				Key: aws.String("Name"),
				Value: aws.String(gwlbName),
			},
		},
		Type: aws.String("gateway"),
	})

	if err != nil {
		fmt.Println("Could not create gateway load balancer", err)
		return
	}

	fmt.Println("Created GWLB", createGwlb)
	
}
```