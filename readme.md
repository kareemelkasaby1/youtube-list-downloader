
# Youtube List Downloader
It is a reliable solution to download any youtube playlist with your choice of mp4 or mp3 formats.
You only run it with a one docker command.

## Getting Started

Please provide your desired absolute path you want to download in, to `./run.sh` file 

### Prerequisites

if you are a developer you need these Prerequisites:

* `NodeJs`
* `python3`
* `Docker`

if you are a user you need these Prerequisites:

* `Linux os`
* `Docker`

### Installing

Make sure that you have docker installed on your machine.
```sh
docker --version

    or

sudo docker --version
```
you only need to run these command and replace
`$the absolute path of the required destination to download in`  with the absolute path of the desired download distintion.
You may need to use `sudo` if your docker does not run under the permissions of normal users.
with the absolute path of directory, you want to download your playlist items in.

```sh
./run.sh $the_absolute_path_of_the_required_distination_to_download_in

or

sudo ./run.sh $the_absolute_path_of_the_required_distination_to_download_in
```
Or if you do not want to clone this repo just run the below docker command as it is, and do not forgit to replace `$the absolute path of the required destination to download in` with the absolute path of the desired download distintion.
```sh
export DESIRED_PATH=$the_absolute_path_of_the_required_distination_to_download_in

docker run -u `id -u`  -v /dev/shm:/dev/shm  -v $DESIRED_PATH:/yotube-list-downloader/downloads -it kareemelkasaby/youtube-list-downloader:latest

or
sudo docker run -u `id -u`  -v /dev/shm:/dev/shm  -v $DESIRED_PATH:/yotube-list-downloader/downloads -it kareemelkasaby/youtube-list-downloader:latest
```
## Built With

* NodeJs   - the [youtube-dl](https://www.npmjs.com/package/youtube-dl) package witch download the videos.
* Python3  - to run the bash script through code.
* Selenium - to open the first link in the playlist and pass it to the Node file by a bash script.
* Bash     - to link the Python file with the Node file and convert the video from mp4 to mp3 format.

## Authors

* **Kareem Elkasaby** - [github](https://gist.github.com/kareemelkasaby1)


