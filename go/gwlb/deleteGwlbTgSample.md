* Following example show how to delete target group and Gateway Load Balancer using AWS SDK for Go.

```go
// Delete Gateway Load Balancer and target group:
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

	tgarn := os.Args[1]
	gwlbarn := os.Args[2]

	// Specify the details of the GWLB that you want to delete.
	deleteGwlb, gwlbErr := elbv2Client.DeleteLoadBalancer(&elbv2.DeleteLoadBalancerInput{
		LoadBalancerArn: aws.String(gwlbarn),
	})

	if gwlbErr != nil {
		fmt.Println("Could not delete gateway load balancer", err)
		return
	}

	fmt.Println("Deleted GWLB", deleteGwlb)

	// Specify the details of the target group that you want to delete.
	deleteTg, tgErr := elbv2Client.DeleteTargetGroup(&elbv2.DeleteTargetGroupInput{
		TargetGroupArn: aws.String(tgarn),
	})

	if tgErr != nil {
		fmt.Println("Could not delete target group", tgErr)
		return
	}

	fmt.Println("Deleted target group", deleteTg)	
	
}
```