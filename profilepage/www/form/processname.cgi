import cgi

formData=cgi.fieldStorage()
Name=formData.getvalue('Name')
PhoneNumber=formData.getvalue('PhoneNumber')
FromEmailAddress=formData.getvalue('FromEmailAddress')
Comments=formData.getvalue('Comments')
print Name,PhoneNumber,FromEmailAddress,Comments