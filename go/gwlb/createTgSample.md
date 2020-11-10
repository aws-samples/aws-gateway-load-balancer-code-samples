* Following example show how to create target group using AWS SDK for Go.

```go
// Creates Target Group
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

	tgName := os.Args[1]
	vpcId := os.Args[2]

	// Create target group
	tg, tgErr := elbv2Client.CreateTargetGroup(&elbv2.CreateTargetGroupInput{
		Name: aws.String(tgName),
		Port: aws.Int64(6081),
		Protocol: aws.String("GENEVE"),
		VpcId: aws.String(vpcId),
		HealthCheckPort: aws.String("80"),
		HealthCheckProtocol: aws.String("HTTP"),
		HealthCheckPath: aws.String("/test.html"),
		TargetType: aws.String("instance"),
	})

	if tgErr != nil {
		fmt.Println("Could not create target group", tgErr)
		return
	}
	
	fmt.Println("Created target group:", tg)
}
```