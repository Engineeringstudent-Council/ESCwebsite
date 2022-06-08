# Engineering Student Council 
## University of California, Berkeley

Codebase for https://esc.berkeley.edu website. 

## Development
The mission of the Engineering Student Council is to represent the engineering student body; support engineering societies in reaching their full potential; and promote a diverse community through successful collaboration between students, faculty, societies, and the College of Engineering.

Starting in Spring 2019, the Engineering Student Council has a GitHub account with all of the website/technical resources. This eases the passdown of ESC Web IP from one Technical Director to another. GitHub also ensures that in case a laptop is stolen/destroyed, our technical assets are safeguarded.

The website is primary developed using HTML, CSS, and Javascript.

## Website Hosting:
The Engineering Student Council uses the Open Computing Facility’s servers to host our website. In 2010, we started using the OCF’s services and created our first website. For 10 years, not much had changed on the UI/UX side of the website. Around 2014, we had an Engineers Week webpage that connected to our main site. Most of the past iterations of ESC websites can be found on the ESC Drive. A lot of these pages were written from scratch by an ESC Technical officer when the website was first formed. In 2019, we migrated to a new UI with a better UX. Primarily, the old format of the website did little to inform and support engineering students and engineering student organizations. 

### Why still code the website in HTML/CSS/Javascript?
We still code the website through the traditional method (instead of using a proxy such as Wix and Wordpress) because web development is relatively easy to learn (unless you want to use Ruby). Additionally, this is a learning opportunity to understand a different coding language. HTML is the outline of a webpage; CSS adds in the beauty aspect of the webpage; Javascript tops out the webpage with functions that make the website adapt to the user (ex. Filtering tables). The first few weeks will be an uphill battle but afterwards, making edits/changes to the website is like clockwork.

## Setting up your computer:
Website Hosting:
The Engineering Student Council uses the Open Computing Facility’s servers to host our website. In 2010, we started using the OCF’s services and created our first website. For 10 years, not much had changed on the UI/UX side of the website. Around 2014, we had an Engineers Week webpage that connected to our main site. Most of the past iterations of ESC websites can be found on the ESC Drive. A lot of these pages were written from scratch by an ESC Technical officer when the website was first formed. In 2019, we migrated to a new UI with a better UX. Primarily, the old format of the website did little to inform and support engineering students and engineering student organizations. 

### Why still code the website in HTML/CSS/Javascript?
We still code the website through the traditional method (instead of using a proxy such as Wix and Wordpress) because web development is relatively easy to learn (unless you want to use Ruby). Additionally, this is a learning opportunity to understand a different coding language. HTML is the outline of a webpage; CSS adds in the beauty aspect of the webpage; Javascript tops out the webpage with functions that make the website adapt to the user (ex. Filtering tables). The first few weeks will be an uphill battle but afterwards, making edits/changes to the website is like clockwork.

## Setting up your computer:
For steps 1-2, if you are in/have already taken CS61A, then you can skip these steps:
For Macs and Linux, open up Terminal. For Windows, please make sure that you have GitBash. Make sure that you use Windows' default console window in the Configuring the terminal emulator to use with Git Bash step. This is very important! If you do not select this option, your terminal won't work with Python! (necessary for HTML code upload)

### Download a text editor (this is where you will edit your code):
* Atom
* Sublime Text 3
* Emacs
* Vim

### Download Web Pages
* Open up GitBash or Terminal 
* Go to a folder that you want the Web Pages to be stored in (`cd ~/[folder path]`)
- cd: command to direct terminal towards (exactly how file explorer operates)
* If you have not already created a folder to store these webpages, just direct to an already existing folder (ie. Desktop)
* Then type in `mkdir [FOLDER_NAME]`
* Then direct to that new folder (`cd ~/original_folder_path/[FOLDER_NAME]`)
  * Example: `cd ~/Desktop/ESC/` ← points to ESC folder in Desktop folder
* `Scp -r [ESC SERVER]:~/public_html . `← period is important
  * `Scp -r`: copies the content
  * `[ESC SERVER]:~/public_html`: content that is being copied
* Type in password: `[ESC SERVER PASSWORD]`
