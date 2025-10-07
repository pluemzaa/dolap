<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4.Counter"/>
        <attribute name="authors" value="akung"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 05:55:04 PM"/>
        <attribute name="created" value="YWt1bmc7S0lERE87MjU2OC0wNy0xNzswNTozMTozMCBQTTsyMTg5"/>
        <attribute name="edited" value="YWt1bmc7S0lERE87MjU2OC0wNy0xNzswNTo1NTowNCBQTTszOzIzMDY="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="n, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="n"/>
            <while expression="i &lt;= n">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>