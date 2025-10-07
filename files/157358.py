<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="number1"/>
        <attribute name="authors" value="ITSeed"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-17 06:47:47 PM"/>
        <attribute name="created" value="SVRTZWVkO0RFU0tUT1AtOEFBRU9QMjsyMDI1LTA3LTE3OzA2OjQ0OjUxIFBNOzI4Nzc="/>
        <attribute name="edited" value="SVRTZWVkO0RFU0tUT1AtOEFBRU9QMjsyMDI1LTA3LTE3OzA2OjQ3OjQ3IFBNOzE7Mjk5Mw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="start, end" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="start"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="end"/>
            <while expression="start&lt;=end">
                <output expression="start" newline="True"/>
                <assign variable="start" expression="start+1"/>
            </while>
        </body>
    </function>
</flowgorithm>