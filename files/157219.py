<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="test3lab3"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 07:31:02 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6NDI6MDUgUE07MjU3Nw=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDc6MzE6MDIgUE07MTsyNjgy"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="n, e, num" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="n"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="e"/>
            <while expression="n &lt;= e">
                <output expression="n" newline="True"/>
                <assign variable="n" expression="n + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>