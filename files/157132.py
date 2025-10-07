<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="testflow3"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 06:22:20 PM"/>
        <attribute name="created" value="VXNlcjtERVNLVE9QLTZPS0QxVTI7MjU2OC0wNy0xNjswNTozNDowNyBQTTsyNzU2"/>
        <attribute name="edited" value="VXNlcjtERVNLVE9QLTZPS0QxVTI7MjU2OC0wNy0xNjswNjoyMjoyMCBQTTs1OzI4NjE="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="n, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="n"/>
            <while expression="i &lt;= n">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>