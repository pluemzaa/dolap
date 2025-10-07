<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="4.3"/>
        <attribute name="authors" value="asus"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 09:01:22 PM"/>
        <attribute name="created" value="YXN1cztMQVBUT1AtNzM3TDlPSFA7MjAyNS0wNy0xNjswODo1MjozMSBQTTsyNzY0"/>
        <attribute name="edited" value="YXN1cztMQVBUT1AtNzM3TDlPSFA7MjAyNS0wNy0xNjswOTowMToyMiBQTTsyOzI4Njg="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="i, e" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="e"/>
            <while expression="i&lt;e">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
            <output expression="i" newline="True"/>
        </body>
    </function>
</flowgorithm>