Open protocol for wireless hacking tools
========================================

This project is still a work in progress and could change
at any time.

Objectives
----------

This protocol has the main objective to allow interoperability between hardware RF devices and
wireless (hacking) tools, independantly of the supported technology. Other objectives include
but are not limited to:

* to provide a protocol that can be implemented in various programming languages
* to optimize the size of the exchanged data
* to allow new features/protocols to be easily added (evolutivity)

Design choices
--------------

This protocol relies on Protocol Buffers because it is supported by a lot of programming
languages, provides a way to model messages and optimized serialization/deserialization. 

However, we added an overlay to allow fragmented chunks of data to be sent and received
by devices and host applications.

### Domains

This protocol has been designed to be used with a variety of wireless protocols and therefore
consider each protocol to be a specific *domain* with associated messages. Using separate
*domains* will allow easier integration of new protocols in the future without having to
change the existing messages.

The following domains are currently supported:

* Bluetooth Low Energy
* 802.15.4: used for ZigBee and other derivated protocols such as RF4CE
* Nordic Semiconductor Enhanced ShockBurst: used for ESB and other derivated protocols
* Logitech Unifying
* PHY: support various modulations (*FSK, *PSK, ASK, LoRa)


### Capabilities

Each device that supports this protocol must support a set of generic messages, independently of the supported
wireless protocols. These messages allow:

* to identify the device including its firmware version and its supported communication protocol version
* to query the domains this device supports
* to query its capabilities per supported domain
* to retrieve the list of messages/commands it supports

This discovery step is part of the communication protocol and allows third-party tools to determine if an
hardware device can be used to achieve a specific task, no matter its firmware.

#### Bluetooth Low Energy capabilities

* Low-level capabilities
	* Advertisements sniffing
    * Connection sniffing (capture of connection initiation request)
    * Connection sniffing (passive monitoring)
    * direct PDU injection
    * PDU injection into an existing connection, to the slave device
    * PDU injection into an existing connection, to the master device
    * Connection hijacking targeting the master
    * Connection hijacking targeting the slave 
	* Connection Man-in-the-Middle targeting initiation requests
    * Connection Man-in-the-Middle targeting an existing connection
    * Connection jamming
    * Advertisements jamming
    * Reactive jamming

* High-level capabilities
	* Scanner role: the device can listen for advertisements and report them
    * Advertiser role: the device can send advertisements
	* Central role: the device can act as a BLE Central device and initiate a connection
	* Peripheral role: the device can act as BLE Peripheral device and receive connections

#### 802.15.4 capabilities

* Low-level capabilities
	* Channel jamming
	* Reactive jamming
	* Packet injection with control of its FCS
    * Packet injection without control of its FCS
    * Packet sniffing
    * Man-in-the-middle attack

* High-level capabilities
	* End device role: device can join a ZigBee network and act as an end device
	* Coordinator role: device can act as a Coordinator and manages its own ZigBee network
	* Router role: device can act as a Router and relay packets

#### Enhanced ShockBurst capabilities

* Low-level capabilities
    * Channel jamming
	* Reactive jamming
	* Packet injection
	* Packet sniffing (any address)
    * Packet sniffing (targeting a specific address)

* High-level capabilities
	* PRX role: the device can listen for packets and send acks
	* PTX role: the device can send packets

#### PHY capabilities
* Low-level capabilities
	* Frequency selection
    * Modulation selection
    * Datarate selection
    * Preambule selection
    * Packet size selection
    * Raw packet sniffing
    * Raw packet injection
    * Channel activity monitoring

