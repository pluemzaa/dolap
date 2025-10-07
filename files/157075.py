<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="FlowLab3"/>
        <attribute name="authors" value="Ninen"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 04:38:55 PM"/>
        <attribute name="created" value="TmluZW47U0FCVFVERTsyMDI1LTA3LTE2OzA0OjMzOjM3IFBNOzIzMTE="/>
        <attribute name="edited" value="TmluZW47U0FCVFVERTsyMDI1LTA3LTE2OzA0OjM4OjU1IFBNOzE7MjQyNA=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="start, end" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="start"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="end"/>
            <while expression="start &lt;= end">
                <output expression="start" newline="True"/>
                <assign variable="start" expression="start+1"/>
            </while>
        </body>
    </function>
</flowgorithm>