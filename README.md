# Astrobites iCal Calendar Generator

## Purpose

Hello scheduler!  Astrobites schedules posts by assigning each author to write a post one day per month, and (typically) to also edit a peer's post one day per month.  To help facilitate this scheduling, we typically create a shared calendar that lists the assigned author and editor for each day.

Use the `schedulegen.py` script to convert a text schedule into a personal information manager (PIM; e.g. google calander) friendly iCal format.

## Usage

First, edit the variables in the `INPUT PARAMETERS` block.  Primarily, you will need to point `infile` to your input schedule file.

Simply run as:

```
python3 schedulegen.py
```

## Tips from Astrobites scheduler @jkcalahan

I find that it is easier to create the schedule by-hand. There have been attempts to create a python script to create a randomly ordered schedule, however we don't want a purely random schedule. A random schedule will have features we don't want, like an author asked to edit their own piece, multiple writing slots in a week for a single author...and fixing those errors is more effort than it's worth, in my opinion.

Here is what I do to make a schedule for Astrobites. If you can find improvements on this method feel free to share back with me!

1. randomize the list of authors you have uisng an online list generator. I use https://www.random.org/lists/ Do this for however many random iterations you need. For astrobites, we have three trimesters of schedules that make up one year, and in each trimester each author writes and edits three times. So I have three random lists of author order.

2. Store those random lists off to the side in an excel spreadsheet (e.g. `example_schedule.xlsx`). The columns of the spreadsheet should be as follows:

* col1: week #, start with 1. A new week starts on Monday. You'll specifiy when the week starts exactly in the python script
* col2: write the week name, Monday, Tuesday, etc..
* col3: what type of writing day, astrobite examples include 'write' 'open' 'queue'
* col4: blank, leave for author
* col5: 'edit' to denote who is editing
* col6: editors
* col7: [optional] second editor
    
3. Now its time to put the authors and editors in order. I simply copy and paste the three randomized lists back to back. For the editing column, I start halfway down the first randomized list and have that being the start of the editors, then continue with the first half of the randomized list...

    very simple example: if my randomized list is "AA,BB,CC,DD,EE,FF,GG,HH"
    then my authors would be "AA,BB,CC,DD,EE,FF,GG,HH"
    and my editor order would be "EE,FF,GG,HH,AA,BB,CC,DD"
    
    I find that this is a great way to incorperate both randomness and avoid doubling up on writing and editing as well as back-to-back editing/writing.
    
    repeat with the second itemized list. Now the only areas you really need to check are where the randomized lists begin and end. i.e. if an author is at the end of one randomized list and the beginning of the next randomized list, that's not idea. You'll move that author to a different spot. 
    
4. Once you have the order you want, save the columns 1-6{7} as a text file. Either "save as" a txt file, or copy and paste into a blank one.

5. An example schedule.txt file should also be found, but here is the format it should follow so that it is read sucessfully by the python script:

    1 Tuesday	write[queue]-SK[JN,HS] edit-WJG[IM,AM]
    1 Wednesday	write-RG edit-PG
    1 Thursday	write-GFA edit-CJ
    1 Friday	write-GD edit-MH
    1 Saturday	write-WY edit-AG
    1 Sunday	open	 edit-
    2 Monday	write[queue]-Lzal[SW,KG] edit-LA[DG,RH]
    2 Tuesday	write-Lzag edit-CC
    ...
    
    This will create events in the first week, with an event on Tuesday called "write[queue]-SK[JN,HS] edit-WJG[IM,AM]" and Friday "write-GD edit-MH". Basically, for the event name, be sure that there is only one space. 
    
6. Next we run the python script `schedulegen.py` the only inputs you should need to edit are lines 15-20, and primarily just the `infile` parameter.

And that's it! I hope that's helpful. Feel free to share any improvements you find in the system. The scheduling contact for astrobites is `scheduling _at_ astrobites.org`.
