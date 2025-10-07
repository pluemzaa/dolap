<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="3281Lab2.4"/>
        <attribute name="authors" value="pppp5"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-17 01:05:07 PM"/>
        <attribute name="created" value="cHBwcDU7Q0xFTTsyMDI1LTA3LTE2OzA3OjM1OjU0IFBNOzIwODE="/>
        <attribute name="edited" value="cHBwcDU7Q0xFTTsyMDI1LTA3LTE3OzAxOjA1OjA3IFBNOzQ7MjE4Mg=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="start, end" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="start"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="end"/>
            <output expression="start" newline="True"/>
            <while expression="start&lt;end">
                <assign variable="start" expression="start + 1"/>
                <output expression="start" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>