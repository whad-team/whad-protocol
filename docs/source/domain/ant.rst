.. _domain_ant:

ANT Domain
===========

The ANT Domain service implements a series of procedures and messages allowing
to interact with ANT devices.

ANT procedures
---------------

Sniffing ANT packets
^^^^^^^^^^^^^^^^^^^^

If the WHAD interface implements the :ref:`ANTSniffCmd` command then it is able
to sniff ANT packets on a given RF channel.

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: SniffCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Host->>+Interface: StartCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        loop
            Interface->>Host: PduReceived / RawPduReceived
        end
        Host->>+Interface: StopCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)

The host sends a :ref:`ANTSniffCmd` command providing the RF channel and
network key (and optionally the device number, device type, and transmission
type). The WHAD interface then starts capturing packets and reports them to the
host through a series of :ref:`ANTPduReceived` or :ref:`ANTRawPduReceived`
messages depending on its capabilities.

Jamming ANT packets
^^^^^^^^^^^^^^^^^^^

If the WHAD interface implements the :ref:`ANTJamCmd` command then it is able
to jam ANT packets on a given RF channel.

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: JamCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Host->>+Interface: StartCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        loop
            Interface->>Host: Jammed
        end
        Host->>+Interface: StopCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)

The host sends a :ref:`ANTJamCmd` command specifying the target RF channel.
Once started, the WHAD interface jams packets on that channel and notifies the
host with :ref:`ANTJammed` messages.

Configuring and opening a channel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before transmitting or receiving data, a channel must be configured and opened.
The following procedure illustrates the typical channel setup sequence.

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: SetNetworkKeyCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Host->>+Interface: AssignChannelCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Host->>+Interface: SetDeviceNumberCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Host->>+Interface: SetDeviceTypeCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Host->>+Interface: SetTransmissionTypeCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Host->>+Interface: SetChannelPeriodCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Host->>+Interface: SetRFChannelCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Host->>+Interface: OpenChannelCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Interface->>Host: ChannelEvent(EVENT_NO_ERROR)

The host configures the network key with :ref:`ANTSetNetworkKeyCmd`, then
assigns the channel to a network with :ref:`ANTAssignChannelCmd`. Channel
parameters (device number, device type, transmission type, channel period and
RF channel) are then set individually before the channel is opened with
:ref:`ANTOpenChannelCmd`. Channel state changes are reported to the host via
:ref:`ANTChannelEventNotif` notifications.

Operating as a Master
^^^^^^^^^^^^^^^^^^^^^

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: MasterModeCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Host->>+Interface: StartCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        loop
            Host->>+Interface: SendCmd
            Interface-->>-Host: CommandResult(result=SUCCESS)
            Interface->>Host: ChannelEvent(EVENT_TX)
        end
        Host->>+Interface: StopCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)

The host puts the WHAD interface into Master mode by sending a
:ref:`ANTMasterModeCmd` message. Once started, the host can transmit ANT
packets using :ref:`ANTSendCmd` messages. Each successful transmission is
confirmed by a :ref:`ANTChannelEvent` notification with event type
``EVENT_TX``.

Operating as a Slave
^^^^^^^^^^^^^^^^^^^^

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: SlaveModeCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Host->>+Interface: StartCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        loop
            Interface->>Host: PduReceived
            Interface->>Host: ChannelEvent
        end
        Host->>+Interface: StopCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)

The host puts the WHAD interface into Slave mode by sending a
:ref:`ANTSlaveModeCmd` message. Once started, the WHAD interface listens for
packets from a Master device and reports them to the host via
:ref:`ANTPduReceived` messages. Channel state changes are reported via
:ref:`ANTChannelEventNotif` notifications.

Sending and receiving PDUs
^^^^^^^^^^^^^^^^^^^^^^^^^^

Once a channel is open, the host can provide the WHAD interface with a PDU to
send. If the WHAD interface does have the ``NoRawData`` capability, the host
must send :ref:`ANTSendCmd` messages. If the WHAD interface can send raw
PDUs, it must send :ref:`ANTSendRawCmd` messages.

A received PDU is notified by the WHAD interface to the host through a
:ref:`ANTPduReceived` message or :ref:`ANTRawPduReceived` message
depending on its capabilities.

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: SendCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Note over Host,Interface: PDU sent by host
        Interface->>Host: PduReceived
        Note over Host,Interface: Interface reports a received PDU

Listing channels and networks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The host can query the WHAD interface for available channels and networks.

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: ListChannelsCmd
        Interface-->>-Host: AvailableChannels
        Host->>+Interface: ListNetworksCmd
        Interface-->>-Host: AvailableNetworks

The host sends a :ref:`ANTListChannelsCmd` and/or :ref:`ANTListNetworksCmd`
message. The WHAD interface replies with :ref:`ANTAvailableChannels` and
:ref:`ANTAvailableNetworks` notifications respectively.


Enumerations
------------

.. _ANTCommand:

ANTCommand
^^^^^^^^^^

This enumeration contains the various ANT command IDs required to create the
domain supported commands bitmap.

.. _ANTChannelType:

AntChannelType
^^^^^^^^^^^^^^^

This enumeration specifies the different channel types available for an ANT
channel.

======================================== ===========================================
Type                                     Description
======================================== ===========================================
BIDIRECTIONAL_RECEIVE_CHANNEL            Bidirectional receive channel
BIDIRECTIONAL_TRANSMIT_CHANNEL           Bidirectional transmit channel
SHARED_BIDIRECTIONAL_RECEIVE_CHANNEL     Shared bidirectional receive channel
SHARED_BIDIRECTIONAL_TRANSMIT_CHANNEL    Shared bidirectional transmit channel
RECEIVE_ONLY_CHANNEL                     Receive-only channel
TRANSMIT_ONLY_CHANNEL                    Transmit-only channel
======================================== ===========================================

.. _ANTChannelEvent:

AntChannelEvent
^^^^^^^^^^^^^^^

This enumeration specifies the different channel events that can occur.

========================================= ================================================
Event                                     Description
========================================= ================================================
EVENT_NO_ERROR                            No error
EVENT_RX_SEARCH_TIMEOUT                   Search timeout on receive
EVENT_RX_FAIL                             Receive failure
EVENT_TX                                  Transmit completed
EVENT_TRANSFER_RX_FAILED                  Burst receive transfer failed
EVENT_TRANSFER_TX_COMPLETED               Burst transmit transfer completed
EVENT_TRANSFER_TX_FAILED                  Burst transmit transfer failed
EVENT_CHANNEL_CLOSED                      Channel has been closed
EVENT_RX_FAIL_TO_GO_TO_SEARCH             Receive failure causing return to search
EVENT_CHANNEL_COLLISION                   Channel collision detected
EVENT_TRANSFER_TX_START                   Burst transmit transfer started
EVENT_TRANSFER_NEXT_DATA_BLOCK            Next data block for burst transfer
EVENT_CHANNEL_IN_WRONG_STATE              Channel is in wrong state for operation
EVENT_CHANNEL_NOT_OPENED                  Channel has not been opened
EVENT_CHANNEL_ID_NOT_SET                  Channel ID has not been configured
EVENT_CLOSE_ALL_CHANNELS                  Request to close all channels
EVENT_TRANSFER_IN_PROGRESS                A transfer is already in progress
EVENT_TRANSFER_SEQUENCE_NUMBER_ERROR      Sequence number error in burst transfer
EVENT_TRANSFER_IN_ERROR                   Transfer encountered an error
========================================= ================================================


Messages
--------

.. _ANTSetDeviceNumberCmd:

SetDeviceNumberCmd
^^^^^^^^^^^^^^^^^^

This message configures the ANT device number for a given channel.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
channel_number   uint32             Target channel number
device_number    uint32             ANT device number to set
================ ================== ===========================================

.. _ANTSetDeviceTypeCmd:

SetDeviceTypeCmd
^^^^^^^^^^^^^^^^

This message configures the ANT device type for a given channel.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
channel_number   uint32             Target channel number
device_type      uint32             ANT device type to set
================ ================== ===========================================

.. _ANTSetTransmissionTypeCmd:

SetTransmissionTypeCmd
^^^^^^^^^^^^^^^^^^^^^^

This message configures the ANT transmission type for a given channel.

================= =================== ===========================================
**Field**         **Type**            **Description**
================= =================== ===========================================
channel_number     uint32             Target channel number
transmission_type  uint32             ANT transmission type to set
================= =================== ===========================================

.. _ANTSetChannelPeriodCmd:

SetChannelPeriodCmd
^^^^^^^^^^^^^^^^^^^

This message configures the ANT channel period for a given channel.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
channel_number   uint32             Target channel number
channel_period   uint32             Channel period to set
================ ================== ===========================================

.. _ANTSetNetworkKeyCmd:

SetNetworkKeyCmd
^^^^^^^^^^^^^^^^

This message provisions a network key associated with a given network number.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
network_number   uint32             Target network number
network_key      bytes              Network key to provision
================ ================== ===========================================

.. _ANTAssignChannelCmd:

AssignChannelCmd
^^^^^^^^^^^^^^^^

This message links a channel number to a network number. Extended optional
parameters may be provided if the dongle supports them.

============================ ========================= ===========================================
**Field**                     **Type**                  **Description**
============================ ========================= ===========================================
channel_number                 uint32                    Channel number to assign
network_number                 uint32                    Network number to link to
channel_type                   :ref:`ANTChannelType`     Channel type
background_scanning            bool, optional            Enable background scanning
frequency_agility              bool, optional            Enable frequency agility
fast_channel_initiation        bool, optional            Enable fast channel initiation
asynchronous_transmission      bool, optional            Enable asynchronous transmission
============================ ========================= ===========================================

.. _ANTUnassignChannelCmd:

UnassignChannelCmd
^^^^^^^^^^^^^^^^^^

This message breaks the link between a channel and a network.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
channel_number   uint32             Channel number to unassign
================ ================== ===========================================

.. _ANTOpenChannelCmd:

OpenChannelCmd
^^^^^^^^^^^^^^

This message opens a channel identified by its channel number.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
channel_number   uint32             Channel number to open
================ ================== ===========================================

.. _ANTCloseChannelCmd:

CloseChannelCmd
^^^^^^^^^^^^^^^

This message closes an open channel identified by its channel number.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
channel_number   uint32             Channel number to close
================ ================== ===========================================

.. _ANTSetRFChannelCmd:

SetRFChannelCmd
^^^^^^^^^^^^^^^

This message sets the RF channel associated with a given channel number.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
channel_number   uint32             Target channel number
rf_channel       uint32             RF channel to assign
================ ================== ===========================================

.. _ANTSniffCmd:

SniffCmd
^^^^^^^^

This message sets the WHAD interface into ANT sniffing mode. The RF channel
and network key are required; the device number, device type, and transmission
type are optional filters.

================== ================== =========================================
**Field**          **Type**           **Description**
================== ================== =========================================
rf_channel         uint32             RF channel to sniff
network_key        bytes              Network key
device_number      uint32, optional   Device number filter
device_type        uint32, optional   Device type filter
transmission_type  uint32, optional   Transmission type filter
================== ================== =========================================

.. _ANTJamCmd:

JamCmd
^^^^^^

This message sets the WHAD interface into ANT jamming mode on the specified RF
channel.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
rf_channel       uint32             RF channel to jam
================ ================== ===========================================

.. _ANTSendCmd:

SendCmd
^^^^^^^

This message transmits an ANT PDU on a given channel.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
rf_channel       uint32, optional   RF channel override
channel_number   uint32             Channel number to use
pdu              bytes              ANT PDU to send
================ ================== ===========================================

.. _ANTSendRawCmd:

SendRawCmd
^^^^^^^^^^

This message transmits a raw ANT PDU on a given channel.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
rf_channel       uint32, optional   RF channel override
channel_number   uint32             Channel number to use
pdu              bytes              Raw ANT PDU to send
================ ================== ===========================================

.. _ANTMasterModeCmd:

MasterModeCmd
^^^^^^^^^^^^^

This message sets the WHAD interface into ANT Master mode on the given channel.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
channel_number   uint32             Channel number to use
================ ================== ===========================================

.. _ANTSlaveModeCmd:

SlaveModeCmd
^^^^^^^^^^^^

This message sets the WHAD interface into ANT Slave mode on the given channel.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
channel_number   uint32             Channel number to use
================ ================== ===========================================

.. _ANTStartCmd:

StartCmd
^^^^^^^^

This message starts the WHAD interface in the currently selected mode.

.. note::

    This message has no specific field.

.. _ANTStopCmd:

StopCmd
^^^^^^^

This message stops the WHAD interface, which then goes idle.

.. note::

    This message has no specific field.

.. _ANTListChannelsCmd:

ListChannelsCmd
^^^^^^^^^^^^^^^

This message requests the list of channels exposed by the device.

.. note::

    This message has no specific field.

.. _ANTListNetworksCmd:

ListNetworksCmd
^^^^^^^^^^^^^^^

This message requests the list of networks supported by the device.

.. note::

    This message has no specific field.

.. _ANTJammed:

Jammed
^^^^^^

This notification message is sent to indicate that packets have been jammed.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
timestamp        uint32             Timestamp of the jamming event
================ ================== ===========================================

.. _ANTAvailableChannels:

AvailableChannels
^^^^^^^^^^^^^^^^^

This notification message reports the number of channels available on the
device.

====================== ================== =====================================
**Field**              **Type**           **Description**
====================== ================== =====================================
number_of_channels     uint32             Number of available channels
====================== ================== =====================================

.. _ANTAvailableNetworks:

AvailableNetworks
^^^^^^^^^^^^^^^^^

This notification message reports the number of networks supported by the
device.

====================== ================== =====================================
**Field**              **Type**           **Description**
====================== ================== =====================================
number_of_networks     uint32             Number of available networks
====================== ================== =====================================

.. _ANTRawPduReceived:

RawPduReceived
^^^^^^^^^^^^^^

This notification message is sent by the WHAD interface to report a raw ANT
PDU (including CRC) received to the host. This message is used by devices that
have access to raw PDU data.

================ ====================== ==========================================
**Field**        **Type**               **Description**
================ ====================== ==========================================
channel_number   uint32                 Channel on which the PDU was received
rssi             int32, optional        Received signal strength indicator
timestamp        uint32, optional       When the PDU was received
crc_validity     bool, optional         ``true`` if CRC is valid, ``false`` otherwise
pdu              bytes                  Raw ANT PDU
crc              uint32                 PDU CRC
rf_channel       uint32                 RF channel on which the PDU was received
================ ====================== ==========================================

.. _ANTPduReceived:

PduReceived
^^^^^^^^^^^

This notification message is sent by the WHAD interface to report a normal ANT
PDU received to the host. This message is used by devices that do not have
access to raw PDU data (i.e. devices exposing the ``NoRawData`` capability).

================ ====================== ==========================================
**Field**        **Type**               **Description**
================ ====================== ==========================================
channel_number   uint32                 Channel on which the PDU was received
rssi             int32, optional        Received signal strength indicator
timestamp        uint32, optional       When the PDU was received
crc_validity     bool, optional         ``true`` if CRC is valid, ``false`` otherwise
pdu              bytes                  ANT PDU
rf_channel       uint32                 RF channel on which the PDU was received
================ ====================== ==========================================

.. _ANTChannelEventNotif:

ChannelEvent
^^^^^^^^^^^^

This notification message is sent by the WHAD interface to inform the host
about the current state of the ANT controller on a given channel.

================ ========================= ==========================================
**Field**        **Type**                  **Description**
================ ========================= ==========================================
channel_number   uint32                    Channel number
event            :ref:`ANTChannelEvent`    Channel event type
================ ========================= ==========================================