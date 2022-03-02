set executable=.\swagger-codegen-cli-2.4.9.jar

set JAVA_OPTS=%JAVA_OPTS% -Xmx1024M
set ags=generate -i .\EK80_param_server.yml -l python -o .\ek80_param_client -c EK80_param_config.json

java %JAVA_OPTS% -jar %executable% %ags%
