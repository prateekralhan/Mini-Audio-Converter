# 🎼🎶 Mini-Audio Converter 🎙🔉 [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)

A simple Streamlit based webapp to convert Audio files of numerous formats to the desired format required by the user.

### Live Web-App can be found [here.](https://mini-audio-converter.herokuapp.com/)

&nbsp;
<kbd>
<img src="demos/demo_2.gif" data-canonical-src="demos/demo_2.gif"/> 
</kbd>

## Installation:
* Simply run the command ***pip install -r requirements.txt*** to install the dependencies.

## Usage:
1. Clone this repository and install the dependencies as mentioned above. Ensure that you have ffmpeg installed before in your system to install pydub successfully. You can find more information [here.](https://github.com/jiaaro/pydub)
2. Simply run the command: 
```
streamlit run app.py
```
4. Navigate to http://localhost:8501 in your web-browser.
5. By default, streamlit allows us to upload files of **max. 200MB**. If you want to have more size for uploading audio files, execute the command :
```
streamlit run your_script.py --server.maxUploadSize=1028
```
<kbd>
<img src="demos/demo_1.gif" data-canonical-src="demos/demo_1.gif"/> 
</kbd>



### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build -f Dockerfile -t app:latest .
```
4. Run the docker:
```
docker run -p 8501:8501 app:latest
```

This will launch the dockerized app. Navigate to ***http://localhost:8501/*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```
