<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_3"/>
        <attribute name="authors" value="elaxy"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-22 08:37:22 PM"/>
        <attribute name="created" value="ZWxheHk7Q0hBTk9OQ0hPVEk7MjAyNS0wNy0xNjswOToyOToxMyBQTTsyNjUy"/>
        <attribute name="edited" value="ZWxheHk7Q0hBTk9OQ0hPVEk7MjAyNS0wNy0yMjswODozNzoyMiBQTTsyOzI3NTY="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="i, count" type="Integer" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="count"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="i"/>
            <while expression="count&lt;=i">
                <output expression="count" newline="True"/>
                <assign variable="count" expression="count + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>