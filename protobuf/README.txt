This folder contains the protobuf definition file for the Simrad EK80
echosounder application REST interface. The .proto file defines the
echosounder subscription datagrams and code generated from the .proto
file is used to serialize and deserialize the datagram data.

More info on protobuf can be found here: https://developers.google.com/protocol-buffers


Note that the EK80 REST API is still in development and subject to change.

As of v21.15, the subscription API is only partially implemented. The
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