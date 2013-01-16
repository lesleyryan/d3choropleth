#!/usr/bin/env python

import csv

def clean_elec_prices():
	count = 0
	avg_elec_price = []
	ind = 0
	stateName = ""

	wf = open('average_price_state_clean.csv', 'w')
	writer = csv.writer(wf, delimiter = ',', quotechar = '"')
	writer.writerow(['State Name', 'State Code', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010'])

	with open('average_price_state.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter = ',', quotechar = '"')

		for row in reader:
	  		# if row is less than 51, get the state and the first value
	  		if count <= 50:
	  			writestring = []
	    			stateName = get_StateName(row[1])
	    			writestring.append(stateName)
  	    			writestring.append(row[1])
	    			writestring.append(row[3])
	    			avg_elec_price.append(writestring)
	    		# keep appending to existing list at each element of multi list
	    		else:
	  			avg_elec_price[ind].append(row[3])

	  			if ind < 50:
	  				ind = ind + 1
	  			else:
	  				ind = 0

	  		count = count + 1

	  	# write each line to csv file
		for i in avg_elec_price:
  			writer.writerow(i)

def get_StateName(stateCode):
	stateCodeName = { 
		'AK' : 'Alaska',
		'AL' : 'Alabama',
		'AR' : 'Arkansas',
		'AZ' : 'Arizona',
		'CA' : 'California',
		'CO' : 'Colorado',
		'CT' : 'Connecticut',
		'DC' : 'District of Columbia',
		'DE' : 'Delaware',
		'FL' : 'Florida',
		'GA' : 'Georgia',
		'HI' : 'Hawaii',
		'IA' : 'Iowa',
		'ID' : 'Idaho',
		'IL' : 'Illinois',
		'IN' : 'Indiana',
		'KS' : 'Kansas',
		'KY' : 'Kentucky',
		'LA' : 'Louisiana',
		'MA' : 'Massachusetts',
		'MD' : 'Maryland',
		'ME' : 'Maine',
		'MI' : 'Michigan',
		'MN' : 'Minnessota',
		'MO' : 'Missouri',
		'MS' : 'Mississippi',
		'MT' : 'Montana',
		'NC' : 'North Carolina',
		'ND' : 'North Dakota',
		'NE' : 'Nebraska',
		'NH' : 'New Hampshire',
		'NJ' : 'New Jersey',
		'NM' : 'New Mexico',
		'NV' : 'Nevada',
		'NY' : 'New York',
		'OH' : 'Ohio',
		'OK' : 'Oklahoma',
		'OR' : 'Oregon',
		'PA' : 'Pennsylvania',
		'RI' : 'Rhode Island',
		'SC' : 'South Carolina',
		'SD' : 'South Dakota',
		'TN' : 'Tennessee',
		'TX' : 'Texas',
		'UT' : 'Utah',
		'VA' : 'Virginia',
		'VT' : 'Vermont',
		'WA' : 'Washington',
		'WI' : 'Wisconsin',
		'WV' : 'West Virginia',
		'WY' : 'Wyoming',
	}

	return stateCodeName[stateCode];

clean_elec_prices();


