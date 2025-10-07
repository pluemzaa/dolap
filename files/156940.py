<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Lab4_3"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 02:40:55 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6Mzc6NDQgUE07MjU4MQ=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6NDA6NTUgUE07MTsyNjg1"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="i, j" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="j"/>
            <while expression="i&lt;(j+1)">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>