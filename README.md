# web-fusee-launcher
Fusee Launcher, in a browser!

# Description
This is a modification of the original web-fusee-launcher
More payloads have been added and example payload has been removed.
I've also added a script which can be used to convert payloads to javascript, even though some manual adjustments need to be done on the resulting file.

# Original Description
This is a port of [fusee-launcher](https://github.com/reswitched/fusee-launcher) to JavaScript using WebUSB. This has been mildly tested and appears to work on Linux, Android (unrooted), OSX and ChromeOS. Today, this only works on Chrome because only Chrome implements WebUSB. It also does NOT work on Windows because the WebUSB Windows implementation does not allow sending the required USB packet.

# Try it out
Either use a web server to host the files (must be on https!) or you can try the [demo](https://netfreak25.github.io/web-fusee-launcher/).
