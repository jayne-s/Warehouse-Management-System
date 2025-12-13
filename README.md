# Warehouse Management System

**Course:** CS 4347 - Database Systems\
**Semester:** Spring 2025\
**Project:** Warehouse Management System - Clothing and Apparel\
**Language:** JavaScript

## Overview

Manual or disjointed warehouse systes lead to inventory inaccuracies, delayed shipments, and miscommunication between suppliers and distributors. Inaccurate inventory causes delays, lost revenue, and frustrated customers. This project seeks to streamline inventory and supply chain operations by building a data-driven warehouse management system that ensures accuracy, reduces costs, and boosts efficiency. Our warehouse management system simulates a regional clothing distribution network and approaches the aforementioned problem by keeping operations accurate and reliable by connecting suppliers, warehouses, racks, and distributors in one smooth flow. Every item is tracked with precision, reducing errors and providing real-time inventory visibility. 

## Business Rules

* Suppliers provide clothing to warehouses through a Supply transaction (tracked by a Supply Chain Manager)
* Warehouses store clothing in Racks, on a unique Aisle section and Warehouse
* Inventory Managers oversee clothing items inside the warehouse
* Regional Managers are linked and supervise multiple warehouses
* Distributors receive clothing from warehouses via Distribute transaction (managed by a Supply Chain Manager)
* Every transaction (supply or distribute) includes processing and arrival dates, item counts, and cost or profit details.

## Entity Relationship Model

![ER Diagram](er.jpg)

## Project Components

| **Class** | **Description** |
| --------- | --------------- |
| LinkedEventList | Doubly Linked List implementation of the FutureEventList interface |
| EventNode | Node class for the linked list |
| Message | Represents a network message (ping request or response) |
| SimpleHost | Concrete implementation of a network host | 
| EventException | Custom unchecked exception for event-related errors |
| Main | Entry point that loads input and runs the simulation |

## Network Model

* **Topology:** Star
* **Message Delay:** 1 unit of distance = 1 unit of simulation time
* **RTT Calculation:** RTT = time received - time sent
* **Assumptions:**
  * Host only pings one destination
  * Ping interval is always greater than RTT
  * Input file is complete and valid
  * Event processing order is time based

## How the Simulation Works

* Read input file
* Create hosts and neighbor relationships
* Bootstrap ping events
* Run simulation loop
  * Pop next event from the FutureEventList
  * Call handle() on the event
  * Continue until no events remain 

## Sample Input
```
5
6 2
7 3
-1
5 7 10 28
```
* First number is the central host address
* Following lines are of the format: ```<neighbor address> <distance>```
* -1 terminates list of neighbors
* Following lines are of the format: ```<source> <destination> <interval> <duration>```

## Sample Output
```
[10ts] Host 5: Sent ping to host 7
[13ts] Host 7: Ping request from host 5
[16ts] Host 5: Ping response from host 7 (RTT = 6ts)
[20ts] Host 5: Sent ping to host 7
[23ts] Host 7: Ping request from host 5
[26ts] Host 5: Ping response from host 7 (RTT = 6ts)
[28ts] Host 5: Stopped sending pings
```
* ```ts```= simulation time units
* Output ordering may differ when multiple events occur at the same time

## How to Run

* Place ```simulation.txt``` in the project root directory.
* Compile: ```javac *.java```
* Run: ```java Main```

## Possible Extensions

* Multi-hop routing
* Packet loss and retransmissions
* Visualization of network traffic
* Support for additional message types

