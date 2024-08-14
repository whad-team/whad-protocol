.. _domain_ble:

Bluetooth Low Energy Domain
===========================

The Bluetooth Low Energy Domain service implements a series of procedures and
messages allowing to interact with BLE devices and connections.

Bluetooth Low Energy procedures
-------------------------------

Discovering access addresses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the WHAD interface implements the :ref:`SniffAccessAddressCmd` command then
it is able to discover access addresses.

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: SniffAccessAddressCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Host->>+Interface: StartCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        loop
            Interface->>Host: AccessAddressDiscovered
        end
        Host->>+Interface: StopCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)


The host sends a :ref:`SniffAccessAddressCmd` command to switch the WHAD
interface into access address sniffing mode and then starts the WHAD interface
with a :ref:`StartCmd`. Discovered access addresses are reported to the host
by the WHAD interface through a series of :ref:`AccessAddressDiscovered`
messages.


Scanning devices
^^^^^^^^^^^^^^^^

The WHAD interface can be set into scanning mode in order to discover
any available devices. This mode can be *passive* or *active*: in *active* mode
the WHAD interface will send a BLE scan request (``SCAN_REQ``) PDU for
each advertisement it receives in order to get more information from devices.

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: ScanModeCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Host->>+Interface: StartCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        loop
            Interface->>Host: PduReceived
        end
        Host->>+Interface: StopCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)

First, the host sends a :ref:`ScanModeCmd` message to the WHAD interface. If
the ``active_scan`` field is set to ``true``, the WHAD interface will send a
scan request for each advertisement it receives. If set to ``false``, only the
received advertisement will be reported to the host.

Initiating a connection to a target device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: CentralModeCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Host->>+Interface: ConnectToCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Host->>+Interface: StartCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Interface->>Host: Connected
        Note over Host,Interface: Connection is established

First, the host puts the WHAD interface in *central* mode by sending a
:ref:`CentralModeCmd` message to the WHAD interface. If this command succeeds,
then the host sends a :ref:`ConnectToCmd` message providing the WHAD interface with
all the information required to initiate a connection to the target device.
The ``bd_address`` and ``addr_type`` can be provided to initiate a normal
connection on a device. 

If the connection cannot be initiated, no :ref:`Connected` message is sent by the
WHAD interface. The host needs to enforce a timeout to determine if the
connection has failed.

Creating a BLE peripheral
^^^^^^^^^^^^^^^^^^^^^^^^^

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: PeripheralModeCmd(adv_data, scanrsp_data)
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Host->>+Interface: StartCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Note over Host,Interface: Peripheral is advertising
        Interface->>Host: Connected
        Note over Host,Interface: Central device is connected
        Interface->>Host: Disconnected
        Note over Host,Interface: Central device has disconnected
        Host->>+Interface: StopCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Note over Host,Interface: Peripheral is stopped, no advertising

First, the host sends a :ref:`PeripheralModeCmd` to the WHAD interface in order
to set it in BLE peripheral mode. This message provides the WHAD interface with
the advertising data and optional scan response to send while advertising. At
this point, the BLE peripheral is configured but not yet advertising.

The host must send a :ref:`StartCmd` message to make the WHAD interface advertising.
Once started, the WHAD interface will wait for BLE connections initiated by other
devices. If a connection is established, the host is notified with a :ref:`Connected`
notification sent by the WHAD interface.

If a device disconnects, a :ref:`Disconnected` notification message is sent
to the host.

The host can stop this BLE peripheral at any time by sending a :ref:`StopCmd`
command.

Sending and receiving PDUs
^^^^^^^^^^^^^^^^^^^^^^^^^^

Once a connection established (in *central* or *peripheral* mode), the host
can provide the WHAD interface with a PDU to send. If the WHAD interface does
have the ``NoRawData`` capability (see. :ref:`Capability`), the host must send
:ref:`SendPduCmd` messages. If the WHAD interface can send raw PDU, it must
send :ref:`SendRawPduCmd` messages.

A received PDU is notified by the WHAD interface to the host through a
:ref:`PduReceived` message or :ref:`RawPduReceived` message depending on its
capabilities.

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: SendPduCmd
        Interface-->>-Host: CommandResult(result=SUCCESS)
        Note over Host,Interface: PDU send by host
        Interface->>Host: PduReceived
        Note over Host,Interface: Interface sends a received PDU


Enumerations
------------

.. _BleCommand:

BleCommand
^^^^^^^^^^

This enumeration contains the various BLE commands ID that are required to
create the domain supported commands bitmap.

.. _BleAdvType:

BleAdvType
^^^^^^^^^^

This enumeration specifies the different advertisement types.

=============== ==========================================
Type            Description
=============== ==========================================
ADV_UNKNOWN     Unknown advertisement type (default)
ADV_IND         Indirected advertisement
ADV_DIRECT_IND  Directed advertisement
ADV_NONCONN_IND Non-connectable indirected advertisement
ADV_SCAN_IND    Indirected scan advertisement
ADV_SCAN_RSP    Scan response
=============== ==========================================

.. _BleDirection:

BleDirection
^^^^^^^^^^^^

This enumeration specifies the direction of a PDU.

=================== ==========================================================
Direction           Description
=================== ==========================================================
UNKNOWN             Direction is unknown (default)
MASTER_TO_SLAVE     PDU is sent by the connection initiator
SLAVE_TO_MASTER     PDU is sent by the advertising device
INJECTION_TO_SLAVE  PDU has to be injected and target the advertising device
INJECTION_TO_MASTER PDU has to be injected and target the initiator
=================== ==========================================================

.. _BleAddrType:

BleAddrType
^^^^^^^^^^^

This enumeration specifies the Bluetooth Device address type.

================ ================================================
Type             Description
================ ================================================
PUBLIC           Device BD address is public
RANDOM           Device BD address is random
================ ================================================

The address type information is part of the protocol, usually specified
by the ``TxAdd``and ``RxAdd`` bits in the BLE header. It is critical to
specify the correct address type for a device or a connection will fail.

Messages
--------

.. _AccessAddressDiscovered:

AccessAddressDiscovered
^^^^^^^^^^^^^^^^^^^^^^^

This notification message is sent each time an access address has been
discovered.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
access_address   uint32             Access address
rssi             int32, optional    Received signal strength indicator
timestamp        uint64, optional   When the access address has been discovered
================ ================== ===========================================

.. _AdvPduReceived:

AdvPduReceived
^^^^^^^^^^^^^^

This notification message is sent whenever an advertising PDU has been
received.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
adv_type         :ref:`BleAdvType`  BLE advertisement type
rssi             int32              Received signal strength indicator
bd_address       bytes              Advertiser BD address
adv_data         bytes              Advertising data
addr_type        :ref:`BleAddrType` Advertiser BD address type
================ ================== ===========================================

.. _AdvModeCmd:

AdvModeCmd
^^^^^^^^^^

This message sets the WHAD device in advertising mode.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
scan_data        bytes              Advertising data (31 bytes max)
scanrsp_data     bytes              Scan response data (31 bytes max)
================ ================== ===========================================

``scan_data`` sets the WHAD interface advertising data while ``scanrsp_data``
provides some extra advertising data that will be used to answer SCAN_REQ PDUs.

``scan_data`` is mandatory while ``scanrsp_data`` is optional.

.. _CentralModeCmd:

CentralModeCmd
^^^^^^^^^^^^^^

This message sets the WHAD interface into Central mode.

.. note::

    This message has no field.

.. _Connected:

Connected
^^^^^^^^^

This notification message is sent when a BLE connection is successfully
established.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
initiator        bytes              Initiator BD address
advertiser       bytes              Advertiser BD address
access_address   uint32             Connection access address
conn_handle      uint32             Connection handle
adv_addr_type    :ref:`BleAddrType` Advertiser BD address type
init_addr_type   :ref:`BleAddrType` Initiator BD address type
================ ================== ===========================================


.. _ConnectToCmd:

ConnectToCmd
^^^^^^^^^^^^

This message specifies a target device to connect to, or an existing connection
to follow.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
bd_address       bytes              Target device BD address (6 bytes)
addr_type        :ref:`BleAddrType` Target device address type
access_address   uint32, optional   Target connection access address
channel_map      bytes, optional    Target connection channel map
hop_increment    uint32, optional   Target connection hop increment (CSA #1)
hop_interval     uint32, optional   Target connection hop interval (CSA #1)
crc_init         uint32, optional   Target connection CRCInit value
================ ================== ===========================================

.. note::

    Only BLE v4 connections synchronization are supported for now, since CSA #2
    is not implemented yet (and requires extra parameters)

.. _DeleteSequenceCmd:

DeleteSequenceCmd
^^^^^^^^^^^^^^^^^

This message deletes a previously registered prepared sequence.

=================== ============ ===========================================
**Field**           **Type**     **Description**
=================== ============ ===========================================
id                  uint32       Prepared sequence ID
=================== ============ ===========================================

.. _Desynchronized:

Desynchronized
^^^^^^^^^^^^^^

This notification message is sent when the WHAD interface is desynchronized
from an active connection.

=================== ============ ===========================================
**Field**           **Type**     **Description**
=================== ============ ===========================================
access_address      uint32       Connection access address
=================== ============ ===========================================

.. _DisconnectCmd:

DisconnectCmd
^^^^^^^^^^^^^

This message terminates an existing connection.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
conn_handle      uint32             Connection handle
================ ================== ===========================================

.. _Disconnected:

Disconnected
^^^^^^^^^^^^

This notification message is sent when a connection has terminated.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
reason           uint32             Termination reason
conn_handle      uint32             Connection handle
================ ================== ===========================================

.. _HijackBothCmd:

HijackBothCmd
^^^^^^^^^^^^^^^

This message sets the WHAD interface into hijacking mode, targeting both the
initiating device and the advertising device.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
access_address   uint32             Target connection access address
================ ================== ===========================================

.. _Hijacked:

Hijacked
^^^^^^^^

This notification message is sent by the WHAD interface to notify the result
of a connection hijacking.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
success          bool               ``true`` if hijacking has succeeded
access_address   uint32             Target connection access address
================ ================== ===========================================


.. _HijackMasterCmd:

HijackMasterCmd
^^^^^^^^^^^^^^^

This message sets the WHAD interface into hijacking mode, targeting the device
that initiated the target connection.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
access_address   uint32             Target connection access address
================ ================== ===========================================


.. _HijackSlaveCmd:

HijackSlaveCmd
^^^^^^^^^^^^^^^

This message sets the WHAD interface into hijacking mode, targeting the
advertising device.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
access_address   uint32             Target connection access address
================ ================== ===========================================



.. _Injected:

Injected
^^^^^^^^

This notification message is sent by the WHAD interface to notify the result
of a packet injection.

================== ================ ===========================================
**Field**          **Type**         **Description**
================== ================ ===========================================
success            bool             ``true`` if hijacking has succeeded
access_address     uint32           Target connection access address
injection_attempts uint32           Number of injection attempts
================== ================ ===========================================


.. _JamAdvCmd:

JamAdvCmd
^^^^^^^^^

This message sets the WHAD interface in BLE advertisements jamming mode.
In this mode, the interface jams all BLE advertising channels.

.. note::

    This message has no field.

.. _JamAdvOnChannelCmd:

JamAdvOnChannelCmd
^^^^^^^^^^^^^^^^^^

This message sets the WHAD interface in single-channel BLE advertisements
jamming mode.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
channel          uint32             Target channel to jam
================ ================== ===========================================

.. note::

    Looks like a duplicate with :ref:`JamAdvCmd`, may be interesting to use
    this command with an optional channel value instead.

.. _JamConnCmd:

JamConnCmd
^^^^^^^^^^

This message sets the WHAD interface into connection jamming.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
access_address   uint32             Target access address
================ ================== ===========================================

``access address`` specifies the Access Address of the connection to jam.

.. _PduReceived:

PduReceived
^^^^^^^^^^^

This notification message is sent by the WHAD interface to report a raw PDU
received to the host.

================== ====================== ============================================
**Field**          **Type**               **Description**
================== ====================== ============================================
direction          :ref:`BleDirection`    Direction
pdu                bytes                  PDU
conn_handle        uint32                 Connection handle
processed          bool                   ``true`` if already processed by firmware
decrypted          bool                   ``true`` if already decrypted by firmware
================== ====================== ============================================


.. _PeripheralModeCmd:

PeripheralModeCmd
^^^^^^^^^^^^^^^^^

This message sets the WHAD interface in peripheral mode. In this mode, the
interface will send advertisements and accept incoming connections.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
scan_data        bytes              Advertising data (31 bytes max)
scanrsp_data     bytes              Scan response data (31 bytes max)
================ ================== ===========================================

.. _PrepareSequenceCmd:

PrepareSequenceCmd
^^^^^^^^^^^^^^^^^^

This message tells the WHAD interface to prepare a sequence of packets for
transmission. This transmission will be triggered by a specific condition.

================ ====================== ===========================================
**Field**        **Type**               **Description**
================ ====================== ===========================================
trigger          :ref:`Trigger`         Reception trigger
id               uint32                 Sequence unique ID
direction        :ref:`BleDirection`    Direction
sequence         :ref:`PendingPacket`   Sequence of prepared packets
================ ====================== ===========================================

``trigger`` must be one of the following available triggers:

- :ref:`ReceptionTrigger`
- :ref:`ConnectionEventTrigger`
- :ref:`ManualTrigger`

.. _RawPduReceived:

RawPduReceived
^^^^^^^^^^^^^^

This notification message is sent by the WHAD interface to report a raw PDU
received to the host.

================== ====================== ============================================
**Field**          **Type**               **Description**
================== ====================== ============================================
direction          :ref:`BleDirection`    Direction
channel            uint32                 BLE channel on which the PDU was received
rssi               int32, optional        Received signal strength indicator
timestamp          uint64. optional       When the PDU has been received
relative_timestmap uint64, optional       Relative timestamp
crc_validity       bool, optional         ``true`` if CRC is valid, ``false``otherwise
access_address     uint32                 Connection access address
pdu                bytes                  PDU
crc                uint32                 PDU CRC
conn_handle        uint32                 Connection handle
processed          bool                   ``true`` if already processed by firmware
decrypted          bool                   ``true`` if already decrypted by firmware
================== ====================== ============================================

.. _ReceptionTrigger:

ReceptionTrigger
~~~~~~~~~~~~~~~~

The reception trigger is basically a pattern-based trigger with offset and mask:

================ ====================== =======================================
**Field**        **Type**               **Description**
================ ====================== =======================================
pattern          bytes                  Pattern to match
mask             bytes                  Bitmask for pattern
offset           uint32                 Pattern offset
================ ====================== =======================================

.. _ConnectionEventTrigger:

ConnectionEventTrigger
~~~~~~~~~~~~~~~~~~~~~~

================ ====================== =======================================
**Field**        **Type**               **Description**
================ ====================== =======================================
connection_event uint32                 Connection event to match
================ ====================== =======================================

.. _ManualTrigger:

ManualTrigger
~~~~~~~~~~~~~

This trigger specifies that the sequence will be triggered manually with a
specific message (:ref:`TriggerSequenceCmd`).

.. note::

    This message have no specific field.

.. _PendingPacket:

PendingPacket
~~~~~~~~~~~~~

This message defines a pending packet.

================ ====================== =======================================
**Field**        **Type**               **Description**
================ ====================== =======================================
packet           bytes                  Packet bytes (PDU)
================ ====================== =======================================


.. _ReactiveJamCmd:

ReactiveJamCmd
^^^^^^^^^^^^^^

This message sets the WHAD interface into reactive jamming mode.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
channel          uint32             Target channel
pattern          bytes              Pattern to trigger jamming
position         uint32             Pattern position in payload
================ ================== ===========================================


.. _ScanModeCmd:

ScanModeCmd
^^^^^^^^^^^

This message sets the WHAD interface into scanning mode.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
active_scan      bool               Enable active mode
================ ================== ===========================================

If ``active_scan`` is set to True, the WHAD device sends a SCAN_REQ for each
advertisement received. If set to False, only advertisements (ADV_IND, ...)
will be reported to host.

.. _SendPduCmd:

SendPduCmd
^^^^^^^^^^

This message specifies a BLE PDU to send. There is no control over its header
nor CRC.

================ =================== ==========================================
**Field**        **Type**            **Description**
================ =================== ==========================================
direction        :ref:`BleDirection` PDU direction
conn_handle      uint32              Connection handle
pdu              bytes               Raw pdu to send
encrypt          bool                Let hardware encrypt PDU if ``true``
================ =================== ==========================================

.. _SendRawPduCmd:

SendRawPduCmd
^^^^^^^^^^^^^

This message specifies a raw BLE PDU to send. Raw PDU gives control over the
BLE PDU header and its CRC.

================ =================== ==========================================
**Field**        **Type**            **Description**
================ =================== ==========================================
direction        :ref:`BleDirection` PDU direction
conn_handle      uint32              Connection handle
access_address   uint32              Connection access address
pdu              bytes               Raw pdu to send
crc              uint32              PDU CRC
encrypt          bool                Let hardware encrypt PDU if ``true``
================ =================== ==========================================

.. warning::

    Only devices without the :ref:`NoRawData` capability can send this message.

.. _SetAdvDataCmd:

SetAdvDataCmd
^^^^^^^^^^^^^

This message sets the advertising data and scan response data.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
scan_data        bytes              Advertising data (31 bytes max)
scanrsp_data     bytes              Scan response data (31 bytes max)
================ ================== ===========================================

`scan_data`` is mandatory while ``scanrsp_data`` is optional.


.. _SetBdAddressCmd:

SetBdAddressCmd
^^^^^^^^^^^^^^^

This message sets the WHAD interface *Bluetooth Device (BD)* address.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
bd_address       bytes              Bluetooth Device address (6 bytes)
addr_type        :ref:`BleAddrType` Address type
================ ================== ===========================================

.. _SetEncryptionCmd:

SetEncryptionCmd
^^^^^^^^^^^^^^^^

This message sets the WHAD interface cryptographic material for a specific
connection.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
conn_handle      uint32             Connection handle
enabled          bool               Enable encryption if set to ``true``
ll_key           bytes              Link-layer encryption key
ll_iv            bytes              Link-layer initialization vector
key              bytes              Encryption key
rand             bytes              Random value
ediv             bytes              Diversifier value
================ ================== ===========================================


.. _SniffAccessAddressCmd:

SniffAccessAddressCmd
^^^^^^^^^^^^^^^^^^^^^

This message sets the WHAD interface into Access Address sniffing mode.

================== ================== =========================================
**Field**          **Type**           **Description**
================== ================== =========================================
monitored_channels bytes              Channel map 
================== ================== =========================================

The ``monitored_channels`` field specifies a BLE channel map which each bit
represent a channel (from 0 to 39). This channel map is stored in a 5-byte
buffer. Usually, advertising channels (37, 38 and 39) are excluded as they
are not used by BLE connections for data exchange.


.. _SniffActiveConnCmd:

SniffActiveConnCmd
^^^^^^^^^^^^^^^^^^

This message sets the WHAD interface into active connection sniffing mode.

================== ================== =========================================
**Field**          **Type**           **Description**
================== ================== =========================================
access_address     uint32             Target access address
crc_init           uint32             CRC initial seed
channel_map        bytes              Connection channel map
hop_interval       uint32             Hop interval (CSA #1)
hop_increment      uint32             Hop increment (CSA #1)
monitored_channels bytes              Channel map used for sniffing
================== ================== =========================================



.. _SniffAdvCmd:

SniffAdvCmd
^^^^^^^^^^^

This message sets the WHAD interface into BLE advertising sniffing mode. The
target channel can be specified, as well as a target BD address.

================ ================== ===========================================
**Field**        **Type**           **Description**
================ ================== ===========================================
use_extended_adv bool               Enable Extended advertisements sniffing
channel          uint32             Target channel to sniff
bd_address       bytes              Target BD address
================ ================== ===========================================

``channel`` specifies the channel to sniff on, usually one of the default BLE
advertising channels (37, 38 or 39).

``bd_address`` specifies a specific BD address used to filter BLE
advertisements and only keep those matching this address, except when set to
``FF:FF:FF:FF:FF:FF`` (a buffer of 6 bytes with value 0xFF).

The ``use_extended_adv`` option can be used with BLE5 compatible WHAD
interfaces to follow extended advertisements that occur on data channels.

.. _SniffConnReqCmd:

SniffConnReqCmd
^^^^^^^^^^^^^^^

This message sets the WHAD interface into BLE connection request sniffing
mode.

=================== ============ ===========================================
**Field**           **Type**     **Description**
=================== ============ ===========================================
show_empty_packets  bool         Report BLE empty PDUs (size = 0)    
show_advertisements bool         Report the target device advertisement
channel             uint32       Target channel to sniff
bd_address          bytes        Target BD address
=================== ============ ===========================================

Setting ``show_empty_packets`` to ``true`` makes the WHAD interface report all
PDUs, even the empty ones. Setting ``show_advertisements`` will report any
advertisement seen on the specified ``channel`` before a connection is
initiated.

``channel`` specifies the advertising channel the WHAD interface will listen on
to capture a ``CONN_REQ`` PDU used to initiate a BLE connection.

If ``bd_address`` is set, it will be used a filter to target a connection to
the corresponding BD address. If set to *FF:FF:FF:FF:FF:FF* (6 0xFF bytes) then
the WHAD interface will not filter connection initiation requests.

.. _StartCmd:

StartCmd
^^^^^^^^

This message starts the WHAD interface in the currently selected mode.

.. note::

    This message has no specific field.

.. _StopCmd:

StopCmd
^^^^^^^

This message stops the WHAD interface that then goes idle.

.. note::

    This message has no specific field.

.. _Synchronized:

Synchronized
^^^^^^^^^^^^

This notification message is sent when the WHAD interface is successfully
synchronized with an active connection.

=================== ============ ===========================================
**Field**           **Type**     **Description**
=================== ============ ===========================================
access_address      uint32       Connection access address
crc_init            uint32       Connection CRCInit value
hop_interval        uint32       Hop interval (CSA #1)
hop_increment       uint32       Hop increment (CSA #1)
channel_map         bytes        Connection channel map
=================== ============ ===========================================


.. _Triggered:

Triggered
^^^^^^^^^

This notification message is sent by the WHAD interface when a prepared
sequence has been triggered.

=================== ============ ===========================================
**Field**           **Type**     **Description**
=================== ============ ===========================================
id                  uint32       Prepared sequence ID
=================== ============ ===========================================

.. _TriggerSequenceCmd:

TriggerSequenceCmd
^^^^^^^^^^^^^^^^^^

This message manually triggers a prepared sequence identified by its id.

=================== ============ ===========================================
**Field**           **Type**     **Description**
=================== ============ ===========================================
id                  uint32       Prepared sequence ID
=================== ============ ===========================================

