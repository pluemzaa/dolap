<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="work3 fc"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 02:10:02 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6MDE6MTMgUE07MjU2OA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6MTA6MDIgUE07MTsyNjc0"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="a, b" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="a"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="b"/>
            <while expression="a&lt;=b">
                <output expression="a" newline="True"/>
                <assign variable="a" expression="a+1"/>
            </while>
        </body>
    </function>
</flowgorithm>