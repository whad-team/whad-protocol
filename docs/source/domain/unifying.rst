.. _domain_unifying:

Logitech Unifyin Domain
=======================

Procedures
----------

Enumerations
------------

.. _UnifyingCommand:

UnifyingCommand
^^^^^^^^^^^^^^^

This enumeration contains the various Unifying commands ID that are required to
create the domain supported commands bitmap.


Messages
--------

.. _JamCmd:

JamCmd
^^^^^^

This message sets the WHAD interface in jamming mode.

============= ========== ===============================
Field         Type       Description
============= ========== ===============================
channel       uint32     Channel to jam
============= ========== ===============================

.. _Jammed:

Jammed
^^^^^^

This message is sent when a specific channel has been successfully jammed.

============= ========== ===============================
Field         Type       Description
============= ========== ===============================
timestamp     uint64     Timestamp in microseconds
============= ========== ===============================

.. _LogitechDongleModeCmd:

LogitechDongleModeCmd
^^^^^^^^^^^^^^^^^^^^^

This message sets the WHAD interface into *Logitech dongle mode*, a mode in
which it will behave as a genuine Logitech Unifying USB dongle.

============= ========== ===============================
Field         Type       Description
============= ========== ===============================
channel       uint32     Channel to use
============= ========== ===============================

.. _LogitechKeyboardModeCmd:

LogitechKeyboardModeCmd
^^^^^^^^^^^^^^^^^^^^^^^

This message sets the WHAD interface into *Logitech keyboard mode*, a mode in
which it will behave as a genuine Logitech wireless keyboard.

============= ========== ===============================
Field         Type       Description
============= ========== ===============================
channel       uint32     Channel to use
============= ========== ===============================

.. _LogitechMouseModeCmd:

LogitechMouseModeCmd
^^^^^^^^^^^^^^^^^^^^^^^

This message sets the WHAD interface into *Logitech mouse mode*, a mode in
which it will behave as a genuine Logitech wireless mouse.

============= ========== ===============================
Field         Type       Description
============= ========== ===============================
channel       uint32     Channel to use
============= ========== ===============================

.. _PduReceived:

This notification message is sent by the WHAD interface to report a
PDU that has been received.

===================== ================ ======================================
Field                 Type             Description
===================== ================ ======================================
channel               uint32           Channel
rssi                  int32, optional  Received signal strength indicator
timestamp             uint64, optional Reception timestamp (microseconds)
crc_validity          bool, optional   Indicates if the CRC is valid or not
address               bytes, optional  ESB address of the sender
pdu                   bytes            ESB PDU
===================== ================ ======================================


.. _RawPduReceived:

This notification message is sent by the WHAD interface to report a raw
PDU that has been received.

===================== ================ ======================================
Field                 Type             Description
===================== ================ ======================================
channel               uint32           Channel
rssi                  int32, optional  Received signal strength indicator
timestamp             uint64, optional Reception timestamp (microseconds)
crc_validity          bool, optional   Indicates if the CRC is valid or not
address               bytes, optional  ESB address of the sender
pdu                   bytes            ESB raw PDU
===================== ================ ======================================



.. _SendCmd:

SendCmd
^^^^^^^

This message provides to the WHAD interface a packet (or PDU) to send.

===================== ========== ======================================
Field                 Type       Description
===================== ========== ======================================
channel               uint32     Channel on which the PDU must be sent
retransmission_count  uint32     Maximum number of retransmission
pdu                   bytes      PDU to send
===================== ========== ======================================

.. _SendRawCmd:

SendRawCmd
^^^^^^^^^^

This message provides to the WHAD interface a raw ESB packet to send.

===================== ========== ======================================
Field                 Type       Description
===================== ========== ======================================
channel               uint32     Channel on which the PDU must be sent
retransmission_count  uint32     Maximum number of retransmission
pdu                   bytes      PDU to send
===================== ========== ======================================

Unlike the :ref:`SendCmd`, this command specifies a complete raw packet
including the ESB header.

.. _SetNodeAddressCmd:

SetNodeAddressCmd
^^^^^^^^^^^^^^^^^

This message sets the ESB address to use for packet transmission.

============= ========== ===============================
Field         Type       Description
============= ========== ===============================
address       bytes      ESB address (2-5 bytes)
============= ========== ===============================

.. _SniffCmd:

SniffCmd
^^^^^^^^

This message sets the WHAD interface into sniffing mode.

====================== ========== ===============================
Field                  Type       Description
====================== ========== ===============================
channel                uint32     Channel to sniff
address                bytes      ESB address
show_acknowledgements  bool       Report ESB acks to host
====================== ========== ===============================

``channel`` must be in range [0, 100]. If ``channel`` is  set to 0xFF,
then the WHAD interface will loop over all channels and sniff any packet.

If ``address`` is specified, only packets sent to this address will be
sniffed.

If ``show_acknowledgements`` is set to ``true``, ESB Ack packets will be
reported to the host.

.. _SniffPairingCmd:

SniffPairingCmd
^^^^^^^^^^^^^^^

This message sets the WHAD interface into pairing sniffing mode.

.. note::

    This message has no specific field.

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