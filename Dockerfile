# Load the wrapper image that includes a base user template
FROM jmcparland/wrapper-test:latest

# clear the dummy routine. replace with contents of this repo
WORKDIR /usr/src/app
RUN rm -rf userspace
WORKDIR /usr/src/app/userspace
ADD userspace .

# process user-defined python requirements
RUN pip install --no-cache-dir -r requirements.txt

# good to go! return to the expected directory
WORKDIR /usr/src/app

# the base container will execute its wrapper script
