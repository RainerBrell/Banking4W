"""
program : Banking4Windows / TopBanking
Version : 8.3 or higher 

 This file is covered by the GNU General Public License.
 You can read the licence by clicking Help->Licence in the NVDA menu
 or by visiting http://www.gnu.org/licenses/old-licenses/gpl-2.0.html

Banking 4W is only available in german/english/french 
Create  : 16. April 2020 by Rainer Brell <nvda@brell.net>
Modify  : 16. mai 2020 / Grid navigation and gesture added 
Modify  : 18. Mai 2020 / SWIFT Bank Name 
Modify  : 05. August  2021 / for Version 7.7.1 (Grid edit customized to cell) 
Modify  : 2.0 - 7. March 2023 / for 8.0 (works not longer under 7.x)
modify  : 2024.03.08 - Made translatable and executable under 2024.1
modify  : 2025.04.21 - Optimized Braille output  in the grid
""" 

import tones
import api 
import config 
import ui
import speech 
import braille 
import controlTypes
import appModuleHandler
from scriptHandler import script
import addonHandler

addonHandler.initTranslation()

firstRun = False 

def braileout_permanently(text):
	showmessage = config.conf["braille"]["showMessages"]
	config.conf["braille"]["showMessages"] = braille.ShowMessages.SHOW_INDEFINITELY
	braille.handler.message(text)
	config.conf["braille"]["showMessages"] = showmessage

class AppModule(appModuleHandler.AppModule):

	def event_appModule_gainFocus(obj):
		global firstRun
		ver = str(obj.productVersion)
		if not firstRun and ver.startswith("7."):
			# Translators: if is runing a older version.
			msg = _("You are using version %s. This customization is intended for Banking4 version 8. \nPress Escape to close this message.")
			msg = msg.replace("%s", ver)
			# Translators: title of the browser dialog 
			tit = _("Note - NVDA AddOn for Banking4 Version 8")
			ui.browseableMessage(msg, tit)
			tones.beep(300, 60)
			firstRun = True 

	def event_gainFocus(self, obj, nextHandler):
		if obj.role == controlTypes.ROLE_UNKNOWN and obj.UIAElement.CurrentClassName == 'DataGridCell':
			#tones.beep(300, 60)
			speech.cancelSpeech()
			msg = obj.description.replace("\r\n", " ")
			braileout_permanently(msg)
		nextHandler()

	@script(
		# Translators: Name of the cell, the column Header
		description=_("Name of the cell"),
		gesture="kb:n"
	)
	def script_columneName(self, gesture):
		obj = api.getFocusObject()
		if obj.role == controlTypes.ROLE_UNKNOWN and obj.UIAElement.CurrentClassName == 'DataGridCell':
			msg = obj.columnHeaderText.split(" ")[0]
			ui.message(msg)
		else:
			gesture.send()

	@script(
		# Translators: Number of the row, the current line 
		description=_("number of the row"),
		gesture="kb:z"
	)

	def script_rowName(self, gesture):
		obj = api.getFocusObject()
		if obj.role == controlTypes.ROLE_UNKNOWN and obj.UIAElement.CurrentClassName == 'DataGridCell':
			l = ""
			for child in obj.parent.children:
				l = l + str(child.description) + ", "
			# Translators: Only the name "Row"
			z = _("Row ") + str(obj.rowNumber) + ": " + l 
			z = z.replace("\r\n", " ")
			ui.message(z) 
		else:
			gesture.send()
