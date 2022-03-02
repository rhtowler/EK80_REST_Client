set executable=.\swagger-codegen-cli-2.4.9.jar

set JAVA_OPTS=%JAVA_OPTS% -Xmx1024M
set ags=generate -i .\EK80_data_server.yml -l python -o .\ek80_data_client -c EK80_data_config.json

java %JAVA_OPTS% -jar %executable% %ags%
