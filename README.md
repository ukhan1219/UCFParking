# UCFParking
UCFParking is a project designed to simplify the often frustrating parking situation at the University of Central Florida (UCF). By leveraging several APIs and web scraping techniques, this tool helps me identify the most efficient parking options on campus, ultimately saving time and reducing stress during the parking process.

## Project Overview
The UCFParking project uses the following technologies:

-  **Twilio**: To send SMS notifications directly to my phone with real-time parking information.
-  **Life360 API**: To track my current location, allowing the system to tailor the parking options based on where I am on campus.
-  **Web Scraping**: The project scrapes data from UCF's official parking website, which provides up-to-date information on the number of available spots in each garage.
### How It Works
1.  **Location Tracking**: Using the Life360 API, the project tracks my current location on or near UCF's campus.
2.  **Data Scraping**: The system scrapes the latest parking data from UCF's website, which lists available spots in each campus garage.
3.  **Data Processing**: The scraped data is converted into a readable format, listing all open garages and the number of available spots.
4.  **SMS Notification**: Twilio is then used to send a text message to my phone with the garage that has the most available spots, saving me time and helping me find parking more efficiently.
### Why This Project?
Parking at UCF is notoriously difficult, especially during peak hours. This project aims to alleviate some of that stress by providing a quick and easy way to determine which garage offers the best chance of finding a spot, all in real-time.

## Getting Started
To use UCFParking, follow these steps:

1.  Clone this repository.
2.  Set up your Twilio and Life360 API keys in the configuration file.
3.  Run the scripts to begin tracking your location and receiving parking updates.
4.  You'll receive a text message with the best parking options every time you're near campus.
### Prerequisites
Python 3.x
Twilio API account and keys
Life360 API account and keys
Additional Python libraries: Requests, BeautifulSoup (for web scraping), etc.
## Contributing
Given the evolving nature of UCF's parking situation and potential updates to their website, contributions are welcome to keep this tool effective. feel free to reach out for improvements and advancements.
