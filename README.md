**Instasll all packages**

```
pip3 install -r requirements.txt
```

**Setup the vitual environment**

```
python3 -m venv blockchain-env
```

**Activate the virtual environment**

```
source blockchain-env/bin/activate
```

_check virtual env is activate_

```
echo $VIRTUAL_ENV
```

**Run the tests**
make sure the virtual env is activated

```
pytest backend/tests
```
