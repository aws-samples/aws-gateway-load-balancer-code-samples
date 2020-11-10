* Following example show how to delete Gateway Load Balancer Endpoint using AWS SDK for Go.

```go
// Delete VPC Endpoint(s):
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

	vpce1Id := os.Args[1]

	deleteVpce, vpceErr := ec2Client.DeleteVpcEndpoints(&ec2.DeleteVpcEndpointsInput{
		VpcEndpointIds: []*string{
			aws.String(vpce1Id),
			//aws.String(vpce2Id),
		},
	})

	if vpceErr != nil{
		fmt.Println("Could not delete vpce:", vpceErr)
		return
	}	
	fmt.Println("Delete vpce:", deleteVpce)

}
```