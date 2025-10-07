<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="beeeee"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-18 11:44:49 AM"/>
        <attribute name="created" value="VXNlcjtMQVBUT1AtVUYzQlNVRDM7MjU2OC0wNy0xODsxMTozNDo1MSBBTTsyNzY0"/>
        <attribute name="edited" value="VXNlcjtMQVBUT1AtVUYzQlNVRDM7MjU2OC0wNy0xODsxMTo0NDo0OSBBTTsxOzI4ODA="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="n, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="n"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="i"/>
            <while expression="n&lt;=i">
                <output expression="n" newline="True"/>
                <assign variable="n" expression="n+1"/>
            </while>
        </body>
    </function>
</flowgorithm>