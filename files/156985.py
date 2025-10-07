<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="3"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 03:05:47 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDE6Mzc6MDEgUE07MjU3Mw=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDM6MDU6NDcgUE07MjsyNjg5"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="s, e" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="s"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="e"/>
            <output expression="s" newline="True"/>
            <while expression="s&lt;e">
                <assign variable="s" expression="s+1"/>
                <output expression="s" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>