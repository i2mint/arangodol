
# arangodol
ArangoDB with a simple (dict-like or list-like) interface


To install:	```pip install arangodol```


A basic ArangoDB persister.

```python
>>> from arangodol import ArangoDbPersister
>>> s = ArangoDbPersister()
>>> k = {'key': '777'} # Each collection will happily accept user-defined _key values.
>>> v = {'val': 'bar'}
>>> for _key in s:
...     del s[_key]
...
>>> k in s
False
>>> len(s)
0
>>> s[k] = v
>>> len(s)
1
>>> s[k]
{'val': 'bar'}
>>> s.get(k)
{'val': 'bar'}
>>> s.get({'not': 'a key'}, {'default': 'val'})  # testing s.get with default
{'default': 'val'}
>>> list(s.values())
[{'val': 'bar'}]
>>> k in s  # testing __contains__ again
True
>>> del s[k]
>>> len(s)
0
>>> s = ArangoDbPersister(db_name='py2store', key_fields=('name',))
>>> for _key in s:
...     del s[_key]
...
>>> s[{'name': 'guido'}] = {'yob': 1956, 'proj': 'python', 'bdfl': False}
>>> s[{'name': 'guido'}]
{'yob': 1956, 'proj': 'python', 'bdfl': False}
>>> s[{'name': 'vitalik'}] = {'yob': 1994, 'proj': 'ethereum', 'bdfl': True}
>>> s[{'name': 'vitalik'}]
{'yob': 1994, 'proj': 'ethereum', 'bdfl': True}
>>> for key, val in s.items():
...     print(f"{key}: {val}")
{'name': 'guido'}: {'yob': 1956, 'proj': 'python', 'bdfl': False}
{'name': 'vitalik'}: {'yob': 1994, 'proj': 'ethereum', 'bdfl': True}

```


ArangoDbStore using tuple keys.

```python
>>> from arangodol import ArangoDbTupleKeyStore
>>> s = ArangoDbTupleKeyStore(collection_name='test', key_fields=('key', 'user'))
>>> k = (1234, 'user')
>>> v = {'name': 'bob', 'age': 42}
>>> if k in s:  # deleting all docs in tmp
...     del s[k]
>>> assert (k in s) == False  # see that key is not in store (and testing __contains__)
>>> orig_length = len(s)
>>> s[k] = v
>>> assert len(s) == orig_length + 1
>>> assert k in list(s)
>>> assert s[k] == v
>>> assert s.get(k) == v
>>> assert v in list(s.values())
>>> assert (k in s) == True # testing __contains__ again
>>> del s[k]
>>> assert len(s) == orig_length
```
