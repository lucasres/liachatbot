# liachatbot

  Code of chatbot of lia, created for NITLAB, in development. The chat consists of a brain.lia file where knowledge is stored, it will be "compiled" and stored in SQLITE3 database.

## Getting Start
  First edit the brain.lia file with the patterns that chatbot contains. Remembering that you should contain the main section.
  Use > for create a pattern, bellow the pattern use < for answer
  
  Example:
  ```
    [section main]
      > ola
      < ola
      < iae
      < oin :)
      < falou comigo?
    [endsection]
  ```
  
  ## Use in your code
    for you to use in your code just include the class chatCore and call the methods below:
  ```
  from core import chatCore
  
  bot = chatCore()
  bot.init()
  bot.conversationText()
  ```
  
  ## useful command
    after the chatbot is initialized to leave the conversation use !sair
    
  ## Authors

* **Lucas Resende de Sousa Amaral** - *Initial work* - [PurpleBooth](https://github.com/mandala21)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
