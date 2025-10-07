<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="LabT4_3"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 04:23:33 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6MTM6NDcgUE07MjU4MA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6MjM6MzMgUE07MTsyNjg0"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="st, sp" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="st"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="sp"/>
            <while expression="st &lt;= sp">
                <output expression="st" newline="True"/>
                <assign variable="st" expression="st+1"/>
            </while>
        </body>
    </function>
</flowgorithm>