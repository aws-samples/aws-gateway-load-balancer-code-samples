* Following example show how to delete VPC Endpoint Service using AWS SDK for Go.

```go
// Delete VPC Endpoint Service(s):
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

	deleteVpceService, serviceErr := ec2Client.DeleteVpcEndpointServiceConfigurations(&ec2.DeleteVpcEndpointServiceConfigurationsInput{
		ServiceIds: []*string{
			aws.String(service1Id),
		},
	})

	if serviceErr != nil{
		fmt.Println("Could not delete vpce service", serviceErr)
		return
	}	
	fmt.Println("Deleted vpce service:", deleteVpceService)

}
```