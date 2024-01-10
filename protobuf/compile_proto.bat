REM Simple script to compile the ProtoBuff .proto file

set THISDIR=%~dp0

set SRC_DIR=%THISDIR%
set DST_DIR=%THISDIR%

protoc -I=%SRC_DIR% --python_out=%DST_DIR% %SRC_DIR%\ek80_datagrams_v2360.proto

