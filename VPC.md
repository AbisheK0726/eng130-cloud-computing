# VPC

## What is a VPC?

A VPC is a virtual network dedicated to your AWS account. It is logically isolated from other virtual networks in the AWS Cloud. You can launch your AWS resources, such as Amazon EC2 instances, into your VPC. You can specify an IP address range for the VPC, add subnets, associate security groups, and configure route tables.

## Internet Gateway

An internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication between instances in your VPC and the internet. It performs network address translation (NAT) for instances that have been assigned public IPv4 addresses.

## Route Table

A route table contains a set of rules, called routes, that are used to determine where network traffic from your subnet or gateway is directed. Each route table contains a local route for the virtual private cloud (VPC) that contains it, and a default route for outbound traffic.

## Cidr Block

CIDR stands for Classless Inter-Domain Routing. It is a method of allocating IP addresses and IP routing. CIDR is a superset of the older system of allocating IP addresses. CIDR uses a slash notation to indicate the number of bits in the network prefix. For example, the CIDR block

## Subnet

A subnet is a range of IP addresses in your VPC. You can launch AWS resources, such as Amazon EC2 instances, into a subnet. You specify the size of the subnet when you create it, and you can't change the size after you create it. You can create as many subnets as you want in a VPC. You can create subnets in each Availability Zone.

## NACL

A network access control list (ACL) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets.

You can use network ACLs to allow or deny traffic to and from specific Amazon EC2 instances in your VPC. You can create a network ACL for each subnet in your VPC, and then associate the network ACL with the subnet.

Each network ACL has an inbound rule list and an outbound rule list. When you add a rule to a network ACL, you specify whether the rule allows or denies traffic, and the rule applies to traffic that matches the rule's destination or source.

Each network ACL has a default inbound rule and a default outbound rule. The default inbound rule denies all inbound traffic, and the default outbound rule allows all outbound traffic.

You can't delete the default rules, but you can change them. When you create a network ACL, by default it has no rules in it, and therefore no traffic is allowed through the network ACL. You must add rules to the network ACL to control traffic.

### Difference between NACL and Security Group

| NACL | Security Group |
| --- | --- |
| NACL is stateless | Security Group is stateful |
| NACL is at subnet level | Security Group is at instance level |
| NACL is a network level firewall | Security Group is a security group level firewall |