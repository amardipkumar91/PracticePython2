# Installation 
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management

If already Image available
Than Run the contauner

docker run -i -t <Image Id>

# Python Version
3.7.7

# Inastall RabbitMQ libraries
python -m pip install pika --upgrade

