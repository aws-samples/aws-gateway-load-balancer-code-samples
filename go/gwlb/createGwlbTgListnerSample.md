* Following example show how to create Gateway Load Balancer, target group and listener using AWS SDK for Go.

```go
// Creates Target Group, Gateway Load Balancer and Listner
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
	gwlbName := os.Args[3]
	subnet1Id := os.Args[4]
	target1Id := os.Args[5]

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

	// Register Targets:
	registerTargets, registerErr := elbv2Client.RegisterTargets(&elbv2.RegisterTargetsInput{
		TargetGroupArn: tg.TargetGroups[0].TargetGroupArn,
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

	// Create gateway load balancer
	gwlb, gwlbErr := elbv2Client.CreateLoadBalancer(&elbv2.CreateLoadBalancerInput{
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

	if gwlbErr != nil {
		fmt.Println("Could not create GWLB", gwlbErr)
		return
	}

	fmt.Println("Created GWLB:", gwlb)

	// Use a waiter function to wait until the gateway load balancer is available
	describeGwlbInput := &elbv2.DescribeLoadBalancersInput{
		LoadBalancerArns: []*string{
			gwlb.LoadBalancers[0].LoadBalancerArn,
		},
	}
	if err := elbv2Client.WaitUntilLoadBalancerAvailable(describeGwlbInput); err != nil {
		panic(err)
	  }
	fmt.Println("GWLB is available.")

	// Create listener
	listener, listenerErr := elbv2Client.CreateListener(&elbv2.CreateListenerInput{
		LoadBalancerArn: gwlb.LoadBalancers[0].LoadBalancerArn,
		DefaultActions:  []*elbv2.Action{
			{
				TargetGroupArn: tg.TargetGroups[0].TargetGroupArn,
				Type: aws.String("forward"),
			},		
		},
	})

	if listenerErr != nil {
		fmt.Println("Could not create listener", listenerErr)
		return
	}

	fmt.Println("Created listener:", listener)	
}
```