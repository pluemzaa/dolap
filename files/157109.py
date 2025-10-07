<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="ssdsds"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 07:10:43 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDM6NDI6MTIgUE07MjU3Mw=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6MDA6MDIgUE07MjsyNjc3"/>
        <attribute name="edited" value="cHVrYW47REVTS1RPUC0yQ04zQTM2OzIwMjUtMDctMTY7MDc6MTA6NDMgUE07NDsyOTM1"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="start, end" type="Real" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="start"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="end"/>
            <while expression="start &lt;= end">
                <output expression="(start)" newline="True"/>
                <assign variable="start" expression="start + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>