<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab2"/>
        <attribute name="authors" value=""/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 11:48:14 PM"/>
        <attribute name="created" value="TGVub3ZvO0RFU0tUT1AtTFRVR0FETjsyNTY4LTA3LTE2OzExOjQ2OjMwIFBNOzMwMzE="/>
        <attribute name="edited" value="TGVub3ZvO0RFU0tUT1AtTFRVR0FETjsyNTY4LTA3LTE2OzExOjQ4OjE0IFBNOzI7MzE0NA=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="start, end, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="start"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="end"/>
            <assign variable="i" expression="start"/>
            <while expression="i &lt;= end">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>