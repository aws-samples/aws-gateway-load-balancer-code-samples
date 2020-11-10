* Following example show how to delete target group using AWS SDK for Go.

```go
// Delete target group:
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

	if err != nil {
		fmt.Println("Could not create session", err)
		return
	}

	elbv2Client := elbv2.New(sess)

	tgArn := os.Args[1]

	// Specify the details of the target group that you want to delete.
	deleteTg, tgErr := elbv2Client.DeleteTargetGroup(&elbv2.DeleteTargetGroupInput{
		TargetGroupArn: aws.String(tgArn),
	})

	if tgErr != nil {
		fmt.Println("Could not delete target group", tgErr)
		return
	}

	fmt.Println("Deleted target group", deleteTg)	
	
}
```