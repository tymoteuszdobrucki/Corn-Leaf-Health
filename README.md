# Corn-Leaf-Health

## Running the code

### 1) Clone the repository

Clone the repository

```bash
https://github.com/tymoteuszdobrucki/Corn-Leaf-Health
```
### 2) Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```


### 3) Install the requirements

```bash
pip install -r requirements.txt
```

### 4) Export as env variables

```bash

export MLFLOW_TRACKING_URI={your_uri}

export MLFLOW_TRACKING_USERNAME={your_username} 

export MLFLOW_TRACKING_PASSWORD={your_password}

```

### 5) Run app.py

```bash
python app.py
```

### 6) Open up you local host and port


## Training/Evaluating the model - DVC for pipeline orchestration

### 1) Initialization

```bash
dvc init
```

### 2) Running

```bash
dvc repro
```