<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<!--
<br />
<div align="center">
  <a href="https://github.com/Pitiedwzr/music_batch_separator">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
-->

<h3 align="center">Music Batch Separator</h3>


![PythonVersion][PythonVersion]
![license][License]
![platform][Platform]

  <p align="center">
    Batch separating music, based on the MVSEP API
    <br />
    <a href="https://github.com/Pitiedwzr/music_batch_separator"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Pitiedwzr/music_batch_separator">View Demo</a>
    ·
    <a href="https://github.com/Pitiedwzr/music_batch_separator/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/Pitiedwzr/music_batch_separator/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

Recently, I've been working on SVC song covers, but since my workstation only has a single AMD card, most music separation models don't support HIP or ROCm. As a result, I've had to rely on [MVSEP](https://mvsep.com) for separating the tracks. However, I often have multiple audio files to process, and since I'm not keen on manually uploading and waiting for the results each time, I decided to develop a program to automate the process by using their API.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![Qt][Qt]][qt-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To use this app, you can either download the portable version from [Releases][Releases] or build it according to the following steps.

### Prerequisites

Make sure you have python 64-bit installed on your computer

### Installation

1. Register an account and get a free API Key at [https://mvsep.com](https://mvsep.com)
2. Clone the repo
   ```sh
   git clone https://github.com/Pitiedwzr/music_batch_saparator
   ```
3. Install packages
   ```sh
   pip install -r requirements.txt
   ```
4. Enter your API in `settings.yaml`
   ```
   token: "YOUR_API_TOKEN"
   ```
5. Use `main.py` to run the main program


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] GUI
    - [ ] Settings
    - [ ] Main window
- [ ] Functions
    - [x] Post to the url
    - [x] Get the result
    - [ ] Download file(s)
    - [ ] Process order

See the [open issues](https://github.com/Pitiedwzr/music_batch_separator/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the LGPL License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best README Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[License]: https://img.shields.io/github/license/Pitiedwzr/music_batch_separator
[Platform]: https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-green
[PythonVersion]: https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=f5f5f5
[product-screenshot]: resource/images/screenshot.png
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org/
[Qt]: https://img.shields.io/badge/Qt-41CD52?style=for-the-badge&logo=qt&logoColor=white
[Qt-url]: https://qt.io/
[Releases]: https://github.com/Pitiedwzr/music_batch_separator/releases