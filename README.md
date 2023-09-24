# Locust Docker Setup

This setup provides an environment to run a Locust load test using a Docker container. The container uses a Python image with ChromeDriver and Selenium installed, suitable for web-based load tests.

## Prerequisites

- Docker installed on your machine.

## Instructions

### 1. Building the Docker Image

To build the Docker image:

```
docker build -f docker_file/Dockerfile -t my_locust_image .
```


This command will build a Docker image with the tag `my_locust_image`.

### 2. Running the Docker Container

To run the Locust test using the Docker container:

```
docker run -p 8089:8089 -v ~/locust_results:/workspace my_locust_image /workspace/locust_start.sh [NUMBER_OF_USERS] [SPAWN_RATE]
```


Replace `[NUMBER_OF_USERS]` with the desired number of users and `[SPAWN_RATE]` with the desired spawn rate. For example, if you want to simulate 10 users with a spawn rate of 2, the command will look like:

```
docker run -p 8089:8089 -v ~/locust_results:/workspace my_locust_image /workspace/locust_start.sh 10 2
```


**Notes:**

- The `-p 8089:8089` argument maps port 8089 in the container to port 8089 on the host.
  
- The `-v ~/locust_results:/workspace` argument mounts the `~/locust_results` directory from your host to the `/workspace` directory in the container. This is where the Locust stats results will be saved.

### 3. Viewing the Results

Once the load test is finished, you can find the results in the `~/locust_results` directory on your main machine.
