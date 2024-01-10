This folder contains the protobuf definition file for the Simrad EK80
echosounder application REST interface. The .proto file defines the
echosounder subscription datagrams and code generated from the .proto
file is used to serialize and deserialize the datagram data.

More info on protobuf can be found here: https://developers.google.com/protocol-buffers


Note that the EK80 REST API is still in development and subject to change.

As of v23.6.0, the subscription API is only partially implemented. The
following subscription datagrams are defined:

BottomDetectionDatagram
IntegrationDatagram
AdcpVelocityDatagram
AdcpOutputDatagram
BeamDataAdcpDatagram
QualityDataAdcpDatagram
BottomDetectionAdcpDatagram
SampleDataDatagram
EchogramDatagram
TSDetectionDatagram
TSDetectionChirpDatagram
SystemStateDatagram

Starting with version 23.6.0, it appears that the .proto file is distributed with
the EK80 application and can be found in C:\ProgramData\Simrad\EK80\RESTAPI