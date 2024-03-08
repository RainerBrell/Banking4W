# the AddOn extends the behavior of Banking 4 as follows

* A character for 'carriage return and line feed' was occasionally displayed via Braille, which has been corrected.
* In the depot and turnover table, only the content of the current table cell is now displayed and spoken when you change the cells with the up/down/up/down arrow. There are now two new functions in these cells:
* n prints the name of the column (amount, purpose, etc.).
* z Outputs which row you are in and reads the entire row.

## In order to get the optimal display via Braille and speech, I recommend making the following settings

1. Start Banking 4 and exit the application
2. In the NVDA menu under "Manage configuration profiles..." select "new" and enter "Banking4" as the profile name, for example.
3. Under "Use this profile for" select Banking 4 and select "OK".

Then select “Show permanently” in the NVDA menu under Options/Settings/braille under “Show messages”.

Finally, set the following in the NVDA menu under Options/Settings/Document Formatting:
* Deactivate the "Tables" check box
