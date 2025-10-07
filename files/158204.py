<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="3"/>
        <attribute name="authors" value="Lenovo"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 11:38:18 AM"/>
        <attribute name="created" value="TGVub3ZvO0xBUFRPUC0xUkpOVURWTTsyNTY4LTA3LTIyOzExOjMwOjM1IEFNOzMwMDk="/>
        <attribute name="edited" value="TGVub3ZvO0xBUFRPUC0xUkpOVURWTTsyNTY4LTA3LTIyOzExOjM4OjE4IEFNOzE7MzEyNg=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="start, end, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="start"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="end"/>
            <while expression="start&lt;=end">
                <output expression="start" newline="True"/>
                <assign variable="start" expression="start+1"/>
            </while>
        </body>
    </function>
</flowgorithm>