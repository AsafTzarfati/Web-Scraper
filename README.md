# Web-Scraper
This project is part of Python Core track by JetBrains academy.

I shared my solution for the last two stages of the Web-Scraper project from HyperSkill.
Stage 4 was mostly about web scraping with the BeautifulSoup library.
Stage 5  was mostly about files in python and directories.


**Stage 4 objectives:**
Create a program that takes the https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3 URL and then goes over the page source code searching for articles.
Detect the article type and the link to view the article tags and their attributes.
Save the contents of each article of the type "News", that is, the text from the article body without the tags, to a separate file named %article_title%.txt. When saving the file, replace the whitespaces in the name of the article with underscores and remove punctuation marks in the filename (str.maketrans and string.punctuation will be useful for this). Also, strip all trailing whitespaces in the article body and title. For example, the article with the title 'Legendary Arecibo telescope will close forever — scientists are reeling' should be saved to the file named Legendary_Arecibo_telescope_will_close_forever_scientists_are_reeling.txt.
(Optional) You may output some result message once the saving is done, but it is not required.
We need to inspect each article to find the tags that represent the article's contents. If you take a closer look at the source code, you will see that every article is enclosed in a pair of <article> tags. Then, each article type is hidden inside a <span> tag containing the data-test attribute with the article.type value. Also, every article includes a link to the article's contents, which is placed inside the <a> tag with the data-track-action="view article" attribute. Once the article page is loaded, save its body wrapped in the <div> tag (look for the word "body" in the class attribute).
  
**Stage 5 objectives:** 
Improve your code so that the function can take two parameters from the user input: the number of pages (an integer) and the type of articles (a string). The integer with the number of pages specifies the number of pages on which the program should look for the articles.
Go back to the https://www.nature.com/nature/articles?sort=PubDate&year=2020 website and find out how to navigate between the pages with the requests module changing the URL.
Create a directory named Page_N (where N is the page number corresponding to the number input by the user) for each page. Search and collect all articles page by page; filter all the articles by the article type and put all the articles that are found on the page with the matched type to the directory Page_N. Mind that when the user enters some number, for example, 4, the program should search all pages up to that number and the respective folders (Folder 1, Folder 2, Folder 3, Folder 4) should be created. Mind also that in articles of different types the content is contained in different tags.
Save the articles to separate *.txt files. Keep the same processing of the titles for the filenames as in the previous stage. You can give users some feedback on completion, but it is not required.
If there's no articles on the page, your program should still create a folder, but in this case the folder would be empty.
