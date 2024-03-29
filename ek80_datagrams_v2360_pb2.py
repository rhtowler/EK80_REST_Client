# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ek80_datagrams_v2360.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x65k80_datagrams_v2360.proto\x12\x02\x64p\x1a\x19google/protobuf/any.proto\",\n\x0e\x43omplexFloat32\x12\x0c\n\x04real\x18\x01 \x01(\x02\x12\x0c\n\x04imag\x18\x02 \x01(\x02\"8\n\x13\x43omplex1Float32Data\x12!\n\x05value\x18\x01 \x01(\x0b\x32\x12.dp.ComplexFloat32\"\xa5\x01\n\x13\x43omplex4Float32Data\x12\"\n\x06value1\x18\x01 \x01(\x0b\x32\x12.dp.ComplexFloat32\x12\"\n\x06value2\x18\x02 \x01(\x0b\x32\x12.dp.ComplexFloat32\x12\"\n\x06value3\x18\x03 \x01(\x0b\x32\x12.dp.ComplexFloat32\x12\"\n\x06value4\x18\x04 \x01(\x0b\x32\x12.dp.ComplexFloat32\".\n\x0ePowerAngleData\x12\r\n\x05power\x18\x01 \x01(\x05\x12\r\n\x05\x61ngle\x18\x02 \x01(\x05\"\x1a\n\tShortData\x12\r\n\x05value\x18\x01 \x01(\x05\"\x1c\n\x0b\x46loat32Data\x12\r\n\x05value\x18\x01 \x01(\x02\"\xe8\x01\n\x17\x42ottomDetectionDatagram\x12\x17\n\x0fsubscription_id\x18\x01 \x01(\x04\x12\x13\n\x0bping_number\x18\x02 \x01(\r\x12\x11\n\tping_time\x18\x03 \x01(\x04\x12\x13\n\x0b\x64\x61ta_source\x18\x04 \x01(\t\x12\x14\n\x0c\x62ottom_depth\x18\x05 \x01(\x01\x12\x14\n\x0creflectivity\x18\x06 \x01(\x01\x12\x1b\n\x13vessel_log_distance\x18\x07 \x01(\x01\x12\x18\n\x10transducer_depth\x18\x08 \x01(\x01\x12\x14\n\x0cquality_flag\x18\t \x01(\x05\"\xed\x01\n\x13IntegrationDatagram\x12\x17\n\x0fsubscription_id\x18\x01 \x01(\x04\x12\x13\n\x0bping_number\x18\x02 \x01(\r\x12\x11\n\tping_time\x18\x03 \x01(\x04\x12\x13\n\x0b\x64\x61ta_source\x18\x04 \x01(\t\x12\x14\n\x0cstatus_value\x18\x05 \x01(\x05\x12\n\n\x02sa\x18\x06 \x01(\x01\x12\x10\n\x08\x64istance\x18\x07 \x01(\x01\x12\x18\n\x10\x66requency_limits\x18\x08 \x03(\x02\x12\x16\n\x0espectrum_count\x18\t \x01(\r\x12\x1a\n\x12\x66requency_spectrum\x18\n \x03(\x02\"\x94\x03\n\x14\x41\x64\x63pVelocityDatagram\x12\x13\n\x0b\x64\x61tagram_id\x18\x01 \x01(\r\x12\x15\n\rdatagram_size\x18\x02 \x01(\r\x12\x13\n\x0bping_number\x18\x03 \x01(\r\x12\x11\n\tping_time\x18\x04 \x01(\x04\x12\x13\n\x0b\x64\x61ta_source\x18\x05 \x01(\t\x12\x13\n\x0bstart_range\x18\x06 \x01(\x02\x12\x13\n\x0btotal_range\x18\x07 \x01(\x02\x12\x18\n\x10transducer_depth\x18\x08 \x01(\x02\x12\x17\n\x0f\x64\x65pth_to_bottom\x18\t \x03(\x02\x12\x15\n\rblanking_zone\x18\n \x01(\x02\x12\x19\n\x11\x63\x65ll_size_samples\x18\x0b \x01(\r\x12\x19\n\x11processing_result\x18\x0c \x01(\r\x12\x1c\n\x14is_valid_bottom_data\x18\r \x01(\x08\x12%\n\tdata_last\x18\x0e \x03(\x0b\x32\x12.dp.VelocityVector\x12$\n\x08\x64\x61ta_avg\x18\x0f \x03(\x0b\x32\x12.dp.VelocityVector\"1\n\x0eVelocityVector\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"\xa6\x02\n\x12\x41\x64\x63pOutputDatagram\x12\x13\n\x0b\x64\x61tagram_id\x18\x01 \x01(\r\x12\x15\n\rdatagram_size\x18\x02 \x01(\r\x12\x13\n\x0bping_number\x18\x03 \x01(\r\x12\x11\n\tping_time\x18\x04 \x01(\x04\x12\x13\n\x0b\x64\x61ta_source\x18\x05 \x01(\t\x12\x13\n\x0bstart_range\x18\x06 \x01(\x02\x12\x13\n\x0btotal_range\x18\x07 \x01(\x02\x12(\n\x08velocity\x18\x08 \x03(\x0b\x32\x16.dp.BeamAdcpDoubleData\x12+\n\x0b\x63orrelation\x18\t \x03(\x0b\x32\x16.dp.BeamAdcpDoubleData\x12&\n\tintensity\x18\n \x03(\x0b\x32\x13.dp.BeamAdcpIntData\".\n\x12\x42\x65\x61mAdcpDoubleData\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x02 \x03(\x01\"+\n\x0f\x42\x65\x61mAdcpIntData\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x02 \x03(\x05\"\xcb\x01\n\x14\x42\x65\x61mDataAdcpDatagram\x12\x13\n\x0b\x64\x61tagram_id\x18\x01 \x01(\r\x12\x15\n\rdatagram_size\x18\x02 \x01(\r\x12\x13\n\x0bping_number\x18\x03 \x01(\r\x12\x11\n\tping_time\x18\x04 \x01(\x04\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x13\n\x0bstart_range\x18\x06 \x01(\x02\x12\x13\n\x0btotal_range\x18\x07 \x01(\x02\x12\x19\n\x11processing_result\x18\x08 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\t \x03(\x01\"\xd9\x02\n\x17QualityDataAdcpDatagram\x12\x13\n\x0b\x64\x61tagram_id\x18\x01 \x01(\r\x12\x15\n\rdatagram_size\x18\x02 \x01(\r\x12\x13\n\x0bping_number\x18\x03 \x01(\r\x12\x11\n\tping_time\x18\x04 \x01(\x04\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x13\n\x0bstart_range\x18\x06 \x01(\x02\x12\x13\n\x0btotal_range\x18\x07 \x01(\x02\x12\x19\n\x11processing_result\x18\x08 \x01(\x05\x12\x14\n\x0cpercent_good\x18\t \x01(\x02\x12 \n\x18\x63orrelation_factor_limit\x18\n \x01(\x02\x12\x1c\n\x14\x65rror_velocity_limit\x18\x0b \x01(\x02\x12\x18\n\x10sv_dbw_low_limit\x18\x0c \x01(\x05\x12\x19\n\x11sv_dbw_high_limit\x18\r \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x0e \x03(\x01\"\xe4\x02\n\x1b\x42ottomDetectionAdcpDatagram\x12\x13\n\x0b\x64\x61tagram_id\x18\x01 \x01(\r\x12\x15\n\rdatagram_size\x18\x02 \x01(\r\x12\x13\n\x0bping_number\x18\x03 \x01(\r\x12\x11\n\tping_time\x18\x04 \x01(\x04\x12\x1c\n\x14is_valid_bottom_data\x18\x05 \x01(\x08\x12)\n!slant_range_to_bottom_backscatter\x18\x06 \x03(\x02\x12)\n!slant_range_to_bottom_correlation\x18\x07 \x03(\x02\x12#\n\x1b\x64\x65pth_to_bottom_correlation\x18\x08 \x03(\x02\x12\x18\n\x10transducer_depth\x18\t \x01(\x02\x12\x1a\n\x12\x62ottom_depth_index\x18\n \x03(\x05\x12\"\n\x1ais_bottom_detection_active\x18\x0b \x01(\x08\"\x86\x04\n\x12SampleDataDatagram\x12\x17\n\x0fsubscription_id\x18\x01 \x01(\x04\x12\x13\n\x0bping_number\x18\x02 \x01(\r\x12\x11\n\tping_time\x18\x03 \x01(\x04\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0bstart_index\x18\x05 \x01(\x04\x12\x1f\n\x17total_number_of_samples\x18\x06 \x01(\x04\x12\x13\n\x0btotal_range\x18\x07 \x01(\x02\x12\x18\n\x10\x63\x65nter_frequency\x18\x08 \x01(\x02\x12<\n\x0b\x64\x61ta_format\x18\t \x01(\x0e\x32\'.dp.SampleDataDatagram.SampleDataFormat\x12\x1a\n\x04\x64\x61ta\x18\n \x03(\x0b\x32\x0c.dp.BeamData\"\xe1\x01\n\x10SampleDataFormat\x12\n\n\x06NoData\x10\x00\x12\x0e\n\nPowerAngle\x10\x01\x12\x13\n\x0f\x43omplex1Float16\x10\x02\x12\x13\n\x0f\x43omplex4Float16\x10\x03\x12\x13\n\x0f\x43omplex1Float32\x10\x04\x12\x13\n\x0f\x43omplex3Float32\x10\x05\x12\x13\n\x0f\x43omplex4Float32\x10\x06\x12\x15\n\x11MixedPowerComplex\x10\x07\x12\x19\n\x15\x41veragedFrequencyData\x10\x08\x12\t\n\x05Short\x10\t\x12\x0b\n\x07\x46loat32\x10\n\"b\n\x08\x42\x65\x61mData\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x11\n\tbeam_name\x18\x02 \x01(\t\x12\x13\n\x0bnum_samples\x18\x03 \x01(\x04\x12\"\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\x14.google.protobuf.Any\"\x87\x02\n\x10\x45\x63hogramDatagram\x12\x17\n\x0fsubscription_id\x18\x01 \x01(\x04\x12\x13\n\x0bping_number\x18\x02 \x01(\r\x12\x11\n\tping_time\x18\x03 \x01(\x04\x12\x13\n\x0b\x64\x61ta_source\x18\x04 \x01(\t\x12\x13\n\x0bstart_index\x18\x05 \x01(\x03\x12\x1f\n\x17total_number_of_samples\x18\x06 \x01(\x03\x12\x13\n\x0bstart_range\x18\x07 \x01(\x02\x12\x13\n\x0btotal_range\x18\x08 \x01(\x02\x12\x14\n\x0c\x62ottom_depth\x18\t \x01(\x02\x12\x19\n\x11processing_result\x18\n \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x0b \x03(\x05\"\xa4\x01\n\x13TSDetectionDatagram\x12\x17\n\x0fsubscription_id\x18\x01 \x01(\x04\x12\x13\n\x0bping_number\x18\x02 \x01(\r\x12\x11\n\tping_time\x18\x03 \x01(\x04\x12\x13\n\x0b\x64\x61ta_source\x18\x04 \x01(\t\x12\x18\n\x10\x66requency_limits\x18\x05 \x03(\x02\x12\x1d\n\x06traces\x18\x06 \x03(\x0b\x32\r.dp.EchoTrace\"\xae\x01\n\x18TSDetectionChirpDatagram\x12\x17\n\x0fsubscription_id\x18\x01 \x01(\x04\x12\x13\n\x0bping_number\x18\x02 \x01(\r\x12\x11\n\tping_time\x18\x03 \x01(\x04\x12\x13\n\x0b\x64\x61ta_source\x18\x04 \x01(\t\x12\x18\n\x10\x66requency_limits\x18\x05 \x03(\x02\x12\"\n\x06traces\x18\x06 \x03(\x0b\x32\x12.dp.EchoTraceChirp\"\x89\x02\n\x0e\x45\x63hoTraceChirp\x12\r\n\x05\x64\x65pth\x18\x01 \x01(\x01\x12\x16\n\x0ets_compensated\x18\x02 \x01(\x01\x12\x18\n\x10ts_uncompensated\x18\x03 \x01(\x01\x12\x17\n\x0f\x61longship_angle\x18\x04 \x01(\x01\x12\x19\n\x11\x61thwartship_angle\x18\x05 \x01(\x01\x12\n\n\x02sa\x18\x06 \x01(\x01\x12&\n\x1e\x63ompensated_frequency_response\x18\x07 \x03(\x02\x12(\n uncompensated_frequency_response\x18\x08 \x03(\x02\x12$\n\x1cwithin_max_beam_compensation\x18\t \x03(\x05\"\x8c\x01\n\tEchoTrace\x12\r\n\x05\x64\x65pth\x18\x01 \x01(\x01\x12\x16\n\x0ets_compensated\x18\x02 \x01(\x01\x12\x18\n\x10ts_uncompensated\x18\x03 \x01(\x01\x12\x17\n\x0f\x61longship_angle\x18\x04 \x01(\x01\x12\x19\n\x11\x61thwartship_angle\x18\x05 \x01(\x01\x12\n\n\x02sa\x18\x06 \x01(\x01\"\xbf\x01\n\x08PingInfo\x12\x13\n\x0bping_number\x18\x01 \x01(\r\x12\x11\n\tping_time\x18\x02 \x01(\x04\x12\x10\n\x08latitude\x18\x03 \x01(\x01\x12\x11\n\tlongitude\x18\x04 \x01(\x01\x12\x0f\n\x07heading\x18\x05 \x01(\x02\x12\x0e\n\x06\x63ourse\x18\x06 \x01(\x02\x12\x19\n\x11speed_over_ground\x18\x07 \x01(\x02\x12\r\n\x05heave\x18\x08 \x01(\x02\x12\r\n\x05pitch\x18\t \x01(\x02\x12\x0c\n\x04roll\x18\n \x01(\x02\"F\n\x0c\x45xternalSync\x12\'\n\tsync_mode\x18\x01 \x01(\x0e\x32\x14.dp.ExternalSyncMode\x12\r\n\x05\x64\x65lay\x18\x02 \x01(\x05\"\xde\x01\n\x10OperationalState\x12)\n\x0eoperation_mode\x18\x01 \x01(\x0e\x32\x11.dp.OperationMode\x12\x1f\n\tping_mode\x18\x02 \x01(\x0e\x32\x0c.dp.PingMode\x12!\n\nplay_state\x18\x03 \x01(\x0e\x32\r.dp.PlayState\x12\x15\n\rping_interval\x18\x04 \x01(\x05\x12\'\n\rexternal_sync\x18\x05 \x01(\x0b\x32\x10.dp.ExternalSync\x12\x1b\n\x13\x61\x63tive_user_setting\x18\x06 \x01(\t\"t\n\x0eNavigationData\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\r\n\x05\x64\x65pth\x18\x03 \x01(\x02\x12\r\n\x05speed\x18\x04 \x01(\x02\x12\x0e\n\x06\x63ourse\x18\x05 \x01(\x02\x12\x0f\n\x07heading\x18\x06 \x01(\x02\"b\n\nMotionData\x12\r\n\x05heave\x18\x01 \x01(\x02\x12\r\n\x05pitch\x18\x02 \x01(\x02\x12\x0c\n\x04roll\x18\x03 \x01(\x02\x12\x0c\n\x04sway\x18\x04 \x01(\x02\x12\r\n\x05surge\x18\x05 \x01(\x02\x12\x0b\n\x03yaw\x18\x06 \x01(\x02\"\x9e\x02\n\x13SystemStateDatagram\x12\x17\n\x0fsubscription_id\x18\x01 \x01(\x04\x12\x14\n\x0c\x63urrent_time\x18\x02 \x01(\x04\x12.\n\x12\x63urrent_navigation\x18\x03 \x01(\x0b\x32\x12.dp.NavigationData\x12&\n\x0e\x63urrent_motion\x18\x04 \x01(\x0b\x32\x0e.dp.MotionData\x12\x37\n\x19\x63urrent_operational_state\x18\x05 \x01(\x0b\x32\x14.dp.OperationalState\x12&\n\x1eping_configuration_change_hint\x18\x06 \x01(\t\x12\x1f\n\tlast_ping\x18\x07 \x01(\x0b\x32\x0c.dp.PingInfo*E\n\rOperationMode\x12\x0c\n\x08Inactive\x10\x00\x12\n\n\x06Normal\x10\x01\x12\n\n\x06Replay\x10\x02\x12\x0e\n\nSimulation\x10\x03*4\n\x08PingMode\x12\x0e\n\nSinglePing\x10\x00\x12\x0b\n\x07Intervl\x10\x01\x12\x0b\n\x07Maximum\x10\x02*1\n\tPlayState\x12\x0b\n\x07Stopped\x10\x00\x12\x0b\n\x07Running\x10\x01\x12\n\n\x06Paused\x10\x02*9\n\x10\x45xternalSyncMode\x12\x0e\n\nStandAlone\x10\x00\x12\n\n\x06Master\x10\x01\x12\t\n\x05Slave\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ek80_datagrams_v2360_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_OPERATIONMODE']._serialized_start=5315
  _globals['_OPERATIONMODE']._serialized_end=5384
  _globals['_PINGMODE']._serialized_start=5386
  _globals['_PINGMODE']._serialized_end=5438
  _globals['_PLAYSTATE']._serialized_start=5440
  _globals['_PLAYSTATE']._serialized_end=5489
  _globals['_EXTERNALSYNCMODE']._serialized_start=5491
  _globals['_EXTERNALSYNCMODE']._serialized_end=5548
  _globals['_COMPLEXFLOAT32']._serialized_start=61
  _globals['_COMPLEXFLOAT32']._serialized_end=105
  _globals['_COMPLEX1FLOAT32DATA']._serialized_start=107
  _globals['_COMPLEX1FLOAT32DATA']._serialized_end=163
  _globals['_COMPLEX4FLOAT32DATA']._serialized_start=166
  _globals['_COMPLEX4FLOAT32DATA']._serialized_end=331
  _globals['_POWERANGLEDATA']._serialized_start=333
  _globals['_POWERANGLEDATA']._serialized_end=379
  _globals['_SHORTDATA']._serialized_start=381
  _globals['_SHORTDATA']._serialized_end=407
  _globals['_FLOAT32DATA']._serialized_start=409
  _globals['_FLOAT32DATA']._serialized_end=437
  _globals['_BOTTOMDETECTIONDATAGRAM']._serialized_start=440
  _globals['_BOTTOMDETECTIONDATAGRAM']._serialized_end=672
  _globals['_INTEGRATIONDATAGRAM']._serialized_start=675
  _globals['_INTEGRATIONDATAGRAM']._serialized_end=912
  _globals['_ADCPVELOCITYDATAGRAM']._serialized_start=915
  _globals['_ADCPVELOCITYDATAGRAM']._serialized_end=1319
  _globals['_VELOCITYVECTOR']._serialized_start=1321
  _globals['_VELOCITYVECTOR']._serialized_end=1370
  _globals['_ADCPOUTPUTDATAGRAM']._serialized_start=1373
  _globals['_ADCPOUTPUTDATAGRAM']._serialized_end=1667
  _globals['_BEAMADCPDOUBLEDATA']._serialized_start=1669
  _globals['_BEAMADCPDOUBLEDATA']._serialized_end=1715
  _globals['_BEAMADCPINTDATA']._serialized_start=1717
  _globals['_BEAMADCPINTDATA']._serialized_end=1760
  _globals['_BEAMDATAADCPDATAGRAM']._serialized_start=1763
  _globals['_BEAMDATAADCPDATAGRAM']._serialized_end=1966
  _globals['_QUALITYDATAADCPDATAGRAM']._serialized_start=1969
  _globals['_QUALITYDATAADCPDATAGRAM']._serialized_end=2314
  _globals['_BOTTOMDETECTIONADCPDATAGRAM']._serialized_start=2317
  _globals['_BOTTOMDETECTIONADCPDATAGRAM']._serialized_end=2673
  _globals['_SAMPLEDATADATAGRAM']._serialized_start=2676
  _globals['_SAMPLEDATADATAGRAM']._serialized_end=3194
  _globals['_SAMPLEDATADATAGRAM_SAMPLEDATAFORMAT']._serialized_start=2969
  _globals['_SAMPLEDATADATAGRAM_SAMPLEDATAFORMAT']._serialized_end=3194
  _globals['_BEAMDATA']._serialized_start=3196
  _globals['_BEAMDATA']._serialized_end=3294
  _globals['_ECHOGRAMDATAGRAM']._serialized_start=3297
  _globals['_ECHOGRAMDATAGRAM']._serialized_end=3560
  _globals['_TSDETECTIONDATAGRAM']._serialized_start=3563
  _globals['_TSDETECTIONDATAGRAM']._serialized_end=3727
  _globals['_TSDETECTIONCHIRPDATAGRAM']._serialized_start=3730
  _globals['_TSDETECTIONCHIRPDATAGRAM']._serialized_end=3904
  _globals['_ECHOTRACECHIRP']._serialized_start=3907
  _globals['_ECHOTRACECHIRP']._serialized_end=4172
  _globals['_ECHOTRACE']._serialized_start=4175
  _globals['_ECHOTRACE']._serialized_end=4315
  _globals['_PINGINFO']._serialized_start=4318
  _globals['_PINGINFO']._serialized_end=4509
  _globals['_EXTERNALSYNC']._serialized_start=4511
  _globals['_EXTERNALSYNC']._serialized_end=4581
  _globals['_OPERATIONALSTATE']._serialized_start=4584
  _globals['_OPERATIONALSTATE']._serialized_end=4806
  _globals['_NAVIGATIONDATA']._serialized_start=4808
  _globals['_NAVIGATIONDATA']._serialized_end=4924
  _globals['_MOTIONDATA']._serialized_start=4926
  _globals['_MOTIONDATA']._serialized_end=5024
  _globals['_SYSTEMSTATEDATAGRAM']._serialized_start=5027
  _globals['_SYSTEMSTATEDATAGRAM']._serialized_end=5313
# @@protoc_insertion_point(module_scope)
