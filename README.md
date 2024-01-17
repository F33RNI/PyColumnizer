# 📃 PyColumnizer

## Classic UNIX-style real-time text formatter with unicode and pipe support

> This program allows you to format one / multiple files or piped stream in the format of classic UNIX docs,
> splitting them into columns, adding line numbers, header, etc. Formatting is done line by line in real time
> (i.e., the output of the program can also be piped to another program)
> In fact, this is an improved version of the "pr" command with Unicode support

----------

## 🏗️ Get started

### Install using pip

```shell
pip install git+https://github.com/F33RNI/PyColumnizer.git
columnizer -h
```

### Build using PyInstaller

```shell
pip install pyinstaller
pyinstaller main.spec
./dist/columnizer -h
```

### Run as python script

```shell
python main.py -h
```

----------

## 📃 Usage

```text
usage: columnizer [-h] [-c COLUMNS] [-w WIDTH] [-p PAGE_SIZE] [-t TITLE] [-s SEPARATOR] [-j] [-a] [-d DATE]
                  [--date-format DATE_FORMAT] [--first-line-number FIRST_LINE_NUMBER]
                  [--first-page-number FIRST_PAGE_NUMBER] [--lines-before-header LINES_BEFORE_HEADER]
                  [--lines-after-header LINES_AFTER_HEADER] [--lines-after-page LINES_AFTER_PAGE]
                  [--line-number-placeholder LINE_NUMBER_PLACEHOLDER]
                  [--page-number-placeholder PAGE_NUMBER_PLACEHOLDER] [--no-line-numbers] [--no-page-numbers]
                  [--no-date] [--no-header] [--skip-empty-lines] [--single-page] [-v]
                  [FILE ...]

classic UNIX-style real-time text formatter with unicode and pipe support

positional arguments:
  FILE                  files to read, if empty, stdin is used

options:
  -h, --help            show this help message and exit
  -c COLUMNS, --columns COLUMNS
                        Number of columns (default: 2)
  -w WIDTH, --width WIDTH
                        total width of each line (default: 80)
  -p PAGE_SIZE, --page-size PAGE_SIZE
                        total lines per page (including header and lines-after-page) (default: 68)
  -t TITLE, --title TITLE
                        text title
  -s SEPARATOR, --separator SEPARATOR
                        column separator (default: 4 whitespaces)
  -j, --justify         justify each line in each column
  -a, --across          print columns across rather than down
  -d DATE, --date DATE  title date in YYYY-MM-DD:HH:mm format (default: current date)
  --date-format DATE_FORMAT
                        title date format (default: %Y-%m-%d %H:%M)
  --first-line-number FIRST_LINE_NUMBER
                        counter at first line (default: 1)
  --first-page-number FIRST_PAGE_NUMBER
                        counter at first page (default: 1)
  --lines-before-header LINES_BEFORE_HEADER
                        number of empty lines before header (default: 2)
  --lines-after-header LINES_AFTER_HEADER
                        number of empty lines after header (default: 2)
  --lines-after-page LINES_AFTER_PAGE
                        number of empty lines between pages (default: 5)
  --line-number-placeholder LINE_NUMBER_PLACEHOLDER
                        Placeholder for line number (default: "{line:>5} ")
  --page-number-placeholder PAGE_NUMBER_PLACEHOLDER
                        Placeholder for page number (default: "Page: {page}")
  --no-line-numbers     turn off line numbering
  --no-page-numbers     turn off page numbering
  --no-date             turn off date in header
  --no-header           turn off entire header
  --skip-empty-lines    ignore empty lines
  --single-page         turn off page separation
  -v, --version         show program's version number and exit
```

----------

## 📝 Examples

> You can download example text from this repo. See `text.txt` file

### Basic example (2 columns, custom page size, title)

```shell
columnizer -c 2 -p 30 -t "Example text" text.txt > output.txt
```

> If you want to get output in console instead of a file, remove `> output.txt`
>
> You can specify multiple input files. For that use `text.txt text2.txt path/to/text3.txt` instead of `text.txt`

<details>
<summary>output.txt</summary>

```text


2024-01-17 12:45                      Example text                       Page: 1


    1   Lorem ipsum dolor sit amet,          21   urna condimentum mattis       
    2   consectetur adipiscing elit,         22   pellentesque id. Et malesuada 
    3   sed do eiusmod tempor                23   fames ac turpis egestas sed   
    4   incididunt ut labore et dolore       24   tempus urna et.               
    5   magna aliqua. Ut placerat orci       25                                 
    6   nulla pellentesque dignissim         26   Enim praesent elementum       
    7   enim. Feugiat pretium nibh           27   facilisis leo. Porttitor lacus
    8   ipsum consequat nisl vel             28   luctus accumsan tortor        
    9   pretium. Parturient montes           29   posuere. Ornare arcu odio ut  
   10   nascetur ridiculus mus mauris        30   sem nulla pharetra. Porta     
   11   vitae ultricies leo integer.         31   lorem mollis aliquam ut       
   12   Non diam phasellus vestibulum        32   porttitor. Libero volutpat sed
   13   lorem sed. Morbi tincidunt           33   cras ornare arcu dui. Netus et
   14   augue interdum velit euismod.        34   malesuada fames ac turpis     
   15   Sit amet massa vitae tortor          35   egestas integer. Dictum sit   
   16   condimentum lacinia quis vel.        36   amet justo donec. Nisi est sit
   17   Sodales ut eu sem integer            37   amet facilisis magna etiam.   
   18   vitae. Ac turpis egestas             38   Malesuada pellentesque elit   
   19   integer eget aliquet nibh            39   eget gravida. At elementum eu 
   20   praesent tristique. Tellus at        40   facilisis sed odio morbi quis 







2024-01-17 12:45                      Example text                       Page: 2


   41   commodo. Ut venenatis tellus  
   42   in metus vulputate eu         
   43   scelerisque felis imperdiet.  
   44   Donec ac odio tempor orci     
   45   dapibus. Non arcu risus quis  
   46   varius quam. Dignissim diam   
   47   quis enim lobortis scelerisque
   48   fermentum dui faucibus. Et    
   49   tortor at risus viverra       
   50   adipiscing at in tellus       
   51   integer.                      















```

</details>

### No paging, single column

```shell
columnizer -c 1 -t "Example text" --single-page text.txt > output.txt
```

> If `--single-page` is specified, in normal mode (not `--across`) only the first column will be filled in,
> because formatting occurs in real time and PyColumnizer does not know the final amount of text in order
> to divide it into columns

<details>
<summary>output.txt</summary>

```text


2024-01-17 12:47                                                    Example text


    1   Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
    2   tempor incididunt ut labore et dolore magna aliqua. Ut placerat orci    
    3   nulla pellentesque dignissim enim. Feugiat pretium nibh ipsum consequat 
    4   nisl vel pretium. Parturient montes nascetur ridiculus mus mauris vitae 
    5   ultricies leo integer. Non diam phasellus vestibulum lorem sed. Morbi   
    6   tincidunt augue interdum velit euismod. Sit amet massa vitae tortor     
    7   condimentum lacinia quis vel. Sodales ut eu sem integer vitae. Ac turpis
    8   egestas integer eget aliquet nibh praesent tristique. Tellus at urna    
    9   condimentum mattis pellentesque id. Et malesuada fames ac turpis egestas
   10   sed tempus urna et.                                                     
   11                                                                           
   12   Enim praesent elementum facilisis leo. Porttitor lacus luctus accumsan  
   13   tortor posuere. Ornare arcu odio ut sem nulla pharetra. Porta lorem     
   14   mollis aliquam ut porttitor. Libero volutpat sed cras ornare arcu dui.  
   15   Netus et malesuada fames ac turpis egestas integer. Dictum sit amet     
   16   justo donec. Nisi est sit amet facilisis magna etiam. Malesuada         
   17   pellentesque elit eget gravida. At elementum eu facilisis sed odio morbi
   18   quis commodo. Ut venenatis tellus in metus vulputate eu scelerisque     
   19   felis imperdiet. Donec ac odio tempor orci dapibus. Non arcu risus quis 
   20   varius quam. Dignissim diam quis enim lobortis scelerisque fermentum dui
   21   faucibus. Et tortor at risus viverra adipiscing at in tellus integer.   

```

</details>

### 3 columns, across formatting, custom width, date format, separator, line numbering and header

```shell
columnizer -a -c 3 -w 100 -p 25 --date-format "%d.%m.%Y" -s " - " -t "Example text" --line-number-placeholder "{line:>2} " --first-line-number 0 --lines-before-header 0 --lines-after-header 1 text.txt > output.txt
```

> If `-a` or `--across` is specified, the text will be divided into columns from left to right,
> then from top to bottom

<details>
<summary>output.txt</summary>

```text
17.01.2024                                   Example text                                    Page: 1

 0 Lorem ipsum dolor sit amet,  -  1 consectetur adipiscing elit, -  2 sed do eiusmod tempor       
 3 incididunt ut labore et      -  4 dolore magna aliqua. Ut      -  5 placerat orci nulla         
 6 pellentesque dignissim enim. -  7 Feugiat pretium nibh ipsum   -  8 consequat nisl vel pretium. 
 9 Parturient montes nascetur   - 10 ridiculus mus mauris vitae   - 11 ultricies leo integer. Non  
12 diam phasellus vestibulum    - 13 lorem sed. Morbi tincidunt   - 14 augue interdum velit        
15 euismod. Sit amet massa      - 16 vitae tortor condimentum     - 17 lacinia quis vel. Sodales ut
18 eu sem integer vitae. Ac     - 19 turpis egestas integer eget  - 20 aliquet nibh praesent       
21 tristique. Tellus at urna    - 22 condimentum mattis           - 23 pellentesque id. Et         
24 malesuada fames ac turpis    - 25 egestas sed tempus urna et.  - 26                             
27 Enim praesent elementum      - 28 facilisis leo. Porttitor     - 29 lacus luctus accumsan tortor
30 posuere. Ornare arcu odio ut - 31 sem nulla pharetra. Porta    - 32 lorem mollis aliquam ut     
33 porttitor. Libero volutpat   - 34 sed cras ornare arcu dui.    - 35 Netus et malesuada fames ac 
36 turpis egestas integer.      - 37 Dictum sit amet justo donec. - 38 Nisi est sit amet facilisis 
39 magna etiam. Malesuada       - 40 pellentesque elit eget       - 41 gravida. At elementum eu    
42 facilisis sed odio morbi     - 43 quis commodo. Ut venenatis   - 44 tellus in metus vulputate eu
45 scelerisque felis imperdiet. - 46 Donec ac odio tempor orci    - 47 dapibus. Non arcu risus quis
48 varius quam. Dignissim diam  - 49 quis enim lobortis           - 50 scelerisque fermentum dui   
51 faucibus. Et tortor at risus - 52 viverra adipiscing at in     - 53 tellus integer.             






```

</details>

### Justified columns, no header and line numbers, empty lines are skipped

```shell
columnizer -j -c 2 -p 30 -t "Example text" --no-header --no-line-numbers --skip-empty-lines text.txt > output.txt
```

> If `-j` or `--justify` is specified, the text in each column will be justified
>
> If `--skip-empty-lines` is specified, empty lines will not be rendered

<details>
<summary>output.txt</summary>

```text
Lorem    ipsum    dolor    sit   amet,    fames   ac   turpis  egestas  integer.
consectetur  adipiscing  elit,  sed do    Dictum  sit amet justo donec. Nisi est
eiusmod tempor incididunt ut labore et    sit   amet   facilisis   magna  etiam.
dolore  magna aliqua. Ut placerat orci    Malesuada   pellentesque   elit   eget
nulla   pellentesque  dignissim  enim.    gravida. At elementum eu facilisis sed
Feugiat  pretium  nibh ipsum consequat    odio  morbi quis commodo. Ut venenatis
nisl  vel  pretium.  Parturient montes    tellus    in    metus   vulputate   eu
nascetur  ridiculus  mus  mauris vitae    scelerisque  felis imperdiet. Donec ac
ultricies   leo   integer.   Non  diam    odio  tempor  orci  dapibus.  Non arcu
phasellus  vestibulum lorem sed. Morbi    risus quis varius quam. Dignissim diam
tincidunt    augue    interdum   velit    quis    enim    lobortis   scelerisque
euismod.  Sit  amet massa vitae tortor    fermentum  dui  faucibus. Et tortor at
condimentum  lacinia quis vel. Sodales    risus  viverra adipiscing at in tellus
ut  eu  sem  integer  vitae. Ac turpis    integer.                              
egestas   integer  eget  aliquet  nibh
praesent  tristique.  Tellus  at  urna
condimentum mattis pellentesque id. Et
malesuada  fames ac turpis egestas sed
tempus             urna            et.
Enim praesent elementum facilisis leo.
Porttitor lacus luctus accumsan tortor
posuere. Ornare arcu odio ut sem nulla
pharetra.  Porta  lorem mollis aliquam
ut porttitor. Libero volutpat sed cras
ornare  arcu  dui.  Netus et malesuada






```

</details>

### Piped input

```shell
echo "Some piped text here\nAnother line\n\nAnd another one after blank line" | columnizer -c 2 -p 15 > output.txt
```

<details>
<summary>output.txt</summary>

```text


2024-01-17 13:23                                                         Page: 1


    1   Some piped text here          
    2   Another line                  
    3                                 
    4   And another one after blank   
    5   line                          






```

</details>

----------

## ✨ Contribution

- Anyone can contribute! Just create a pull request
