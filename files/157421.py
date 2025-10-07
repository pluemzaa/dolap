<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="dokbia"/>
        <attribute name="authors" value="Acer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-18 08:45:55 PM"/>
        <attribute name="created" value="QWNlcjtERVNLVE9QLTJPQkhPODg7MjU2OC0wNy0xODswNzowODozMSBQTTsyNzIw"/>
        <attribute name="edited" value="QWNlcjtERVNLVE9QLTJPQkhPODg7MjU2OC0wNy0xODswODo0NTo1NSBQTTszOzI4Mzg="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, year, i" type="Real" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="i" expression="0"/>
            <while expression="i &lt; year">
                <assign variable="money" expression="money*(1+interest/100)"/>
                <output expression="&quot;Year &quot; &amp;(i+1)&amp; &quot;: &quot; &amp;money" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>