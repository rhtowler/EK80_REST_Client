# EK80_REST_Client
### A Python based client for the Simrad EK80 Echosounder

Release 21.15 of the EK80 scientific echosounder application introduced a new REST-ful API for application control and data subscription. The API is described using the swagger/OpenAPI spec allowing clients to be auto-generated using swagger-codegen. This project aims to wrap the "data" and "parameter" thin clients into a single, er, thicker, client for general purpose command and control of EK80 systems using Python.

The client is in the very early stages of development but does currently support bottom detection subscriptions. The intent is to add subscription types and methods for getting/setting operational parameters as needed.

## Example
Check out basic_example.py for an example of how to use the client in an application.

```plaintext
C:\Users\rick.towler\Work\AFSCGit\EK80_REST_Client>python ./basic_example.py --server 192.168.0.131
['WBT 998500-15 ES18_ES', 'WBT 978217-15 ES38-7_ES', 'WBT 978213-15 ES70-7C_ES', 'WBT 976714-15 ES120-7C_ES', 'WBT 978208-15 ES200-7C_ES']
{'subscriptionId': '57', 'pingNumber': 21644, 'pingTime': datetime.datetime(2021, 3, 7, 1, 8, 13, 332297), 'dataSource': 'test', 'bottomDepth': 269.4148485775577, 'reflectivity': -42.356527750963096, 'vesselLogDistance': 927.7324919444445, 'transducerDepth': 8.969446316870961}
{'subscriptionId': '57', 'pingNumber': 21645, 'pingTime': datetime.datetime(2021, 3, 7, 1, 8, 14, 411416), 'dataSource': 'test', 'bottomDepth': 269.20092634885754, 'reflectivity': -42.56642095250384, 'vesselLogDistance': 927.7351270555556, 'transducerDepth': 8.809882235559853}
{'subscriptionId': '57', 'pingNumber': 21646, 'pingTime': datetime.datetime(2021, 3, 7, 1, 8, 15, 509735), 'dataSource': 'test', 'bottomDepth': 268.67797428407516, 'reflectivity': -42.45373304946418, 'vesselLogDistance': 927.7378086111112, 'transducerDepth': 8.809882235559853}
{'subscriptionId': '57', 'pingNumber': 21647, 'pingTime': datetime.datetime(2021, 3, 7, 1, 8, 16, 610332), 'dataSource': 'test', 'bottomDepth': 269.25330715872997, 'reflectivity': -42.56751345119521, 'vesselLogDistance': 927.740356888889, 'transducerDepth': 9.96814909122822}
CTRL-C detected. Shutting down...
Cleaning up the client...
Client cleanup complete.
Application exiting...
```

## Python Dependencies

* Python > 3.5
* PyQt5
* certifi >= 2017.4.17
* python-dateutil >= 2.1
* urllib3 >= 1.23
* six >= 1.10
* [pyzmq](https://pypi.org/project/pyzmq/)
* [protobuf](https://pypi.org/project/protobuf/)

You must also install the ek80_data_client and ek80_param_client packages that are part of this package.

```plaintext
C:\Users\rick.towler\Work\AFSCGit\EK80_REST_Client>cd ek80_data_client
C:\Users\rick.towler\Work\AFSCGit\EK80_REST_Client\ek80_data_client>ls -l
total 139
-rw-r--r-- 1 rick.towler NMFS+Group(513) 39590 Mar  2 08:56 README.md
drwxr-xr-x 1 rick.towler NMFS+Group(513)     0 Mar  2 10:51 build
drwxr-xr-x 1 rick.towler NMFS+Group(513)     0 Mar  2 08:56 docs
drwxr-xr-x 1 rick.towler NMFS+Group(513)     0 Mar  2 08:56 ek80_data_client
drwxr-xr-x 1 rick.towler NMFS+Group(513)     0 Mar  2 10:51 ek80_data_client.egg-info
-rwxr-xr-x 1 rick.towler NMFS+Group(513)  1663 Mar  2 08:56 git_push.sh
-rw-r--r-- 1 rick.towler NMFS+Group(513)    96 Mar  2 08:56 requirements.txt
-rw-r--r-- 1 rick.towler NMFS+Group(513)  1640 Mar  2 08:56 setup.py
drwxr-xr-x 1 rick.towler NMFS+Group(513)     0 Mar  2 08:56 test
-rw-r--r-- 1 rick.towler NMFS+Group(513)    69 Mar  2 08:56 test-requirements.txt
-rw-r--r-- 1 rick.towler NMFS+Group(513)   149 Mar  2 08:56 tox.ini

C:\Users\rick.towler\Work\AFSCGit\EK80_REST_Client\ek80_data_client>pip install .
Processing c:\users\rick.towler\work\afscgit\ek80_rest_client\ek80_data_client
  Preparing metadata (setup.py) ... done
Requirement already satisfied: certifi>=2017.4.17 in c:\wpy64-3890\python-3.8.9.amd64\lib\site-packages (from ek80-data-client==0.1.0) (2020.12.5)
Requirement already satisfied: python-dateutil>=2.1 in c:\wpy64-3890\python-3.8.9.amd64\lib\site-packages (from ek80-data-client==0.1.0) (2.8.1)
Requirement already satisfied: six>=1.10 in c:\wpy64-3890\python-3.8.9.amd64\lib\site-packages (from ek80-data-client==0.1.0) (1.15.0)
Requirement already satisfied: urllib3>=1.23 in c:\wpy64-3890\python-3.8.9.amd64\lib\site-packages (from ek80-data-client==0.1.0) (1.26.4)
Building wheels for collected packages: ek80-data-client
  Building wheel for ek80-data-client (setup.py) ... done
  Created wheel for ek80-data-client: filename=ek80_data_client-0.1.0-py3-none-any.whl size=257946 sha256=5ff9183007a2995cc4f3c2eb3ba7ba816040fcad69953579f8c76f738b622036
  Stored in directory: C:\Users\rick.towler\AppData\Local\Temp\pip-ephem-wheel-cache-ngt4rhqf\wheels\85\c8\5c\2a0639f04a6d4ac7541d074ab6dab5a40d739015fd10a391d9
Successfully built ek80-data-client
Installing collected packages: ek80-data-client
Successfully installed ek80-data-client-0.1.0
```