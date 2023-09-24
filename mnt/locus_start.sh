#!/bin/bash

# Get arguments for number of users and spawn rate
NUM_USERS=$1
SPAWN_RATE=$2

# Run Locust in headless mode with provided arguments and save stats to a CSV file
locust -f locustfile.py --host https://bi-test.mojasrednjaskola.gov.rs/ --headless --users $NUM_USERS --spawn-rate $SPAWN_RATE --csv=locust_stats
