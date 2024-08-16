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

.. _AddressType:

AddressType
^^^^^^^^^^^

This enumeration contains the different types of addresses.

================ ===================================================
Field            Description
================ ===================================================
SHORT            16-bit short address
EXTENDED         64-bit extended address
================ ===================================================

Messages
--------


.. _CoordinatorCmd:

CoordinatorCmd
^^^^^^^^^^^^^^

This message sets the WHAD interface in coordinator mode.

============= =================== ===============================
Field         Type                Description
============= =================== ===============================
channel       uint32              Channel to use
============= =================== ===============================

.. _EndDeviceCmd:

EndDeviceCmd
^^^^^^^^^^^^

This message sets the WHAD interface in end-device mode.

============= =================== ===============================
Field         Type                Description
============= =================== ===============================
channel       uint32              Channel to use
============= =================== ===============================

.. _EnergyDetectionCmd:

EnergyDetectionCmd
^^^^^^^^^^^^^^^^^^

This message sets the WHAD interface in energy detection mode.

============= =================== ===============================
Field         Type                Description
============= =================== ===============================
channel       uint32              Channel to analyze
============= =================== ===============================

.. _EnergyDetectionSample:

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


.. _JamCmd:

JamCmd
^^^^^^

This message sets the WHAD interface in jamming mode.

============= =================== ===============================
Field         Type                Description
============= =================== ===============================
channel       uint32              Channel to analyze
============= =================== ===============================

.. _Jammed:

Jammed
^^^^^^

This notification message is sent by the WHAD interface when a channel
has been successfully jammed.

============= =================== ===============================
Field         Type                Description
============= =================== ===============================
timestamp     uint64              Timestamp in microseconds
============= =================== ===============================

.. _ManInTheMiddleCmd:

ManInTheMiddleCmd
^^^^^^^^^^^^^^^^^

This message sets the WHAD interface in man-in-the-middle role.

============= ====================== ===============================
Field         Type                   Description
============= ====================== ===============================
role          :ref:`Dot15d4MitmRole` Mitm Role to use
============= ====================== ===============================

.. _PduReceived:

PduReceived
^^^^^^^^^^^

This notification message is sent by the WHAD interface each time a raw
PDU is received.

============= ====================== ======================================
Field         Type                   Description
============= ====================== ======================================
channel       uint32                 Channel
rssi          int32, optional        Received signal strength indicator
timestamp     uint64, optional       Timestamp in microseconds
fcs_validyt   bool, optional         Frame Check Sequence validity
pdu           bytes                  PDU
lqi           uint32, optional       Link quality indicator
============= ====================== ======================================


.. _RawPduReceived:

RawPduReceived
^^^^^^^^^^^^^^

This notification message is sent by the WHAD interface each time a raw
PDU is received.

============= ====================== ======================================
Field         Type                   Description
============= ====================== ======================================
channel       uint32                 Channel
rssi          int32, optional        Received signal strength indicator
timestamp     uint64, optional       Timestamp in microseconds
fcs_validyt   bool, optional         Frame Check Sequence validity
pdu           bytes                  PDU
fcs           uint32                 Frame Check Sequence
lqi           uint32, optional       Link quality indicator
============= ====================== ======================================

.. _RouterCmd:

RouterCmd
^^^^^^^^^

This message sets the WHAD interface in router mode.

============= =================== ===============================
Field         Type                Description
============= =================== ===============================
channel       uint32              Channel to use
============= =================== ===============================

.. _SendCmd:

SendCmd
^^^^^^^

This message provides the WHAD interface with a PDU to send.

============= =================== ===============================
Field         Type                Description
============= =================== ===============================
channel       uint32              Target channel
pdu           bytes               IEEE 802.15.4 PDU to send
============= =================== ===============================


.. _SendRawCmd:

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



.. _SetNodeAddressCmd:

SetNodeAddressCmd
^^^^^^^^^^^^^^^^^

This message sets the WHAD interface node address.

============= =================== ===============================
Field         Type                Description
============= =================== ===============================
address       uint64              64-bit extended address
address_type  :ref:`AddressType`  Node address type
============= =================== ===============================

.. _SniffCmd:

SniffCmd
^^^^^^^^

This message sets the WHAD interface in sniffing mode.

============= =================== ===============================
Field         Type                Description
============= =================== ===============================
channel       uint32              Channel to sniff
============= =================== ===============================

.. _StartCmd:

StartCmd
^^^^^^^^

This message activates the current selected mode.

.. note::

    This message has no specific field.


.. _StopCmd:

StopCmd
^^^^^^^^

This message terminates the current selected mode.

.. note::

    This message has no specific field.