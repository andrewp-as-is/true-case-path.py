<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/true-case-path.svg?longCache=True)](https://pypi.org/project/true-case-path/)
[![](https://img.shields.io/pypi/v/true-case-path.svg?maxAge=3600)](https://pypi.org/project/true-case-path/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/true-case-path.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/true-case-path.py/)

#### Installation
```bash
$ [sudo] pip install true-case-path
```

#### Functions
function|`__doc__`
-|-
`true_case_path.true_case_filename(path, filename)` |return a string with case exact filename as stored in the filesystem
`true_case_path.true_case_path(path)` |return a string with case exact path as stored in the filesystem

#### Examples
```python
>>> from true_case_path import true_case_path
>>> true_case_path('/Users/username/downloads')
'/Users/username/Downloads'
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>