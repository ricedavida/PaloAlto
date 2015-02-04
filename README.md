####################################################################
#
# PaloAlto API Python3 Bindings
#
####################################################################

Authors:
	David Rice riceda@potsdam.edu

Files:
	- paconnect.conf  	# File containing the baseurl of the PaloAlto and the API key used for authentication
	- PaAPI.py			# File used to transfer Rule objects back and forth in ways that the PaloAlto can read
	- Rules.py			# Rule objects used by the PaAPI.py file
	- testAPI.py		# Test that rules can be written to, committed and deleted from the PaloAlto
	- testRules.py		# Test to make sure Rule objects are being handled correctly

Purpose:
	- This project is designed to interact with the PaloAlto PAN-OS 4 XMLAPI
	
Features:
	- Read firewall rules from the PaloAlto
	- Write firewall rules to the PaloAlto
	- Delete firewall rules form the PaloAlto
	- Commit changes made to the PaloAlto
	
License:
	- Copyright (C) 2015  David Rice

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.