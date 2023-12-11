# Training Cluster Mobileye Assignment


## Test Requirements

[x] Create MNIST server that serves a GRPC endpoint for streaming MNIST sample images
[x] Create a client server that connects to the MNIST server and ingests the images 


## System Requirements

- Python 3.11
- venv

## Development


### Docker compose

You can start the system by running in the root folder:
```
docker compose up
```

### In terminal

To run locally, follow the steps below to run the server:
1. (Optional) In a new terminal, start a python virtual environment and activate it
2. `cd services/server`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the code with `python server.py`

Then you can run the client following the steps:
1. (Optional) In a new terminal, start a python virtual environment and activate it
2. `cd services/client`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the code with `python client.py`


## Rebuilding protobufs

To rebuild the protobufs, run inside each service: `python compile_protos.py`


## Testing

To test the server, you can run `python -m pytest` in the `server` folder.  


## Deployment

To deploy the system, you can create 2 docker images, one for each service. You can do so by running `./scripts/build-image.sh server` for the server and `./scripts/build-image.sh client` for the client


## Environment Vars


### Server
    The only variable is `PORT` which by default is set to `50051`

### Client
    The only variable is `MNIST_SERVER_URL` which by default is set to `localhost:50051`


## Known issues

- If when after rebuilding the protobufs you see the error `No module named 'mnist_pb2'`, please add `from .` before line 5, so it will be as such: `from . import mnist_pb2 as mnist__pb2`