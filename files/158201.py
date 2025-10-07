<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="flowtest3"/>
        <attribute name="authors" value="Acer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-22 11:09:33 AM"/>
        <attribute name="created" value="QWNlcjtMQVBUT1AtUjUyMTQ5VlE7MjAyNS0wNy0yMjsxMTowNTo0MCBBTTsyNjU4"/>
        <attribute name="edited" value="QWNlcjtMQVBUT1AtUjUyMTQ5VlE7MjAyNS0wNy0yMjsxMTowOTozMyBBTTsxOzI3NzI="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="i, n" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="n"/>
            <while expression="i&lt;=n">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>