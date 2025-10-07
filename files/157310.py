<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="loop"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 03:39:32 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMjozMjowNCBQTTsyNTQw"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzozOTozMiBQTTsyOzI2NTg="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="start" type="Integer" array="False" size=""/>
            <declare name="end" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="start"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="end"/>
            <while expression="start&lt;=end">
                <assign variable="start" expression="start+1"/>
                <output expression="(start-1)" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>