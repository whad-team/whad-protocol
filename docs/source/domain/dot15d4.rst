.. _domain_dot15d4:

IEEE 802.15.4 Domain
=====================

Procedures
----------

Sniffing 802.15.4 packets
^^^^^^^^^^^^^^^^^^^^^^^^^

Receiving 802.1.5.4 packets
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting interface in Coordinator mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting interface in Router mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting interface in EndDevice mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Enumerations
------------

.. _Dot15d4Command:

Dot15d4Command
^^^^^^^^^^^^^^

This enumeration contains the various Dot15d4 commands ID that are required to
create the domain supported commands bitmap.

.. _Dot15d4MitmRole:

Dot15d4MitmRole
^^^^^^^^^^^^^^^

This enumeration specifies the type of Mitm to perform.

================ ===================================================
Field            Description
================ ===================================================
REACTIVE_JAMMER  Perform reactive jamming
CORRECTOR        Corrector
================ ===================================================

.. _Dot15d4AddressType:

AddressType
^^^^^^^^^^^

This enumeration contains the different types of addresses.

================ ===================================================
Field            Description
================ ===================================================
SHORT            16-bit short address
EXTENDED         64-bit extended address
================ ===================================================


.. _Dot15d4LinkType:

LinkType (TSCH specific)
^^^^^^^^^^^^^^^^^^^^^^^^^

This enumeration contains the different types of TSCH links.

================ ===================================================
Field            Description
================ ===================================================
NORMAL            Normal Link
DISCOVERY         Discovery-specific Link
BROADCAST         Broadcast Link
JOIN              Join Link
================ ===================================================


.. _Dot15d4LinkOptions:

LinkOptions (TSCH specific)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This enumeration contains the different options associated to TSCH links.

================ ===================================================
Field            Description
================ ===================================================
UNKNOWN           Unknown options (default value)
SHARED            Link can be used both for transmission or reception
RECEIVE           Link can be used for reception only
TRANSMIT          Link can be used for transmission only
================ ===================================================

Messages
--------

.. _Dot15d4CoordinatorCmd:

CoordinatorCmd
^^^^^^^^^^^^^^

This message sets the WHAD interface in coordinator mode.

============= =================== ===============================
Field         Type                Description
============= =================== ===============================
channel       uint32              Channel to use
============= =================== ===============================

.. _Dot15d4EndDeviceCmd:

EndDeviceCmd
^^^^^^^^^^^^

This message sets the WHAD interface in end-device mode.

============= =================== ===============================
Field         Type                Description
============= =================== ===============================
channel       uint32              Channel to use
============= =================== ===============================

.. _Dot15d4EnergyDetectionCmd:

EnergyDetectionCmd
^^^^^^^^^^^^^^^^^^

This message sets the WHAD interface in energy detection mode.

============= =================== ===============================
Field         Type                Description
============= =================== ===============================
channel       uint32              Channel to analyze
============= =================== ===============================

.. _Dot15d4EnergyDetectionSample:

EnergyDetectionSample
^^^^^^^^^^^^^^^^^^^^^

This notification message sent by the WHAD interface reports an energy
detection sample.

============= =================== ===============================
Field         Type                Description
============= =================== ===============================
sample        uint32              Sample value
timestamp     uint64              Timestamp in microseconds
============= =================== ===============================


.. _Dot15d4JamCmd:

JamCmd
^^^^^^

This message sets the WHAD interface in jamming mode.

============= =================== ===============================
Field         Type                Description
============= =================== ===============================
channel       uint32              Channel to analyze
============= =================== ===============================

.. _Dot15d4Jammed:

Jammed
^^^^^^

This notification message is sent by the WHAD interface when a channel
has been successfully jammed.

============= =================== ===============================
Field         Type                Description
============= =================== ===============================
timestamp     uint64              Timestamp in microseconds
============= =================== ===============================

.. _Dot15d4ManInTheMiddleCmd:

ManInTheMiddleCmd
^^^^^^^^^^^^^^^^^

This message sets the WHAD interface in man-in-the-middle role.

============= ====================== ===============================
Field         Type                   Description
============= ====================== ===============================
role          :ref:`Dot15d4MitmRole` Mitm Role to use
============= ====================== ===============================

.. _Dot15d4PduReceived:

PduReceived
^^^^^^^^^^^

This notification message is sent by the WHAD interface each time a raw
PDU is received.

======================== ====================== ===========================================================
Field                    Type                    Description
======================== ====================== ===========================================================
channel                   uint32                 Channel
rssi                      int32, optional        Received signal strength indicator
timestamp                 uint64, optional       Timestamp in microseconds
fcs_validity              bool, optional         Frame Check Sequence validity
pdu                       bytes                  PDU
lqi                       uint32, optional       Link quality indicator
asn                       uint64, optional       Absolute Slot Number (TSCH specific)
start_of_slot_timestamp   uint32, optional       Start of slot Timestamp in microseconds (TSCH specific)
time_slot                 uint32, optional       Time slot linked to the PDU (TSCH specific)
base_channel_frequency    uint32, optional       Base Channel Frequency (TSCH specific)
number_of_channels        uint32, optional       Number of active RF channels (TSCH specific)
channel_spacing           uint32, optional       Spacing between RF channels (TSCH specific)
======================== ====================== ===========================================================

.. note::

    This message has been extended with optional fields for TSCH mode (introduced in v3.0).


.. _Dot15d4RawPduReceived:

RawPduReceived
^^^^^^^^^^^^^^

This notification message is sent by the WHAD interface each time a raw
PDU is received.

======================== ====================== ===========================================================
Field                    Type                    Description
======================== ====================== ===========================================================
channel                   uint32                 Channel
rssi                      int32, optional        Received signal strength indicator
timestamp                 uint64, optional       Timestamp in microseconds
fcs_validity              bool, optional         Frame Check Sequence validity
pdu                       bytes                  PDU
fcs                       uint32                 FCS associated to the frame
lqi                       uint32, optional       Link quality indicator
asn                       uint64, optional       Absolute Slot Number (TSCH specific)
start_of_slot_timestamp   uint32, optional       Start of slot Timestamp in microseconds (TSCH specific)
time_slot                 uint32, optional       Time slot linked to the PDU (TSCH specific)
base_channel_frequency    uint32, optional       Base Channel Frequency (TSCH specific)
number_of_channels        uint32, optional       Number of active RF channels (TSCH specific)
channel_spacing           uint32, optional       Spacing between RF channels (TSCH specific)
======================== ====================== ===========================================================

.. note::

    This message has been extended with optional fields for TSCH mode (introduced in v3.0).

.. _Dot15d4RouterCmd:

RouterCmd
^^^^^^^^^

This message sets the WHAD interface in router mode.

============= =================== ===============================
Field         Type                Description
============= =================== ===============================
channel       uint32              Channel to use
============= =================== ===============================

.. _Dot15d4SendCmd:

SendCmd
^^^^^^^

This message provides the WHAD interface with a PDU to send.

============= =================== ===============================
Field         Type                Description
============= =================== ===============================
channel       uint32              Target channel
pdu           bytes               IEEE 802.15.4 PDU to send
============= =================== ===============================


.. _Dot15d4SendRawCmd:

SendRawCmd
^^^^^^^^^^

This message provides the WHAD interface with a raw PDU to send.

============= =================== ===============================
Field         Type                Description
============= =================== ===============================
channel       uint32              Target channel
pdu           bytes               IEEE 802.15.4 PDU to send
fcs           uint32              Frame Check Sequence
============= =================== ===============================



.. _Dot15d4SetNodeAddressCmd:

SetNodeAddressCmd
^^^^^^^^^^^^^^^^^

This message sets the WHAD interface node address.

============= ========================== ===============================
Field         Type                       Description
============= ========================== ===============================
address       uint64                     64-bit extended address
address_type  :ref:`Dot15d4AddressType`  Node address type
============= ========================== ===============================

.. _Dot15d4SniffCmd:

SniffCmd
^^^^^^^^

This message sets the WHAD interface in sniffing mode.

============= =================== ===============================
Field         Type                Description
============= =================== ===============================
channel       uint32              Channel to sniff
============= =================== ===============================

.. _Dot15d4StartCmd:

StartCmd
^^^^^^^^

This message activates the current selected mode.

.. note::

    This message has no specific field.


.. _Dot15d4StopCmd:

StopCmd
^^^^^^^^

This message terminates the current selected mode.

.. note::

    This message has no specific field.

.. _Dot15d4ConfigureTSCHCmd:

ConfigureTSCHCmd (TSCH specific)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This message enables or disables the Time-Slotted Channel Hopping (TSCH) mode.

============= =================== ==================================
Field         Type                Description
============= =================== ==================================
enabled       bool                Indicator of TSCH mode activation
============= =================== ==================================

.. note::

    This message is specific to TSCH mode (introduced in v3.0).

.. _Dot15d4AddLinkCmd:

_AddLinkCmd (TSCH specific)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This message adds a new TSCH Link in the WHAD interface.

============== ========================== ===================================================
Field          Type                       Description
============== ========================== ===================================================
superframe_id  uint32                     ID of the corresponding superframe
src            uint32                     Source address of the link
time_slot      uint32                     Time slot associated to the link (in superframe)
channel_offset uint32                     Channel offset of the link
neighbor       uint32                     Neigbor address of the link
options        :ref:`Dot15d4LinkOptions`  Options associated to the link
type           :ref:`Dot15d4LinkType`     Type of the link
============== ========================== ===================================================

.. note::

    This message is specific to TSCH mode.

.. _Dot15d4DeleteLinkCmd:

__DeleteLinkCmd (TSCH specific)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This message deletes an existing TSCH Link in the WHAD interface.

============== =================== ===================================================
Field          Type                Description
============== =================== ===================================================
superframe_id  uint32              ID of the corresponding superframe
time_slot      uint32              Time slot associated to the link (in superframe)
channel_offset uint32              Channel offset of the link
============== =================== ===================================================

.. note::

    This message is specific to TSCH mode.

.. _Dot15d4UpdateSuperframeCmd:

__UpdateSuperframeCmd (TSCH specific)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This message adds or update a TSCH Superframe in the WHAD interface.

=============== =================== ======================================================
Field           Type                Description
=============== =================== ======================================================
superframe_id   uint32              ID of the corresponding superframe
number_of_slots uint32              Size of the superframe (in number of slots)
flags           uint32              Set of flags associated to the superframe
asn             uint64, optional    Absolute Slot Number (ASN) where the operation occurs 
=============== =================== ======================================================

.. note::

    This message is specific to TSCH mode.

.. _Dot15d4DeleteSuperframeCmd:

__DeleteSuperframeCmd (TSCH specific)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This message deletes an existing TSCH Superframe in the WHAD interface.

=============== =================== ======================================================
Field           Type                Description
=============== =================== ======================================================
superframe_id   uint32              ID of the superframe to delete
=============== =================== ======================================================

.. note::

    This message is specific to TSCH mode.

.. _Dot15d4SetChannelMapCmd:

__SetChannelMapCmd (TSCH specific)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This message configure the Channel Map associated to channel hopping in the WHAD interface.

=============== =================== ======================================================
Field           Type                Description
=============== =================== ======================================================
channel_map     uint32              Bitmap of enabled channels in channel hopping mode
=============== =================== ======================================================

.. note::

    This message is specific to TSCH mode.

.. _Dot15d4DiscoveredCommunication:

__DiscoveredCommunication (TSCH specific)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This message notifies that a new communication has been discovered by the WHAD interface. 
It allows to discover existing links and add them to the known superframe.

=============== =================== ======================================================
Field           Type                Description
=============== =================== ======================================================
time_slot       uint32              Slot number of the discovered communication
channel_offset  uint32              Channel offset when the communication was detected
pdu             bytes               Main PDU associated with the communication
=============== =================== ======================================================

.. note::

    This message is specific to TSCH mode.