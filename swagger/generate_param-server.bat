REM As of 1/2024, the newest version of swagger-codegen (2.4.39) generates
REM a broken python library. While newer versions may work, version 2.4.9
REM is known to work and it is the version used to generate the client libraries.
set executable=.\swagger-codegen-cli-2.4.9.jar

set JAVA_OPTS=%JAVA_OPTS% -Xmx1024M
set ags=generate -i .\EK80_param_server_23.6.json -l python -o .\ek80_param_client -c EK80_param_config.json

java %JAVA_OPTS% -jar %executable% %ags%
