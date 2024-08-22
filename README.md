## About FaizanHeaders

![email](https://github.com/user-attachments/assets/e208df07-3002-4e04-bd43-9560fbfb5409)

- What is FaizanHeaders?
- 
First of all, it is a tool based on [MailMeta](https://github.com/gr33nm0nk2802/mailMeta) by Syed Modassir Ali, which I used as inspiration to develop this tool.
**FaizanHeaders** is a python based forensic tool which reads through the email headers from the email file and extracts crucial information to identify if the email is legitimate. 

-  What are the advantages of using FaizanHeaders?

Have you ever heared of **email hacking** or **sophisticated email crimes** where a spoofed email is sent to the victim and the victim trusts this email based on the email address which is infact fake. These email contains mallicious links which can be used to extract some information or install some malware or backdoors on your device. So, in order to avoid you from this FaizanHeaders comes to your rescue.
  
 Here I have added instructions on how to download the email from the file and then pass it to the FaizanHeaders executable. It then parses the headers and informs you if the mail is genuine or not. Whenever you are suspicious about an email be sure to check it once here. It can save you in most of the scenarios. If anyone has some ideas/updates feel free to open an issue or create a pull request.
 
 - What are the information revealed by the FaizanHeaders?
FaizanHeaders parses the following headers:
   
   * Message-ID 
   * SPF-Record
   * DKIM-Record
   * DMARC-Record
   * Spoofed Email detection based on the above headers
   * IP-Address of the sender
   * Service Provider used for sending the email
   * Content-Type
   * Data and Time 
   * Subject
 
 - Why is it important to check such parameters?
   * [ONGC Email Phising](https://indianexpress.com/article/business/companies/identity-theft-ongc-falls-prey-to-cyber-fraud-loses-rs-197-crore/)
   There are many more such cases which you can find online releated to email crimes.
 
## Installation

You have two methods to use FaizanHeaders. Either you can download the github repo and run the FaizanHeaders.py file from the command line. Make sure you have all requirements installed in this case like python3. You may also run the standalone binaries. This is for those who have very little technical knowledge.

<br>
1. Clone the repository

  ```(bash)
    git clone https://github.com/Faizan-Khanx/FaizanHeaders
  ```

2.  Running from the FaizanHeaders.py file

  ```(bash)
    cd FaizanHeaders
    python3 FaizanHeaders.py
  ```
## Usage

Either you are on windows or linux first download the original metadata of the email using the **show original** / **view raw** / **download original** option. 

Then we pass the `eml` file to the executable.
<br>
#

![mail-download](images/mail-download.gif)

### Linux

1. Use `FaizanHeaders.py` from the cloned repo. (Python is required)

```
python3 FaizanHeaders.py -f a.eml
```

![linux-metapy](https://github.com/user-attachments/assets/90143cda-fd25-4774-9862-0c97f261a86c)

## Demo

This is a sample demonstration explaining all the procedures. First it has the steps for running on linux then it has the steps needed for running on windows just in case you are struck.

![cc](https://github.com/user-attachments/assets/fb57f32c-ca28-43b1-94bb-eeb124659a16)

![aa](https://github.com/user-attachments/assets/06fce8f7-14d7-45e1-a499-5ad220503050)

![bb](https://github.com/user-attachments/assets/51cd1dc8-3585-4322-a0d2-95f196f42de0)

# Feedback
- If you have any feedback, please reach out to us at
-  [INSTAGRAM](https://instagram.com/ethicalfaizan)
-  [GITHUB](https://github.com/faizan-khanx)
-  [EMAIL](mailto:fk776794@gmail.com)
  


