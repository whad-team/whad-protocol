# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protocol/device.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15protocol/device.proto\x12\tdiscovery\"\x12\n\x10\x44\x65viceResetQuery\"\x11\n\x0f\x44\x65viceReadyResp\"\"\n\x11SetTransportSpeed\x12\r\n\x05speed\x18\x01 \x01(\r\"\xe0\x01\n\x0e\x44\x65viceInfoResp\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\r\n\x05\x64\x65vid\x18\x02 \x01(\x0c\x12\x15\n\rproto_min_ver\x18\x03 \x01(\r\x12\x11\n\tmax_speed\x18\x04 \x01(\r\x12\x11\n\tfw_author\x18\x05 \x01(\x0c\x12\x0e\n\x06\x66w_url\x18\x06 \x01(\x0c\x12\x18\n\x10\x66w_version_major\x18\x07 \x01(\r\x12\x18\n\x10\x66w_version_minor\x18\x08 \x01(\r\x12\x16\n\x0e\x66w_version_rev\x18\t \x01(\r\x12\x18\n\x0c\x63\x61pabilities\x18\n \x03(\rB\x02\x10\x01\"B\n\x14\x44\x65viceDomainInfoResp\x12\x0e\n\x06\x64omain\x18\x01 \x01(\r\x12\x1a\n\x12supported_commands\x18\x02 \x01(\x04\"$\n\x0f\x44\x65viceInfoQuery\x12\x11\n\tproto_ver\x18\x01 \x01(\r\"\'\n\x15\x44\x65viceDomainInfoQuery\x12\x0e\n\x06\x64omain\x18\x01 \x01(\r\"\xfd\x02\n\x07Message\x12\x32\n\x0breset_query\x18\x01 \x01(\x0b\x32\x1b.discovery.DeviceResetQueryH\x00\x12\x30\n\nready_resp\x18\x02 \x01(\x0b\x32\x1a.discovery.DeviceReadyRespH\x00\x12\x30\n\ninfo_query\x18\x03 \x01(\x0b\x32\x1a.discovery.DeviceInfoQueryH\x00\x12.\n\tinfo_resp\x18\x04 \x01(\x0b\x32\x19.discovery.DeviceInfoRespH\x00\x12\x38\n\x0c\x64omain_query\x18\x05 \x01(\x0b\x32 .discovery.DeviceDomainInfoQueryH\x00\x12\x36\n\x0b\x64omain_resp\x18\x06 \x01(\x0b\x32\x1f.discovery.DeviceDomainInfoRespH\x00\x12\x31\n\tset_speed\x18\x07 \x01(\x0b\x32\x1c.discovery.SetTransportSpeedH\x00\x42\x05\n\x03msg*\xc9\x01\n\x06\x44omain\x12\x0f\n\x0b_DomainNone\x10\x00\x12\x0e\n\x07Generic\x10\x80\x80\x80\x08\x12\x10\n\tBtClassic\x10\x80\x80\x80\x10\x12\x0b\n\x04\x42tLE\x10\x80\x80\x80\x18\x12\r\n\x06Zigbee\x10\x80\x80\x80 \x12\x10\n\tSixLowPan\x10\x80\x80\x80(\x12\n\n\x03\x45sb\x10\x80\x80\x80\x30\x12\x17\n\x10LogitechUnifying\x10\x80\x80\x80\x38\x12\r\n\x06Mosart\x10\x80\x80\x80@\x12\n\n\x03\x41NT\x10\x80\x80\x80H\x12\x0f\n\x08\x41NT_Plus\x10\x80\x80\x80P\x12\r\n\x06\x41NT_FS\x10\x80\x80\x80X*P\n\nDeviceType\x12\x12\n\x0e\x45sp32BleFuzzer\x10\x00\x12\r\n\tButterfly\x10\x01\x12\x0c\n\x08\x42tleJack\x10\x02\x12\x11\n\rVirtualDevice\x10\x04*|\n\nCapability\x12\x0c\n\x08_CapNone\x10\x00\x12\x08\n\x04Scan\x10\x01\x12\t\n\x05Sniff\x10\x02\x12\n\n\x06Inject\x10\x04\x12\x07\n\x03Jam\x10\x08\x12\n\n\x06Hijack\x10\x10\x12\x08\n\x04Hook\x10 \x12\x10\n\x0cSimulateRole\x10@\x12\x0e\n\tNoRawData\x10\x80\x01\x62\x06proto3')

_DOMAIN = DESCRIPTOR.enum_types_by_name['Domain']
Domain = enum_type_wrapper.EnumTypeWrapper(_DOMAIN)
_DEVICETYPE = DESCRIPTOR.enum_types_by_name['DeviceType']
DeviceType = enum_type_wrapper.EnumTypeWrapper(_DEVICETYPE)
_CAPABILITY = DESCRIPTOR.enum_types_by_name['Capability']
Capability = enum_type_wrapper.EnumTypeWrapper(_CAPABILITY)
_DomainNone = 0
Generic = 16777216
BtClassic = 33554432
BtLE = 50331648
Zigbee = 67108864
SixLowPan = 83886080
Esb = 100663296
LogitechUnifying = 117440512
Mosart = 134217728
ANT = 150994944
ANT_Plus = 167772160
ANT_FS = 184549376
Esp32BleFuzzer = 0
Butterfly = 1
BtleJack = 2
VirtualDevice = 4
_CapNone = 0
Scan = 1
Sniff = 2
Inject = 4
Jam = 8
Hijack = 16
Hook = 32
SimulateRole = 64
NoRawData = 128


_DEVICERESETQUERY = DESCRIPTOR.message_types_by_name['DeviceResetQuery']
_DEVICEREADYRESP = DESCRIPTOR.message_types_by_name['DeviceReadyResp']
_SETTRANSPORTSPEED = DESCRIPTOR.message_types_by_name['SetTransportSpeed']
_DEVICEINFORESP = DESCRIPTOR.message_types_by_name['DeviceInfoResp']
_DEVICEDOMAININFORESP = DESCRIPTOR.message_types_by_name['DeviceDomainInfoResp']
_DEVICEINFOQUERY = DESCRIPTOR.message_types_by_name['DeviceInfoQuery']
_DEVICEDOMAININFOQUERY = DESCRIPTOR.message_types_by_name['DeviceDomainInfoQuery']
_MESSAGE = DESCRIPTOR.message_types_by_name['Message']
DeviceResetQuery = _reflection.GeneratedProtocolMessageType('DeviceResetQuery', (_message.Message,), {
  'DESCRIPTOR' : _DEVICERESETQUERY,
  '__module__' : 'protocol.device_pb2'
  # @@protoc_insertion_point(class_scope:discovery.DeviceResetQuery)
  })
_sym_db.RegisterMessage(DeviceResetQuery)

DeviceReadyResp = _reflection.GeneratedProtocolMessageType('DeviceReadyResp', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEREADYRESP,
  '__module__' : 'protocol.device_pb2'
  # @@protoc_insertion_point(class_scope:discovery.DeviceReadyResp)
  })
_sym_db.RegisterMessage(DeviceReadyResp)

SetTransportSpeed = _reflection.GeneratedProtocolMessageType('SetTransportSpeed', (_message.Message,), {
  'DESCRIPTOR' : _SETTRANSPORTSPEED,
  '__module__' : 'protocol.device_pb2'
  # @@protoc_insertion_point(class_scope:discovery.SetTransportSpeed)
  })
_sym_db.RegisterMessage(SetTransportSpeed)

DeviceInfoResp = _reflection.GeneratedProtocolMessageType('DeviceInfoResp', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEINFORESP,
  '__module__' : 'protocol.device_pb2'
  # @@protoc_insertion_point(class_scope:discovery.DeviceInfoResp)
  })
_sym_db.RegisterMessage(DeviceInfoResp)

DeviceDomainInfoResp = _reflection.GeneratedProtocolMessageType('DeviceDomainInfoResp', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEDOMAININFORESP,
  '__module__' : 'protocol.device_pb2'
  # @@protoc_insertion_point(class_scope:discovery.DeviceDomainInfoResp)
  })
_sym_db.RegisterMessage(DeviceDomainInfoResp)

DeviceInfoQuery = _reflection.GeneratedProtocolMessageType('DeviceInfoQuery', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEINFOQUERY,
  '__module__' : 'protocol.device_pb2'
  # @@protoc_insertion_point(class_scope:discovery.DeviceInfoQuery)
  })
_sym_db.RegisterMessage(DeviceInfoQuery)

DeviceDomainInfoQuery = _reflection.GeneratedProtocolMessageType('DeviceDomainInfoQuery', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEDOMAININFOQUERY,
  '__module__' : 'protocol.device_pb2'
  # @@protoc_insertion_point(class_scope:discovery.DeviceDomainInfoQuery)
  })
_sym_db.RegisterMessage(DeviceDomainInfoQuery)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'protocol.device_pb2'
  # @@protoc_insertion_point(class_scope:discovery.Message)
  })
_sym_db.RegisterMessage(Message)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DEVICEINFORESP.fields_by_name['capabilities']._options = None
  _DEVICEINFORESP.fields_by_name['capabilities']._serialized_options = b'\020\001'
  _DOMAIN._serialized_start=870
  _DOMAIN._serialized_end=1071
  _DEVICETYPE._serialized_start=1073
  _DEVICETYPE._serialized_end=1153
  _CAPABILITY._serialized_start=1155
  _CAPABILITY._serialized_end=1279
  _DEVICERESETQUERY._serialized_start=36
  _DEVICERESETQUERY._serialized_end=54
  _DEVICEREADYRESP._serialized_start=56
  _DEVICEREADYRESP._serialized_end=73
  _SETTRANSPORTSPEED._serialized_start=75
  _SETTRANSPORTSPEED._serialized_end=109
  _DEVICEINFORESP._serialized_start=112
  _DEVICEINFORESP._serialized_end=336
  _DEVICEDOMAININFORESP._serialized_start=338
  _DEVICEDOMAININFORESP._serialized_end=404
  _DEVICEINFOQUERY._serialized_start=406
  _DEVICEINFOQUERY._serialized_end=442
  _DEVICEDOMAININFOQUERY._serialized_start=444
  _DEVICEDOMAININFOQUERY._serialized_end=483
  _MESSAGE._serialized_start=486
  _MESSAGE._serialized_end=867
# @@protoc_insertion_point(module_scope)
