# Use the official Ubuntu base image
FROM ubuntu:22.04

# Set environment variables
ENV SPARK_VERSION=3.5.3
ENV SCALA_VERSION=2.13
ENV JAVA_VERSION=21
ENV PYTHON_VERSION=3.10

COPY requirements.txt /requirements.txt


# Install dependencies
RUN apt-get update && apt-get install -y \
    openjdk-21-jdk \
    python3 \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Install Spark
RUN curl -L "https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop3.tgz" -o /tmp/spark.tgz \
    && tar -xzf /tmp/spark.tgz -C /opt/ \
    && mv /opt/spark-* /opt/spark \
    && rm /tmp/spark.tgz


# Set environment variables for Spark
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# Upgrade pip and install Jupyter and PySpark
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install jupyter \
    && python3 -m pip install pyspark==$SPARK_VERSION \
    && python3 -m pip install -r /requirements.txt 

# Expose Spark and Jupyter ports
EXPOSE 7077 8080 8081 4040 8888

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]
