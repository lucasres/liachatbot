# liachatbot

  Code of chatbot of lia, created for NITLAB, in development. The chat consists of a brain.lia file where knowledge is stored, it will be "compiled" and stored in SQLITE3 database.

## Class of project

  chatCore - consists of making the similarity clause between the input and the pattern
  prebot - input preprocessing
  pattern - analyzes the brain's codex
  connections - connection to the database
  
  
## Database
  
  The database consists of 2 tables, one to store the patterns and another to store the answers. Below is the columns of the tables:
  
  #### Pattern
* Id 
* Pattern 
* Section

  #### Response
* Id 
* Response 
* patternId
