# IR-with-LSH

We have implemented the LSH algorithm to build a search engine. Then did a comparative analysis for different 50, 100, and 200 hash functions. For each value, output the pairs that have an estimated similarity at least 0.5, and report the number of false positives and false negatives that you obtain. For the false positives and negatives, report the averages for 5 different runs.

Next, break up the signature table into b bands with r hash functions per band and implement Locality Sensitive Hashing. The goal is to find candidate pairs with similarity at least 0.6. Experiment with r=5, b =10 for the table with the 50 hash functions, r=5, b=20 for the table with the 100 hash functions, r = 5, b = 40 and r=10, b= 20 for the table with the 200 hash functions.

<!-- ABOUT THE PROJECT -->
## About The Project

A Local Sensitive hashing for finding similarity between shakespeare's plays.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With


* [Python](https://www.python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.


### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/shashwatanand1801/Project-Management.git
   ```
2. For running LSH without bands :
   ```sh
   cd First
   pyhton3 test.py
   ```
3. For running LSH with bands :
   ```sh
   cd Second
   pyhton3 second.py
   ```
4. Also if you want to modify the data then you can ghenerate new data using processing.py in data processing folder
   ```sh
   cd "Data Processing"
   ```
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Results

<!-- Few snaps of working application -->


![LSH without Bands](../media/images/LSH_withoutBands.png?raw=true)



<p align="right">(<a href="#top">back to top</a>)</p>




<!-- Dataset -->
## Dataset
We used Shakespeare plays dataset for project. More details can be found here <a href="https://www.kaggle.com/datasets/kingburrito666/shakespeare-plays">Shakespeare plays</a>



<p align="right">(<a href="#top">back to top</a>)</p>




<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Shashwat anand- [@shashwat_anand](https://www.linkedin.com/in/shashwat-anand/) - shashwatanand1801@gmail.com

Project Link: [https://github.com/shashwatanand1801/IR-with-LSH](https://github.com/shashwatanand1801/IR-with-LSH)

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/shashwatanand1801/Project-Management.svg?style=for-the-badge
[contributors-url]: https://github.com/shashwatanand1801/Project-Management/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/shashwatanand1801/Project-Management.svg?style=for-the-badge
[forks-url]: https://github.com/shashwatanand1801/Project-Management/network/members
[stars-shield]: https://img.shields.io/github/stars/shashwatanand1801/Project-Management.svg?style=for-the-badge
[stars-url]: https://github.com/shashwatanand1801/Project-Management/stargazers
[issues-shield]: https://img.shields.io/github/issues/shashwatanand1801/Project-Management.svg?style=for-the-badge
[issues-url]: https://github.com/shashwatanand1801/Project-Management/issues
[license-shield]: https://img.shields.io/github/license/shashwatanand1801/Project-Management.svg?style=for-the-badge
[license-url]: https://github.com/shashwatanand1801/Project-Management/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/shashwat-anand/
[product-screenshot]: readme_images/landing.png
