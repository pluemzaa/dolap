<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="TOOD3"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-20 12:53:06 AM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6Mzg6MTYgUE07MjU4Mw=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6NDA6MzggUE07MTsyNjg4"/>
        <attribute name="edited" value="c2Fuc287TEFQVE9QLTA3UTVERjFROzIwMjUtMDctMjA7MTI6NTM6MDYgQU07MTsyOTM0"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="n, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="n"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="i"/>
            <while expression="n &lt;= i">
                <output expression="n" newline="True"/>
                <assign variable="n" expression="n+1"/>
            </while>
        </body>
    </function>
</flowgorithm>