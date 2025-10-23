Create Conda venv:
```console
conda create -n deepfill python=3.7.0 anaconda
```

Install requirements:
```python
pip install -r requirements.txt
```

Install neuralgym
```python
pip install git+https://github.com/JiahuiYu/neuralgym
```
Make flist for train, val, test:
```python
python flist_maker.py
```