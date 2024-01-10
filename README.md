# Gic
Gic is a Googlebot IP checker that process a list of IP addresses and check them with the public Googlebot list.
This project aims to be a collection of small code snippets in many languages.

## How it works
Google publish a [list of networks](https://developers.google.com/search/apis/ipranges/googlebot.json) that are their Googlebot networks.
The code uses this list to check whether the IP you want to check is a known Googlebot agent or not.

### What about the double DNS check?
The code could have used the DNS double check that we can found in other solutions.
This method consists in getting the host name from the IP, check if it's a Google domain name, if the IP is part of the domain name and finally if the domain name points to the original IP.

There is 2 drawbacks in this solution:
- it's slooooooooooow
- it generates 2 DNS requests so it generates load on DNS servers

This script was at the begining intended to quickly check if I didn't banned a Googlebot agent over a list of 1k IP addresses so this solution is not the fastest way to do it.

## How to contribute
If you find this project useful but your favorite programming language is not available, feel free to send a Merge request with your contribution.
Same goes to improvements.

Coding rules:
- Use camelCase for names (unless required by the common conventions and/or language itself)
- Provide a CLI version if and only if it's easy to create and if it will not collide with user code (e.g. C/C++ cannot have CLI because it will collide with `main()` function of the user)
- Provide the smallest number of files (i.e. 1 file only in most cases, 2 files in languages like C or C++)
- Comment your code, either for the functions documentation AND for the code inside
- Don't use 1-character variable names except for loop counters
- Each language must reside in its folder
- Add the MIT licence in all file headers
