# ECR_EC2_Workflows
An experiment to implement word counting using a simplified version of MapReduce with ECS tasks and S3, encouraging creativity in the approach.

<img width="366" height="112" alt="image" src="https://github.com/user-attachments/assets/a4b54320-4a93-41b2-baa0-06653fe26c78" />

Snahil Singh@HP-Pavilion-Laptop-15 MINGW64 ~
$ aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 654654368158.dkr.ecr.us-west-2.amazonaws.com

Login Succeeded

<img width="1052" height="92" alt="image" src="https://github.com/user-attachments/assets/5d3608bc-0089-480b-895b-9e6fa1efeb34" />




<img width="1244" height="678" alt="image" src="https://github.com/user-attachments/assets/81733c08-c945-40db-90f9-96622e4ef478" />


<img width="843" height="232" alt="image" src="https://github.com/user-attachments/assets/abc036dc-e63d-4b12-99b2-3ad4f459858a" />



<img width="1898" height="894" alt="image" src="https://github.com/user-attachments/assets/aded549f-676d-4c18-af92-9e14e6d64215" />


<img width="1624" height="698" alt="image" src="https://github.com/user-attachments/assets/42852ee5-a2a9-41c8-8cef-b44aa7abf1b6" />


<img width="806" height="378" alt="image" src="https://github.com/user-attachments/assets/61543f4b-6472-477c-a0a6-2bf0a1774493" />


1️⃣ EC2 vs ECS

I first explored EC2 and ECS to understand how AWS manages compute resources.

With EC2, I realized that I have full control over virtual machines, including the operating system, networking, and installed software. I am responsible for scaling, patching, and deploying applications myself. It gave me a strong appreciation for having complete control over the server environment.

With ECS, I saw that I only manage containers, while AWS orchestrates deployment, scaling, and the lifecycle of tasks. Using Fargate mode, I didn’t need to provision EC2 instances myself, which made running microservices much simpler.

From this, I learned that EC2 is like managing the entire computer myself, while ECS is more about telling AWS: “Here’s my container, run it efficiently.”

2️⃣ VPC and Subnet

I then explored networking in AWS.

A VPC (Virtual Private Cloud) is my isolated network within AWS. It allows me to define IP ranges, routing rules, and security policies. For my work, I used the default VPC, which AWS had already created, giving me immediate access to launch resources without extra setup.

Within the VPC, I found subnets, which are smaller segments of the network. Some subnets are public (with internet access), while others are private. ECS tasks or EC2 instances need to be launched inside a subnet to communicate properly.

From this, I learned that understanding VPCs and subnets is essential for securely and efficiently launching resources.

3️⃣ TCP vs UDP

I next explored the difference between TCP and UDP.

TCP (Transmission Control Protocol) is connection-oriented. I learned that it guarantees packets arrive in order and without loss, making it reliable but slightly slower due to error checking. Examples include HTTP, HTTPS, and SSH.

UDP (User Datagram Protocol) is connectionless. I saw that it sends packets without guaranteeing delivery, making it faster but less reliable. It’s used in streaming, DNS queries, and online gaming.

From this, I understood that TCP is like sending a tracked package with confirmation, while UDP is like tossing letters quickly without tracking.

4️⃣ Controlling Resources for ECS Tasks

Finally, I explored how to control CPU and memory for ECS tasks.

I defined resource limits in my Task Definitions, specifying CPU and memory for the entire task as well as individual containers. This ensured my containers didn’t exceed allocated resources or interfere with others.

I also learned about task placement strategies, which allow me to control which subnets or instances my tasks run on.

This taught me that resource allocation is crucial for reliability and efficiency when running multiple containers in ECS.

💡 Reflection:
By exploring these concepts, I now understand the differences between EC2 and ECS, the role of networking through VPCs and subnets, how TCP and UDP handle communication, and how to allocate resources effectively in ECS. It gave me a much clearer picture of how AWS manages compute and networking behind the scenes.



