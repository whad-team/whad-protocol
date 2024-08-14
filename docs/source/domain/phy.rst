.. _domain_phy:

PHY Domain
==========

Procedures
----------

Enumerations
------------

.. _Endianness:

Endianness
^^^^^^^^^^

This enumeration lists the possible endian values.

========== =========================
Value      Description
========== =========================
BIG        big-endian
LITTLE     little-endian
========== =========================

.. _JammingMode:

JammingMode
^^^^^^^^^^^

This enumeration specifies the jamming mode.

========== =========================
Value      Description
========== =========================
CONTINUOUS Continuous jamming
REACTIVE   Reactive jamming
========== =========================


.. _LoRaCodingRate:

LoRaCodingRate
^^^^^^^^^^^^^^

This enumeration contains all the possible values for LoRa coding rate.

========== =========================
Value      Description
========== =========================
CR45       Coding rate 4/5
CR46       Coding rate 4/6
CR47       Coding rate 4/7
CR48       Coding rate 4/8
========== =========================


.. _LoRaSpreadingFactor:

LoRaSpreadingFactor
^^^^^^^^^^^^^^^^^^^

This enumeration contains all the possible values for LoRa spreading
factor.

========== =========================
Value      Description
========== =========================
SF7        Spreading factor 7
SF8        Spreading factor 8
SF9        Spreading factor 9
SF10       Spreading factor 10
SF11       Spreading factor 11
SF12       Spreading factor 12
========== =========================

.. _Modulation:

Modulation
^^^^^^^^^^

This enumeration contains all the possible modulation supported by
the PHY domain.

========== =================================
Value      Description
========== =================================
ASK        Amplitude Shift Keying
FSK        Frequency Shift Keying
FOURFSK    4 Frequency Shift Keying
GFSK       Gaussian Frequency Shift Keying
MSK        Minimum-Shift Keying
BPSK       Binary Phase Shift Keying
QPSK       Quadrature Phase Shift Keying
LORA       Semtech LoRa
========== =================================

.. _PhyCommand:

PhyCommand
^^^^^^^^^^

This enumeration contains the various PHY commands ID that are required to
create the domain supported commands bitmap.

.. _TXPower:

TXPower
^^^^^^^

This enumeration contains the different transmit power values accepted
by WHAD PHY domain.

========== =================================
Value      Description
========== =================================
LOW        Low power
MEDIUM     Medium power
HIGH       High power
========== =================================

Messages
--------

.. _GetSupportedFrequenciesCmd:

GetSupportedFrequenciesCmd
^^^^^^^^^^^^^^^^^^^^^^^^^^

This message requests the supported frequencies for the WHAD interface.

.. note::

    This message has no specific field.

.. _JamCmd:

JamCmd
^^^^^^

This message sets the WHAD interface in jamming mode.

============= ============================= ===============================
Field         Type                          Description
============= ============================= ===============================
mode          :ref:`JammingMode`            Jamming mode
============= ============================= ===============================


.. _Jammed:

Jammed
^^^^^^

This notification message is sent by the WHAD interface when jamming is
successful.

============= ================== ==============================================
Field         Type               Description
============= ================== ==============================================
timestamp     uint64             Timestamp in microseconds
============= ================== ==============================================


.. _MonitorCmd:

MonitorCmd
^^^^^^^^^^

This message sets the WHAD interface in monitor mode on the currently selected
frequency.

.. note::

    This message has no specific field.

.. _MonitoringReport:

MonitoringReport
^^^^^^^^^^^^^^^^

This notification is sent by the WHAD interface to report monitoring values.

============= ================== ==============================================
Field         Type               Description
============= ================== ==============================================
timestamp     uint64             Timestamp in microseconds
report        uint32[]           Report values
============= ================== ==============================================

.. _PacketReceived:

PacketReceived
^^^^^^^^^^^^^^

This notification message is sent by the WHAD interface when a packet is
received.

============= ================== ==============================================
Field         Type               Description
============= ================== ==============================================
frequency     uint32             Current frequency
rssi          int32, optional    Received signal strength indicator
timestamp     uint64, optional   Timestamp in microseconds
packet        bytes              Packet bytes
deviation     uint32             Current frequency deviation
datarate      uint32             Current data rate
endian        :ref:`Endianness`  Current endianness
modulation    :ref:`Modulation`  Current modulation
syncword      bytes              Current synchronization word
============= ================== ==============================================

.. _PacketSent:

PacketSent
^^^^^^^^^^

This message notification is sent by the WHAD interface when a packet has been
sent.

============= ================== ==============================================
Field         Type               Description
============= ================== ==============================================
timestamp     uint64             Timestamp in microseconds
============= ================== ==============================================


.. _RawPacketReceived:

RawPacketReceived
^^^^^^^^^^^^^^^^^

This notification message is sent by the WHAD interface when a packet is
received.

============= ================== ==============================================
Field         Type               Description
============= ================== ==============================================
frequency     uint32             Current frequency
rssi          int32, optional    Received signal strength indicator
timestamp     uint64, optional   Timestamp in microseconds
packet        bytes              Packet bytes
iq            int32[]            Corresponding IQs
deviation     uint32             Current frequency deviation
datarate      uint32             Current data rate
endian        :ref:`Endianness`  Current endianness
modulation    :ref:`Modulation`  Current modulation
syncword      bytes              Current synchronization word
============= ================== ==============================================

.. _ScheduleSendCmd:

ScheduleSendCmd
^^^^^^^^^^^^^^^

This message provides the WHAD interface with a packet to send at a specific
time.

============= ================== ===============================
Field         Type               Description
============= ================== ===============================
packet        bytes              PDU to send
timestamp     uint64             Timestamp in microseconds
============= ================== ===============================


.. _SchedulePacketResp:

SchedulePacketResp
^^^^^^^^^^^^^^^^^^

This message is sent by the WHAD interface to notify the result of a
schedule packet command.

============= ================== ===============================
Field         Type               Description
============= ================== ===============================
id            int32              Schedule packet slot ID
full          bool               Indicate schedule queue is full
============= ================== ===============================

.. _SchedulePacketSent:

SchedulePacketSent
^^^^^^^^^^^^^^^^^^

This message is sent by the WHAD interface to notify the transmission
of a schedule packet.

============= ================== ===============================
Field         Type               Description
============= ================== ===============================
id            int32              Schedule packet slot ID
============= ================== ===============================

.. _SendCmd:

SendCmd
^^^^^^^

This message provides the WHAD interface with a PDU to send

============= ================== ===============================
Field         Type               Description
============= ================== ===============================
packet        bytes              PDU to send
============= ================== ===============================


.. _SendRawCmd:

SendRawCmd
^^^^^^^^^^

This message provides the WHAD interface with IQs to send

============= ================== ===============================
Field         Type               Description
============= ================== ===============================
iq            int32[]            IQs to send
============= ================== ===============================

.. _Set4FSKModulationCmd:

Set4FSKModulationCmd
^^^^^^^^^^^^^^^^^^^^

This message sets the WHAD interface in 4FSK mode.

============= ========== ===============================
Field         Type       Description
============= ========== ===============================
deviation     uint32     Frequency deviation in Hz
============= ========== ===============================

.. _SetASKModulationCmd:

SetASKModulationCmd
^^^^^^^^^^^^^^^^^^^

This message sets the WHAD interface in ASK mode.

============= ========== ===============================
Field         Type       Description
============= ========== ===============================
ook           bool       Enable OOK mode
============= ========== ===============================

.. _SetBPSKModulationCmd:

SetBPSKModulationCmd
^^^^^^^^^^^^^^^^^^^^

This message sets the WHAD interface in BPSK mode.

.. note::

    This message has no specific field.


.. _SetDataRateCmd:

SetDataRateCmd
^^^^^^^^^^^^^^

This message sets the WHAD interface data rate.

============= ========== ===============================
Field         Type       Description
============= ========== ===============================
rate          uint32     Data rate in bits/second
============= ========== ===============================

.. _SetEndiannessCmd:

SetEndiannessCmd
^^^^^^^^^^^^^^^^

This message sets the WHAD interface endianness.

============= ================== ===============================
Field         Type               Description
============= ================== ===============================
endianness    :ref:`Endianness`  Endianness to use
============= ================== ===============================

.. _SetFrequencyCmd:

SetFrequencyCmd
^^^^^^^^^^^^^^^

This message sets the WHAD interface base frequency.

============= ========== ===============================
Field         Type       Description
============= ========== ===============================
frequency     uint32     Frequency in Hz
============= ========== ===============================

.. _SetFSKModulationCmd:

SetFSKModulationCmd
^^^^^^^^^^^^^^^^^^^

This message sets the WHAD interface in FSK mode.

============= ========== ===============================
Field         Type       Description
============= ========== ===============================
deviation     uint32     Frequency deviation in Hz
============= ========== ===============================

.. _SetGFSKModulationCmd:

SetGFSKModulationCmd
^^^^^^^^^^^^^^^^^^^^

This message sets the WHAD interface in GFSK mode.

============= ========== ===============================
Field         Type       Description
============= ========== ===============================
deviation     uint32     Frequency deviation in Hz
============= ========== ===============================

.. _SetLoRaModulationCmd:

SetLoRaModulationCmd
^^^^^^^^^^^^^^^^^^^^

This message sets the WHAD interface in LoRa mode.

================== ============================ ===============================
Field              Type                         Description
================== ============================ ===============================
bandwidth          uint32                       Bandwidth in Hz
spreading_factor   :ref:`LoRaSpreadingFactor`   Spreading factor
coding_rate        :ref:`LoRaCodingRate`        Coding rate
preamble_length    uint32                       Preamble length in bits
enable_crc         bool                         Enable LoRa CRC
explicit_mode      bool                         Use LoRa explicit mode
invert_iq          bool                         Enable IQ inversion
================== ============================ ===============================

.. _SetMSKModulationCmd:

SetMSKModulationCmd
^^^^^^^^^^^^^^^^^^^

This message sets the WHAD interface in MSK mode.

============= ========== ===============================
Field         Type       Description
============= ========== ===============================
deviation     uint32     Frequency deviation in Hz
============= ========== ===============================

.. _SetPacketSizeCmd:

SetPacketSizeCmd
^^^^^^^^^^^^^^^^

This message sets the WHAD interface packet size.

============= ================== ===============================
Field         Type               Description
============= ================== ===============================
packet_size   uint32             Packet size in bytes
============= ================== ===============================


.. _SetQPSKModulationCmd:

SetQPSKModulationCmd
^^^^^^^^^^^^^^^^^^^^

This message sets the WHAD interface in QPSK mode.

============= ========== ===============================
Field         Type       Description
============= ========== ===============================
offset_qpsk   bool       Use an offset
============= ========== ===============================

.. _SetSyncWordCmd:

SetSyncWordCmd
^^^^^^^^^^^^^^

This message sets the WHAD interface synchronization word.

============= ================== ===============================
Field         Type               Description
============= ================== ===============================
sync_word     bytes              Synchronization word
============= ================== ===============================

.. _SetTXPowerCmd:

SetTXPowerCmd
^^^^^^^^^^^^^

This message sets the WHAD interface TX power.

============= ================== ===============================
Field         Type               Description
============= ================== ===============================
tx_power      :ref:`TXPower`     Transmit power
============= ================== ===============================

.. _SniffCmd:

SniffCmd
^^^^^^^^

This message sets the WHAD interface in sniffing mode.

============= ================== ===============================
Field         Type               Description
============= ================== ===============================
iq_stream     bool               Enable capture of IQs
============= ================== ===============================

.. _StartCmd:

StartCmd
^^^^^^^^

This message activates the currently selected mode. By default, the WHAD
interface is in idle mode.

.. note::

    This message has no specific field.

.. _StopCmd:

StopCmd
^^^^^^^

This message stops the current mode and put the WHAD interface into idling
mode.

.. note::

    This message has no specific field.

.. _SupportedFrequencyRanges:

SupportedFrequencyRanges
^^^^^^^^^^^^^^^^^^^^^^^^

This message is sent by the WHAD interface to report its supported frequency
ranges.

================= ======================== ===============================
Field             Type                     Description
================= ======================== ===============================
frequency_ranges  :ref:`FrequencyRange` []  List of frequency ranges
================= ======================== ===============================

.. _FrequencyRange:

FrequencyRange
~~~~~~~~~~~~~~

This submessage specifies a frequency range.

================= ======================== ===============================
Field             Type                     Description
================= ======================== ===============================
start             uint32                   Frequency range start (in Hz)
end               uint32                   Frequency range end (in Hz)
================= ======================== ===============================