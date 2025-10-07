<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="w3"/>
        <attribute name="authors" value="staff"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-19 12:28:43 PM"/>
        <attribute name="created" value="c3RhZmY7REVTS1RPUC1NNDUwQ002OzIwMjUtMDctMTk7MTI6MTM6NTQgUE07MjgyOQ=="/>
        <attribute name="edited" value="c3RhZmY7REVTS1RPUC1NNDUwQ002OzIwMjUtMDctMTk7MTI6Mjg6NDMgUE07MTsyOTQx"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="start, end" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="start"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="end"/>
            <while expression="start &lt;= end">
                <output expression="start" newline="True"/>
                <assign variable="start" expression="start + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>