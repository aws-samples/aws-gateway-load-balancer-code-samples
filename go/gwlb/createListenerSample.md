* Following example show how to create listener using AWS SDK for Go.

```go
//Create Listener:
package main

import (
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/elbv2"

	"fmt"
	"os"
)

func main(){

	sess, sessErr := session.NewSessionWithOptions(session.Options{
		// Force enable Shared Config support
		SharedConfigState: session.SharedConfigEnable,
	})

	if sessErr != nil {
		fmt.Println("Could not create session", sessErr)
		return
	}

	elbv2Client := elbv2.New(sess)

	tgArn := os.Args[1]
	gwlbArn := os.Args[2]

	// Create listener
	listener, listenerErr := elbv2Client.CreateListener(&elbv2.CreateListenerInput{
		LoadBalancerArn: aws.String(gwlbArn),
		DefaultActions:  []*elbv2.Action{
			{
				TargetGroupArn: aws.String(tgArn),
				Type: aws.String("forward"),
			},		
		},
		// Port: aws.Int64(6081),
		// Protocol: aws.String("GENEVE"),
	})

	if listenerErr != nil {
		fmt.Println("Could not create listener", listenerErr)
		return
	}

	fmt.Println("Created listener:", listener)
}
```