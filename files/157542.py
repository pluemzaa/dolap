<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="AAAA3"/>
        <attribute name="authors" value="Sumat"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 10:21:30 PM"/>
        <attribute name="created" value="U3VtYXQ7VE9OR19UT05HX1NIVVI7MjU2OC0wNy0yMDswOTo0MjowOSBQTTsyOTU2"/>
        <attribute name="edited" value="U3VtYXQ7VE9OR19UT05HX1NIVVI7MjU2OC0wNy0yMDsxMDoyMTozMCBQTTsxOzMwNDc="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="a, b" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="a"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="b"/>
            <while expression="a &lt;= b">
                <output expression="a" newline="True"/>
                <assign variable="a" expression="a+1"/>
            </while>
        </body>
    </function>
</flowgorithm>