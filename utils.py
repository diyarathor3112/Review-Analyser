import time
import random

def polite_delay(min_s=0.5, max_s=1.5):
    time.sleep(random.uniform(min_s, max_s))
