# Custom_Api_Mbpj
EXTENDED VERSION FROM IDD ESERVICES MBPJ API DATA ADUAN [20220921] 

## Table of contents
* [Overview](#overview)
* [Objective](#objective)
* [Feauture](#features)

## Overview

This project presents a custom API application designed to convert the official MBPJ (Majlis Bandaraya Petaling Jaya) API's unsupported JSON format into a supported JSON format. The purpose of this conversion is to make the data accessible and compatible with the "My Map" application, enabling seamless integration and utilization of MBPJ data in the application.

## Objective

The primary objective of this project is to bridge the gap between the existing MBPJ API's JSON format and the specific JSON format required by the "My Map" application. By converting the data into the supported format, we ensure that the "My Map" application can efficiently consume and display the MBPJ data without any compatibility issues.

## Features

* Custom API Endpoint: The application provides a dedicated API endpoint designed to accept requests for MBPJ data conversion.
* Data Conversion: Upon receiving a request, the custom API performs the necessary data conversion from the official MBPJ API's JSON format to the supported JSON format for "My Map" application consumption.
	
## Technologies
Project is created with:
* Python Flask
* Python Requests Library
* Docker Container

## Usage
* Make a Get Request To The API With valid Mbpj Token:
```
http://<server_ip>:60015/<valid_mbpj_token>/api?rid=<rid_value>”)
```
* Make a Get Request To The API with Optional Parameter:
```
http://<server_ip>:60015/<valid_mbpj_token>/api?rid=<rid_value>&year=<input_year>&month=<input_month>”)
```

	
## Setup
Step by step to deploy this project:

* Clone Project:
```
git clone https://github.com/katakkentut/Custom_Api_Mbpj.git
```
* Build Container:
```
docker build -t <specify_any_tag_name> .
```
* Verify Image:
```
docker images
```
* Run The Container:
```
docker run --name <specify_any_container_name> -d -p 60015:60015 <replace_with_tag_name_before>
```
* Verify The Container is Running:
```
docker ps -a
```


