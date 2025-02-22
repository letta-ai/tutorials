# Letta Python SDK Tutorial 

To run this tutorial, you will need: 
* Python >= 3.10
* OpenAI API key 
* Docker (optional) 

## Setting up a Letta server
To run this tutorial, you will need access to a Letta server. 

### Running with Docker (recommended) 
```
export OPENAI_API_KEY=... 

docker run \                                                                                                            ─╯
  -v ~/.letta/.persist/pgdata:/var/lib/postgresql/data \
  -p 8283:8283 \
  -e OPENAI_API_KEY=$OPENAI_API_KEY \
  letta/letta:latest
```

### Running the `pip` 
You can also install a Letta server via pip:
```
# install the letta server
pip install 'letta>=0.6.30'

# run the letta server
export OPENAI_API_KEY=... 
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
