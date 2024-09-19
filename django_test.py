"""
Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer
with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready,
we just need to understand your logic.
"""

import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(5)  # Simulate a long-running task
    print("Signal handler finished")


user = User.objects.create(username='testuser', password='password')
print("User created")


"""
Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet 
that conclusively proves your stance. The code does not need to be elegant and production ready, 
we just need to understand your logic.
"""

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")


def create_user():
    print(f"Main thread: {threading.current_thread().name}")
    user = User.objects.create(username='testuser', password='password')


create_user()


"""
Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer
with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, 
we just need to understand your logic.
"""

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal fired for user: {instance.username}")


def create_user_with_rollback():
    try:
        with transaction.atomic():
            user = User.objects.create(username='testuser', password='password')
            print(f"User created inside transaction: {user.username}")
            raise Exception("Simulated error - rolling back transaction")
    except Exception as e:
        print(f"Transaction rolled back: {e}")


create_user_with_rollback()


"""
Topic: Custom Classes in Python

Description: You are tasked with creating a Rectangle class with the following requirements:

1.	An instance of the Rectangle class requires length:int and width:int to be initialized.
2.	We can iterate over an instance of the Rectangle class 
3.	When an instance of the Rectangle class is iterated over, we first get its length in the 
    format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Define the iterator method
    def __iter__(self):
        # Return length and width in the required format
        yield {'length': self.length}
        yield {'width': self.width}

