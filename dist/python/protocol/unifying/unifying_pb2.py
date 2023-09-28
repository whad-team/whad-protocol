# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protocol/unifying/unifying.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n protocol/unifying/unifying.proto\x12\x08unifying\"$\n\x11SetNodeAddressCmd\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\"K\n\x08SniffCmd\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0c\x12\x1d\n\x15show_acknowledgements\x18\x03 \x01(\x08\"\x19\n\x06JamCmd\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\"E\n\x07SendCmd\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\x12\x1c\n\x14retransmission_count\x18\x02 \x01(\r\x12\x0b\n\x03pdu\x18\x03 \x01(\x0c\"H\n\nSendRawCmd\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\x12\x1c\n\x14retransmission_count\x18\x02 \x01(\r\x12\x0b\n\x03pdu\x18\x03 \x01(\x0c\"(\n\x15LogitechDongleModeCmd\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\"*\n\x17LogitechKeyboardModeCmd\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\"\'\n\x14LogitechMouseModeCmd\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\"\n\n\x08StartCmd\"\t\n\x07StopCmd\"\x11\n\x0fSniffPairingCmd\"\x1b\n\x06Jammed\x12\x11\n\ttimestamp\x18\x01 \x01(\r\"\xbe\x01\n\x0eRawPduReceived\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\x12\x11\n\x04rssi\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x16\n\ttimestamp\x18\x03 \x01(\rH\x01\x88\x01\x01\x12\x19\n\x0c\x63rc_validity\x18\x04 \x01(\x08H\x02\x88\x01\x01\x12\x14\n\x07\x61\x64\x64ress\x18\x05 \x01(\x0cH\x03\x88\x01\x01\x12\x0b\n\x03pdu\x18\x06 \x01(\x0c\x42\x07\n\x05_rssiB\x0c\n\n_timestampB\x0f\n\r_crc_validityB\n\n\x08_address\"\xbb\x01\n\x0bPduReceived\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\x12\x11\n\x04rssi\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x16\n\ttimestamp\x18\x03 \x01(\rH\x01\x88\x01\x01\x12\x19\n\x0c\x63rc_validity\x18\x04 \x01(\x08H\x02\x88\x01\x01\x12\x14\n\x07\x61\x64\x64ress\x18\x05 \x01(\x0cH\x03\x88\x01\x01\x12\x0b\n\x03pdu\x18\x06 \x01(\x0c\x42\x07\n\x05_rssiB\x0c\n\n_timestampB\x0f\n\r_crc_validityB\n\n\x08_address\"\xea\x04\n\x07Message\x12\x34\n\rset_node_addr\x18\x01 \x01(\x0b\x32\x1b.unifying.SetNodeAddressCmdH\x00\x12#\n\x05sniff\x18\x02 \x01(\x0b\x32\x12.unifying.SniffCmdH\x00\x12\x1f\n\x03jam\x18\x03 \x01(\x0b\x32\x10.unifying.JamCmdH\x00\x12!\n\x04send\x18\x04 \x01(\x0b\x32\x11.unifying.SendCmdH\x00\x12(\n\x08send_raw\x18\x05 \x01(\x0b\x32\x14.unifying.SendRawCmdH\x00\x12\x31\n\x06\x64ongle\x18\x06 \x01(\x0b\x32\x1f.unifying.LogitechDongleModeCmdH\x00\x12\x35\n\x08keyboard\x18\x07 \x01(\x0b\x32!.unifying.LogitechKeyboardModeCmdH\x00\x12\x32\n\x05mouse\x18\x08 \x01(\x0b\x32!.unifying.LogitechKeyboardModeCmdH\x00\x12#\n\x05start\x18\t \x01(\x0b\x32\x12.unifying.StartCmdH\x00\x12!\n\x04stop\x18\n \x01(\x0b\x32\x11.unifying.StopCmdH\x00\x12\x32\n\rsniff_pairing\x18\x0e \x01(\x0b\x32\x19.unifying.SniffPairingCmdH\x00\x12\"\n\x06jammed\x18\x0b \x01(\x0b\x32\x10.unifying.JammedH\x00\x12+\n\x07raw_pdu\x18\x0c \x01(\x0b\x32\x18.unifying.RawPduReceivedH\x00\x12$\n\x03pdu\x18\r \x01(\x0b\x32\x15.unifying.PduReceivedH\x00\x42\x05\n\x03msg*\xc0\x01\n\x0fUnifyingCommand\x12\x12\n\x0eSetNodeAddress\x10\x00\x12\t\n\x05Sniff\x10\x01\x12\x07\n\x03Jam\x10\x02\x12\x08\n\x04Send\x10\x03\x12\x0b\n\x07SendRaw\x10\x04\x12\x16\n\x12LogitechDongleMode\x10\x05\x12\x18\n\x14LogitechKeyboardMode\x10\x06\x12\x15\n\x11LogitechMouseMode\x10\x07\x12\t\n\x05Start\x10\x08\x12\x08\n\x04Stop\x10\t\x12\x10\n\x0cSniffPairing\x10\nb\x06proto3')

_UNIFYINGCOMMAND = DESCRIPTOR.enum_types_by_name['UnifyingCommand']
UnifyingCommand = enum_type_wrapper.EnumTypeWrapper(_UNIFYINGCOMMAND)
SetNodeAddress = 0
Sniff = 1
Jam = 2
Send = 3
SendRaw = 4
LogitechDongleMode = 5
LogitechKeyboardMode = 6
LogitechMouseMode = 7
Start = 8
Stop = 9
SniffPairing = 10


_SETNODEADDRESSCMD = DESCRIPTOR.message_types_by_name['SetNodeAddressCmd']
_SNIFFCMD = DESCRIPTOR.message_types_by_name['SniffCmd']
_JAMCMD = DESCRIPTOR.message_types_by_name['JamCmd']
_SENDCMD = DESCRIPTOR.message_types_by_name['SendCmd']
_SENDRAWCMD = DESCRIPTOR.message_types_by_name['SendRawCmd']
_LOGITECHDONGLEMODECMD = DESCRIPTOR.message_types_by_name['LogitechDongleModeCmd']
_LOGITECHKEYBOARDMODECMD = DESCRIPTOR.message_types_by_name['LogitechKeyboardModeCmd']
_LOGITECHMOUSEMODECMD = DESCRIPTOR.message_types_by_name['LogitechMouseModeCmd']
_STARTCMD = DESCRIPTOR.message_types_by_name['StartCmd']
_STOPCMD = DESCRIPTOR.message_types_by_name['StopCmd']
_SNIFFPAIRINGCMD = DESCRIPTOR.message_types_by_name['SniffPairingCmd']
_JAMMED = DESCRIPTOR.message_types_by_name['Jammed']
_RAWPDURECEIVED = DESCRIPTOR.message_types_by_name['RawPduReceived']
_PDURECEIVED = DESCRIPTOR.message_types_by_name['PduReceived']
_MESSAGE = DESCRIPTOR.message_types_by_name['Message']
SetNodeAddressCmd = _reflection.GeneratedProtocolMessageType('SetNodeAddressCmd', (_message.Message,), {
  'DESCRIPTOR' : _SETNODEADDRESSCMD,
  '__module__' : 'protocol.unifying.unifying_pb2'
  # @@protoc_insertion_point(class_scope:unifying.SetNodeAddressCmd)
  })
_sym_db.RegisterMessage(SetNodeAddressCmd)

SniffCmd = _reflection.GeneratedProtocolMessageType('SniffCmd', (_message.Message,), {
  'DESCRIPTOR' : _SNIFFCMD,
  '__module__' : 'protocol.unifying.unifying_pb2'
  # @@protoc_insertion_point(class_scope:unifying.SniffCmd)
  })
_sym_db.RegisterMessage(SniffCmd)

JamCmd = _reflection.GeneratedProtocolMessageType('JamCmd', (_message.Message,), {
  'DESCRIPTOR' : _JAMCMD,
  '__module__' : 'protocol.unifying.unifying_pb2'
  # @@protoc_insertion_point(class_scope:unifying.JamCmd)
  })
_sym_db.RegisterMessage(JamCmd)

SendCmd = _reflection.GeneratedProtocolMessageType('SendCmd', (_message.Message,), {
  'DESCRIPTOR' : _SENDCMD,
  '__module__' : 'protocol.unifying.unifying_pb2'
  # @@protoc_insertion_point(class_scope:unifying.SendCmd)
  })
_sym_db.RegisterMessage(SendCmd)

SendRawCmd = _reflection.GeneratedProtocolMessageType('SendRawCmd', (_message.Message,), {
  'DESCRIPTOR' : _SENDRAWCMD,
  '__module__' : 'protocol.unifying.unifying_pb2'
  # @@protoc_insertion_point(class_scope:unifying.SendRawCmd)
  })
_sym_db.RegisterMessage(SendRawCmd)

LogitechDongleModeCmd = _reflection.GeneratedProtocolMessageType('LogitechDongleModeCmd', (_message.Message,), {
  'DESCRIPTOR' : _LOGITECHDONGLEMODECMD,
  '__module__' : 'protocol.unifying.unifying_pb2'
  # @@protoc_insertion_point(class_scope:unifying.LogitechDongleModeCmd)
  })
_sym_db.RegisterMessage(LogitechDongleModeCmd)

LogitechKeyboardModeCmd = _reflection.GeneratedProtocolMessageType('LogitechKeyboardModeCmd', (_message.Message,), {
  'DESCRIPTOR' : _LOGITECHKEYBOARDMODECMD,
  '__module__' : 'protocol.unifying.unifying_pb2'
  # @@protoc_insertion_point(class_scope:unifying.LogitechKeyboardModeCmd)
  })
_sym_db.RegisterMessage(LogitechKeyboardModeCmd)

LogitechMouseModeCmd = _reflection.GeneratedProtocolMessageType('LogitechMouseModeCmd', (_message.Message,), {
  'DESCRIPTOR' : _LOGITECHMOUSEMODECMD,
  '__module__' : 'protocol.unifying.unifying_pb2'
  # @@protoc_insertion_point(class_scope:unifying.LogitechMouseModeCmd)
  })
_sym_db.RegisterMessage(LogitechMouseModeCmd)

StartCmd = _reflection.GeneratedProtocolMessageType('StartCmd', (_message.Message,), {
  'DESCRIPTOR' : _STARTCMD,
  '__module__' : 'protocol.unifying.unifying_pb2'
  # @@protoc_insertion_point(class_scope:unifying.StartCmd)
  })
_sym_db.RegisterMessage(StartCmd)

StopCmd = _reflection.GeneratedProtocolMessageType('StopCmd', (_message.Message,), {
  'DESCRIPTOR' : _STOPCMD,
  '__module__' : 'protocol.unifying.unifying_pb2'
  # @@protoc_insertion_point(class_scope:unifying.StopCmd)
  })
_sym_db.RegisterMessage(StopCmd)

SniffPairingCmd = _reflection.GeneratedProtocolMessageType('SniffPairingCmd', (_message.Message,), {
  'DESCRIPTOR' : _SNIFFPAIRINGCMD,
  '__module__' : 'protocol.unifying.unifying_pb2'
  # @@protoc_insertion_point(class_scope:unifying.SniffPairingCmd)
  })
_sym_db.RegisterMessage(SniffPairingCmd)

Jammed = _reflection.GeneratedProtocolMessageType('Jammed', (_message.Message,), {
  'DESCRIPTOR' : _JAMMED,
  '__module__' : 'protocol.unifying.unifying_pb2'
  # @@protoc_insertion_point(class_scope:unifying.Jammed)
  })
_sym_db.RegisterMessage(Jammed)

RawPduReceived = _reflection.GeneratedProtocolMessageType('RawPduReceived', (_message.Message,), {
  'DESCRIPTOR' : _RAWPDURECEIVED,
  '__module__' : 'protocol.unifying.unifying_pb2'
  # @@protoc_insertion_point(class_scope:unifying.RawPduReceived)
  })
_sym_db.RegisterMessage(RawPduReceived)

PduReceived = _reflection.GeneratedProtocolMessageType('PduReceived', (_message.Message,), {
  'DESCRIPTOR' : _PDURECEIVED,
  '__module__' : 'protocol.unifying.unifying_pb2'
  # @@protoc_insertion_point(class_scope:unifying.PduReceived)
  })
_sym_db.RegisterMessage(PduReceived)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'protocol.unifying.unifying_pb2'
  # @@protoc_insertion_point(class_scope:unifying.Message)
  })
_sym_db.RegisterMessage(Message)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _UNIFYINGCOMMAND._serialized_start=1536
  _UNIFYINGCOMMAND._serialized_end=1728
  _SETNODEADDRESSCMD._serialized_start=46
  _SETNODEADDRESSCMD._serialized_end=82
  _SNIFFCMD._serialized_start=84
  _SNIFFCMD._serialized_end=159
  _JAMCMD._serialized_start=161
  _JAMCMD._serialized_end=186
  _SENDCMD._serialized_start=188
  _SENDCMD._serialized_end=257
  _SENDRAWCMD._serialized_start=259
  _SENDRAWCMD._serialized_end=331
  _LOGITECHDONGLEMODECMD._serialized_start=333
  _LOGITECHDONGLEMODECMD._serialized_end=373
  _LOGITECHKEYBOARDMODECMD._serialized_start=375
  _LOGITECHKEYBOARDMODECMD._serialized_end=417
  _LOGITECHMOUSEMODECMD._serialized_start=419
  _LOGITECHMOUSEMODECMD._serialized_end=458
  _STARTCMD._serialized_start=460
  _STARTCMD._serialized_end=470
  _STOPCMD._serialized_start=472
  _STOPCMD._serialized_end=481
  _SNIFFPAIRINGCMD._serialized_start=483
  _SNIFFPAIRINGCMD._serialized_end=500
  _JAMMED._serialized_start=502
  _JAMMED._serialized_end=529
  _RAWPDURECEIVED._serialized_start=532
  _RAWPDURECEIVED._serialized_end=722
  _PDURECEIVED._serialized_start=725
  _PDURECEIVED._serialized_end=912
  _MESSAGE._serialized_start=915
  _MESSAGE._serialized_end=1533
# @@protoc_insertion_point(module_scope)
