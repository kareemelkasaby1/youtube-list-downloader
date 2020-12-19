
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
`$the absolute path of the required destination to download in`
You may need to use `sudo` if your docker does not run under the permissions of normal users.
with the absolute path of directory, you want to download your playlist items in.

```sh
./run.sh $the_absolute_path_of_the_required_distination_to_download_in

```

## Built With

* NodeJs   - the [youtube-dl](https://www.npmjs.com/package/youtube-dl) package witch download the videos.
* Python3  - to run the bash script through code.
* Selenium - to open the first link in the playlist and pass it to the Node file by a bash script.
* Bash     - to link the Python file with the Node file and convert the video from mp4 to mp3 format.

## Authors

* **Kareem Elkasaby** - [github](https://gist.github.com/kareemelkasaby1)


