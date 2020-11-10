* Following example show how to modify VPC Endpoint Service Configuration using AWS SDK for Go.

```go
// Modify VPC Endpoint Service Configuration
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

	service1Id := os.Args[1]

	modifyVpceService, serviceErr := ec2Client.ModifyVpcEndpointServiceConfiguration(&ec2.ModifyVpcEndpointServiceConfigurationInput{
		ServiceId: aws.String(service1Id),
		AcceptanceRequired: aws.Bool(false),
	})

	if serviceErr != nil{
		fmt.Println("Could not modify vpce service", serviceErr)
		return
	}

	fmt.Println("Modify vpce service:", modifyVpceService)

}
```