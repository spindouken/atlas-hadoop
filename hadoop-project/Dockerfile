# using ubuntu 20.04 as the base image
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# environment variables
ENV HADOOP_HOME /opt/hadoop
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV HADOOP_VERSION 3.2.2

# install packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    ssh \
    rsync \
    vim \
    net-tools \
    openjdk-8-jdk \
    python2.7 \
    python2.7-dev \
    libxml2-dev \
    libkrb5-dev \
    libffi-dev \
    libssl-dev \
    libldap2-dev \
    python-lxml \
    libxslt1-dev \
    libgmp3-dev \
    libsasl2-dev \
    libsqlite3-dev \
    libmysqlclient-dev \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

# install pip for Python 2.7
RUN curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py && \
    python2.7 get-pip.py && \
    rm get-pip.py

# install snakebite using pip for Python 2.7
RUN python2.7 -m pip install snakebite

# Create a symlink for Python
RUN if [ ! -e /usr/bin/python ]; then ln -s /usr/bin/python2.7 /usr/bin/python; fi

# download and install Hadoop version specified in environmental variables section
RUN wget https://archive.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz -P /tmp && \
    tar -xzf /tmp/hadoop-${HADOOP_VERSION}.tar.gz -C /opt/ && \
    rm /tmp/hadoop-${HADOOP_VERSION}.tar.gz && \
    mv /opt/hadoop-${HADOOP_VERSION} $HADOOP_HOME

# add Hadoop and Java to PATH
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

# Hadoop users and permissions
RUN for user in hadoop hdfs yarn mapred; do \
         useradd -U -M -d /opt/hadoop/ --shell /bin/bash ${user}; \
    done && \
    for user in root hdfs yarn mapred; do \
         usermod -G hadoop ${user}; \
    done

# Hadoop environment variables
RUN echo "export JAVA_HOME=$JAVA_HOME" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
    echo "export HDFS_DATANODE_USER=root" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
    echo "export HDFS_NAMENODE_USER=root" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
    echo "export HDFS_SECONDARYNAMENODE_USER=root" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
    echo "export YARN_RESOURCEMANAGER_USER=root" >> $HADOOP_HOME/etc/hadoop/yarn-env.sh && \
    echo "export YARN_NODEMANAGER_USER=root" >> $HADOOP_HOME/etc/hadoop/yarn-env.sh

# SSH configuration for Hadoop
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
    chmod 0600 ~/.ssh/authorized_keys

# utilize configuration files
ADD *xml $HADOOP_HOME/etc/hadoop/
ADD ssh_config /root/.ssh/config

# expose ports
EXPOSE 8088 9870 9864 19888 8042 8888

# use start-up scripts to initialize Hadoop and services
ADD start-all.sh start-all.sh
CMD bash start-all.sh
