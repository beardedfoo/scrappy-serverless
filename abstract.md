Many have struggled to understand exactly what serverless is, and many talks
have been given at meetups, conferences, and in elevators in an attempt to
explain it. Rather than adding yet another explanation of serverless, I will
/show/ what serverless is, by building out a FaaS service live on stage, in
about 100 lines of python code.

The proof of concept FaaS I build will utilize docker and redis queues to
automatically build images, deploy functions in containers, and translate HTTP
connections into simple, distributed calls on dynamically submitted python
functions.
