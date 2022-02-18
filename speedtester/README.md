## Speedtester v.01
Project utilizes the [speedtest.net executable](https://www.speedtest.net/apps/cli "speedtest.net executable")  to gather network statistics
viewable results on [Grafana](https://jesseruth.grafana.net)

Saves the results to a Azure instance of postgreSQL
```
...\speedtest.py
Table already exists
Running speedtest.exe - This will take a few seconds
Finished in 25.26 second(s)
Inserting results into the db
Completed!
```
#### To DOs / Future
- Enhance main script with better coding practices
- Check errors on executings 
- Allow command line arguments 
- Setup logging module 
- Auto download speedtest for your OS
- Gather additional details if poor network performance is detected
