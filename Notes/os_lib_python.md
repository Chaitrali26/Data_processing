# OS library Methods:

**1. Listing Files & Directories**

| Method   | Description |
| -------- | ------- |
| os.listdir(path) | Returns a list of files & directories in path. |
| os.scandir(path)	            | Returns an iterator of DirEntry objects for files & directories in path. |
| glob.glob(pattern)	           | Returns a list of files matching a pattern (e.g., "*.txt"). |
| pathlib.Path(path).iterdir()	| Returns an iterator of Path objects for files & directories in path. |
|  |  |

**2. Joining & Manipulating Paths**

| Method   | Description |
| -------- | ------- |
| os.path.join(dir, file) | Joins directory & file names into a full path. |
| os.path.abspath(path) | Returns the absolute path of path. |
| os.path.dirname(path) | Returns the directory part of path. |
| os.path.basename(path) | Returns the filename part of path. |
| os.path.exists(path) | Checks if path exists (file or directory). |
| os.path.isfile(path) | Checks if path is a file. |
| os.path.isdir(path) | Checks if path is a directory. |
| pathlib.Path(path).resolve() | Returns the absolute path using pathlib. |

**3. Walking Through Directories**

| Method   | Description |
| -------- | ------- |
| os.walk(top) | Recursively lists directories & files under top. |
| pathlib.Path(path).rglob(pattern) | Recursively finds files matching a pattern. |

**4. File Operations**

| Method   | Description |
| -------- | ------- |
| shutil.copy(src, dst) | Copies a file from src to dst. |
| shutil.move(src, dst) | Moves a file or directory to dst. |
| shutil.rmtree(path) | Deletes a directory and all its contents. |
| os.remove(path) | Deletes a file. |
| os.rename(src, dst) | Renames/moves a file or directory. |
| open(path, "r") | Opens a file for reading. |

**5. Getting File Information**

| Method   | Description |
| -------- | ------- |
| os.stat(path)|Returns file metadata like size, modified time, etc. |
| os.path.getsize(path)	| Returns the size of a file in bytes. |
| os.path.getmtime(path)| 	Returns the last modified time of a file. |
| os.path.getctime(path)| 	Returns the creation time of a file. |
