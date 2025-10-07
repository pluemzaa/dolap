<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Lab2.2"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 03:01:05 PM"/>
        <attribute name="created" value="VXNlcjtMQVBUT1AtUUwxSzI1TEk7MjU2OC0wNy0xNzsxMjo0OTo1NyBBTTsyNzUw"/>
        <attribute name="edited" value="VXNlcjtMQVBUT1AtUUwxSzI1TEk7MjU2OC0wNy0xNzswMzowMTowNSBQTTszOzI4NTY="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="s, e" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="s"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="e"/>
            <while expression="s &lt;= e">
                <output expression="s" newline="True"/>
                <assign variable="s" expression="s+1"/>
            </while>
        </body>
    </function>
</flowgorithm>