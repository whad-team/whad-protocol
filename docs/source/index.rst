.. Wireless HAcking Devices Protocol documentation master file, created by
   sphinx-quickstart on Fri Jul  8 15:02:33 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Wireless HAcking Devices Protocol's documentation!
=============================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   generic.rst
   domain/ble/index.rst


Introduction
------------

The *WHAD* protocol aims at providing a unique communication protocol between various
wireless hacking devices used to target specific wireless protocols (BLE, ZigBee, ANT, Mosart, etc.),
quite similar in its principle as the *Bluetooth Host Controller Interface* (*HCI*).

This protocol provides messages to discover compatible devices, determine their capabilities
and every wireless protocol they support as well as the actions that can be performed on one
or multiple remote devices or networks, depending on the wireless technologies they support.

By providing this unified communication interface, *WHAD* allows various tools to use any
*WHAD*-compatible device to sniff or launch attacks on specific wireless protocols, thus
allowing users to use various different hardware devices but also new tools
to be developed upon our per-domain *WHAD* library.

How does it work ?
------------------

*WHAD* protocol provides a discovery service and domain-based messages. The discovery service
is as generic as possible and is used to query a device in order to determine what type
of device it is, what are its capabilities and what are the supported domains. For each
supported domain, the device can provide a set of supported commands that may be used to
interact with a specific wireless protocol, **in a standardized way** defined by the *WHAD*
domain library.

*WHAD* uses Google's Protobuf library for communication between any compatible hardware
device and its client library.


WHAD Services
-------------

* :ref:`WHAD generic service <generic_service>`
* :ref:`WHAD discovery service <discovery_service>`
* :ref:`WHAD Bluetooth Domain service <domain_ble>`



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

