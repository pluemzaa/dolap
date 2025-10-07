<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="4_3"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 11:23:47 PM"/>
        <attribute name="created" value="VXNlcjtMQVBUT1AtTkJHUzEyR0Q7MjU2OC0wNy0xNzsxMToxMzozMyBQTTsyNzUy"/>
        <attribute name="edited" value="VXNlcjtMQVBUT1AtTkJHUzEyR0Q7MjU2OC0wNy0xNzsxMToyMzo0NyBQTTsxOzI4NjY="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="sn, en" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="sn"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="en"/>
            <while expression="sn &lt;= en">
                <output expression="sn" newline="True"/>
                <assign variable="sn" expression="sn+1"/>
            </while>
        </body>
    </function>
</flowgorithm>