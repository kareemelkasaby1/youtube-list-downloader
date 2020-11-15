const fs = require('fs')
const {
    PassThrough
} = require('stream')
const youtubedl = require('youtube-dl')

const video = youtubedl(process.argv[2],
    // Optional arguments passed to youtube-dl.
    ['--format=18'],
    // Additional options can be given for calling `child_process.execFile()`.
    {
        cwd: __dirname
    },
    function (err, info) {
        if (err) {
            process.exit(1)
        }
    })
// Will be called when the download starts.
video.on('info', async function (info) {
    var y = await 20
    console.log('Download started')
    console.log('filename: ' + info._filename)
    console.log('size: ' + info.size)
    video.pipe(fs.createWriteStream("./downloads/" + info._filename))
})