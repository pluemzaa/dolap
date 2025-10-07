<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="FClab02"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 04:20:28 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6MDg6MzYgUE07MjU4Mg=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6MjA6MjggUE07MjsyNjg2"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="z, x" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="z"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="x"/>
            <while expression="z&lt;=x">
                <output expression="z" newline="True"/>
                <assign variable="z" expression="z+1"/>
            </while>
        </body>
    </function>
</flowgorithm>