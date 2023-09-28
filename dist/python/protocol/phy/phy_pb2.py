# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protocol/phy/phy.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16protocol/phy/phy.proto\x12\x03phy\"\"\n\x13SetASKModulationCmd\x12\x0b\n\x03ook\x18\x01 \x01(\x08\"(\n\x13SetFSKModulationCmd\x12\x11\n\tdeviation\x18\x01 \x01(\r\")\n\x14Set4FSKModulationCmd\x12\x11\n\tdeviation\x18\x01 \x01(\r\")\n\x14SetGFSKModulationCmd\x12\x11\n\tdeviation\x18\x01 \x01(\r\"(\n\x13SetMSKModulationCmd\x12\x11\n\tdeviation\x18\x01 \x01(\r\"\x16\n\x14SetBPSKModulationCmd\"+\n\x14SetQPSKModulationCmd\x12\x13\n\x0boffset_qpsk\x18\x01 \x01(\x08\"\x9b\x01\n\x14SetLoRaModulationCmd\x12%\n\tbandwidth\x18\x01 \x01(\x0e\x32\x12.phy.LoRaBandwidth\x12\x32\n\x10spreading_factor\x18\x02 \x01(\x0e\x32\x18.phy.LoRaSpreadingFactor\x12(\n\x0b\x63oding_rate\x18\x03 \x01(\x0e\x32\x13.phy.LoRaCodingRate\"\x1c\n\x1aGetSupportedFrequenciesCmd\"$\n\x0fSetFrequencyCmd\x12\x11\n\tfrequency\x18\x01 \x01(\r\"\x1e\n\x0eSetDataRateCmd\x12\x0c\n\x04rate\x18\x01 \x01(\r\"7\n\x10SetEndiannessCmd\x12#\n\nendianness\x18\x01 \x01(\x0e\x32\x0f.phy.Endianness\"/\n\rSetTXPowerCmd\x12\x1e\n\x08tx_power\x18\x01 \x01(\x0e\x32\x0c.phy.TXPower\"\'\n\x10SetPacketSizeCmd\x12\x13\n\x0bpacket_size\x18\x01 \x01(\r\"#\n\x0eSetSyncWordCmd\x12\x11\n\tsync_word\x18\x01 \x01(\x0c\"0\n\x08SniffCmd\x12\x16\n\tiq_stream\x18\x01 \x01(\x08H\x00\x88\x01\x01\x42\x0c\n\n_iq_stream\"\x19\n\x07SendCmd\x12\x0e\n\x06packet\x18\x01 \x01(\x0c\"\x1c\n\nSendRawCmd\x12\x0e\n\x02iq\x18\x01 \x03(\x05\x42\x02\x10\x01\"\n\n\x08StartCmd\"\t\n\x07StopCmd\"(\n\x06JamCmd\x12\x1e\n\x04mode\x18\x01 \x01(\x0e\x32\x10.phy.JammingMode\"\x0c\n\nMonitorCmd\"u\n\x0ePacketReceived\x12\x11\n\tfrequency\x18\x01 \x01(\r\x12\x11\n\x04rssi\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x16\n\ttimestamp\x18\x03 \x01(\rH\x01\x88\x01\x01\x12\x0e\n\x06packet\x18\x04 \x01(\x0c\x42\x07\n\x05_rssiB\x0c\n\n_timestamp\"\x88\x01\n\x11RawPacketReceived\x12\x11\n\tfrequency\x18\x01 \x01(\r\x12\x11\n\x04rssi\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x16\n\ttimestamp\x18\x03 \x01(\rH\x01\x88\x01\x01\x12\x0e\n\x06packet\x18\x04 \x01(\x0c\x12\x0e\n\x02iq\x18\x05 \x03(\x05\x42\x02\x10\x01\x42\x07\n\x05_rssiB\x0c\n\n_timestamp\"\x1b\n\x06Jammed\x12\x11\n\ttimestamp\x18\x01 \x01(\r\"9\n\x10MonitoringReport\x12\x11\n\ttimestamp\x18\x01 \x01(\r\x12\x12\n\x06report\x18\x02 \x03(\rB\x02\x10\x01\"\x90\x01\n\x18SupportedFrequencyRanges\x12\x46\n\x10\x66requency_ranges\x18\x01 \x03(\x0b\x32,.phy.SupportedFrequencyRanges.FrequencyRange\x1a,\n\x0e\x46requencyRange\x12\r\n\x05start\x18\x01 \x01(\r\x12\x0b\n\x03\x65nd\x18\x02 \x01(\r\"\x80\t\n\x07Message\x12+\n\x07mod_ask\x18\x01 \x01(\x0b\x32\x18.phy.SetASKModulationCmdH\x00\x12+\n\x07mod_fsk\x18\x02 \x01(\x0b\x32\x18.phy.SetFSKModulationCmdH\x00\x12-\n\x08mod_gfsk\x18\x03 \x01(\x0b\x32\x19.phy.SetGFSKModulationCmdH\x00\x12-\n\x08mod_bpsk\x18\x04 \x01(\x0b\x32\x19.phy.SetBPSKModulationCmdH\x00\x12-\n\x08mod_qpsk\x18\x05 \x01(\x0b\x32\x19.phy.SetQPSKModulationCmdH\x00\x12-\n\x08mod_4fsk\x18\x06 \x01(\x0b\x32\x19.phy.Set4FSKModulationCmdH\x00\x12+\n\x07mod_msk\x18\x07 \x01(\x0b\x32\x18.phy.SetMSKModulationCmdH\x00\x12=\n\x12get_supported_freq\x18\x08 \x01(\x0b\x32\x1f.phy.GetSupportedFrequenciesCmdH\x00\x12(\n\x08set_freq\x18\t \x01(\x0b\x32\x14.phy.SetFrequencyCmdH\x00\x12\'\n\x08\x64\x61tarate\x18\n \x01(\x0b\x32\x13.phy.SetDataRateCmdH\x00\x12+\n\nendianness\x18\x0b \x01(\x0b\x32\x15.phy.SetEndiannessCmdH\x00\x12&\n\x08tx_power\x18\x0c \x01(\x0b\x32\x12.phy.SetTXPowerCmdH\x00\x12,\n\x0bpacket_size\x18\r \x01(\x0b\x32\x15.phy.SetPacketSizeCmdH\x00\x12(\n\tsync_word\x18\x0e \x01(\x0b\x32\x13.phy.SetSyncWordCmdH\x00\x12\x1e\n\x05sniff\x18\x0f \x01(\x0b\x32\r.phy.SniffCmdH\x00\x12\x1c\n\x04send\x18\x10 \x01(\x0b\x32\x0c.phy.SendCmdH\x00\x12#\n\x08send_raw\x18\x11 \x01(\x0b\x32\x0f.phy.SendRawCmdH\x00\x12\x1e\n\x05start\x18\x12 \x01(\x0b\x32\r.phy.StartCmdH\x00\x12\x1c\n\x04stop\x18\x13 \x01(\x0b\x32\x0c.phy.StopCmdH\x00\x12\x1a\n\x03jam\x18\x14 \x01(\x0b\x32\x0b.phy.JamCmdH\x00\x12\"\n\x07monitor\x18\x15 \x01(\x0b\x32\x0f.phy.MonitorCmdH\x00\x12%\n\x06packet\x18\x16 \x01(\x0b\x32\x13.phy.PacketReceivedH\x00\x12,\n\nraw_packet\x18\x17 \x01(\x0b\x32\x16.phy.RawPacketReceivedH\x00\x12\x1d\n\x06jammed\x18\x18 \x01(\x0b\x32\x0b.phy.JammedH\x00\x12/\n\x0emonitor_report\x18\x19 \x01(\x0b\x32\x15.phy.MonitoringReportH\x00\x12\x37\n\x0esupported_freq\x18\x1a \x01(\x0b\x32\x1d.phy.SupportedFrequencyRangesH\x00\x12-\n\x08mod_lora\x18\x1b \x01(\x0b\x32\x19.phy.SetLoRaModulationCmdH\x00\x42\x05\n\x03msg*\x95\x03\n\nPhyCommand\x12\x14\n\x10SetASKModulation\x10\x00\x12\x14\n\x10SetFSKModulation\x10\x01\x12\x15\n\x11SetGFSKModulation\x10\x02\x12\x15\n\x11SetBPSKModulation\x10\x03\x12\x15\n\x11SetQPSKModulation\x10\x04\x12\x15\n\x11Set4FSKModulation\x10\x05\x12\x14\n\x10SetMSKModulation\x10\x06\x12\x1b\n\x17GetSupportedFrequencies\x10\x07\x12\x10\n\x0cSetFrequency\x10\x08\x12\x0f\n\x0bSetDataRate\x10\t\x12\x11\n\rSetEndianness\x10\n\x12\x0e\n\nSetTXPower\x10\x0b\x12\x11\n\rSetPacketSize\x10\x0c\x12\x0f\n\x0bSetSyncWord\x10\r\x12\t\n\x05Sniff\x10\x0e\x12\x08\n\x04Send\x10\x0f\x12\x0b\n\x07SendRaw\x10\x10\x12\x07\n\x03Jam\x10\x11\x12\x0b\n\x07Monitor\x10\x12\x12\t\n\x05Start\x10\x13\x12\x08\n\x04Stop\x10\x14\x12\x15\n\x11SetLoRaModulation\x10\x15*!\n\nEndianness\x12\x07\n\x03\x42IG\x10\x00\x12\n\n\x06LITTLE\x10\x01*(\n\x07TXPower\x12\x07\n\x03LOW\x10\x00\x12\n\n\x06MEDIUM\x10\x01\x12\x08\n\x04HIGH\x10\x02*+\n\x0bJammingMode\x12\x0e\n\nCONTINUOUS\x10\x00\x12\x0c\n\x08REACTIVE\x10\x01*N\n\x13LoRaSpreadingFactor\x12\x07\n\x03SF7\x10\x00\x12\x07\n\x03SF8\x10\x01\x12\x07\n\x03SF9\x10\x02\x12\x08\n\x04SF10\x10\x03\x12\x08\n\x04SF11\x10\x04\x12\x08\n\x04SF12\x10\x05*8\n\x0eLoRaCodingRate\x12\x08\n\x04\x43R45\x10\x00\x12\x08\n\x04\x43R46\x10\x01\x12\x08\n\x04\x43R47\x10\x02\x12\x08\n\x04\x43R48\x10\x03*0\n\rLoRaBandwidth\x12\t\n\x05\x42W125\x10\x00\x12\t\n\x05\x42W250\x10\x01\x12\t\n\x05\x42W500\x10\x02\x62\x06proto3')

_PHYCOMMAND = DESCRIPTOR.enum_types_by_name['PhyCommand']
PhyCommand = enum_type_wrapper.EnumTypeWrapper(_PHYCOMMAND)
_ENDIANNESS = DESCRIPTOR.enum_types_by_name['Endianness']
Endianness = enum_type_wrapper.EnumTypeWrapper(_ENDIANNESS)
_TXPOWER = DESCRIPTOR.enum_types_by_name['TXPower']
TXPower = enum_type_wrapper.EnumTypeWrapper(_TXPOWER)
_JAMMINGMODE = DESCRIPTOR.enum_types_by_name['JammingMode']
JammingMode = enum_type_wrapper.EnumTypeWrapper(_JAMMINGMODE)
_LORASPREADINGFACTOR = DESCRIPTOR.enum_types_by_name['LoRaSpreadingFactor']
LoRaSpreadingFactor = enum_type_wrapper.EnumTypeWrapper(_LORASPREADINGFACTOR)
_LORACODINGRATE = DESCRIPTOR.enum_types_by_name['LoRaCodingRate']
LoRaCodingRate = enum_type_wrapper.EnumTypeWrapper(_LORACODINGRATE)
_LORABANDWIDTH = DESCRIPTOR.enum_types_by_name['LoRaBandwidth']
LoRaBandwidth = enum_type_wrapper.EnumTypeWrapper(_LORABANDWIDTH)
SetASKModulation = 0
SetFSKModulation = 1
SetGFSKModulation = 2
SetBPSKModulation = 3
SetQPSKModulation = 4
Set4FSKModulation = 5
SetMSKModulation = 6
GetSupportedFrequencies = 7
SetFrequency = 8
SetDataRate = 9
SetEndianness = 10
SetTXPower = 11
SetPacketSize = 12
SetSyncWord = 13
Sniff = 14
Send = 15
SendRaw = 16
Jam = 17
Monitor = 18
Start = 19
Stop = 20
SetLoRaModulation = 21
BIG = 0
LITTLE = 1
LOW = 0
MEDIUM = 1
HIGH = 2
CONTINUOUS = 0
REACTIVE = 1
SF7 = 0
SF8 = 1
SF9 = 2
SF10 = 3
SF11 = 4
SF12 = 5
CR45 = 0
CR46 = 1
CR47 = 2
CR48 = 3
BW125 = 0
BW250 = 1
BW500 = 2


_SETASKMODULATIONCMD = DESCRIPTOR.message_types_by_name['SetASKModulationCmd']
_SETFSKMODULATIONCMD = DESCRIPTOR.message_types_by_name['SetFSKModulationCmd']
_SET4FSKMODULATIONCMD = DESCRIPTOR.message_types_by_name['Set4FSKModulationCmd']
_SETGFSKMODULATIONCMD = DESCRIPTOR.message_types_by_name['SetGFSKModulationCmd']
_SETMSKMODULATIONCMD = DESCRIPTOR.message_types_by_name['SetMSKModulationCmd']
_SETBPSKMODULATIONCMD = DESCRIPTOR.message_types_by_name['SetBPSKModulationCmd']
_SETQPSKMODULATIONCMD = DESCRIPTOR.message_types_by_name['SetQPSKModulationCmd']
_SETLORAMODULATIONCMD = DESCRIPTOR.message_types_by_name['SetLoRaModulationCmd']
_GETSUPPORTEDFREQUENCIESCMD = DESCRIPTOR.message_types_by_name['GetSupportedFrequenciesCmd']
_SETFREQUENCYCMD = DESCRIPTOR.message_types_by_name['SetFrequencyCmd']
_SETDATARATECMD = DESCRIPTOR.message_types_by_name['SetDataRateCmd']
_SETENDIANNESSCMD = DESCRIPTOR.message_types_by_name['SetEndiannessCmd']
_SETTXPOWERCMD = DESCRIPTOR.message_types_by_name['SetTXPowerCmd']
_SETPACKETSIZECMD = DESCRIPTOR.message_types_by_name['SetPacketSizeCmd']
_SETSYNCWORDCMD = DESCRIPTOR.message_types_by_name['SetSyncWordCmd']
_SNIFFCMD = DESCRIPTOR.message_types_by_name['SniffCmd']
_SENDCMD = DESCRIPTOR.message_types_by_name['SendCmd']
_SENDRAWCMD = DESCRIPTOR.message_types_by_name['SendRawCmd']
_STARTCMD = DESCRIPTOR.message_types_by_name['StartCmd']
_STOPCMD = DESCRIPTOR.message_types_by_name['StopCmd']
_JAMCMD = DESCRIPTOR.message_types_by_name['JamCmd']
_MONITORCMD = DESCRIPTOR.message_types_by_name['MonitorCmd']
_PACKETRECEIVED = DESCRIPTOR.message_types_by_name['PacketReceived']
_RAWPACKETRECEIVED = DESCRIPTOR.message_types_by_name['RawPacketReceived']
_JAMMED = DESCRIPTOR.message_types_by_name['Jammed']
_MONITORINGREPORT = DESCRIPTOR.message_types_by_name['MonitoringReport']
_SUPPORTEDFREQUENCYRANGES = DESCRIPTOR.message_types_by_name['SupportedFrequencyRanges']
_SUPPORTEDFREQUENCYRANGES_FREQUENCYRANGE = _SUPPORTEDFREQUENCYRANGES.nested_types_by_name['FrequencyRange']
_MESSAGE = DESCRIPTOR.message_types_by_name['Message']
SetASKModulationCmd = _reflection.GeneratedProtocolMessageType('SetASKModulationCmd', (_message.Message,), {
  'DESCRIPTOR' : _SETASKMODULATIONCMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.SetASKModulationCmd)
  })
_sym_db.RegisterMessage(SetASKModulationCmd)

SetFSKModulationCmd = _reflection.GeneratedProtocolMessageType('SetFSKModulationCmd', (_message.Message,), {
  'DESCRIPTOR' : _SETFSKMODULATIONCMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.SetFSKModulationCmd)
  })
_sym_db.RegisterMessage(SetFSKModulationCmd)

Set4FSKModulationCmd = _reflection.GeneratedProtocolMessageType('Set4FSKModulationCmd', (_message.Message,), {
  'DESCRIPTOR' : _SET4FSKMODULATIONCMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.Set4FSKModulationCmd)
  })
_sym_db.RegisterMessage(Set4FSKModulationCmd)

SetGFSKModulationCmd = _reflection.GeneratedProtocolMessageType('SetGFSKModulationCmd', (_message.Message,), {
  'DESCRIPTOR' : _SETGFSKMODULATIONCMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.SetGFSKModulationCmd)
  })
_sym_db.RegisterMessage(SetGFSKModulationCmd)

SetMSKModulationCmd = _reflection.GeneratedProtocolMessageType('SetMSKModulationCmd', (_message.Message,), {
  'DESCRIPTOR' : _SETMSKMODULATIONCMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.SetMSKModulationCmd)
  })
_sym_db.RegisterMessage(SetMSKModulationCmd)

SetBPSKModulationCmd = _reflection.GeneratedProtocolMessageType('SetBPSKModulationCmd', (_message.Message,), {
  'DESCRIPTOR' : _SETBPSKMODULATIONCMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.SetBPSKModulationCmd)
  })
_sym_db.RegisterMessage(SetBPSKModulationCmd)

SetQPSKModulationCmd = _reflection.GeneratedProtocolMessageType('SetQPSKModulationCmd', (_message.Message,), {
  'DESCRIPTOR' : _SETQPSKMODULATIONCMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.SetQPSKModulationCmd)
  })
_sym_db.RegisterMessage(SetQPSKModulationCmd)

SetLoRaModulationCmd = _reflection.GeneratedProtocolMessageType('SetLoRaModulationCmd', (_message.Message,), {
  'DESCRIPTOR' : _SETLORAMODULATIONCMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.SetLoRaModulationCmd)
  })
_sym_db.RegisterMessage(SetLoRaModulationCmd)

GetSupportedFrequenciesCmd = _reflection.GeneratedProtocolMessageType('GetSupportedFrequenciesCmd', (_message.Message,), {
  'DESCRIPTOR' : _GETSUPPORTEDFREQUENCIESCMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.GetSupportedFrequenciesCmd)
  })
_sym_db.RegisterMessage(GetSupportedFrequenciesCmd)

SetFrequencyCmd = _reflection.GeneratedProtocolMessageType('SetFrequencyCmd', (_message.Message,), {
  'DESCRIPTOR' : _SETFREQUENCYCMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.SetFrequencyCmd)
  })
_sym_db.RegisterMessage(SetFrequencyCmd)

SetDataRateCmd = _reflection.GeneratedProtocolMessageType('SetDataRateCmd', (_message.Message,), {
  'DESCRIPTOR' : _SETDATARATECMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.SetDataRateCmd)
  })
_sym_db.RegisterMessage(SetDataRateCmd)

SetEndiannessCmd = _reflection.GeneratedProtocolMessageType('SetEndiannessCmd', (_message.Message,), {
  'DESCRIPTOR' : _SETENDIANNESSCMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.SetEndiannessCmd)
  })
_sym_db.RegisterMessage(SetEndiannessCmd)

SetTXPowerCmd = _reflection.GeneratedProtocolMessageType('SetTXPowerCmd', (_message.Message,), {
  'DESCRIPTOR' : _SETTXPOWERCMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.SetTXPowerCmd)
  })
_sym_db.RegisterMessage(SetTXPowerCmd)

SetPacketSizeCmd = _reflection.GeneratedProtocolMessageType('SetPacketSizeCmd', (_message.Message,), {
  'DESCRIPTOR' : _SETPACKETSIZECMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.SetPacketSizeCmd)
  })
_sym_db.RegisterMessage(SetPacketSizeCmd)

SetSyncWordCmd = _reflection.GeneratedProtocolMessageType('SetSyncWordCmd', (_message.Message,), {
  'DESCRIPTOR' : _SETSYNCWORDCMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.SetSyncWordCmd)
  })
_sym_db.RegisterMessage(SetSyncWordCmd)

SniffCmd = _reflection.GeneratedProtocolMessageType('SniffCmd', (_message.Message,), {
  'DESCRIPTOR' : _SNIFFCMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.SniffCmd)
  })
_sym_db.RegisterMessage(SniffCmd)

SendCmd = _reflection.GeneratedProtocolMessageType('SendCmd', (_message.Message,), {
  'DESCRIPTOR' : _SENDCMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.SendCmd)
  })
_sym_db.RegisterMessage(SendCmd)

SendRawCmd = _reflection.GeneratedProtocolMessageType('SendRawCmd', (_message.Message,), {
  'DESCRIPTOR' : _SENDRAWCMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.SendRawCmd)
  })
_sym_db.RegisterMessage(SendRawCmd)

StartCmd = _reflection.GeneratedProtocolMessageType('StartCmd', (_message.Message,), {
  'DESCRIPTOR' : _STARTCMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.StartCmd)
  })
_sym_db.RegisterMessage(StartCmd)

StopCmd = _reflection.GeneratedProtocolMessageType('StopCmd', (_message.Message,), {
  'DESCRIPTOR' : _STOPCMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.StopCmd)
  })
_sym_db.RegisterMessage(StopCmd)

JamCmd = _reflection.GeneratedProtocolMessageType('JamCmd', (_message.Message,), {
  'DESCRIPTOR' : _JAMCMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.JamCmd)
  })
_sym_db.RegisterMessage(JamCmd)

MonitorCmd = _reflection.GeneratedProtocolMessageType('MonitorCmd', (_message.Message,), {
  'DESCRIPTOR' : _MONITORCMD,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.MonitorCmd)
  })
_sym_db.RegisterMessage(MonitorCmd)

PacketReceived = _reflection.GeneratedProtocolMessageType('PacketReceived', (_message.Message,), {
  'DESCRIPTOR' : _PACKETRECEIVED,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.PacketReceived)
  })
_sym_db.RegisterMessage(PacketReceived)

RawPacketReceived = _reflection.GeneratedProtocolMessageType('RawPacketReceived', (_message.Message,), {
  'DESCRIPTOR' : _RAWPACKETRECEIVED,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.RawPacketReceived)
  })
_sym_db.RegisterMessage(RawPacketReceived)

Jammed = _reflection.GeneratedProtocolMessageType('Jammed', (_message.Message,), {
  'DESCRIPTOR' : _JAMMED,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.Jammed)
  })
_sym_db.RegisterMessage(Jammed)

MonitoringReport = _reflection.GeneratedProtocolMessageType('MonitoringReport', (_message.Message,), {
  'DESCRIPTOR' : _MONITORINGREPORT,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.MonitoringReport)
  })
_sym_db.RegisterMessage(MonitoringReport)

SupportedFrequencyRanges = _reflection.GeneratedProtocolMessageType('SupportedFrequencyRanges', (_message.Message,), {

  'FrequencyRange' : _reflection.GeneratedProtocolMessageType('FrequencyRange', (_message.Message,), {
    'DESCRIPTOR' : _SUPPORTEDFREQUENCYRANGES_FREQUENCYRANGE,
    '__module__' : 'protocol.phy.phy_pb2'
    # @@protoc_insertion_point(class_scope:phy.SupportedFrequencyRanges.FrequencyRange)
    })
  ,
  'DESCRIPTOR' : _SUPPORTEDFREQUENCYRANGES,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.SupportedFrequencyRanges)
  })
_sym_db.RegisterMessage(SupportedFrequencyRanges)
_sym_db.RegisterMessage(SupportedFrequencyRanges.FrequencyRange)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'protocol.phy.phy_pb2'
  # @@protoc_insertion_point(class_scope:phy.Message)
  })
_sym_db.RegisterMessage(Message)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SENDRAWCMD.fields_by_name['iq']._options = None
  _SENDRAWCMD.fields_by_name['iq']._serialized_options = b'\020\001'
  _RAWPACKETRECEIVED.fields_by_name['iq']._options = None
  _RAWPACKETRECEIVED.fields_by_name['iq']._serialized_options = b'\020\001'
  _MONITORINGREPORT.fields_by_name['report']._options = None
  _MONITORINGREPORT.fields_by_name['report']._serialized_options = b'\020\001'
  _PHYCOMMAND._serialized_start=2583
  _PHYCOMMAND._serialized_end=2988
  _ENDIANNESS._serialized_start=2990
  _ENDIANNESS._serialized_end=3023
  _TXPOWER._serialized_start=3025
  _TXPOWER._serialized_end=3065
  _JAMMINGMODE._serialized_start=3067
  _JAMMINGMODE._serialized_end=3110
  _LORASPREADINGFACTOR._serialized_start=3112
  _LORASPREADINGFACTOR._serialized_end=3190
  _LORACODINGRATE._serialized_start=3192
  _LORACODINGRATE._serialized_end=3248
  _LORABANDWIDTH._serialized_start=3250
  _LORABANDWIDTH._serialized_end=3298
  _SETASKMODULATIONCMD._serialized_start=31
  _SETASKMODULATIONCMD._serialized_end=65
  _SETFSKMODULATIONCMD._serialized_start=67
  _SETFSKMODULATIONCMD._serialized_end=107
  _SET4FSKMODULATIONCMD._serialized_start=109
  _SET4FSKMODULATIONCMD._serialized_end=150
  _SETGFSKMODULATIONCMD._serialized_start=152
  _SETGFSKMODULATIONCMD._serialized_end=193
  _SETMSKMODULATIONCMD._serialized_start=195
  _SETMSKMODULATIONCMD._serialized_end=235
  _SETBPSKMODULATIONCMD._serialized_start=237
  _SETBPSKMODULATIONCMD._serialized_end=259
  _SETQPSKMODULATIONCMD._serialized_start=261
  _SETQPSKMODULATIONCMD._serialized_end=304
  _SETLORAMODULATIONCMD._serialized_start=307
  _SETLORAMODULATIONCMD._serialized_end=462
  _GETSUPPORTEDFREQUENCIESCMD._serialized_start=464
  _GETSUPPORTEDFREQUENCIESCMD._serialized_end=492
  _SETFREQUENCYCMD._serialized_start=494
  _SETFREQUENCYCMD._serialized_end=530
  _SETDATARATECMD._serialized_start=532
  _SETDATARATECMD._serialized_end=562
  _SETENDIANNESSCMD._serialized_start=564
  _SETENDIANNESSCMD._serialized_end=619
  _SETTXPOWERCMD._serialized_start=621
  _SETTXPOWERCMD._serialized_end=668
  _SETPACKETSIZECMD._serialized_start=670
  _SETPACKETSIZECMD._serialized_end=709
  _SETSYNCWORDCMD._serialized_start=711
  _SETSYNCWORDCMD._serialized_end=746
  _SNIFFCMD._serialized_start=748
  _SNIFFCMD._serialized_end=796
  _SENDCMD._serialized_start=798
  _SENDCMD._serialized_end=823
  _SENDRAWCMD._serialized_start=825
  _SENDRAWCMD._serialized_end=853
  _STARTCMD._serialized_start=855
  _STARTCMD._serialized_end=865
  _STOPCMD._serialized_start=867
  _STOPCMD._serialized_end=876
  _JAMCMD._serialized_start=878
  _JAMCMD._serialized_end=918
  _MONITORCMD._serialized_start=920
  _MONITORCMD._serialized_end=932
  _PACKETRECEIVED._serialized_start=934
  _PACKETRECEIVED._serialized_end=1051
  _RAWPACKETRECEIVED._serialized_start=1054
  _RAWPACKETRECEIVED._serialized_end=1190
  _JAMMED._serialized_start=1192
  _JAMMED._serialized_end=1219
  _MONITORINGREPORT._serialized_start=1221
  _MONITORINGREPORT._serialized_end=1278
  _SUPPORTEDFREQUENCYRANGES._serialized_start=1281
  _SUPPORTEDFREQUENCYRANGES._serialized_end=1425
  _SUPPORTEDFREQUENCYRANGES_FREQUENCYRANGE._serialized_start=1381
  _SUPPORTEDFREQUENCYRANGES_FREQUENCYRANGE._serialized_end=1425
  _MESSAGE._serialized_start=1428
  _MESSAGE._serialized_end=2580
# @@protoc_insertion_point(module_scope)
