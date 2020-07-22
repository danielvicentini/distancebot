# Social Distance

This is the social distance project description


## Business/Technical Challenge
As work environment re-opens after the COVID-19 pandemic peak, a new normal will have to be defined. 
While we all hope that there will not be another pandemic in this proportion, we are all aware that it is extremely likely that similar situations will recur. 

Unfortunately, companies nowadays have no means of reinforcing preventive measures in the workplace, such as wearing facial masks or maximum number of people in a room, let alone tracking the times and locations within their sites that an employee or visitor has passed, once he/she reports being infected.  

## Proposed Solution
In order to address this challenge, our team proposes building a platform capable of capturing and analyzing information from multiple sources, giving visibility about the issues listed above. 

Platform will be composed of multiple blocks, implementing an architecture that allow the platform to expand.
There will be three kind of modules: 
 -Monitoring modules: responsible for capturing information from multiple sources. 
 -Backend modules: responsible for storing and analyzing this information, extracting insights from it. 
 -Frontend modules: responsible for platform configuration, alerts and reports. 

Webex Teams will be leveraged as the frontend.    

Regarding monitoring modules, the following is implemented: 
 * Detection of people not using facial mask, leveraging video analytic build over Meraki cameras. 
 * Identification and counting of people in a certain site leveraging Meraki cameras native analytics, Meraki WiFi location APIs and others.
 * Tracing people with whom an infected person had contact within the work environment during the period when he was supposed to have had the virus incubated.
 
 Regarding Backend modules:
 * DB system: reponsible to receive and store data generated by the monitoring modules. Responsible to generate reports for Facility manager and employees to help suport office social distance regulations. 
 * Dashboard System: Web Based application that provides to the facility manager the healthy state of the offices.
 * Alert System: reponsible to alert, based on real time information, facility manager and employees of current social distance out of compliance rules.
 * (FUTURE) - Detecting the minimum distance between people in a site (stretch goal), levering video analytics build over Meraki cameras.  

Regarding Frontend Modules:
 * Webex Bot: responsible to communicate with the facility manager of the office and the users to interact with this Solution.
 * We design an easy "normal human/non-IT users" communication system where the bot tries to understand user needs and helps them with simple step questions to get configurations and or reports done.
 * Facility Manager can setup Max Room people presence to comply with company regulations, activate Camera Mask Detection and ask current or past information about office status to take proper decisions.
 * Employess can talk to the bot to identify the best days to go to the office according to Occupancy History.
 * Bot send alerts to users in the office and the facility manager when people without mask is detected and if the quantity of people in a particular room reaches a certain treshold.

### Cisco Products Technologies/ Services
Our solution will levegerage the following Cisco technologies

* Meraki Cameras and Access-Point (http://meraki.cisco.com)
* Webex Teams (http://teams.webex.com)

## Team Members
* Marcos Alves <maralves@cisco.com> - TSS-GVE
* Daniel Vicentini <dvicenti@cisco.com> - PSE
* Andrey Cassemiro <acassemi@cisco.com> - SE
* Flavio Correa <flcorrea@cisco.com> - TSA


## Solution Components

Infrastructure Components:
* Linux Server to host applications
* Python applications to exchange information at the Backend, Monitoring Modules and Front End modules
* Influx DB for data storage
* Grafana Server for Dashboard GUI
* A cloud IaaS service to host all the components - In our project we host it on Digital Ocean Service.
* Cisco Webex Teams Cloud Services as a Fronted for the users
* Cisco Meraki Cloud Services to interact with the necessary information

Cisco Hardware:
* Meraki MV and MR devices to generate Data


## Usage

## Front End Interaction

Users must have a proper Webex Teams account created and the Webex Teams client (Desktop or Mobile) installed.

Theres are two types of users known by the Frontend system: the regular employess wich are Webex Teams users and the Admin users that are the Facility Managers/People responsible for the Social Distance compliance at the offices. The Admin users are also Cisco Webex Teams users.

The Webex Teams users (both admin or regular users) will interact with the Bot which it will understand certain configured commands. When a user chat with the bot, it will automaticaly understand if a user is or isn't a admin users. After that it will provide users with the available commands for them.

The Bot will try to understand what user is typing and provide the closest know option it knows.

### Initiating Chat with the bot

Firts, look for bot name at the Webex Teams "People" list. After finding it, starts a 1:1 chat room.

### Commands available for All users

* Help:  Will provided the known commands for the users depending of his/her role (regular or admin)
* Report Best Days to go to office: this option will tell user what is the best days to go to a room at the office. Users will provide a past day information where bot will use to generate a data block to compute days of week with lowest Occupancy. Example - past 15 days.

### Commands available for Admin Users

* Configure Room Distancing: define the maximum allowed quantity of people in a certain Room. The maximum information will serve as the threshold for alerts after this condition is reached. The maximum information will impact reporting around out of compliance Social Distancing. Bot will ask room name and max qty of people in that room.
* Start/Stop Camera (for mask detection): define wich Meraki Cameras will be used to take snapshots and analyze if there's people in the room without Masks. Bot will ask for Camera name.
* Show Running Configuration: this option will show 1) the current configuration wich is the Admin users id; 2) The "Admins Room' name used for the bot to inform admin alerts and 3) the configured rooms with Room Name and Max people quantity defined.
* Show Inventory: this option will show the actual Meraki Devices been used for the system to gather information and interact for Mask Detection in the case of MV Cameras.
* Report historic of Distancing: this option will information by rooms and dates the shifts that Occupancy of rooms where beyond Social Distance Rules, reaching out of compliance. Bot will ask user to provied a past time information to provide the report - example past 15 days.
* Report Mask Detection: thil option will report how many People with no-mask events were detected in the past days. Bot will ask user to provied a past time information to provide the report - example past 15 days.
* Report Tracing: this option will report a list of people that were at the office and rooms with a suspect of contagion in a certain period. Bot will ask userid of suspect and a time frame to investigate the list of users. Example: userid, startdate, end date.

## Installation

### Pre-requisites

The Following resources will be needed before the installation:
* For Webex Teams bot will be necessary to create the bot identity. Please check how to create a bot at http://develeper.webex.com if necessary.
* The following 4 Webex Teams pieces of information are necessary: bot email, bot token, bot tag, and bot public URL address - This URL should be the public address where this application will be hosted. Any public Internet Source service that hosts aplications and provide public Web access should work.
* A Meraki API-key. The application connects with Meraki Dashboard and Meraki MV API. The API-Key can be generate in the Settings Dashboard at http://dashboard.meraki.com


## Documentation

Pointer to reference documentation for this project.


## License

Provided under Cisco Sample Code License, for details see [LICENSE](./LICENSE.md)

## Code of Conduct

Our code of conduct is available [here](./CODE_OF_CONDUCT.md)

## Contributing

See our contributing guidelines [here](./CONTRIBUTING.md)
