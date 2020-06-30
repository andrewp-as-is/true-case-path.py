__all__ = ['true_case_filename', 'true_case_path']


import os


def true_case_filename(path, filename):
    """return a string with case exact filename as stored in the filesystem"""
    if os.path.exists(os.path.join(path, filename)):
        return filename
    for l in os.listdir(path):
        if l.lower() == filename.lower():
            return l


def true_case_path(path):
    """return a string with case exact path as stored in the filesystem"""
    true_paths = []
    path = os.path.abspath(path)
    for filename in filter(None, path.split(os.sep)):
        _path = "/%s" % "/".join(true_paths + [filename])
        f = true_case_filename(os.path.dirname(_path), filename)
        if not f:
            return
        true_paths.append(f)
    return "/%s" % "/".join(true_paths)
