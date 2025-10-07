<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="test3"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 02:38:03 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6MzI6MjAgUE07MjU3MA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6Mzg6MDMgUE07MjsyNjg2"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Start, End" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="Start"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="End"/>
            <while expression="Start&lt;(End+1)">
                <output expression="Start" newline="True"/>
                <assign variable="Start" expression="Start+1"/>
            </while>
        </body>
    </function>
</flowgorithm>