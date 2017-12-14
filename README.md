# A sample gRPC client #

## Overview ##

This client hooks up to a gRPC channel running on port 50051 and attempts to call the GetMatches method remotely.

## Installation ##

    git clone git@github.com:ryanisnan/grpc-python-testclient.git
    cd grpc-python-testclient
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Run the client ##

    python client.py
