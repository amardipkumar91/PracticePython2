import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello1')


channel.basic_publish(exchange='',routing_key='hello1',body='Hello World! this is amardip Hi Guys')
print(" [x] Sent 'Hello World!'")
connection.close()