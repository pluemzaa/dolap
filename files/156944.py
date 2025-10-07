<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab43"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 02:43:56 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6NDA6MDcgUE07MjU3NA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6NDM6NTYgUE07MTsyNjg5"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="n, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="n"/>
            <while expression="i &lt;= n">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>