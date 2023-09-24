# Use the docker-python-chromedriver image as a base
FROM joyzoursky/python-chromedriver:3.9-selenium

# Set the working directory
WORKDIR /workspace

RUN apt-get update
RUN apt-get install psmisc

# Install Locust
RUN pip install --no-cache-dir locust

# Copy your Locust script and the start script into the Docker image
COPY mnt/locustfile.py /workspace/
COPY mnt/locust_start.sh /workspace/

# Ensure the script is executable
RUN chmod +x /workspace/locust_start.sh

# Expose the Locust port
EXPOSE 8089

