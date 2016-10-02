Roll_no=[]
Marks=[]
Name=[]
flag=1
index=0
import re
import urllib2
pattern=re.compile("^\s+[<]td[>]15CS[0-9]+$")#Roll_no
pattern01=re.compile("^\s+[<]td[>]15CS[0-9]+[<][/]td[>].+$")#roll_no
pattern1=re.compile('^\s+[<]td[>][<]a href[=]["][/][~]wbcm[/]cgi[-]bin[/]wbcm[/]common[/]showMarks[.]cgi[?]ccode[=]cs29003[&]year[=]2016[&]sem[=]a[&]catno[=][0-9][&]asgnid[=][0-9]+[&]roll[=][0-9]+CS[0-9]+["][>][0-9][0-9][*][<][/]a[>]$')#marks
pattern5=re.compile('^\s+[<]td[>][<]a href[=]["][/][~]wbcm[/]cgi[-]bin[/]wbcm[/]common[/]showMarks[.]cgi[?]ccode[=]cs29003[&]year[=]2016[&]sem[=]a[&]catno[=][0-9][&]asgnid[=][0-9]+[&]roll[=][0-9]+CS[0-9]+["][>][0-9][*][<][/]a[>]$')
pattern3=re.compile('^\s+[<]td[>][<]a href[=]["][/][~]wbcm[/]cgi[-]bin[/]wbcm[/]common[/]showMarks[.]cgi[?]ccode[=]cs29003[&]year[=]2016[&]sem[=]a[&]catno[=][0-9][&]asgnid[=][0-9]+[&]roll[=][0-9]+CS[0-9]+["][>][<]b[>][?][<]b[>][<][/]a[>]$')
pattern4=re.compile('^\s+[<]td[>][<]a href[=]["][/][~]wbcm[/]cgi[-]bin[/]wbcm[/]common[/]showMarks[.]cgi[?]ccode[=]cs29003[&]year[=]2016[&]sem[=]a[&]catno[=][0-9][&]asgnid[=][0-9]+[&]roll[=][0-9]+CS[0-9]+["][>][0-9][<][/]a[>]$')
pattern6=re.compile('^\s+[<]td[>][<]a href[=]["][/][~]wbcm[/]cgi[-]bin[/]wbcm[/]common[/]showMarks[.]cgi[?]ccode[=]cs29003[&]year[=]2016[&]sem[=]a[&]catno[=][0-9][&]asgnid[=][0-9]+[&]roll[=][0-9]+CS[0-9]+["][>][0-9][0-9][<][/]a[>]$')
pattern8=re.compile("^\s+[<]td align[=]left[>].+[<][/]td[>]$")#name
fo=urllib2.urlopen("http://cse.iitkgp.ac.in/~wbcm/wbcm/subLog/cs290032016a/sec1/")
to=open("xyz.txt",'w')
to.write(fo.read())
to=open("xyz.txt",'r')
ch=0
for line in to:
  if(flag==1 or flag==2):
  		if(pattern.match(line)):
                  Roll_no.append(line[6:-1])
                  if(flag==2):
                      Marks.append(ch)
                      ch=0
                  flag=0

  if(flag==0):
  		if(pattern01.match(line)):
    			flag=2

  		elif(pattern8.match(line)):
    			Name.append(line[17:-6])
    		
  if(flag==2):
  		if(pattern4.match(line)):   
     			ch+=(int(line[-6:-5]))
  		if(pattern3.match(line)):
     			ch+=(int('0'))
  		if(pattern1.match(line)):
     			ch+=(int(line[-8:-6]))
  		if(pattern5.match(line)):
     			ch+=(int(line[-7:-6]))
  		if(pattern6.match(line)):
     			ch+=(int(line[-7:-5]))

Marks.append(ch)



j=2
for i in range(1,len(Roll_no)):
		for h in range(0,len(Roll_no)-j+1):
				if Marks[h]<=Marks[h+1]:
						temp=Roll_no[h]
						Roll_no[h]=Roll_no[h+1]
						Roll_no[h+1]=temp
						temp=Marks[h]
						Marks[h]=Marks[h+1]
						Marks[h+1]=temp
						temp=Name[h]
						Name[h]=Name[h+1]
						Name[h+1]=temp
		j+=1
u=0
for i in Marks:
		if u>=len(Roll_no):
				break
		print u+1,"--",Roll_no[u],"--",Name[u],"  ",i
		u+=1
