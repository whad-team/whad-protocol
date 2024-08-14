.. _discovery_service:

WHAD Discovery service
======================

The discovery service is a key element of WHAD, as it provides a series
of messages that are used to discover a device information, supported domains
and capabilities.

All the following messages are defined in the `device.proto` file.

Discovery procedures
--------------------

Device initialization
^^^^^^^^^^^^^^^^^^^^^

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: DeviceResetQuery
        Interface->>-Host:DeviceReadyResp

When WHAD initializes a device, it sends a :ref:`DeviceResetQuery` message
to this device and expects to receive a :ref:`DeviceReadyResp` once the
device has successfully restarted and is ready to use.

Supporting this message is mandatory as it is litterally the first message WHAD will
send to a device. Most of our compatible devices just reset their internal state
and answer back with a :ref:`DeviceReadyResp` message.

Once the device reset, the host sends a :ref:`DeviceInfoQuery` message to get
some information on this device and to determine:

- the version of WHAD protocol it supports in order to avoid sending messages this device will not understand
- the supported domains and the related capabilities for each of them

The device **must** answer with a :ref:`DeviceInfoResp` message including all the
required information. If it does not, the host will consider the device unresponding
and will stop the communication.



Device domains discovery
^^^^^^^^^^^^^^^^^^^^^^^^

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: DeviceInfoQuery
        Interface->>-Host: DeviceInfoResp
        

Once the device reset, the host sends a :ref:`DeviceInfoQuery` message to get
some information on this device and to determine:

- the version of WHAD protocol it supports in order to avoid sending messages this device will not understand
- the supported domains and the related capabilities for each of them

The device **must** answer with a :ref:`DeviceInfoResp` message including all the
required information. If it does not, the host will consider the device unresponding
and will stop the communication.

Per-domain capabilities discovery
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: DeviceDomainInfoQuery(domain=Domain.BtLE)
        Interface->>-Host: DeviceDomainInfoResp
        Host->>+Interface: DeviceDomainInfoQuery(domain=Domain.Phy)
        Interface->>-Host: DeviceDomainInfoResp

Once the domains have been successfully discovered, the host will send for each of
them a :ref:`DeviceDomainInfoQuery` message and expect the device to answer each one
with a corresponding :ref:`DeviceDomainInfoResp` message.

Device transport speed modification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. mermaid::

    sequenceDiagram
        participant Host
        participant Interface
        Host->>+Interface: SetTransportSpeed(1000000)
        Interface->>Host: CommandResult(result=SUCCESS)
        Host->>Host: Update transport speed
        Interface->>-Host: DeviceReadyResp

This discovery phase is always performed with the transport default speed. For UART,
it is set to 115200 bauds by default. Some devices however support higher speeds and
keeping using a low speed while communication may be faster is not a good idea.

The host can ask the WHAD device to update its communication speed by sending a
:ref:`SetTransportSpeed` message. Once this message issued, the target device
is expected to update its speed while the host also reconfigure its interface,
and the host expects to receive a :ref:`DeviceReadyResp` message from the device.

If no message is received by the host after its interface reconfiguration, the
device is considered as disconnected and the host will drop the communication.

Enumerations
------------

.. _Domain:

Domain
^^^^^^

This enumeration lists all the supported domains, including some that are not
yet defined in our WHAD protocol.

.. _DeviceType:

DeviceType
^^^^^^^^^^

This enumeration lists some of the currently supported devices. You can ask us
to add yours in this list.

.. _Capability:

Capability
^^^^^^^^^^

This enumeration lists all the capability flags that can be combined in a :ref:`DeviceInfoResp`
message. 

================ =========================================
Value            Description
================ =========================================
_CapNone         No specific capability
Scan             Device can scan and detect other devices
Sniff            Device is able to sniff data
Inject           Device can inject/send data
Jam              Device can jam
Hijack           Device is able to hijack connections
SimulateRole     Device can act as a specific role
NoRawData        Device cannot send or receive raw data
================ =========================================

Messages
--------

.. _DeviceResetQuery:

DeviceResetQuery
^^^^^^^^^^^^^^^^

This message asks the device to reset its internal state to default. If the
device was performing some action, this action is stopped and it switches to
idle mode.

.. note::
    
    This message has no field.

.. _DeviceReadyResp:

DeviceReadyResp
^^^^^^^^^^^^^^^

This message is sent by a WHAD device to its host, notifying the device is ready
to operate and in idle mode.

.. note::
    
    This message has no fields

.. _DeviceInfoQuery:

DeviceInfoQuery
^^^^^^^^^^^^^^^

This message is sent by the host to a compatible device to ask for its information.

================ =============== ==============================================
**Field**        **Type**        **Description**
================ =============== ==============================================
proto_ver        uint32          Version of WHAD protocol supported by the host
================ =============== ==============================================

.. _DeviceInfoResp:

DeviceInfoResp
^^^^^^^^^^^^^^^

This message is sent by the host to the device to retrieve some information about
the device:

================ =============== ===========================================
**Field**        **Type**        **Description**
================ =============== ===========================================
type             uint32          Device type, represented by a standard code
devid            bytes           Device unique ID (can be readable)
proto_min_ver    uint32          Minimal WHAD protocol supported version
max_speed        uint32          Maximum supported speed for transport
fw_author        bytes           Firmware author name
fw_url           bytes           Firmware source code URL (github repo, ...)
fw_version_major uint32          Firmware version major number
fw_version_minor uint32          Firmware version minor number
fw_version_rev   uint32          Firmware version rev number
capabilities     uint32[]        List of capabilities
================ =============== ===========================================

Device capabilities are provided as a list of *uint32* values, with each
value composed of a domain (from `Domain`) or'ed with a set of `Capability`.
The host can therefore enumerates the supported domains and for each of them
retrieve the supported capabilities.

In WHAD, a capability determine what a device can do related to a specific protocol:

- `_CapNone`: indicates the device has no capability at all
- `Scan`: can scan on the target protocol and discover devices
- `Sniff`: can sniff packets or data and report it to the host
- `Inject`: can inject packets or data (not related to a *connection*)
- `Jam`: can jam the target protocol, usually a single channel
- `Hijack`: can take over an existing connection
- `Hook`: can perform a Man-in-the-Middle attack
- `SimulateRole`: can mimick a protocol-specific role
- `NoRawData`: cannot report raw data (use this when a WHAD device cannot get all the low-level layer for a specific protocol)

.. _DeviceDomainInfoQuery:

DeviceDomainInfoQuery
^^^^^^^^^^^^^^^^^^^^^

This message is sent by the host to ask a compatible device to give a detailed
overview of the commands it supports for a given domain.

================ =============== ===========================================
**Field**        **Type**        **Description**
================ =============== ===========================================
domain           uint32          Target domain as defined in `Domain`
================ =============== ===========================================

.. _DeviceDomainInfoResp:

DeviceDomainInfoResp
^^^^^^^^^^^^^^^^^^^^

This message is sent by the device to the host and specifies the supported
commands for the requested domain.

================== =============== ===========================================
**Field**          **Type**        **Description**
================== =============== ===========================================
domain             uint32          Target domain as defined in `Domain`
supported_commands uint64          Bitmap of supported commands  
================== =============== ===========================================

The ``supported_commands`` bitmap has a bit set for each command ID it supports,
meaning each domain can have a maximum number of 64 commands.

.. _SetTransportSpeed:

SetTransportSpeed
^^^^^^^^^^^^^^^^^

This message asks the device to change its communication speed. If the device
uses UART communication, then it **must** update its baudrate to the one provided
by the host, and then issue a :ref:`DeviceReadyResp` to tell the host that it is
ready to proceed.

================== =============== ===========================================
**Field**          **Type**        **Description**
================== =============== ===========================================
speed              uint32          Requested speed
================== =============== ===========================================

.. attention::

    Requested speed must not exceed the device's maximal speed as stated in its
    :ref:`DeviceInfoResp` message.