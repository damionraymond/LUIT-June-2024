from helpers import *  # Import all functions from the helpers module

def create_instances(ec2_client: 'EC2.Client', instance_amount: int, instance_type: str) -> None:
    """
    Creates the specified number of EC2 instances of a given type.

    Args:
        ec2_client (EC2.Client): The EC2 client used to create instances.
        instance_amount (int): The number of instances to create.
        instance_type (str): The type of instance to create ('Ubuntu', 'Amazon Linux 2023', 'Amazon Linux 2').

    Returns:
        None
    """
    for i in range(instance_amount):  # Iterate over the number of instances to create
        # Check if the instance type is 'Ubuntu' (case-insensitive)
        if instance_type.strip().lower() == 'ubuntu':
            create_ubuntu_instance(ec2_client)  # Create an Ubuntu instance
            print('Created Ubuntu Instance')
        # Check if the instance type is 'Amazon Linux 2023' (case-insensitive)
        elif instance_type.strip().lower() == 'amazon linux 2023':
            create_amazon_linux_2023_instance(ec2_client)  # Create an Amazon Linux 2023 instance
            print('Created Amazon Linux 2023 Instance')
        # Check if the instance type is 'Amazon Linux 2' (case-insensitive)
        elif instance_type.strip().lower() == 'amazon linux 2':
            create_amazon_linux_2_instance(ec2_client)  # Create an Amazon Linux 2 instance
            print('Created Amazon Linux 2 Instance')
        else:
            print('Invalid Instance AMI')  # Print an error message if the instance type is invalid

# Example usage
ec2_client = get_ec2_client()  # Get the EC2 client
create_instances(ec2_client, 3, "ubuntu")  # Create 3 Ubuntu instances