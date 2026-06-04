.. _domain_esb:

Enhanced ShockBurst Domain
==========================

Enhanced ShockBurst procedures
------------------------------

Sniffing ESB packets
^^^^^^^^^^^^^^^^^^^^

Sniffing ESB packets is quite simple, we only need to put the WHAD interface
in sniffing mode on a channel and listen for packets.

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: SniffCmd(channel=5)
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Host->>+Interface: StartCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        loop
            Interface->>Host: PduReceived | RawPduReceived
        end
        Host->>+Interface: StopCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)

First, the host sends a :ref:`ESBSniffCmd` message to switch the WHAD interface into
sniffing mode. The host **must** provide at least a channel number to sniff,
but can also provide an ESB address that will be used by the WHAD interface to
only keep packets sent to this address. The ``show_acknowledgements`` boolean
field can be set to ``true`` to also capture ESB acknowledgements.

Once the WHAD interface configured in sniffing mode on a specific channel, the
host sends a :ref:`ESBStartCmd` to start sniffing actual packets. The WHAD interface
will report any packet through a :ref:`ESBPduReceived` or :ref:`ESBRawPduReceived`
message (depending on its capabilities).

When sniffing mode is enabled, packets can also be injected into a specific
channel through the use of :ref:`ESBSendCmd` message:

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: SendCmd(channel=5, pdu=...)
        Interface-->>-Host: CommandResult(result=SUCCESS)

Sniffing can be stopped by the host by sending a :ref:`ESBStopCmd` message.

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: StopCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)

Receiving ESB packets in PRX mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

WHAD interfaces supporting ESB can also, if implemented, behave as an ESB
device in *primary receiver mode* or *PRX*. In *PRX* mode, the device has an
ESB address and receives ESB packets. For each received packet, it sends out
an acknowledgement except if the packet header has the ``no_ack`` flag set.

To put a WHAD interface in *PRX* mode, the host simply has to set the interface
ESB address and then put it in *PRX* mode:

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: SetNodeAddressCmd(address=00:11:22:33:44)
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Host->>+Interface: PrimaryReceiverModeCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)

Once put in *PRX* mode, the host start the interface and waits for received
packets:

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: StartCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        loop
            Interface->>Host: PduReceived | RawPduReceived
        end


Sending ESB packets in PTX mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compatible WHAD interface can also behave as an ESB transmitter in *primary transmitter mode*.
It is very similar to the *PRX* mode except that the WHAD interface will send packets to
a specified address.

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: SetNodeAddressCmd(address=00:11:22:33:44)
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Host->>+Interface: PrimaryTransmitterModeCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Host->>+Interface: StartCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        loop
            Host->>Interface: SendCmd(channel=5, pdu=...)
        end

First, the host sends a :ref:`ESBSetNodeAddressCmd` to set the WHAD interface ESB
address. Then, the hosts sets the WHAD interface into *PTX* mode by sending a
:ref:`ESBPrimaryTransmitterModeCmd` and activates the interface by sending a
:ref:`ESBStartCmd`. Once started, it can send packets on various channels through
:ref:`ESBSendCmd` or :ref:`ESBSendRawCmd` messages.


Jamming an ESB channel
^^^^^^^^^^^^^^^^^^^^^^

The host can put the WHAD interface in ESB jamming mode targeting a specific
channel and start jamming it:

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: JamCmd(channel=5)
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Host->>+Interface: StartCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        loop
            Host->>Interface: Jammed
        end
        Host->>+Interface: StopCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)        


Enumerations
------------

.. _ESBCommand:

ESBCommand
^^^^^^^^^^

This enumeration contains the various ESB commands ID that are required to
create the domain supported commands bitmap.


Messages
--------

.. _ESBJamCmd:

JamCmd
^^^^^^

This message sets the WHAD interface in jamming mode.

============= ========== ===============================
Field         Type       Description
============= ========== ===============================
channel       uint32     Channel to jam
============= ========== ===============================

.. _ESBJammed:

Jammed
^^^^^^

This message is sent when a specific channel has been successfully jammed.

============= ========== ===============================
Field         Type       Description
============= ========== ===============================
timestamp     uint64     Timestamp in microseconds
============= ========== ===============================

.. _ESBPduReceived:

PduReceived
^^^^^^^^^^^^

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

.. _ESBPrimaryReceiverMode:

PrimaryReceiverMode
^^^^^^^^^^^^^^^^^^^

This messages sets the WHAD interface into primary receive mode (PRX). In this
mode, the WHAD interface will receive ESB PDUs and send back show_acknowledgements
if required.

===================== ========== ======================================
Field                 Type       Description
===================== ========== ======================================
channel               uint32     Channel on which PDUs must be received
===================== ========== ======================================

``channel`` specifies the channel number the WHAD interface must listen.


.. _ESBPrimaryTransmitterModeCmd:

PrimaryTransmitterModeCmd
^^^^^^^^^^^^^^^^^^^^^^^^^

This messages sets the WHAD interface into primary transmit mode (PTX).
In this mode, the WHAD interface will send ESB PDUs and look back for
acknowledgements.

===================== ========== ======================================
Field                 Type       Description
===================== ========== ======================================
channel               uint32     Channel on which PDUs must be sent
===================== ========== ======================================

``channel`` specifies the channel number the WHAD interface must use.


.. _ESBRawPduReceived:

RawPduReceived
^^^^^^^^^^^^^^^

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



.. _ESBSendCmd:

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

.. _ESBSendRawCmd:

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

Unlike the :ref:`ESBSendCmd`, this command specifies a complete raw packet
including the ESB header.

.. _ESBSetNodeAddressCmd:

SetNodeAddressCmd
^^^^^^^^^^^^^^^^^

This message sets the ESB address to use for packet transmission.

============= ========== ===============================
Field         Type       Description
============= ========== ===============================
address       bytes      ESB address (2-5 bytes)
============= ========== ===============================

.. _ESBSniffCmd:

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

.. _ESBStartCmd:

StartCmd
^^^^^^^^

This message activates the currently selected mode. By default, the WHAD
interface is in idle mode.

.. note::

    This message has no specific field.

.. _ESBStopCmd:

StopCmd
^^^^^^^

This message stops the current mode and put the WHAD interface into idling
mode.

.. note::

    This message has no specific field.