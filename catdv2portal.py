#!/usr/bin/env /usr/bin/python

# CatDV to Portal XSLT tool

import sys
import getpass
import os
import requests
from xml.dom import minidom
import xml.etree.ElementTree as ET

os.system("clear")

print "Welcome to the CatDV to Portal XSLT Tool"
print ""
print "We need some information to proceed"
print ""
portal_ip = raw_input("Portal IP: ")
portal_user = raw_input("Portal Admin Username: ")
portal_pass = getpass.getpass("Portal SuperUser password: ")
catdv_xml_file = raw_input("CatDV XML File Path: ").replace("\\","").strip()
print ""
print "Attempting to open file" + catdv_xml_file + "..."
print ""

#check to see if it a is a valid file
if os.path.isfile(catdv_xml_file) is not True:
	print "Couldn't open file " + catdv_xml_file
	print "Please check that your path is correct"
	print ""
	exit()

#parse our CatDV XML	
tree = ET.parse(catdv_xml_file)
root = tree.getroot()

#get all the field names of our CatDV XML
catdv_fields = []

for child in root:
	for grandchild in child:
		catdv_fields.append(grandchild.tag)

#present these fields for mapping
print "We now need to map Portal fields to CatDV fields."
print "Please input the equivalent Portal field where you would like the values stored for each CatDV field"
print ""		
portal_fields = []

#build a list of all the portal mapped fields associated with CatDV fields
for field in catdv_fields:
	if field == "NAME":
		map = "title"
	elif field.startswith("USER"):
		findstring = './CLIP/' + field + ""
		fieldname = root.findall(findstring)
		for hname in fieldname:
			map = raw_input(hname.attrib['name'] + ": ")
	else:
		map = raw_input(field + ": ")
		
	portal_fields.append(map)

#build the XSLT file
xslt = """<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="xs">
  <xsl:output method="xml" encoding="UTF-8" indent="yes"/>
  <xsl:template match="/">
    <MetadataDocument xmlns="http://xml.vidispine.com/schema/vidispine">
      <group>CatDV</group>
      <timespan>
        <xsl:attribute name="start" namespace="">-INF</xsl:attribute>
        <xsl:attribute name="end" namespace="">+INF</xsl:attribute>
"""

#print out the xslt
i = 0
for field in catdv_fields:
	if portal_fields[i]:
		xslt = xslt + """
	<!--CatDV Field:""" + field + """-->
	<field>
		<name>""" + portal_fields[i] + """</name>
		<value>
			<xsl:value-of select="string(/CLIPS/CLIP/""" + field + """)"/>        	
		</value>
	</field>"""
			
#		print "CatDV Field: " + field + "\t\tPortal Mapped Field: " + portal_fields[i]
	i = i + 1

xslt = xslt + """
      </timespan>
    </MetadataDocument>
  </xsl:template>
</xsl:stylesheet>  
"""

print ""
print "Attempting to update projection \"CatDV\""
headers = {'content-type': 'application/xml'}
r = requests.put("http://" + portal_ip + ":8080/API/projection/CatDV/incoming/",headers=headers,auth=(portal_user,portal_pass),data=xslt)
print "Portal Response:"
print r.text
