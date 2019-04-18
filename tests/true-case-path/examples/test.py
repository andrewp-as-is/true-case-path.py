#!/usr/bin/env python
import os
from nose.tools import eq_
from true_case_path import true_case_path

eq_(true_case_path(__file__.upper()), os.path.abspath(__file__))
eq_(true_case_path("/USR/Local"), "/usr/local")
eq_(true_case_path("/not-existing"), None)
