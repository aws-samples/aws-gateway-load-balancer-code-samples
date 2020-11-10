* Following example show how to register targets to target group using AWS SDK for Go.

```go
// Register targets:
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
	target1Id := os.Args[5]

	// Register Targets:
	registerTargets, registerErr := elbv2Client.RegisterTargets(&elbv2.RegisterTargetsInput{
		TargetGroupArn: aws.String(tgArn),
		Targets: []*elbv2.TargetDescription{
			{
				Id: aws.String(target1Id),
			},
		},
	})

	if registerErr != nil {
		fmt.Println("Could not register targets", registerErr)
		return
	}
	
	fmt.Println("Registered targets:", registerTargets)
}
```