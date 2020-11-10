* Following example show how to delete Gateway Load Balancer using AWS SDK for Go.

```go
// Delete Gateway Load Balancer:
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

	gwlbArn := os.Args[1]

	// Specify the details of the GWLB that you want to delete.
	deleteGwlb, err := elbv2Client.DeleteLoadBalancer(&elbv2.DeleteLoadBalancerInput{
		LoadBalancerArn: aws.String(gwlbArn),
	})

	if err != nil {
		fmt.Println("Could not delete gateway load balancer", err)
		return
	}

	fmt.Println("Deleted GWLB", deleteGwlb)
	
}
```