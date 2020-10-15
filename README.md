# volga &emsp; [![travis]][build] [![codecov]][codecov-page] [![license]][license-file] [![release]][releases] [![python-version]][pypi] [![open-issues]][issues] ![stars]

[codecov]: https://codecov.io/gh/yefrig/volga/branch/master/graph/badge.svg?token=0QW3OTFQD5
[codecov-page]: https://codecov.io/gh/yefrig/volga

[travis]: https://travis-ci.com/yefrig/volga.svg?branch=master
[build]: https://travis-ci.com/yefrig/volga

[license]: https://img.shields.io/github/license/yefrig/volga
[license-file]: https://github.com/yefrig/volga/blob/master/LICENSE

[release]: https://img.shields.io/github/v/release/yefrig/volga?include_prereleases&sort=semver
[releases]: https://github.com/yefrig/volga/releases

[python-version]: https://img.shields.io/pypi/pyversions/volga
[pypi]: https://pypi.org/project/volga/

[open-issues]: https://img.shields.io/github/issues/yefrig/volga
[issues]: https://github.com/yefrig/volga/issues

[stars]: https://img.shields.io/github/stars/yefrig/volga?style=social



## What is it?

**volga is a framework for *de*serializing Python data structures.**

---

volga will allow you to *flow* your data into any format that you'd like.

Example:
```python3
  import attr
  from volga import json
  
  # auto generated methods that conform to Serialize and Deserialize protocols
  @Serialize
  @Deserialize
  @attr.s(auto_attribs=True)
  class User():
    name: str
    age: int
    
  user: User = User('john', 43)
  
  serialized: str = json.to_string(user)
  print(serialized) # prints {"name":"john","age":43}
  
  deserialized: User = json.from_string(serialized)
  print(deserialized) # prints User(name='john', age=43)
```

## The volga Data Model
The data model serves as an API for data formats and your python objects to interact.

volga v0.2.0 supports the following types:
- dict
- list
- int
- float
- boolean
- str
- None

## Team Members

- Yefri Gaitan [@yefrig](https://github.com/yefrig)

 - Ecenaz (Jen) Ozmen [@eozmen410](https://github.com/eozmen410)
