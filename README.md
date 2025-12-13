# Warehouse Management System (Discrete Event Simulator)

**Course:** CS 4347 - Database Systems\
**Semester:** Spring 2025\
**Project:** Warehouse Management System - Clothung and Apparel\
**Language:** Java

## Overview

This project implements a discrete-event network simulator that models single-hop network traffic in a star topology. 
Hosts communicate by sending ping requests and ping responses, and the simulator computes round-trip time (RTT) for each ping using a Future Event List (FEL).
The simulation is event-driven and processes events strictly in time order, closely resembling how real-world network simulators operate.

## Key Features

**Discrete Event Simulation**
* Uses a custom FutureEventList implemented as a doubly-linked list
* Events are processed in increasing simulation time order

**Network Messaging**
* Supports ping requests and ping responses
* Calculates and reports RTT for each completed ping

**Star Topology**
* One central host connected to multiple neighboring hosts
* Communication is always between neighbors

**Extensible Design**
* Built using abstract classes and interfaces
* Designed to mirror real-world simulation frameworks

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

