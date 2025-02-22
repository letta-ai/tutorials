# Letta Python SDK Tutorial 

To run this tutorial, you will need: 
* Python >= 3.10
* Docker (optional)

## Getting the tutorial files
```sh
git clone https://github.com/letta-ai/tutorials
```
```sh
cd tutorials/python
```

## Setting up a Letta server
To run this tutorial, you will need access to a Letta server.

You will need to run the Letta server in the background (e.g. in a separate terminal window) while you execute the code in the notebook.

### Running with Docker (recommended) 
```
docker run \                                                                                                            ─╯
  -v ~/.letta/.persist/pgdata:/var/lib/postgresql/data \
  -p 8283:8283 \
  letta/letta:latest
```

### Running with `pip` 
You can also install a Letta server via pip:
```
# install the letta server
pip install 'letta>=0.6.30'

# run the letta server
letta server
```
Please note this version of the Letta server is not production ready and does not support migrations accross versions. 

## Running the tutorial  
```
pip install -r requirements.txt
```

To run the tutorial, start a Jupyter notebook: 
```
jupyter notebook
```
