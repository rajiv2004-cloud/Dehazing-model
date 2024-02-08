# AI-ML Based Dehazing / De-smoking Algorithm

## Project Overview

This repository contains the code and documentation for an AI-ML based intelligent de-smoking/de-hazing algorithm developed for disaster management purposes, specifically aimed at aiding rescue operations during indoor fire hazards. The algorithm is designed to remove smoke and haze from real-time video footage, thereby enhancing visibility in fire-affected areas.

## Table of Contents

1. [Introduction](#introduction)
2. [Objective](#objective)
3. [Abstract](#abstract)
4. [Idea Description](#idea-description)
5. [Features](#features)
6. [Installation](#installation)
7. [Usage](#usage)
8. [Contributing](#contributing)
9. [License](#license)

## Introduction

Fire accidents in indoor environments pose significant threats to human life and property. The presence of smoke or haze can severely reduce visibility, hindering rescue operations. To address this challenge, an AI-ML based de-smoking/de-hazing algorithm has been developed to provide clear, enhanced video footage from areas under fire.

## Objective

The primary objective of this project is to develop a robust algorithm capable of:

- Removing smoke/haze from real-time video footage.
- Enhancing visibility in fire-affected areas.
- Facilitating efficient and safe execution of rescue operations.

## Abstract

This project focuses on the conception and implementation of an AI-ML powered Intelligent De-smoking/De-hazing Algorithm. The algorithm aims to deliver real-time, enhanced video feed from spaces afflicted by fire in indoor environments, thereby augmenting the capabilities of rescue teams and facilitating expedited and more effective response efforts.

## Idea Description

The project encompasses the following key phases:

1. **Data Collection**: Gathering data from controlled fire scenarios and publicly available datasets containing images and videos affected by haze and smoke.

2. **Data Preprocessing**: Segmentation of smoke/haze affected regions, annotating data, and applying noise reduction and enhancement techniques.

3. **Model Design and Training**: Utilization of Convolutional Neural Network (CNN) structure for effective smoke and haze removal, extensive training using augmented datasets.

## Features

- **Real-time Processing**: Optimized for real-time applications, processes high-definition video feeds without significant lag.
- **Adaptive Learning**: Can adapt to various smoke densities and types, with fine-tuning options available based on specific indoor environments.
- **Integration Capability**: Can be integrated into existing CCTV systems or specialized cameras used by rescue teams, provides an API for custom applications and third-party software integration.
- **Potential Applications**: Suitable for firefighting operations, surveillance during hazardous situations, and integration into smart building systems for automated hazard detection and management.

### Installation Steps
1. Clone or download the repository from [GitHub](https://github.com/whitehats/image-dehazing-toolkit).
2. Install the required dependencies using pip:
    ```
    pip install opencv-python numpy
    ```

## Parameters
The `remove_haze()` function accepts the following optional parameters for fine-tuning the dehazing process:
- `airlightEstimation_windowSze`: Size of the window for estimating the airlight (default: 15)
- `boundaryConstraint_windowSze`: Size of the window for boundary constraints (default: 3)
- `C0`, `C1`: Constants for boundary constraints (default: C0=20, C1=300)
- `regularize_lambda`: Regularization parameter (default: 0.1)
- `sigma`: Standard deviation for the weighting function (default: 0.5)
- `delta`: Fine-tuning parameter for dehazing (default: 0.85)
- `showHazeTransmissionMap`: Whether to display the haze transmission map (default: True)

## Contributing
Contributions to the Whitehats Image Dehazing Toolkit are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request on GitHub.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
