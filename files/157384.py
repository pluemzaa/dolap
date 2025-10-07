<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab_3"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-19 03:21:42 PM"/>
        <attribute name="created" value="VXNlcjtMQVBUT1AtQTczQTFDTlQ7MjAyNS0wNy0xODsxMjo0Mjo1MSBBTTsyNzA3"/>
        <attribute name="edited" value="VXNlcjtMQVBUT1AtQTczQTFDTlQ7MjAyNS0wNy0xOTswMzoyMTo0MiBQTTsxNDsyODgw"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="start, end, i" type="Integer" array="False" size=""/>
            <input variable="start"/>
            <input variable="end"/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <assign variable="i" expression="start"/>
            <while expression="i&lt;=end">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>